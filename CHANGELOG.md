# Changelog

## Unreleased

### 2026-09-22 - Historical feasibility and no-send automation hardening

- Defined and published the exact-pair hit-rate metric separately from portfolio returns. On the shared 106-window baseline slice, no tested route improved on protected v14.
- Recorded the current decision feasibility ceiling: 89 of 111 decisions, with growth-like and transition maximum feasible runs below five.
- Made report archives record preview, provider acknowledgement, or failure. A dry run now leaves the same-day dispatch marker unchanged and skips failure email and auto-heal state changes.
- Verified a no-send report preview with zero proposed actions. No live email, trade, broker write, scheduler mutation, or model promotion occurred in this verification.
- Documented that external email delivery remains unverified without an AgentMail sent-label readback.

### 2026-09-22 - Read-only AgentMail status verification

- A read-only metadata lookup found one `sent`-labeled report at the same time as the stored 20:31 report archive, with the configured recipient matching.
- The message body was not retrieved, so exact content matching remains unverified. No email was sent by this task.

### 2026-08-08 - Public repository bootstrap

- Created the personal `ai-hedge-fund-plus-system` publication layer.
- Added an Atlan-inspired context-repository architecture without claiming Atlan affiliation.
- Added links for Agent Skills, Kronos, the upstream AI Hedge Fund project, and the market-data, broker-readback, and delivery providers used by the private runtime.
- Added preference-driven replication prompts, a portable skill, example configuration, evidence methodology, and publication audits.
- Recorded a redacted operator update; account activity and amounts are excluded from public documentation.
- Preserved the rule that no sale may appear without a corresponding buy or an explicitly documented proceeds hold.

### 2026-08-10 - Daily benchmark and candidate gates

- Made daily, five-session, monthly, and open-position all-time benchmark comparisons use current market-close data instead of a stale user-confirmed daily percentage.
- Added a pending Fidelity funding record that is excluded from buying power until the operator confirms arrival.
- Enforced three ETF-only 04A cards, including standalone held-ETF reviews when no replacement gate fails.
- Enforced two daily 04B individual-stock cards with catalyst and momentum-exhaustion gates; account-specific ticker and forecast details are excluded here.
- Removed the obsolete model references and retained Kronos as the sole forecast-model link.

## Change-log practice

Every future system change should include its date, the advice or evidence that motivated it, the operator's decision, the files or rules changed, and the verification result. Failed ideas remain in the log with their failure condition.

### 2026-10-30 - Reconcile AI Hedge Fund documentation

- Added a reading guide, research timeline, experiment history, evaluation summary, and limitations page.
- Reconciled source-register identifiers while preserving dated AIHF evidence and excluding unrelated project material from this candidate.
- Expanded the publication validator to require the new documentation pages and reject repeated source identifiers.
- Validation result is recorded in the source register and evidence progress after checks run. This local review candidate has not been published.
