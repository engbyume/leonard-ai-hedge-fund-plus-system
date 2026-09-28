# Changelog

## Unreleased

### 2026-09-25 - Yahoo automated-access boundary

- Added SRC-026 with official regional Yahoo terms evidence and the failed U.S. terms-page retrieval.
- Recorded the fail-closed operating decision: automated Yahoo collection remains unavailable until express permission or a licensed alternative is verified. This is not a legal conclusion.
- No Yahoo-derived staged data, candidate picks, or performance claim was published.

### 2026-09-25 - Price refresh coverage gate

- Appended 9,702 fixed-cohort bars through the 2026-09-24 session and verified SQLite integrity.
- Recorded incomplete September 22 coverage and a same-provider retry that added no rows. Deferred aligned feature-cache rebuilding and selector replay because the full daily boundary is not yet verified.
- No prediction-accuracy claim, candidate promotion, trade, broker write, email send, or scheduler change was made.
- Reran a direct no-send report preview after delivery-gate hardening. It recorded `previewed`, zero delivery attempts, and zero proposed orders; live delivery remains blocked while model-card Cash App availability is unverified. Thirty-six focused tests and both wrapper syntax checks passed.
- Audited no-cost historical-data options and the existing September 22 Yahoo path. Thirty-two saved retry slices covered 3,154 symbols; 243 were returned and zero new bars were inserted. A fresh 20-symbol missing-data sample returned no bars, while five existing-data controls returned five bars. These bounded samples do not prove all missing symbols lack data.
- Official documentation identifies Alpaca Basic as a possible free historical SIP source for data older than 15 minutes, but it requires authenticated access. Tiingo's free plan is limited to 500 unique symbols per month, and Alpha Vantage's free service to 25 requests per day. No new account, authenticated request, or paid API call occurred.
- Follow-up official-source review found StashGamma's free daily history requires an account and API key, while HistoricalData.net sells its full adjusted archive and limits no-account access to metadata and fixed sample rows. No provider request, account setup, or purchase occurred; this was not an exhaustive source survey.
- A read-only alias audit compared 3,754 dated-manifest symbols with the main price store: 3,214 intersected, 540 were absent, and none had a stored slash/dash or dot/dash variant. This excludes only simple punctuation mismatches; no API call or database write occurred.
- A six-batch no-write Yahoo history probe over the 540 symbols absent from the main store returned 18,775 adjusted-price bars for 36 symbols. Results were not persisted; post-probe integrity and row counts were unchanged. No provider-wide availability or accuracy conclusion is inferred.
- Rematerialized the dated historical-universe store from the main price store only after manifest and full old-row parity checks passed. The refreshed store passes integrity with 2,106,844 bars through September 24; all 2,040,294 prior rows match exactly and 66,550 rows were added. The September 22 gap remains, so no feature rebuild or replay was run.
- Re-fetched those 36 symbols through the existing append-only path in an isolated database copy, validated their source/content hashes and exact prior-row parity, then appended 18,775 bars and rebuilt the dated store. Main and dated old rows were preserved exactly. The dynamic September 18 baseline is now 3,182, with September 22 coverage at 271/3,182 and September 24 at 3,181/3,182; the remaining daily gap keeps feature rebuild and replay closed.
- Performed a read-only AgentMail Sent-label lookup for the September 24 scheduled report. One Sent-labeled message at 20:36:05 Central matched the configured recipient, one second after the local archive timestamp. The archived report records provider acknowledgement only; its body and message ID were not compared, and no new send occurred.
- Follow-up coverage verification added 2,909 of 2,911 missing September 22 baseline bars and closed the single September 24 gap. Coverage is 3,180/3,182 on September 21 and 22 and 3,182/3,182 on September 23 and 24. The same two symbols have no raw or adjusted Yahoo bars on both dates; this bounded result does not prove delisting or provider-wide unavailability. The staged cache passed strict reload, but no new replay result was accepted. The next aligned label requires the September 25 close; no promotion or external action occurred.

### 2026-09-22 - Historical feasibility and no-send automation hardening

- Defined and published the exact-pair hit-rate metric separately from portfolio returns. On the shared 106-window baseline slice, no tested route improved on protected v14.
- Recorded the current decision feasibility ceiling: 89 of 111 decisions, with growth-like and transition maximum feasible runs below five.
- Made report archives record preview, provider acknowledgement, or failure. A dry run now leaves the same-day dispatch marker unchanged and skips failure email and auto-heal state changes.
- Verified a no-send report preview with zero proposed actions. No live email, trade, broker write, scheduler mutation, or model promotion occurred in this verification.
- At the time of this no-send verification, external delivery had no AgentMail sent-label readback; a later read-only check is recorded in the following entry.

### 2026-09-22 - Read-only AgentMail status verification

- A read-only metadata lookup found one `sent`-labeled report at the same time as the stored 20:31 report archive, with the configured recipient matching.
- The message body was not retrieved, so exact content matching remains unverified. No email was sent by this task.

### 2026-08-08 - Public repository bootstrap

- Created the personal `ai-hedge-fund-plus-system` publication layer.
- Added an Atlan-inspired context-repository architecture without claiming Atlan affiliation.
- Added links for Agent Skills, Kronos, the upstream AI Hedge Fund project, and the market-data, broker-readback, and delivery providers used by the private runtime.
- Added preference-driven replication prompts, a portable skill, example configuration, evidence methodology, and publication audits.
- Recorded the current Cash App decision as redacted operator evidence: SNOW was added, while DXCM was not purchased because the $150 trade limit was reached.
- Preserved the rule that no sale may appear without a corresponding buy or an explicitly documented proceeds hold.

### 2026-08-10 - Daily benchmark and candidate gates

- Made daily, five-session, monthly, and open-position all-time benchmark comparisons use current market-close data instead of a stale user-confirmed daily percentage.
- Added a pending Fidelity funding record that is excluded from buying power until the operator confirms arrival.
- Enforced three ETF-only 04A cards, including standalone held-ETF reviews when no replacement gate fails.
- Enforced two daily 04B individual-stock cards, with one SNOW replacement and one future-add candidate that both beat SNOW's current forecasts and clear catalyst and momentum-exhaustion gates.
- Removed the obsolete model references and retained Kronos as the sole forecast-model link.

## Change-log practice

Every future system change should include its date, the advice or evidence that motivated it, the operator's decision, the files or rules changed, and the verification result. Failed ideas remain in the log with their failure condition.
