#!/usr/bin/env python3
"""Dependency-free publication audit for the public repository."""

from __future__ import annotations

import csv
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
    "docs/system-map.md",
    "docs/timeline.md",
    "docs/model-history.md",
    "docs/experiment-history.md",
    "docs/evaluation-and-results.md",
    "docs/successes-and-failures.md",
    "docs/limitations-and-next-steps.md",
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
    "scripts/validate_repo.py",
    "assets/leonard-system-map.png",
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

RETIRED_FORECAST_PATTERNS = (
    re.compile("chrono" + "s", re.IGNORECASE),
    re.compile(r"times" + r"fm[-_ ]?(?:1(?:\.0)?|2(?:\.5)?|2p5)\b", re.IGNORECASE),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_public_text(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            content = read_text(path)
        except (UnicodeDecodeError, OSError):
            continue
        relative = path.relative_to(ROOT)
        if "\u2014" in content:
            errors.append(f"em dash is not allowed: {relative}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"possible secret pattern in {relative}: {pattern.pattern}")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(content):
                errors.append(f"private path or identity pattern in {relative}: {pattern.pattern}")
        for pattern in RETIRED_FORECAST_PATTERNS:
            if pattern.search(content):
                errors.append(f"retired forecast reference in {relative}")


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


def check_local_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"!?\[[^\]]+\]\(([^)]+)\)", read_text(path)):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if relative_target and not (path.parent / relative_target).exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")


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
    for term in ("purpose", "evidence", "public", "private", "install", "not financial advice", "kronos"):
        if term not in text:
            errors.append(f"README is missing required concept: {term}")
    if "ai-hedge-fund-plus-system" not in text:
        errors.append("README does not name the requested repository")


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
        if None in row:
            errors.append(f"evidence row {index} has extra unquoted fields")
        if any(value is None for value in row.values()):
            errors.append(f"evidence row {index} has missing fields")
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
    check_local_links(errors)
    check_skill(errors)
    check_prompts(errors)
    check_readme(errors)
    check_evidence(errors)
    if errors:
        print("PUBLICATION AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PUBLICATION AUDIT PASSED: {len(REQUIRED_FILES)} required files and redacted evidence checks are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
