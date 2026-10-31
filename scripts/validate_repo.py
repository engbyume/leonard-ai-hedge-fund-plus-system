#!/usr/bin/env python3
"""Dependency-free publication audit for the public repository."""

from __future__ import annotations

import csv
from collections import Counter
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "ARCHITECTURE.md",
    "THIRD_PARTY_NOTICES.md",
    "docs/purpose-and-success.md",
    "docs/guide.md",
    "docs/evaluation-and-results.md",
    "docs/experiment-history.md",
    "docs/limitations-and-next-steps.md",
    "docs/timeline.md",
    "docs/system-map.md",
    "docs/model-history.md",
    "docs/source-authority.md",
    "docs/reference-patterns.md",
    "docs/reproduction.md",
    "docs/privacy-and-publication.md",
    "docs/evidence-methodology.md",
    "docs/daily-operations.md",
    "docs/decision-protocol.md",
    "integrations/tools.md",
    "integrations/public-sources.md",
    "config/example-profile.yml",
    "config/example-portfolio.yml",
    "skills/atlan-scale/SKILL.md",
    "skills/atlan-scale/references/benchmarking.md",
    "skills/atlan-scale/references/safety.md",
    "skills/atlan-scale/templates/daily-log.md",
    "prompts/00-bootstrap.md",
    "prompts/01-install-and-verify.md",
    "prompts/02-configure-your-experiment.md",
    "prompts/03-daily-operator.md",
    "prompts/04-review-and-update.md",
    "prompts/05-evidence-import.md",
    "prompts/replicate-the-system.md",
    "evidence/README.md",
    "evidence/progress.md",
    "evidence/weekly-checkpoints.csv",
    "evidence/decision-log.md",
    "evidence/source-register.md",
    "evidence/success-failure-analysis.md",
    "scripts/validate_repo.py",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|PRIVATE)"),
    re.compile(r"(?i)(?:api[_ -]?key|secret|token)\s*[:=]\s*[\"']?[A-Za-z0-9_\-/]{24,}"),
]

FORBIDDEN_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9._-]+"),
    re.compile(r"/home/[A-Za-z0-9._-]+"),
    re.compile(r"(?i)jiscool231@gmail\.com"),
]

RETIRED_FORECAST_TERMS = ("chrono" + "s", "times" + "fm 1.0", "times" + "fm-1.0", "times" + "fm 2.5", "times" + "fm-2.5")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_forecast_reference(relative: Path, lower_content: str, errors: list[str]) -> None:
    for term in RETIRED_FORECAST_TERMS:
        if term in lower_content:
            errors.append(f"retired forecast reference in {relative}")
    model_name = "times" + "fm"
    supported_version = model_name + " 3.0"
    allowed_paths = (
        "README.md",
        "CHANGELOG.md",
        "evidence/source-register.md",
        "docs/model-history.md",
    )
    if model_name in lower_content and (
        supported_version not in lower_content or relative.as_posix() not in allowed_paths
    ):
        errors.append(f"unsupported forecast model reference in {relative}")


PUBLIC_TEXT_EXCLUDED_DIRS = {".git", "node_modules", "dist", "graft"}


def iter_public_text_files():
    for root, directories, filenames in os.walk(ROOT):
        directories[:] = sorted(
            directory for directory in directories
            if directory not in PUBLIC_TEXT_EXCLUDED_DIRS
        )
        for filename in filenames:
            if filename == ".git":
                continue
            path = Path(root) / filename
            if path.is_file():
                yield path


def check_public_text_file(path: Path, errors: list[str]) -> None:
    try:
        content = read_text(path)
    except (UnicodeDecodeError, OSError):
        return
    relative = path.relative_to(ROOT)
    if chr(0x2014) in content:
        errors.append(f"em dash is not allowed: {relative}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            errors.append(f"possible secret pattern in {relative}: {pattern.pattern}")
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(content):
            errors.append(f"private path or identity pattern in {relative}: {pattern.pattern}")
    check_forecast_reference(relative, content.lower(), errors)


def check_public_text(errors: list[str]) -> None:
    # Scan ignored files too, except vendor, build, and Git output that is not published.
    for path in iter_public_text_files():
        check_public_text_file(path, errors)



def check_links(errors: list[str]) -> None:
    path = ROOT / "integrations/tools.md"
    if not path.is_file():
        return
    text = read_text(path)
    if re.search(r"(?<!https:)//", text):
        errors.append("integrations/tools.md contains a non-HTTPS URL")
    urls = re.findall(r"https?://[^\s|)]+", text)
    if len(urls) < 6:
        errors.append("integrations/tools.md has too few public links")
    if any(url.startswith("http://") for url in urls):
        errors.append("all integration URLs must use HTTPS")


def check_skill(errors: list[str]) -> None:
    path = ROOT / "skills/atlan-scale/SKILL.md"
    if not path.is_file():
        return
    text = read_text(path)
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append("skill is missing YAML frontmatter")
    if not re.search(r"(?m)^name:\s*[a-z0-9][a-z0-9-]*\s*$", text):
        errors.append("skill frontmatter is missing a valid name")
    if not re.search(r"(?m)^description:\s*.+$", text):
        errors.append("skill frontmatter is missing a description")
    for required in ("benchmark", "catalyst", "settlement", "external", "confirmation"):
        if required.lower() not in text.lower():
            errors.append(f"skill is missing required concept: {required}")


def check_prompts(errors: list[str]) -> None:
    combined = "\n".join(
        read_text(path)
        for path in (ROOT / "prompts").glob("*.md")
        if path.is_file()
    ).lower()
    for term in ("benchmark", "schedule", "preferences", "dry run", "live trading", "paired", "catalyst"):
        if term not in combined:
            errors.append(f"prompts are missing required concept: {term}")


def check_readme(errors: list[str]) -> None:
    path = ROOT / "README.md"
    if not path.is_file():
        return
    text = read_text(path).lower()
    for term in ("purpose", "evidence", "public", "private", "install", "not financial advice", "kronos", "forecast model history"):
        if term not in text:
            errors.append(f"README is missing required concept: {term}")
    if "ai-hedge-fund-plus-system" not in text:
        errors.append("README does not name the requested repository")


def check_model_history(errors: list[str]) -> None:
    path = ROOT / "docs/model-history.md"
    if not path.is_file():
        return
    text = read_text(path).lower()
    required = (
        "times" + "fm 3.0",
        "non-commercial",
        "non-production",
        "opt-in",
        "fake model outputs",
        "no direct call site",
        "src-002",
        "src-184",
    )
    for term in required:
        if term not in text:
            errors.append(f"model-history page is missing required evidence: {term}")
    readme = read_text(ROOT / "README.md").lower()
    if "docs/model-history.md" not in readme:
        errors.append("README does not link to the model-history page")
    register = read_text(ROOT / "evidence/source-register.md").lower()
    license_url = "https://huggingface.co/google/" + "times" + "fm-3.0-pytorch/blob/main/license"
    if "src-184" not in register or license_url not in register:
        errors.append("model-history source register entry is missing or incomplete")


def check_source_register(errors: list[str]) -> None:
    path = ROOT / "evidence/source-register.md"
    if not path.is_file():
        return
    ids = re.findall(r"^\|\s*(SRC-\d+)\s*\|", read_text(path), re.MULTILINE)
    duplicates = sorted(identifier for identifier, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append("source register has duplicate IDs: " + ", ".join(duplicates))


def check_evidence(errors: list[str]) -> None:
    path = ROOT / "evidence/weekly-checkpoints.csv"
    if not path.is_file():
        return
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        errors.append(f"cannot parse evidence CSV: {exc}")
        return
    required = {
        "date",
        "period",
        "portfolio_return_pct",
        "benchmark_return_pct",
        "spread_pp",
        "evidence_type",
    }
    if not rows:
        errors.append("evidence CSV has no rows")
    if rows and not required.issubset(rows[0]):
        errors.append("evidence CSV is missing required columns")
    for index, row in enumerate(rows, start=2):
        try:
            portfolio = float(row["portfolio_return_pct"])
            benchmark = float(row["benchmark_return_pct"])
            spread = float(row["spread_pp"])
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"evidence row {index} has invalid numeric data: {exc}")
            continue
        if round(portfolio - benchmark, 2) != round(spread, 2):
            errors.append(f"evidence row {index} spread does not equal portfolio minus benchmark")
        if row.get("evidence_type") not in {"machine_observed", "user_confirmed", "public_source", "inference", "unverified"}:
            errors.append(f"evidence row {index} has an unknown evidence type")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_public_text(errors)
    check_links(errors)
    check_skill(errors)
    check_prompts(errors)
    check_readme(errors)
    check_model_history(errors)
    check_evidence(errors)
    check_source_register(errors)
    if errors:
        print("PUBLICATION AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PUBLICATION AUDIT PASSED: {len(REQUIRED_FILES)} required files and redacted evidence checks are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
