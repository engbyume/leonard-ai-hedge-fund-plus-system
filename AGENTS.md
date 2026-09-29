# Repository operating rules

This repository is a public, personal documentation and orchestration layer. Keep private runtime state outside the checkout.

## Source of truth

- Public architecture, prompts, schemas, and redacted evidence live here.
- A user's private runtime is the local source for live account state and credentials.
- Public claims require a source register entry and a date.
- Historical evidence is never silently rewritten after a later result becomes available.

## Safety

- Never commit credentials, cookies, API keys, account identifiers, raw emails, broker exports, or private filesystem paths.
- Never place a live trade or send an external message from a dry-run workflow.
- Require explicit operator confirmation before any external action.
- Treat platform availability as unverified until the operator confirms it.
- Every proposed sell must have a corresponding buy or a documented, approved proceeds-hold instruction.
- A momentum spike is not durable momentum. Review breadth, late-week behavior, and the largest-up-day share.

## Task model routing

- Default regular tasks to GPT-6 Luna with max reasoning.
- Route hard, complex, high-risk, or broad-scope work to GPT-6 Sol with high reasoning.
- Route very complex, tightly bounded work predicted under 10 minutes to GPT-6 Astra with high reasoning, only when the active runtime exposes that exact model and effort.
- Use Sol Foreman and its Sol High parent only when complex coordination is justified. Do not make it the regular-task default.
- The allowed standard GPT model/effort pairs are Luna/max, Sol/high, and Astra/high. Verify the active session separately from these routing defaults.

## Evidence

Record benchmark, dates, cash-flow treatment, costs, return method, drawdown, and data freshness with every performance comparison. Use redacted percentages in public files. Label user reports, machine observations, inferences, and verified public sources separately.

## Changes

Make the smallest change that fulfills the request. Add a dated entry to `CHANGELOG.md` for meaningful system changes and update the appropriate evidence or decision-log entry. Run `python3 scripts/validate_repo.py` before publishing.
