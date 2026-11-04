# Privacy and publication boundary

## Publish

- public documentation and links
- generic prompts and configuration schemas
- reproducible validation scripts
- aggregate percentage returns with dates and benchmark definition
- decision rationale without account details
- failed ideas, invalidation signals, and method changes

## Keep private

- provider keys, email tokens, cookies, session files, and `.env` files
- broker account numbers, recipient addresses, and exact balances
- exact order amounts if they can identify the account or expose personal finances
- current or historical account-specific holdings, individual positions, account-linked watchlist membership, and transaction limits
- raw generated reports, raw email bodies, local logs, SQLite databases, cached market exports, and home-directory paths
- data files copied from licensed services without permission

## Redaction rules

1. Replace account values with percentages or `pending`.
2. Replace recipient and account identifiers with role labels.
3. Keep event dates and decision dates when they are needed to reproduce reasoning.
4. Mark each statement as machine-observed, user-confirmed, public-source, or inference.
5. Never turn an unverified user belief into a measured performance claim.
6. Replace account-linked tickers and actions with role labels. Keep public ticker examples only when they are not presented as holdings or account-specific watchlist items.

## Local runtime pattern

Keep private state in `runtime/`, which is ignored by `.gitignore`:

```text
runtime/
  profile.yml
  portfolio.yml
  sources-private.yml
  reports/
  logs/
  .env
```

Before a commit, run `python3 scripts/validate_repo.py` and inspect the staged diff manually. The validator is a guardrail, not a substitute for judgment.
