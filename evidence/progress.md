# Progress narrative

## Documentation reconciliation, October 30, 2026

The public-doc review candidate was created from the current main-line base. Local AIHF material and the prior remote history contain different meanings for several source-register IDs; the candidate gives each claim a unique ID. The dirty checkout also contains unrelated project and system-maintenance material, which is excluded from the candidate. The publication audit passed 45 required-file and redacted-evidence checks on the AIHF-only candidate. The validator also checks for duplicate source IDs. This entry records local review only; no changes have been published. Source: SRC-268.

## Non-proxy full-market source access screen, October 9, 2026

The official-source screen found no ready path that supplies exact point-in-time full-market membership and complete daily price labels without an account or purchase. QuantConnect is the closest candidate: its broad non-OTC Coarse Universe has free Cloud access, but Cloud use requires an account, its latest actual data date and immutable history vintage remain unverified, and local bulk downloads are paid. Its `ScaledRaw` mode uses corporate actions before QuantBook `EndDate`; per-decision cutoff safety still needs an end-to-end check. LSEG describes selected historical index files with quarterly-in-arrears updates. NYSE Daily TAQ has a purchase path and no index membership. SEC EDGAR needs no authentication but has no daily prices or index constituents. This bounded screen does not prove no account-specific or proprietary source exists. No login, account query, provider request, data query, download, purchase, or promotion occurred. See SRC-227.

## QuantConnect data-access scope as of October 8, 2026

Official QuantConnect documentation distinguishes free Cloud U.S. equity access from paid local bulk downloads. Its Coarse Universe is a daily universe of all U.S.-traded stocks, about 8,000 per day, with closing price and volume. Cloud use still requires an organization/account. This broader universe does not establish exact membership for the unchanged replay target or historical Cash App eligibility. No account or dataset was accessed. Source: SRC-218.

## Historical membership and Cash App availability source recheck, October 8, 2026

LSEG's public data pages list historical constituent and weight files for selected indices, typically quarterly in arrears. Its public Russell reconstitution page shows dated additions and deletions and describes later daily adjustments, but it does not establish a complete daily Russell 3000 membership-and-weight history. QuantConnect's historical ETF Constituents product is a separate ETF-holdings universe, not Russell membership; local bulk downloads are paid. Cash App's stock page directs customers to in-app search, and its agreement permits the offered list to change without notice. The public pages reviewed do not establish a dated historical Cash App roster. No account, in-app lookup, data query, download, or purchase occurred. The full-market target, frozen top-65, and five-week gate remain unchanged. Sources: SRC-219 and SRC-220.

## Approved-map feasibility and Cash App availability as of October 8, 2026

The dated September 21, 2026 approved-map artifact records 700 raw CSV rows and 677 usable approved symbols. Its realized-label feasibility upper bound evaluated 111 decisions and found two approved, non-proxy members of the diagnostic realized top 30 in 89 decisions. Maximum consecutive feasible runs were 5 defensive, 4 growth-like, 6 oil-like, and 3 transition. This was an upper-bound check only; it selected no symbols. The artifact found no historical membership authority, and its 1,050-row expanded manifest has zero operator-confirmed and zero platform-verified symbols. Under this tested boundary, growth-like and transition cannot reach five consecutive feasible decisions. The result does not prove exact historical full-market membership, selector performance, or Cash App availability.

The Cash App Investing agreement, last updated February 12, 2026, allows the available-security list to change at any time without prior notice. A frozen present-day approved CSV cannot establish historical availability. The approved list and exact-two/full-market promotion contract remain unchanged. No account lookup, provider request, purchase, candidate selection, or promotion occurred. Sources: SRC-214 and SRC-215.

## Nightly report path revalidation as of October 8, 2026

The loaded LaunchAgent is idle after 15 runs with last exit code 0. Its environment has neither AIHF_YAHOO_EXPRESS_PERMISSION_CONFIRMED nor AIHF_EMAIL_SEND_AUTHORIZED. The latest report remains dated September 25, with dry_run=false, delivery_status=blocked_cash_app_availability, zero delivery attempts, and delivery_verification=not_applicable. This archived report is not a current preview.

The offline renderer, dry-run dispatch, auto-heal authorization, generator import-safety, and Yahoo source-guard suite passed 47 tests through the canonical Python runner with UV_OFFLINE=1. Nine Cash App approval-policy checks also passed. AgentMail calls are mocked, and the retry tests inject OSError fixtures. The report HTML, text, metadata, dispatch markers, and dispatch-log fingerprint were unchanged before and after the checks.

The canonical runbook still blocks a generator dry run until Yahoo express permission is documented. No current report render, provider request, send, scheduler change, or promotion occurred. Source: SRC-216.

## Private adapter and source-gate verification as of October 8, 2026

Six optional forecast-adapter tests passed using fake model outputs, including the non-production opt-in boundary. Five Yahoo source-access guard tests passed with mocked provider functions. They cover the disabled path, an authorized mocked path, and the independent Financial Datasets route. No model weights, inference, Yahoo request, or data refresh occurred. These checks verify local guard behavior only; they do not grant permission, establish full-market data coverage, improve prediction accuracy, or pass the promotion gate. Source: SRC-217.

## Historical research status as of October 7, 2026

The historical selector remains research-only and has not passed the five-consecutive-qualified-week promotion gate. Read-only queries found 2,163,389 bars across 3,318 symbols in the raw store and 2,128,529 bars across 3,250 symbols in the materialized evaluator store. Both end on September 24, 2026; both return zero rows for September 25 and 26. These counts describe stored data, not exact point-in-time Russell 3000 membership, listing and delisting history, or Cash App availability.

Protected v14 remains unchanged at SHA-256 `3119bb102d9786368c3c49d84ae236a4092607119b4d2dada151102c77cb0384`, with 106 evaluated windows, 3 qualified weeks, a longest streak of 1, and `pass=false`. Its last decision is August 13 and its last label is August 20. The required dated approval ledger is missing. No candidate or v14 promotion occurred in this revalidation.

The latest report artifacts are still from September 25, with `delivery_status=blocked_cash_app_availability` and zero delivery attempts. A read-only health and LaunchAgent recheck at 20:47 CDT shows the calendar job idle after 15 runs, with last exit 0. Its 20:30 dispatch log records the Yahoo permission gate skipping profile refresh, report generation, and delivery. No current report render or live delivery was verified.

Yahoo express permission remains undocumented, so the canonical runbook blocks the generator dry run. The approval-policy suite passed 9 offline checks, and the private Yahoo source-access suite passed 5 mocked checks. These do not prove a current report render or live delivery.

The October 7 official-source screen identified Intrinio USCOMP as a conditional per-date US-market price candidate, but a bounded Python/TOML and provider-named file search found no Intrinio integration or local data artifact in the inspected AIHF app and canonical automation roots. This search does not cover other storage or external accounts. Intrinio access requires a separate account or trial gate and further scope and terms validation. The dated approval ledger is still missing. No account, API call, data pull, or purchase occurred. Sources: SRC-204 and SRC-205. Keep all universe and promotion gates unchanged.

## Official exact-universe source recheck as of October 7, 2026

Current FTSE Russell access pages say historical constituent and weight files are available for a selection of indices, published quarterly in arrears, while Russell historical index-level data is a separate product. The public pages do not confirm complete daily Russell 3000 constituent history. QuantConnect's US Equity Security Master covers corporate actions and delistings for a broad US equity set, but is not underlying price data; its US Equities price dataset requires a separate AlgoSeek license. These sources do not establish a free, accessible full-market membership and price feed for the replay. No account, login, API request, data pull, sales request, or purchase occurred. Source: SRC-212.

## Historical-window cache freshness as of October 7, 2026

The default cache was last modified August 24, its metadata August 25, and the local price database September 25. `load_windows(..., strict_read_only=True)` rejected the cache as stale or mismatched. No canonical cache refresh was attempted. An initial in-memory rebuild exceeded the local fallback's 60-second limit and returned no window or model metrics. A later isolated trusted-session rebuild and strict readback are recorded below. No provider request occurred. Source: SRC-209. The stored v14 artifact remains the frozen baseline; the follow-up diagnostic does not replace it.

## Trusted-session diagnostic follow-up as of October 7, 2026

The existing trusted-session rebuild helper rebuilt the complete current window set into a temporary cache. Strict readback passed for 123 valid windows, with last decision September 11 and last label September 18. The current evaluator covered 110 windows, produced 3 qualified weeks, reached a maximum streak of 1, and kept `pass=false`.

On the 106 decision dates shared with protected v14, the diagnostic produced 25 picks in the realized top 30 across 22 windows. V14 produced 26 hits across 23 windows. Mean selected realized rank worsened from 1301.91 to 1383.00. The diagnostic uses `official_blackrock_iwb_iwm_dated_holdings_csv`, a dated IWB/IWM proxy. It does not prove exact full-market membership or Cash App availability, so the candidate was rejected and not promoted. The canonical database, default cache, and v14 hashes remained unchanged. The temporary cache was removed. Source: SRC-210.

## Nightly report and delivery checks as of October 7, 2026

The loaded LaunchAgent is idle after 15 runs with last exit code 0. The latest report artifacts remain dated September 25, with `delivery_status=blocked_cash_app_availability` and zero delivery attempts. No report render or live delivery ran.

The canonical runbook requires documented Yahoo express permission before generator dry runs, direct generation, or scheduled dispatch. Permission remains undocumented, so the generator dry run was not attempted. An offline suite passed 47 mocked renderer, dispatch, import-safety, auto-heal authorization, and private source-guard tests; the Cash App approval-policy checks passed 9 cases. These tests use temporary files and mocks and make no provider call or send. Source: SRC-211.

## Portfolio report status as of August 10, 2026

The latest redacted machine observation is the August 10, 2026 report, using market closes through August 7, 2026. The experiment's own report text says a two-month trial began on July 11, 2026, but a separately archived July 11, 2026 baseline is not present in the public evidence. The all-time figure is therefore an open-position comparison from the first confirmed position date, not a verified trial-start result.

Jeremy believes the portfolio may be about 3% ahead of the S&P since the start. That is retained as a user-reported hypothesis, not a measured claim. The latest month spread is -0.38 percentage points versus SPY, and the latest all-time open-position spread is -0.16 percentage points, so the available evidence does not support saying that the system is consistently beating the benchmark.

## What the observations suggest

- On July 18, 2026, the portfolio's month return was 1.72 percentage points better than SPY while both the portfolio and benchmark were measured in a weak daily or monthly environment. This is consistent with the intended diversification and custom-weighting thesis, but it does not prove causation.
- On July 22, 2026, the month spread was nearly neutral at -0.10 percentage points while the benchmark was slightly ahead, showing that the advantage was not persistent across every checkpoint.
- On July 30, 2026, all reported periods were zero versus zero. This is treated as neutral or low-information rather than as evidence of skill.
- On August 3, 2026, the month spread was positive by 0.22 percentage points, but the day and week spreads were negative.
- On August 5, 2026, the portfolio was up 1.81% for the month versus SPY at 2.95%, a -1.14 percentage-point spread. This is the clearest current warning against overclaiming success.
- On August 10, 2026, the latest report showed Fidelity behind SPY by 0.31 points for the day, 1.38 points for the latest five-session week, 0.38 points for the latest 21-session month, and 0.16 points for the open-position comparison since June 12, 2026. The report excluded the expected contribution until arrival is confirmed.

## Why the system changed

The operating rules became more catalyst-first and exhaustion-aware after the system surfaced candidates whose returns were driven by one unusually large day. A company-specific catalyst is now required for an individual-stock thesis, while five-day breadth, late-versus-early momentum, and largest-up-day share can reduce or reject a candidate. Cross-market event risk, availability uncertainty, settlement, and paired sell-buy checks were added as explicit gates.

## Latest operator decision

On August 8, 2026, a user-confirmed portfolio update changed the held-position state in the canonical snapshot. Unpurchased candidates remained outside holdings, and a pending contribution remained outside buying power until arrival was confirmed. The public record omits security names, transaction limits, balance values, and order identifiers. This is workflow evidence, not a broker-verified transaction or performance result.

## What must be measured next

The next reliable update should provide a verified baseline, comparable portfolio and SPY dates, cash-flow treatment, costs, drawdown, downside capture, and the current review date. Until then, the evidence is useful for system iteration but insufficient for a durable performance conclusion.

## WRDS FTSE Russell catalog revalidation, October 8, 2026

The official WRDS catalog was rechecked against the candidate already recorded in SRC-189 and the stale sample boundary in SRC-190. It still lists FTSE Russell US under schema ftse_russell_us, December 29, 1978 through August 31, 2026, with monthly updates and 670.8 MiB. The current page says it was last updated September 10, 2026 and specifies no identifiers. Its linked data dictionary redirects to WRDS login, so public evidence still does not establish Russell 3000 constituent coverage, field schema, membership interval, inactive-security history, or permitted-use rights. No login, sample access, account, data request, download, purchase, or contact occurred. Keep this candidate only. Exact full-market membership and the frozen Cash App top-65 remain unresolved. Source: SRC-221.

## Public Russell change-file availability, October 8, 2026

LSEG's public pages expose final Russell 3000 additions and deletions for 2024, 2025, and 2026. Its IPO additions page says additions are quarterly, with 2Q and 4Q documents included with the semi-annual reconstitution lists. The subscription-data page describes a Daily Events Monitor for changes completed during the prior two weeks and pending changes, and historical constituent and weight files for selected indices updated quarterly in arrears. The Index Notices page says full announcement versions require registration and are available to subscribers.

These public lists provide partial dated event evidence. The reviewed public material does not establish a complete point-in-time Russell 3000 roster or membership-change history for every weekly decision, or inactive-security history. This scoped finding does not claim that no full-history product exists. No files were downloaded locally; no login, sample, account, data request, purchase, or contact occurred. The exact full-market target, frozen Cash App top-65, protected v14, and five-consecutive-week promotion gate remain unchanged. Source: SRC-222.


## October 9, 2026 - Matched-window candidate comparison

The official evaluator compared a stable-support candidate with its baseline on the same 110 decision dates. There were zero label-session mismatches, zero stored-rank mismatches, and zero contract violations.

| Route | Top-30 name hits | Both-pick windows | Longest streak | Mean selected realized rank |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 27 | 3 | 1 | 1263.432 |
| Causal | 15 | 2 | 1 | 1305.741 |
| Global | 15 | 3 | 1 | 1294.455 |
| State | 21 | 2 | 1 | 1160.014 |

The state route improved mean rank but did not improve name-hit or both-pick counts. No route improved validated prediction accuracy or reached five consecutive qualified weeks. The maximum market-type pair streak was 1, and growth-like pair windows were 0. Protected v14 remains unchanged at 106 windows, 3 qualified weeks, longest streak 1, and `pass=false`.

This result is diagnostic, not a promotion. It uses a dated IWB/IWM proxy, not exact point-in-time full-market membership. The price stores end September 24, the latest complete label is September 18, the September 22 receipt and broad-store row counts are unreconciled, and the dated approval ledger is absent. No provider or account query, cache refresh, promotion, trade, send, schedule change, or publication occurred. Source: SRC-226.
