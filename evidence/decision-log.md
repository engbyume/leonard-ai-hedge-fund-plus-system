# Decision log

This log records what the system advised, what Jeremy chose, why the system changed, and what remains unproven. It separates advice from execution and outcome.

## 2026-09-25 05:17 Central - Historical price-source and store-preservation gate

- A fresh read-only audit confirmed the main price store reaches 2026-09-24 with 2,141,704 bars and SQLite integrity `ok`; the dated historical-universe store remains at 2026-08-24 with 2,040,294 bars and integrity `ok`.
- Saved metadata for the September 22 retry records 32 slices over 3,154 symbols, 243 returned symbols, and zero inserted bars. A 20-symbol sample of missing rows returned no Yahoo bars, while five existing-row controls returned five bars. A separate direct-history probe returned no bars for three sampled missing names while its control succeeded. These probes did not write to either store and do not establish provider-wide unavailability.
- The store materializer constructs a new temporary database and replaces the existing derived store from the narrower source. It was not run because the overlap is not proven and replacement could remove rows that are absent from the source.
- Official provider pages list a free Alpaca Basic plan and historical SIP access for requests ending more than 15 minutes in the past, but API authentication is required. No account setup or API request occurred. The free Tiingo and Alpha Vantage limits are too low for the full cohort. No data-source change, feature rebuild, replay, purchase, or promotion occurred.

## 2026-09-25 - Dated historical-universe store refresh

- The source manifest hash matched the dated store metadata, and every existing dated-store row was present in the main store with matching close, volume, source, fetch timestamp, and content hash.
- A candidate built in an isolated directory passed SQLite integrity, retained all 2,040,294 previous rows with zero mismatches, and added 66,550 rows through 2026-09-24. A byte-identical backup was retained before atomic promotion.
- The promoted store now contains 2,106,844 bars across 685 sessions and 3,214 symbols. September 22 remains incomplete at 243/3,154, so the feature cache was not rebuilt and no selector replay was run.
- No trade, broker write, email send, scheduler change, paid API request, purchase, or candidate or v14 promotion occurred.

## 2026-09-25 - Sent-label readback for scheduled report

- The local September 24 report archive is timestamped 20:36:04 Central and records `provider_acknowledged`, one attempt, and `delivery_verification=not_checked`.
- A read-only AgentMail list returned one `sent`-labeled message at 20:36:05 Central with the configured recipient, one second after the archive timestamp.
- The list reached its 100-message limit. No message body was retrieved, and the message ID was not compared with the archive. This confirms a matching sent-labeled message in the scheduled window but does not prove exact report-content matching.
- No email was sent by this task, and the scheduler was not changed.

## 2026-09-25 - No-send delivery and Cash App verification gate

- A direct no-send render recorded `previewed`, zero delivery attempts, and zero proposed orders. It did not call AgentMail.
- The rendered report identified the Cash App holdings snapshot as stale and required manual availability confirmation for the fallback watchlist. Live delivery now returns a blocked status before AgentMail when model-card availability is not confirmed.
- Focused mocked tests passed 36 cases, including sent-label readback, no-resend behavior, preview safety, and the Cash App delivery gate. Both wrapper shell syntax checks passed.
- No live email, trade, broker write, scheduler change, or promotion occurred. Optional Capitol Trades data was rate-limited and Kronos could not load; neither is treated as model or accuracy evidence.

## 2026-09-25 - Alternative data-source billing gate

- Official Financial Datasets pricing and terms state that each API request is billable; the pay-as-you-go option is $20 for 1,000 requests.
- The current account plan and remaining request allowance are unverified. No API request or purchase was made.
- Decision: keep the price database unchanged and do not use this source until an authorized allowance or spending instruction is confirmed. This review does not resolve the September 22 coverage gap or the missing HUBB row.

## 2026-09-25 - Follow-up no-account historical-price source screen

- Official StashGamma pages advertise free daily OHLCV history but require account sign-in and an API key. No account was created and no endpoint was called.
- HistoricalData.net describes its full adjusted archive as a one-time purchase. Its no-account endpoints expose product metadata and a few fixed sample rows, not the purchased current dataset. No purchase or data request occurred.
- Decision: neither option meets the existing no-account, no-cost requirement for resolving the historical-universe gap. Keep authenticated access and purchase gates closed. This bounded documentation screen does not establish that no other provider exists.

## 2026-09-25 - Dated-manifest ticker-alias audit

- A read-only comparison found 3,754 normalized manifest symbols and 3,282 distinct symbols in the main price store; 3,214 symbols were shared and 540 manifest symbols were absent from the store.
- For those 540 missing names, slash/dash and dot/dash punctuation variants produced zero matches among the main-store symbols.
- Decision: simple punctuation aliases do not explain the current missing set. This does not establish that a provider lacks data for every missing symbol, and it does not explain the separate September 22 daily-session gap. No provider request or database write occurred.

## 2026-09-25 - No-write Yahoo historical probe for unpriced manifest symbols

- Ran the existing adjusted-price helper in six sequential batches over the 540 normalized manifest symbols absent from the main store, for 2024-01-02 through the 2026-09-24 close. It returned non-empty bars for 36 symbols and 18,775 bars total.
- Re-read both SQLite stores after the probe. The main store remained at 2,141,704 bars and the dated store at 2,106,844; both integrity checks returned `ok`. No probe results were persisted.
- Decision: treat the returned bars as an ingestion lead only. Per-symbol completeness and the other 504 results remain unverified. Any backfill must use the existing append-only path with isolated-candidate and prior-row parity checks. Keep feature rebuilding and replay closed until the separate daily gap and aligned-label gates pass. No paid request, account access, database write, or promotion occurred.

## 2026-09-25 - Backfill of 36 unpriced manifest symbols

- Re-ran the existing free Yahoo adjusted-price helper over the 540 manifest symbols that had no main-store history. The staged run returned 18,775 bars for 36 symbols across six batches.
- The staged database passed integrity, all 2,141,704 prior main-store rows matched exactly, and the 18,775 new rows had `yfinance.adjusted_close` provenance and valid content hashes. They were appended with `INSERT OR IGNORE`, so prior rows were not overwritten.
- Rematerialized the dated store from the main store. All 2,106,844 previous dated rows matched exactly; the refreshed store has 2,125,619 bars across 3,250 symbols and 685 sessions through September 24.
- The new 36 symbols expanded the dynamic September 18 baseline from 3,154 to 3,182. September 22 coverage is 271/3,182 and September 24 is 3,181/3,182. The September 22 gap remains. Keep feature-cache rebuilding and replay closed until daily coverage and the complete aligned label are ready. No candidate or v14 promotion occurred.

## 2026-09-25 - Price boundary refresh and coverage gate

- The append-only refresh added 9,702 bars through the 2026-09-24 session for the fixed 3,154-symbol cohort. SQLite integrity passed, and all 2,132,002 pre-existing rows through 2026-09-18 remain present.
- Coverage was incomplete on September 22: 243 of 3,154 cohort symbols had rows. A bounded same-provider retry added zero rows. The September 24 session has 3,153 of 3,154 rows. Official exchange calendars do not list a September 22 closure.
- Decision: do not rebuild aligned features or run the selector with this incomplete daily boundary. Preserve the exact full-market top-30 target, prior-label cutoff, route and market-type gates, and protected v14.
- No prediction-accuracy improvement is inferred. No candidate was promoted, and no trade, broker write, email send, or scheduler change occurred.

## 2026-09-22 - Scheduled report sent-label readback

- Read-only AgentMail metadata found one `sent`-labeled report at 20:31 local, matching the timestamp of the stored live-candidate report and the configured recipient.
- The message body was not retrieved, so its content has not been compared with the archived render.
- This was readback of the existing scheduled run. No email was sent by this task, and the scheduler was not changed.

## 2026-09-22 - Historical gate and report-delivery verification

- Evidence: the approved working-list feasibility upper bound found 89 eligible decisions of 111. Maximum consecutive feasible runs were 5 defensive, 4 growth-like, 6 oil-like, and 3 transition. The strict five-week gate remains false.
- Accuracy method: count a qualified decision only when both distinct non-proxy picks land in the realized full-market top 30. On the shared 106-window slice, protected v14 scored 3/106. The stable-support diagnostic scored 2/106 causal, 3/106 global, and 2/106 state, with maximum streaks of 1. No route improved the baseline.
- System change: report metadata now distinguishes preview, provider acknowledgement, and delivery failure. Dry-run mode preserves the same-day dispatch marker and suppresses auto-heal state changes and failure email.
- Verification: the no-send render recorded `dry_run=true`, `delivery_status=previewed`, zero delivery attempts, and zero proposed actions. Isolated wrapper tests left the dispatch marker and auto-heal state unchanged. Focused automation tests passed 35 tests, and targeted private prototype tests passed 24 tests.
- Delivery status at this checkpoint: a prior attempt logged a provider connection error, and the live-candidate archive did not contain a sent-label readback. The later read-only metadata lookup is recorded above and confirms one sent-labeled report with a matching archive time and configured recipient; its body remains unverified. This verification sent no email and made no trade, broker write, scheduler change, or promotion.
- Limitation: the dry-run reported an unavailable optional local forecast backend. The render proves report generation only. It does not prove a fresh model forecast or investment return.

## 2026-07-11 - Trial start reported, baseline not archived

- Advice received: begin a two-month benchmark trial and compare the custom portfolio with the S&P 500 proxy.
- Jeremy's decision: start the experiment with a custom mix intended to avoid fixed benchmark sector concentration.
- System change: establish a review window and a benchmark comparison section.
- Verification: later reports reference the start date, but an independently archived 2026-07-11 baseline is not present.
- Unproven: cumulative return and the user's later estimate of approximately 3% outperformance.

## 2026-07-18 - First archived checkpoint

- Advice received: continue the custom allocation while monitoring month spread and downside behavior.
- Evidence: archived report showed a +1.72 percentage-point month spread versus SPY, with the benchmark down over the month.
- Jeremy's decision: continue the trial rather than declare victory.
- System change: retain benchmark, day, week, and month fields in the report.
- Verification: the checkpoint is published in the percentage-only table.
- Unproven: whether the spread came from intentional diversification, timing, or noise.

## 2026-07-19 through 2026-07-26 - Catalyst and breadth hardening

- Advice received: broaden the Cash App screening universe, research company catalysts, and penalize exhaustion instead of ranking raw trailing returns.
- Jeremy's decision: keep the system focused on individual catalysts and custom sector exposure, while requiring platform availability to be confirmed separately.
- System change: retained a broad 700-row screening universe, added five-day returns, breadth, late-versus-early momentum, exhaustion fields, catalyst context, countercase, and invalidation signals.
- Verification: focused tests and dry renders passed in the private runtime; raw reports and candidate files are not published.
- Unproven: whether the expanded universe improves realized returns after costs and execution constraints.

## 2026-07-27 - Cross-market risk haircut

- Advice received: scan energy, shipping, rates, currency, credit, geopolitical, and policy proxies for unscheduled shocks that could affect a candidate's sector.
- Jeremy's decision: keep the macro scan as a risk haircut rather than allowing it to replace company research.
- System change: added sector-sensitive uncertainty haircuts and required each candidate card to name relevant risks.
- Verification: a no-send report incorporated both scheduled and unscheduled event risk.
- Unproven: the predictive value of the haircut in future markets.

## 2026-07-30 - Delivery reliability repair

- Advice received: retry delivery of the already-rendered report without regenerating or changing the research output, and stop an interactive auto-healer from creating duplicate runs.
- Jeremy's decision: keep delivery and research separate, with no duplicate email on a failed provider attempt.
- System change: added bounded provider retry, deterministic fallback narrative, and explicit generation-versus-delivery verification.
- Verification: a no-send end-to-end run produced a report and the focused suite passed.
- Unproven: provider reliability outside the verified run.

## 2026-08-03 - Momentum-exhaustion correction and replacement decision

- Advice received: DXCM had a tangible company catalyst, but its largest positive day contributed 71% of its positive five-day move. SNOW had a specific data-cloud and AI-platform thesis. YUMC was the replacement watchlist comparison after DXCM failed the exhaustion gate.
- Jeremy's decision: keep the 60% threshold as a hard exclusion, do not use the 71% statistic as a positive signal, and treat SNOW and YUMC as watchlist or holding-state decisions subject to availability.
- System change: reject weekly replacement candidates at or above 60% largest-up-day share, invalidate stale DXCM watchlists, and keep watchlist cards distinct from trade instructions.
- Verification: the corrected report omitted DXCM from the eligible watchlist and retained the candidate availability warning.
- Unproven: whether YUMC or SNOW will outperform after the catalyst window and after execution costs.

## 2026-08-03 - Paired action invariant

- Advice received: a proposed Fidelity sale must not appear by itself.
- Jeremy's decision: require a corresponding buy or explicitly approved proceeds hold for every sale.
- System change: preserve the paired plan of SELL XLV with BUY CIBR, QQQ, and XLF in the private action renderer, with settlement required before dependent buys.
- Verification: dry-render and focused tests confirmed no unmatched sale in the reviewed plan.
- Unproven: execution and settlement until an authorized account readback confirms them.

## 2026-08-08 - SNOW added, DXCM unbought because of the trade limit

- Advice received: the prior watchlist contained SNOW and DXCM as possible individual-stock candidates, with availability requiring manual confirmation.
- Jeremy's decision: confirm SNOW was added to Cash App; do not record DXCM as held because the $150 trade limit was reached.
- System change: update the private holdings source's confirmation date and preserve SNOW as a value-pending holding while retaining DXCM as unbought.
- Verification: the canonical JSON parses, the generator reads that file as its Cash App source of truth, and the next report is expected to show SNOW as held rather than as a new candidate.
- Unproven: SNOW's cost basis, current value, sale proceeds, and realized performance.

## 2026-08-10 - Daily benchmark refresh and one-held-stock watchlist correction

- Advice received: refresh Fidelity versus SPY from current market-close data every report, keep the pending contribution outside buying power until Jeremy confirms arrival, always show ETF coverage, and compare individual-stock candidates against SNOW without retaining the weaker YUMC idea.
- Jeremy's decision: expect a Fidelity contribution during the current week but do not treat it as landed; require one SNOW replacement candidate and one better future-add candidate while keeping all proposed sells paired with buys or an approved proceeds hold.
- System change: daily, weekly, monthly, and all-time open-position benchmark fields now use fresh report calculations; ETF coverage falls back to three standalone ETF reviews when no replacement gate fails; the Cash App stock ranking requires both forecast horizons to beat the held baseline and excludes YUMC.
- Verification: the 2026-08-10 report measured Fidelity at +0.30% for the day, +2.13% for the latest five-session week, +2.49% for the latest 21-session month, and +4.09% open-position since 2026-06-12, versus SPY at +0.61%, +3.51%, +2.87%, and +4.25%. The report used market closes through 2026-08-07 and was dry-rendered without delivery.
- Current watchlist result: GWRE is the SNOW replacement comparison and VEEV is the better future-add comparison. Official company releases provide the catalyst context, while forecasts remain model evidence rather than realized performance.
- Unproven: the pending contribution date, current cost basis, realized proceeds, and whether either watchlist candidate will outperform after availability, costs, and execution constraints.
