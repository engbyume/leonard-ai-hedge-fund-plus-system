# Decision log

This log records what the system advised, what the operator chose, why the system changed, and what remains unproven. It separates advice from execution and outcome.

## 2026-09-22 - Scheduled report sent-label readback

- Read-only AgentMail metadata found one `sent`-labeled report at 20:31 local, matching the timestamp of the stored live-candidate report and the configured recipient.
- The message body was not retrieved, so its content has not been compared with the archived render.
- This was readback of the existing scheduled run. No email was sent by this task, and the scheduler was not changed.

## 2026-09-22 - Historical gate and report-delivery verification

- Evidence: the approved working-list feasibility upper bound found 89 eligible decisions of 111. Maximum consecutive feasible runs were 5 defensive, 4 growth-like, 6 oil-like, and 3 transition. The strict five-week gate remains false.
- Accuracy method: count a qualified decision only when both distinct non-proxy picks land in the realized full-market top 30. On the shared 106-window slice, protected v14 scored 3/106. The stable-support diagnostic scored 2/106 causal, 3/106 global, and 2/106 state, with maximum streaks of 1. No route improved the baseline.
- System change: report metadata now distinguishes preview, provider acknowledgement, and delivery failure. Dry-run mode preserves the same-day dispatch marker and suppresses auto-heal state changes and failure email.
- Verification: the no-send render recorded `dry_run=true`, `delivery_status=previewed`, zero delivery attempts, and zero proposed actions. Isolated wrapper tests left the dispatch marker and auto-heal state unchanged. Focused automation tests passed 35 tests, and targeted private prototype tests passed 24 tests.
- Delivery status: a prior attempt logged a provider connection error. The later live-candidate report did not include an external sent-label readback, so delivery remains unverified. This verification sent no email and made no trade, broker write, scheduler change, or promotion.
- Limitation: the dry-run reported an unavailable optional local forecast backend. The render proves report generation only. It does not prove a fresh model forecast or investment return.

## 2026-07-11 - Trial start reported, baseline not archived

- Advice received: begin a two-month benchmark trial and compare the custom portfolio with the S&P 500 proxy.
- Operator decision: start the experiment with a custom mix intended to avoid fixed benchmark sector concentration.
- System change: establish a review window and a benchmark comparison section.
- Verification: later reports reference the start date, but an independently archived 2026-07-11 baseline is not present.
- Unproven: cumulative return and the user's later estimate of approximately 3% outperformance.

## 2026-07-18 - First archived checkpoint

- Advice received: continue the custom allocation while monitoring month spread and downside behavior.
- Evidence: archived report showed a +1.72 percentage-point month spread versus SPY, with the benchmark down over the month.
- Operator decision: continue the trial rather than declare victory.
- System change: retain benchmark, day, week, and month fields in the report.
- Verification: the checkpoint is published in the percentage-only table.
- Unproven: whether the spread came from intentional diversification, timing, or noise.

## 2026-07-19 through 2026-07-26 - Catalyst and breadth hardening

- Advice received: broaden the Cash App screening universe, research company catalysts, and penalize exhaustion instead of ranking raw trailing returns.
- Operator decision: keep the system focused on individual catalysts and custom sector exposure, while requiring platform availability to be confirmed separately.
- System change: retained a broad 700-row screening universe, added five-day returns, breadth, late-versus-early momentum, exhaustion fields, catalyst context, countercase, and invalidation signals.
- Verification: focused tests and dry renders passed in the private runtime; raw reports and candidate files are not published.
- Unproven: whether the expanded universe improves realized returns after costs and execution constraints.

## 2026-07-27 - Cross-market risk haircut

- Advice received: scan energy, shipping, rates, currency, credit, geopolitical, and policy proxies for unscheduled shocks that could affect a candidate's sector.
- Operator decision: keep the macro scan as a risk haircut rather than allowing it to replace company research.
- System change: added sector-sensitive uncertainty haircuts and required each candidate card to name relevant risks.
- Verification: a no-send report incorporated both scheduled and unscheduled event risk.
- Unproven: the predictive value of the haircut in future markets.

## 2026-07-30 - Delivery reliability repair

- Advice received: retry delivery of the already-rendered report without regenerating or changing the research output, and stop an interactive auto-healer from creating duplicate runs.
- Operator decision: keep delivery and research separate, with no duplicate email on a failed provider attempt.
- System change: added bounded provider retry, deterministic fallback narrative, and explicit generation-versus-delivery verification.
- Verification: a no-send end-to-end run produced a report and the focused suite passed.
- Unproven: provider reliability outside the verified run.

## 2026-08-03 - Momentum-exhaustion correction and replacement decision

- Advice received: DXCM had a tangible company catalyst, but its largest positive day contributed 71% of its positive five-day move. SNOW had a specific data-cloud and AI-platform thesis. YUMC was the replacement watchlist comparison after DXCM failed the exhaustion gate.
- Operator decision: keep the 60% threshold as a hard exclusion, do not use the 71% statistic as a positive signal, and treat SNOW and YUMC as watchlist or holding-state decisions subject to availability.
- System change: reject weekly replacement candidates at or above 60% largest-up-day share, invalidate stale DXCM watchlists, and keep watchlist cards distinct from trade instructions.
- Verification: the corrected report omitted DXCM from the eligible watchlist and retained the candidate availability warning.
- Unproven: whether YUMC or SNOW will outperform after the catalyst window and after execution costs.

## 2026-08-03 - Paired action invariant

- Advice received: a proposed Fidelity sale must not appear by itself.
- Operator decision: require a corresponding buy or explicitly approved proceeds hold for every sale.
- System change: preserve the reviewed paired sale-and-buy plan in the private action renderer, with settlement required before dependent buys. The public log omits the account-specific tickers.
- Verification: dry-render and focused tests confirmed no unmatched sale in the reviewed plan.
- Unproven: execution and settlement until an authorized account readback confirms them.

## 2026-08-08 - SNOW added, DXCM unbought because of the trade limit

- Advice received: the prior watchlist contained SNOW and DXCM as possible individual-stock candidates, with availability requiring manual confirmation.
- Operator decision: confirm SNOW was added to Cash App; do not record DXCM as held because a trade limit was reached.
- System change: update the private holdings source's confirmation date and preserve SNOW as a value-pending holding while retaining DXCM as unbought.
- Verification: the canonical JSON parses, the generator reads that file as its Cash App source of truth, and the next report is expected to show SNOW as held rather than as a new candidate.
- Unproven: SNOW's cost basis, current value, sale proceeds, and realized performance.

## 2026-08-10 - Daily benchmark refresh and one-held-stock watchlist correction

- Advice received: refresh Fidelity versus SPY from current market-close data every report, keep a pending contribution outside buying power until the operator confirms arrival, always show ETF coverage, and compare individual-stock candidates against SNOW without retaining the weaker YUMC idea.
- Operator decision: do not treat an expected contribution as landed; require one SNOW replacement candidate and one better future-add candidate while keeping all proposed sells paired with buys or an approved proceeds hold.
- System change: daily, weekly, monthly, and all-time open-position benchmark fields now use fresh report calculations; ETF coverage falls back to three standalone ETF reviews when no replacement gate fails; the Cash App stock ranking requires both forecast horizons to beat the held baseline and excludes YUMC.
- Verification: the 2026-08-10 report measured Fidelity at +0.30% for the day, +2.13% for the latest five-session week, +2.49% for the latest 21-session month, and +4.09% open-position since 2026-06-12, versus SPY at +0.61%, +3.51%, +2.87%, and +4.25%. The report used market closes through 2026-08-07 and was dry-rendered without delivery.
- Current watchlist result: GWRE is the SNOW replacement comparison and VEEV is the better future-add comparison. Official company releases provide the catalyst context, while forecasts remain model evidence rather than realized performance.
- Unproven: the pending contribution date, current cost basis, realized proceeds, and whether either watchlist candidate will outperform after availability, costs, and execution constraints.
