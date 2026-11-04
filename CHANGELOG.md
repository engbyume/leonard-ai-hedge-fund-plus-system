# Changelog

## Unreleased

### 2026-10-31 - Documentation audit follow-up

- Updated README and reproduction clone commands to the current public GitHub slug, removed a duplicate guide sentence, and aligned the validator's repository-name check.
- Reframed SnapTrade as a capability reference for account data, without asserting a user's account link, and added dated source entry SRC-270.
- Narrowed SRC-268's historical URL-check wording and added SRC-269 to state exactly what the validator checks; no project-wide Markdown link or claim-source coverage is claimed.
- Added SRC-271 to document QuantConnect's Free Cloud data access, no-export terms, Free-plan API limit, and the prior zero-row probe; no account query or dataset request was made.

### 2026-11-03 - QuantConnect source boundary recheck

- Rechecked the official Terms, pricing, tier-features, and US Equities pages. The Terms list paid export paths through a purchased CLI data license or a signed institutional derived-data agreement; neither was used or authorized. The Free plan still excludes API access while allowing Cloud data use. The US Equities page describes live SIP coverage that excludes OTC and lists all historical data at daily resolution. Account entitlement, exact ETF coverage, and the top-five signal list's exportability remain unverified. Added SRC-272.

### 2026-11-03 - Phase-two target and prototype status

- Corrected the public phase-two target citation and updated its status: the private prototype is synthetic-only, with no validated real-data forecast or causal walk-forward result. Added SRC-273 and SRC-274; exact holdings remain private.

### 2026-11-03 - Historical account-detail redaction

- Generalized account-specific security and transaction-limit references in the public history. Retained aggregate benchmark percentages under the existing publication policy. Recorded the review in SRC-275.

### 2026-11-03 - Account-specific holding privacy rule

- Clarified that the public documentation excludes current and historical account-linked holdings, positions, watchlists, and transaction limits. Added SRC-276.

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
