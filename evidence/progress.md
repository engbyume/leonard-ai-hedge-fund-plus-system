# Progress narrative

## Post-backfill update, 2026-09-25 08:40 Central

The existing no-write Yahoo probe found usable history for 36 of 540 manifest symbols with no main-store prices. A staged rerun returned 18,775 adjusted bars. The append preserved all 2,141,704 previous main-store rows, and the dated-store rebuild preserved all 2,106,844 previous rows. The main store now has 2,160,479 bars across 3,318 symbols. The dated store now has 2,125,619 bars across 3,250 symbols and 685 sessions through September 24. The 18,775 new bars passed source/content-hash checks.

The dynamic September 18 baseline is now 3,182 symbols. September 22 has 271/3,182 rows, and September 24 has 3,181/3,182. The earlier status below records the pre-backfill 3,154-symbol boundary and remains as historical evidence. September 22 is still incomplete, and the September 25 closing label is not available at this morning check. No feature-cache rebuild, selector replay, accuracy claim, or candidate promotion was made.

## Status as of 2026-09-25

The fixed-cohort price database was refreshed through the 2026-09-24 session. The refresh added 9,702 bars across 3,154 baseline symbols. The earlier rows through 2026-09-18 were preserved, and SQLite integrity passed.

Coverage is incomplete for one scheduled session: 2026-09-22 has 243 of 3,154 rows. A bounded same-provider retry returned no new rows. The 2026-09-24 session has 3,153 of 3,154 rows. Official Nasdaq and NYSE calendars show no scheduled closure on September 22. Treat this as an unresolved source-coverage gap, not as evidence that the session was closed.

The aligned feature cache still ends at label session 2026-09-18. The 2026-09-25 closing label is not yet available, and the intervening daily coverage is incomplete. No feature cache rebuild, selector replay, accuracy claim, or candidate promotion was made from this refresh.

An alternative-source review found that Financial Datasets bills every API request; its pay-as-you-go option is $20 per 1,000 requests. The current account plan and remaining allowance were not verified, and no request was made. This review adds no price-coverage evidence and does not resolve the September 22 or HUBB gaps.

A direct no-send report preview after delivery-gate hardening recorded `delivery_status=previewed`, zero delivery attempts, zero proposed orders, and a 38,762-byte HTML render. The preview labeled the Cash App snapshot stale and marked model-card availability as unverified; a live delivery now blocks until the confirmation gate passes. Thirty-six focused mocked tests and both wrapper syntax checks passed. A Capitol Trades request returned HTTP 429 and Kronos did not load because Torch was unavailable; neither result supports an accuracy claim. No email was sent.

A fresh read-only check confirmed the main price store passes integrity at 2,141,704 bars through 2026-09-24. The dated historical-universe store was then rematerialized from the main store under the unchanged dated IWB/IWM manifest. It now passes integrity with 2,106,844 bars across 685 sessions and 3,214 symbols. A byte-level backup was retained before promotion. All 2,040,294 prior rows match exactly, and 66,550 rows were added. Coverage remains 3,152 on September 21, 243 on September 22, 3,154 on September 23, and 3,153 on September 24.

The source-mapping check found 3,754 symbols in the dated proxy, 3,214 stored symbols, and 540 with insufficient historical price coverage. The main store contains all existing dated-store symbols and 68 additional symbols outside the dated proxy. The September 22 retry metadata covers 3,154 symbols in 32 slices; 243 returned and zero inserted. A bounded Yahoo probe returned no bars for 20 sampled missing symbols, while five in-store controls returned five bars. A separate direct-history probe returned no bars for three sampled missing symbols while one control succeeded. These samples do not prove provider-wide unavailability.

Official provider documentation identifies Alpaca Basic as a free candidate for authenticated historical SIP queries older than 15 minutes. Its multi-symbol historical-bars endpoint supports corporate-action adjustment, but access requires API credentials and no account or request was made. Tiingo's free tier is limited to 500 unique symbols per month; Alpha Vantage's standard free service is limited to 25 requests per day. Stooq's verification gate was not bypassed, and Financial Datasets remains billable per request. Operator direction is pending on whether to use an existing Alpaca Basic account or authorize free setup. No feature cache rebuild, selector replay, or promotion occurred.

A follow-up documentation-only screen found that StashGamma's free daily OHLCV API requires account sign-in and an API key. HistoricalData.net sells the full adjusted archive; unauthenticated access returns metadata and a few fixed sample rows only. Neither option supplies no-account, no-cost current history for the remaining gap. No provider endpoint was called, no account was created, and no purchase occurred. This screen is bounded and is not an exhaustive provider survey.

A separate read-only ticker-alias audit compared the 3,754-symbol dated manifest union with the 3,282 distinct symbols in the main store. The sets shared 3,214 symbols; 540 manifest symbols were absent from the store. Slash/dash and dot/dash variants of those missing names produced zero matches in the main-store symbols. This rules out only simple punctuation aliases, not provider-wide unavailability, and does not resolve the September 22 session gap. No API call or database write occurred.

A six-batch no-write historical Yahoo probe covered those 540 unpriced manifest symbols from 2024-01-02 through the 2026-09-24 close. It returned 18,775 adjusted-price bars for 36 symbols. The remaining 504 returned no bars in this probe, but provider-wide unavailability is not inferred. Both databases passed post-probe integrity checks with unchanged row counts, and no result was persisted. Any future ingestion must preserve existing rows and provenance; the separate September 22 daily gap and aligned-label gate still block replay.

A read-only AgentMail list returned one Sent-labeled message at 20:36:05 Central with the configured recipient, one second after the September 24 archive timestamp. The archive metadata records `provider_acknowledged`, one attempt, and verification not checked. The list returned its 100-message limit; the message body and message ID were not compared with the archive, so exact content matching remains unverified. No email was sent by this task.

## Status as of 2026-09-22

The latest aligned historical boundary contains 123 windows and 111 evaluated decisions through label session 2026-09-18. Both realized top-30 members were in the current 677-symbol working list for 89 decisions. This is decision-level feasibility, not proof of historical platform availability. No dated Cash App membership ledger was found, and the expanded 1,050-symbol manifest remains unverified.

The maximum consecutive feasible runs were 5 defensive, 4 growth-like, 6 oil-like, and 3 transition windows. The exact five-week gate remains false because growth-like and transition cannot sustain five consecutive feasible decisions on this boundary.

For accuracy, the exact-pair hit rate counts a window only when both distinct non-proxy picks reach the realized full-market top 30. On the 106 shared decision-label windows, protected v14 recorded 3 hits. The stable-support diagnostic recorded 2 causal, 3 global, and 2 state-route hits, with maximum streaks of 1. The global route tied v14; no route improved it. The additional five decisions through the 2026-09-18 label added no qualified pairs. No candidate was promoted.

The canonical report generator completed a no-send preview with `dry_run=true`, `delivery_status=previewed`, and zero proposed actions. This verification made no AgentMail call. A read-only AgentMail metadata lookup found one `sent`-labeled report at the same 20:31 time as the earlier live-candidate archive, with the configured recipient matching. The message body was not retrieved, so exact content matching remains unverified. The preview also reported that an optional local forecast backend could not load; its output is not treated as fresh model-accuracy evidence.

Focused verification passed 35 canonical automation tests and 24 targeted private prototype tests. Shell syntax and Python compilation passed. The isolated dry-run wrapper checks preserved the dispatch marker and auto-heal state.

## Status as of 2026-08-10

The latest redacted machine observation is the 2026-08-10 report, using market closes through 2026-08-07. The experiment's own report text says a two-month trial began on 2026-07-11, but a separately archived 2026-07-11 baseline is not present in the public evidence. The all-time figure is therefore an open-position comparison from the first confirmed position date, not a verified trial-start result.

Jeremy believes the portfolio may be about 3% ahead of the S&P since the start. That is retained as a user-reported hypothesis, not a measured claim. The latest month spread is -0.38 percentage points versus SPY, and the latest all-time open-position spread is -0.16 percentage points, so the available evidence does not support saying that the system is consistently beating the benchmark.

## What the observations suggest

- On 2026-07-18, the portfolio's month return was 1.72 percentage points better than SPY while both the portfolio and benchmark were measured in a weak daily or monthly environment. This is consistent with the intended diversification and custom-weighting thesis, but it does not prove causation.
- On 2026-07-22, the month spread was nearly neutral at -0.10 percentage points while the benchmark was slightly ahead, showing that the advantage was not persistent across every checkpoint.
- On 2026-07-30, all reported periods were zero versus zero. This is treated as neutral or low-information rather than as evidence of skill.
- On 2026-08-03, the month spread was positive by 0.22 percentage points, but the day and week spreads were negative.
- On 2026-08-05, the portfolio was up 1.81% for the month versus SPY at 2.95%, a -1.14 percentage-point spread. This is the clearest current warning against overclaiming success.
- On 2026-08-10, the latest report showed Fidelity behind SPY by 0.31 points for the day, 1.38 points for the latest five-session week, 0.38 points for the latest 21-session month, and 0.16 points for the open-position comparison since 2026-06-12. The report excluded the expected contribution until arrival is confirmed.

## Why the system changed

The operating rules became more catalyst-first and exhaustion-aware after the system surfaced candidates whose returns were driven by one unusually large day. A company-specific catalyst is now required for an individual-stock thesis, while five-day breadth, late-versus-early momentum, and largest-up-day share can reduce or reject a candidate. Cross-market event risk, availability uncertainty, settlement, and paired sell-buy checks were added as explicit gates.

## Latest operator decision

On 2026-08-08, Jeremy confirmed that SNOW had been added to Cash App. DXCM was not purchased because the $150 trade limit was reached. The 2026-08-10 private report keeps an expected contribution outside buying power until arrival is confirmed, shows three standalone ETF reviews when no ETF fails its replacement gate, and compares GWRE and VEEV against SNOW. YUMC is excluded from the candidate universe. The public record contains no account value, cost basis, recipient, or order identifier.

## What must be measured next

The next reliable update should provide a verified baseline, comparable portfolio and SPY dates, cash-flow treatment, costs, drawdown, downside capture, and the current review date. Until then, the evidence is useful for system iteration but insufficient for a durable performance conclusion.
