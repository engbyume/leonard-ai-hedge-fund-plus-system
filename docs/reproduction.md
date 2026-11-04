# Reproduction guide

This guide reproduces the public method without importing any private account state.

## 1. Create an isolated workspace

Clone the repository into a new directory and create a private `runtime/` directory. The runtime is ignored by Git and should contain only local configuration, generated reports, and provider-specific secrets.

```bash
git clone https://github.com/engbyume/leonard-ai-hedge-fund-plus-system.git
cd leonard-ai-hedge-fund-plus-system
python3 scripts/validate_repo.py
mkdir -p runtime
```

## 2. Run the preference intake

Give an AI agent [`prompts/02-configure-your-experiment.md`](../prompts/02-configure-your-experiment.md). It must ask for a benchmark, baseline, risk constraints, sector and position limits, rebalance rule, schedule, delivery channel, and whether external actions are allowed. If the operator does not answer, use `null` and keep live actions disabled.

## 3. Install optional components

Use [`prompts/01-install-and-verify.md`](../prompts/01-install-and-verify.md). The agent must inspect the current host, Python version, GPU availability, package manager, and licensing before installing anything. Kronos is optional. A missing model must produce a labeled fallback, not a fabricated forecast.

## 4. Produce a dry report

Run research with no external send and no trade authorization. The report must show:

- benchmark and portfolio measurement dates
- source freshness
- company-specific catalyst and catalyst persistence
- countercase and invalidation
- one-week, two-week, and month forecast horizons when available
- five daily returns, green/red breadth, late-versus-early momentum, and largest-up-day share
- macro and cross-market risk haircuts
- platform availability status
- paired sell-buy state and settlement gate

## 5. Review and record

Use [`prompts/04-review-and-update.md`](../prompts/04-review-and-update.md). Record what the system advised, what the operator selected or rejected, why, and what happened afterward. Keep failed ideas and stale hypotheses with their failure condition.

## 6. Schedule only after validation

Schedule a local dry run first. Verify the output, duplicate prevention, data freshness, and action gates. Enable external delivery only after explicit confirmation. Enable live trading only in a separately audited integration, with a second explicit confirmation and an independent settlement check.
