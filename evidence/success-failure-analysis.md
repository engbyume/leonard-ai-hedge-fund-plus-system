# Historical replay success and failure analysis

Date: August 20, 2026

## October 7, 2026 current-state revalidation

Outcome: not complete. The strict research gate remains false and the required source and approval evidence are still missing.

| Requirement | Current evidence |
| --- | --- |
| Five consecutive qualified weeks and improved accuracy | Protected v14 has 106 windows, 3 qualified weeks, longest streak 1, and `pass=false`. Its last decision and label are August 13 and August 20. A later matched-date proxy diagnostic regressed v14 and did not establish full-market accuracy improvement. Source: SRC-210. |
| Full-market top-30, exact two, and strict prior labels | The raw and materialized stores end September 24, with no September 25 or 26 rows. Stored symbol counts do not establish exact point-in-time Russell membership, listing or delisting coverage, or Cash App availability. A later IWB/IWM proxy replay remains diagnostic-only. |
| Frozen Cash App top-65 and dated approval | No availability list was changed. The dated approval ledger is absent, so no final pick set can be validated. |
| Causal, global, state-route, and market-type gates | The protected v14 contract remains unchanged and false. No new route or market-type result was promoted. |
| Report generation, rendering, and delivery | The latest report remains dated September 25 with `blocked_cash_app_availability` and zero attempts. The canonical runbook bars a generator dry run until documented Yahoo express permission exists. No current render or delivery ran. |
| Nightly schedule and failure handling | Read-only health at 16:26 CDT showed the job not running, 14 runs, and last exit 0. Four mocked dispatch checks and one mocked auto-heal email-authorization check passed. They do not prove loaded send state or a live delivery. |
| Conditional historical-source candidates | Intrinio USCOMP daily exchange prices remain conditional; account/trial access, exact eligible-security coverage, and plan terms are unverified. The official LSEG pages list historical constituents only for selected indices, quarterly in arrears, without confirming complete daily Russell 3000 history. QuantConnect's Security Master provides corporate-action/delisting records, not equity price bars; US Equities prices require a separate AlgoSeek license. No source was accessed. See SRC-204, SRC-205, and SRC-212. |
| Forecast adapter, heartbeat, and system-map documentation | No changes were made in this audit. This audit did not revalidate model performance, heartbeat active state, or image rendering. |

No source request, provider call, trade, broker write, email, scheduler change, v14 or candidate promotion, data purchase, new account, commit, push, or publication occurred. The Yahoo source gate and approval gates remain closed. Source: SRC-203.

## October 7, 2026 trusted-session diagnostic follow-up

After the 20:47 current-state audit, the existing trusted-session rebuild helper ran against the current materialized price store in an isolated temporary cache. It produced 123 valid windows through decision September 11 and label September 18. Strict cache readback passed. The evaluator covered 110 windows and still produced only 3 qualified weeks, a maximum streak of 1, and `pass=false`.

The 106 decision dates shared with v14 provide the matched comparison. The diagnostic had 25 top-30 hits across 22 windows, while v14 had 26 across 23. Mean selected realized rank worsened from 1301.91 to 1383.00. This was a regression on the dated IWB/IWM holdings proxy, not a full-market validation. The exact full-market and Cash App availability gates remain unmet. The canonical database, default cache, and v14 hashes stayed unchanged, and the temporary cache was removed. Source: SRC-210.

## October 7, 2026 mocked renderer, dispatch, and failure checks

The focused offline test batch passed 47 tests across the portfolio renderer, dry-run dispatch wrapper, auto-heal email authorization, generator import safety, and private Yahoo source guard. Nine Cash App approval-policy checks also passed. The delivery tests patch AgentMail and use temporary report archives; the dispatch tests copy wrapper scripts into temporary directories. No provider request, send, scheduler action, or live generator run occurred.

The loaded nightly LaunchAgent is idle after 15 runs with last exit code 0. The latest report remains September 25 with Cash App availability blocking delivery and zero attempts. The source-permission gate prevents a canonical generator dry run while Yahoo express permission remains undocumented. These checks confirm mocked behavior only. Source: SRC-211.

## October 3, 2026 completion and blocker audit

Outcome: not complete. Verified local work does not clear the strict research or current-report requirements.

| Requirement | Authoritative evidence and result |
| --- | --- |
| Five-week promotion and improved validated accuracy | Protected v14: 106 selections, three qualified weeks, longest streak one, pass=false. No full-market accuracy improvement or solid-strategy claim is established. |
| Frozen Cash App scope and top-65 | Width remains 65. This continuation did not modify or refresh the availability list. The dated approval ledger is missing. |
| Two distinct non-proxy picks and full-market top 30 | Pick count two, target 30, proxy exclusion, and five-session labels remain required. The IWB/IWM proxy does not establish exact historical full-market membership. |
| Prior-label, causal/global/state, and market-type gates | Prior labels must precede the decision. Every route aggregate and market type requires the original five-week streak. Code is preserved; a new strict replay is blocked. |
| Five extras and one or two approved choices | The repaired policy requires exactly five extras, excludes unapproved choices, and retains a sole approved diagnostic choice. One pick cannot qualify a week. Nine policy and three legacy checks pass. |
| Protected v14 | SHA-256 remains 3119bb102d9786368c3c49d84ae236a4092607119b4d2dada151102c77cb0384. |
| Forecast component | [Model history](../docs/model-history.md) records the research opt-in and six mocked adapter checks. No weights were loaded or validated forecast improvement established. |
| Generation, rendering, and delivery | No-send dispatch and direct generation stop at the source gate. Thirty-six renderer/delivery mocks pass. The latest report is a September 25 live-candidate render blocked by availability with zero attempts. A fresh current render is blocked. |
| Schedule and failures | The nightly job is idle, last exit zero, schedule 20:30, with source/send flags absent. Four dispatch and two import/failure-email checks pass. Dry-run report artifacts, markers, broker snapshot, refresh status, and auto-heal state were unchanged. |
| Five-hour heartbeat | Viewed without changes. Active/paused state is not exposed by the tool. |
| Leonard and stable identifiers | Public docs, private README, CLI/agent labels, frontend title, and report labels use Leonard. Runtime paths, authorization names, scheduler IDs, and atlan-scale are stable. |
| README and linked docs | The 53-line index links the detailed pages. Verified Obsidian history is retained. Four official reference pages were re-read; architecture patterns remain guidance, not performance proof. |
| Image through image_gen after review | Archived invocation followed architecture reads. The current PNG matches its archived hash and was visually checked against current architecture. |
| Validation, existing edits, and action gates | Public 37-file audit and whitespace check pass. Private whole-tree whitespace errors are pre-existing and preserved; no full private-suite pass is claimed. No publication, send, trade, broker write, purchase, new account, scheduler change, or promotion occurred. |

Three bounded AAPL probes requested the September 25 daily-history interval. The first queried during initialization; two follow-ups queried after the run, including ordinary Python source. All returned zero rows with a future-history warning. The follow-ups logged September 25-26 configuration but a July 6 runtime clock, processed two data points, and reported zero orders. These observations leave the bar unverified and do not establish provider-wide absence or a local source replacement. See SRC-196 and SRC-199.

Both local price stores still end September 24 with zero September 25 rows. Exact point-in-time full-market membership, a complete aligned label, dated approval evidence, and a permitted data source remain unavailable. The frozen availability list must stay unchanged.

The same input blocker persisted through three goal turns. Bounded local repairs and documentation checks are finished. Remaining meaningful progress requires valid source/approval evidence or an external-state change. The goal is not complete; no accuracy gain or promotion is justified. Sources: SRC-179, SRC-185, SRC-196, SRC-197, SRC-198, and SRC-199.

## October 3, 2026 historical diagnostic scope correction

The September 29 winner-prototype retrieval and October 2 ordered conditional-pair diagnostics used the validated 123-window, date-scoped IWB/IWM holdings proxy. Candidate and realized-label rows ranged from 400 to 2,948 per window, with medians of 2,647. The latest window had 401 candidate rows and 400 label rows. The holdings source is not exact FTSE Russell membership, historical listing or delisting evidence, or Cash App availability.

The scope correction does not change the measured results. Winner-prototype retrieval produced 0/110 qualified weeks, a maximum streak of 0, and 0.018182 mean top-30 hits per decision. Ordered conditional pairs produced 2/110 qualified weeks, a maximum streak of 1, and 0.290909 mean hits. The same-sample and stored ridge references remain 3/110 with 0.227273 mean hits; fixed-ridge top two produced 4/110 with 0.300000 mean hits. Both diagnostics preserved exact-two picks and strict prior-label cutoffs. Route, market-type, and approval gates were not evaluated. The full-market target remains unchanged.

## October 3, 2026 realized-label boundary recheck

The raw and materialized historical price stores end on September 24, 2026. Only four trading sessions, September 21-24, follow the latest complete September 18 label. The fifth session, September 25, is missing, so this continuation has no new complete label to evaluate. The existing 123-window IWB/IWM proxy cache remains diagnostic-only and does not supply the exact full-market or Cash App approval evidence required for promotion.

## October 3, 2026 corporate-action price-boundary audit

The protected v14 artifact remains at its recorded hash and still fails the five-week gate. Its raw price-quality audit flags three extreme moves. SEC filings confirm nearby reverse-split actions, but the stored daily bars do not align uniformly with the stated effective or split-adjusted trading dates. The current strict proxy cache does not include the three flagged symbols in the checked August event windows; BRCC is excluded there for incomplete 63-session history. This limits the impact on those specific proxy outputs but does not validate the broader market source. The canonical ledger, price stores, and v14 were not changed.

## September 7, 2026 anchor-stable pair scorer

The selector tested a stability-aware pair stage against the unchanged Cash App-only top-65 contract. It used 655 candidates, 168 features, 120 windows, strict prior-label filtering, exact two distinct non-proxy picks, and separate chronological early, middle, and recent pair environments. The final pair score was the environment mean minus a fixed 0.5 standard-deviation penalty.

The replay evaluated 108 decisions and produced causal/global/state qualified counts of 1/1/2. Maximum streaks were 1/1/1. Market-type qualified counts were causal defensive/growth/oil/transition 0/0/0/1, global 0/0/0/1, and state 1/0/0/1. The artifact SHA-256 is `9d4f3cb443889d0f2ad5f984fd2abac56cb302ba51a4b3e94bb360d0cec5149e`.

The branch is weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 and did not improve the five-consecutive-week gate. It was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and the latest decision, label, and price-database boundaries remain August 20, 2026, August 27, 2026, and August 28, 2026. Verification passed two anchor-stable tests, 341 historical tests, compilation, plugin checks, public validation, and whitespace checks.

## September 7, 2026 dynamic Bradley-Terry causal ranking

The selector tested a time-varying pairwise ranking family against the unchanged Cash App-only top-65 contract. It used the dynamic Bradley-Terry approach described in [Nonparametric Estimation in the Dynamic Bradley-Terry Model](https://proceedings.mlr.press/v108/bong20a.html): prior top-30 symbols were compared with prior non-top-30 symbols, each comparison received a Gaussian weight based on its distance from the current decision window, and symbol strengths were estimated with a weighted Bradley-Terry maximum-likelihood update.

The replay evaluated 108 decisions and produced causal/global/state qualified counts of 1/1/2. Maximum streaks were 1/1/1. Market-type qualified counts were causal defensive/growth/oil/transition 1/0/0/0, global 1/0/0/0, and state 2/0/0/0. The artifact SHA-256 is `f210b51679a46c99f5e6accdcd77c8d81c62de740d28732e10d388e7251f215d`.

The branch is weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 and did not improve the five-consecutive-week gate. It was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and no candidate, trade, send, publication, scheduler action, or promotion was promoted. Verification passed 51 selector tests, two dynamic-BTL tests, two anchor-stable tests, compilation, public validation, and whitespace checks. The unrelated full XBRL ledger test partition exceeded the five-minute runner limit.

## September 7, 2026 kernel rank centrality causal ranking

The selector tested a spectral pairwise aggregation family after dynamic Bradley-Terry. The method follows [A Statistical Convergence Perspective of Algorithms for Rank Aggregation from Pairwise Data](https://proceedings.mlr.press/v32/rajkumar14.html) and the time-varying kernel rank-centrality method in [A Spectral Approach for the Dynamic Bradley-Terry Model](https://arxiv.org/abs/2307.16642). It used the same strictly prior top-30 versus non-top-30 comparisons, Gaussian time weights, a normalized transition graph, and stationary scores.

The replay evaluated 108 decisions and produced causal/global/state qualified counts of 1/1/1. Maximum streaks were 1/1/1. Each route qualified once in transition and zero times in defensive, growth, and oil. The artifact SHA-256 is `e41bad1d81d9c0c69a4372b77817e20480311c2816d58d87fab46502f953e393`.

The branch is weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 and did not improve the five-consecutive-week gate. It was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and no candidate, trade, send, publication, scheduler action, or promotion was promoted. Verification passed 51 selector tests, three dynamic/KRC tests, compilation, public validation, and whitespace checks.

## September 7, 2026 HodgeRank causal aggregation

The selector tested a weighted least-squares HodgeRank family after dynamic Bradley-Terry and Kernel Rank Centrality. It follows [A Statistical Convergence Perspective of Algorithms for Rank Aggregation from Pairwise Data](https://proceedings.mlr.press/v32/rajkumar14.html). It used strictly prior top-30 versus non-top-30 comparisons, Gaussian time weights, and symbol potentials fit from pairwise residuals.

The replay evaluated 108 decisions and produced causal/global/state qualified counts of 3/2/2. Maximum streaks were 1/1/1. Market-type qualified counts were causal defensive/growth/oil/transition 2/0/0/1, global 0/1/0/1, and state 1/0/0/1. The artifact SHA-256 is `af16d22fe0c713aec8f69dd88f9773118104ef684157e03dc73f97a351806a81`.

The branch is weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 and did not improve the five-consecutive-week gate. It was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and no candidate, trade, send, publication, scheduler action, or promotion was promoted. Verification passed 51 selector tests, four dynamic/KRC/HodgeRank tests, compilation, public validation, and whitespace checks.

## September 7, 2026 artifact-policy combination tournament

The selector combined six completed, contract-compatible Cash App top-65 policies without retraining them. For each later decision, it selected the policy with the best prior hit fraction over a bounded history. The source policies were peer graph plus ExtraTrees, the earlier combined tournament, dynamic Bradley-Terry, HodgeRank, Kernel Rank Centrality, and anchor-stable pair scoring.

The aligned replay covered 108 decisions and preserved the exact two-pick outputs from the source artifacts. It produced causal/global/state qualified counts of 3/2/2 with maximum streak 1/1/1. Market-type counts were causal defensive/growth/oil/transition 2/0/0/1, global 2/0/0/0, and state 2/0/0/0. The artifact SHA-256 is `12c7bcd42e4f5e2b6096cf9bd00136ee651f3475125114d7039fcaedb03069c4`.

The combination is weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 and did not improve the five-consecutive-week gate. It was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and no external action occurred. Verification passed two artifact-policy tests, compilation, public validation, and whitespace checks.

## September 7, 2026 feature-BTL least-squares causal ranker

The selector tested a feature-aware least-squares pairwise ranker based on [A Graph Theoretic Approach for Preference Learning with Feature Information](https://proceedings.mlr.press/v244/saha24a.html). It used strictly prior top-30 versus non-top-30 comparisons, Gaussian time weights, current-window feature differences, and ridge regularization.

The replay evaluated 108 decisions and produced causal/global/state qualified counts of 0/0/0. Maximum streaks were 0/0/0. The artifact SHA-256 is `a993fb5f360bd29e958593882455347712f9dead4f50fe3e3cf510024cffcd1d`.

The branch failed to qualify any route and was rejected. Contract violations were zero, protected inputs and official v14 were unchanged, and no candidate, trade, send, publication, scheduler action, or promotion was promoted. Verification passed five feature/rank tests, compilation, public validation, and whitespace checks.

## September 7, 2026 context-HGB policy combination extension

The artifact-policy tournament was extended with the completed context-aware HGB retrieval policy. The seven-policy replay stayed walk-forward and contract-compatible, but produced causal/global/state qualified counts of 3/2/1 with maximum streak 1/1/1. Artifact SHA-256 is `a08563c42bad84adc73331d52c51d444505f72d2896d9c8dcea3a4ba327f10ca`.

Adding context HGB reduced state performance relative to the six-policy result of 3/2/2 and remained below peer graph plus ExtraTrees at 4/3/3. The extension was rejected. No promotion or external action occurred.

## September 7, 2026 current-cache arm-consensus retrieval

The selector tested a standalone arm-consensus retrieval policy. It counted support for each candidate across the protected current-cache top-30 arm inventory, then selected the top two supported symbols without reading the current label. The arm index reduced discovery to 197 cache-matching artifact files and 396 aligned policy routes.

The Cash App-only top-65 replay evaluated 108 decisions and produced causal/global/state qualified counts of 1/1/1. Maximum streaks were 1/1/1. The artifact SHA-256 is `c39ca2bb2c0196c31318a74c346f4cf846633959f42bf5839613a0a276464e3d`.

The diagnostic was weaker than peer graph plus ExtraTrees at 4/3/3 and was rejected. It was not added to the actual selector. No contract violation, protected-input change, promotion, trade, send, publication, scheduler action, or promotion occurred.

## September 7, 2026 candidate-prefilter blocker audit

The best peer-graph plus ExtraTrees artifact was audited by separating top-65 retrieval coverage from pair-stage performance. At least two realized top-30 winners were inside the top-65 prefilter in 67 of 108 causal decisions, 65 of 108 global decisions, and 63 of 108 state decisions.

The selected pair still missed both winners in 63/67 causal, 62/65 global, and 60/63 state cases. The current-cache candidate-union oracle can pass all market-type gates. This is direct evidence that the blocker is joint retention and ranking of reachable candidates inside the fixed top-65 pool, not missing source count alone.

Audit artifact: `historical_candidate_prefilter_blocker_audit_20260907.json`. No promotion, trade, send, publication, scheduler action, or v14 change occurred.

## September 5, 2026 source expansion and causal representation audit

The current corrected Cash App-only cache was composed with four additional point-in-time overlays: vintage macro data, SEC Forms 3/4/5, SEC 13F holdings breadth, and SEC fails-to-deliver. This created a 202-feature cache over 655 candidates and 120 windows. The cache SHA-256 is `ab69d712f86b72c9830f28876c5749b0d8ad5dd441820dcd1a458852684934c8`.

The nine-source peer-graph plus ExtraTrees replay evaluated 108 decisions and produced causal/global/state qualified counts of 2/2/1. Maximum streaks were 1/1/1. It selected exactly two distinct non-proxy symbols, reported zero contract violations, preserved protected inputs, and preserved the official v14 artifact. The replay SHA-256 is `2268848687c2581766829e01bb67ede3b893dc3e41be19d8a50046a4f82a721d`.

Two representation controls were also completed. Adding strictly prior temporal context to the graph learner produced 0/0/0, with artifact SHA-256 `b87da746fc3d30a87779c8d69c906afe271fe8261d960739a7431e59987e545b`. Equal-weight robust source-block graph distances produced 2/0/2, with artifact SHA-256 `7091a2a933c901f7d833a8e25fccaaddbafbff661989b7b890ae0e9a18eb25bd`.

These results are weaker than the current peer-graph plus ExtraTrees diagnostic at 4/3/3 qualified windows, also with maximum streak 1. The original five-week gate remains false. The evidence-backed failure point is stable causal ranking of both winners across consecutive weeks and market types. Source expansion, temporal context, and block-distance weighting did not resolve it. The latest decision remains August 20, 2026, the latest complete label remains August 27, 2026, and the local price database reaches August 28, 2026.

Verification passed 339 historical tests after the graph change, four Sol Advisor cost-audit tests, the Sol Advisor checkout verifier, compilation, public validation, and whitespace checks. No model, candidate, trade, send, publication, scheduler action, or promotion was promoted.

## September 4, 2026 temporal model tournament

The selector added a temporal tournament over three existing causal candidate scorers: logistic, HistGradientBoosting, and context MLP. At each decision it used only earlier top-30 precision, required two observations before trusting a score, and selected ties in a fixed order. It did not use the current label.

The Cash App-only replay covered 655 historical candidates, a top-65 candidate pool, a realized top-30 target, exactly two distinct picks, and 108 evaluated decisions. The ExtraTrees pair stage produced 3, 2, and 2 qualified windows for causal, global, and state routes. Maximum streaks were 1, 1, and 1. Contract violations were zero and protected inputs were unchanged. Artifact SHA-256 is `7ab3ed2546ca96949f84b1dfb2209c3075f60e12f4c7b69c46229fc10b5fc468`.

The tournament did not improve the peer-graph plus ExtraTrees diagnostic at 4/3/3, so it was rejected. The precise blocker remains stable causal selection of both winners across consecutive weeks and market types. No model, candidate, trade, send, publication, scheduler action, or promotion was promoted.

## September 3, 2026 group-robust training and private forecasting maintenance

The selector tested a new market-type robust objective. It used only strictly earlier labeled rows and multiplied the existing recency weights by learned group weights based on each market type's past log loss. The Cash App-only cache remained 655 historical candidates, with top 65 candidate selection, realized top 30 qualification, exactly two distinct picks, and 108 evaluated decisions.

The ExtraTrees pair replay produced 0, 1, and 1 qualified windows for causal, global, and state routes. Maximum streaks were 0, 1, and 1. The result had zero contract violations and unchanged protected inputs, but it was weaker than the peer-graph plus ExtraTrees diagnostic at 4/3/3. The branch was rejected. The stable blocker remains causal ranking of both winners across consecutive weeks and market types.

Private forecasting maintenance was handled outside this public historical-evidence layer. It did not change the historical selector, and it caused no report delivery or external action.

## September 1, 2026 temporal contrastive candidate identification

The selector tested a new time-aware representation against the corrected Cash App-only cache. It used 655 historical candidates, a top-65 candidate pool, a realized top-30 success rule, exactly two distinct picks, and 108 evaluated decisions. The current Cash App list is still a research allowlist, not proof of historical platform availability.

For each decision, the temporal branch compared current symbols with positive and negative centroids built from strictly earlier labeled windows. It weighted examples by similarity between the old and current market context and by age. Unknown later labels were excluded. The current decision label was not read until after selection.

The full replay with the ExtraTrees pair scorer produced 3, 2, and 2 qualified windows for causal, global, and state routes. Every route had maximum streak 1 and ending streak 0. The metadata-corrected artifact selected exactly two distinct symbols, reported zero contract violations, preserved all protected inputs, and preserved the official v14 artifact. Its SHA-256 is `a2097e51782aea629a6dd3ac8c8ae7b29a0950681e6525775540c1309fb4d145`.

This result is weaker than the current best peer-graph plus ExtraTrees diagnostic at 4/3/3 qualified windows, also with maximum streak 1. The temporal representation was rejected for promotion. It did not resolve the blocker: stable causal ranking of both winners across consecutive weeks and market types. No model, candidate, trade, send, publication, scheduler action, or promotion was promoted.

## September 1, 2026 peer-graph and retrieval battery

The selector stayed inside the approved Cash App research allowlist, using 655 historical candidates, a top-65 candidate pool, a realized top-30 threshold, and 108 evaluated decisions. All selections remained exactly two distinct non-proxy symbols. Current Cash App availability and historical platform membership are not proven by the public source, so every result remains diagnostic.

The best new representation was a decision-time peer graph. It robustly scaled each current-window vector, connected each symbol to eight nearest peers, and added local centroid, residual, dispersion, and density features to the individual HGB score head. It used no labels for the current window. A second metric measured recall only among realized top-30 winners present in that window's candidate map.

The peer graph with the existing logistic pair model produced 2, 0, and 2 qualified windows for causal, global, and state routes, with maximum streak 1. Mean ordinary recall was 7.93%, 7.78%, and 7.25%, and mean reachable recall was 57.04%, 55.78%, and 52.04%. Replacing the pair model with the strongest ExtraTrees control produced 4, 3, and 3 qualified windows, again with maximum streak 1. The retrieval improvement did not create a consecutive run, so the branch was rejected.

Additional causal controls failed to improve the gate. Matured peer history produced 2/1/1, raw-HGB plus peer-graph rank blending produced 2/1/1, source-blocked quality-weighted RRF produced 1/0/1, rank-quantile HGB produced 0/0/0, and graph hard-negative sampling produced 1/1/0. Earlier SEC Form 3/4/5, 13F, and fails-to-deliver overlays also failed to improve the route and market-type gate.

The private Cash App audit now distinguishes a pair that was not fully realized in the later top 30 from an actual decision-contract violation. The completed artifacts still show zero temporal, proxy, feature-date, and current-label violations, unchanged protected inputs, and unchanged official v14. The original five-week gate remains false. The precise current blocker is stable causal retrieval and pair selection across market types, not a missing source family or a broken pool-width rule. No model, candidate, trade, send, publication, scheduler action, or promotion was promoted.

The cache metadata was corrected after review. Its top-level candidate list now contains only the 655 filtered candidates inside the approved Cash App allowlist. CB-RRF quality observations also retain their source window index and are filtered strictly before use. The official v14 binding remains the price-backtest artifact at SHA-256 `3119...`; the `1b934...` file is a separate fixed-regime diagnostic.

## August 31, 2026 masked-label selector battery and SEC insider-filing overlay

The selector now excludes unknown future labels by default during individual fitting and replay. This removes the failure mode where an unavailable later label could be treated as a non-hit. The corrected top-65 Cash App-only battery still used 108 evaluated decisions, an exact pair, a realized top-30 target, and strictly prior training windows.

The strongest result was the context-conditioned MLP at 3/1/1 qualified windows for causal/global/state, with maximum streak 1. Broad ensemble reached 2/0/0; quantile reached 1/1/2; listwise, hard-negative, pair-objective, recency, score-memory, and pair-model controls did not clear the active gate. Every completed artifact had zero contract violations and unchanged protected inputs.

A separate SEC Form 3/4/5 overlay was collected from public submissions. It contains 123,606 point-in-time events across 671 symbols and 176 total features after appending eight ranked features to the 168-feature base cache. The acceptance-time policy is conservative, but the public submissions endpoint can be revised and the summary does not include transaction direction. The overlay produced 0/0/0 qualified windows with maximum streak 0 under the strongest selector, so it was rejected for promotion.

The original five-week gate remains false. The current failure point is stable causal selection of both winners together. No model, source overlay, candidate, or external action was promoted.

## August 31, 2026 Cash App-only top-65 scope

The historical candidate universe was restricted to the approved Cash App CSV. The file contains 700 rows. After ticker normalization, known ETF or proxy removal, and explicit non-plain-common removal, 677 approved research symbols remain. Intersecting them with the historical feature windows leaves 655 symbols overall, with 615 to 655 symbols per window. Current in-app availability and historical Cash App membership remain unverified, so this is a diagnostic allowlist.

The source surface also added 619 official FINRA consolidated daily short-sale volume files with 1,842,975 parsed records and six prior-session features. The source uses the latest trade date strictly before each decision session, excludes later `Updated` files, and remains diagnostic because public archive revision history is not a full historical vintage.

The matched logistic selector produced 0/0/0 qualified weeks for both top-50 and top-65 pair pools, with maximum streak 0 across 108 decisions. The strongest prior uncertainty-aware selector under the Cash App-only top-65 scope produced 1/0/1 with maximum streak 1. All artifacts had zero scope or contract violations and unchanged protected inputs. The dedicated audit confirms that top 65 is the candidate-pool width and realized top 30 remains the success rule.

The exact five-week gate remains false. The current failure point is still stable causal selection of both winners together, not a missing source file or an invalid Cash App scope. No model, candidate, or external action was promoted.

## August 30, 2026 direct top-30 membership voting

The ensemble was changed from continuous rank averaging to direct voting on whether each member placed a stock in its top 30. Average rank was used only to break equal vote counts. This directly targets the required top-30 membership rule.

The causal, global, and state routes produced 4, 3, and 4 qualified windows out of 108, with maximum streak 1. Contract violations were 0 and protected inputs were unchanged. The branch was rejected because it did not improve consecutive stability.

The fresh audit covers 279 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 weekly rank-correlation objective

The new individual scorer optimized centered within-window rank agreement plus a small top-30 membership term. This changes the training objective from class probability or return magnitude to the weekly ordering used by the final selection rule.

The causal, global, and state routes produced 1, 1, and 1 qualified windows out of 108, with maximum streak 1. Contract violations were 0 and protected inputs were unchanged. The branch was rejected.

The fresh audit covers 276 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 online expert weighting control

The dynamic ensemble was changed to exponential online expert weighting. Each member's weight was based on its earlier top-30 loss history, then applied to within-window ranks from logistic, tree, and neural forecasts. This tests a sequential weighting rule beyond the existing mean-quality weighting.

The causal, global, and state routes produced 4, 3, and 4 qualified windows out of 108, with maximum streak 1. Contract violations were 0 and protected inputs were unchanged. The branch was rejected because it did not improve consecutive stability.

The fresh audit covers 273 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 individual pairwise rank control

The individual selector was trained with direct winner-versus-negative comparisons instead of a binary membership target. Each earlier top-30 winner was compared with bounded near-cutoff negatives and stable sampled negatives, with weights based only on earlier ranks and recency.

The causal, global, and state routes produced 0, 0, and 1 qualified windows out of 108, with maximum streaks 0, 0, and 1. Contract violations were 0 and protected inputs were unchanged. The branch was rejected.

The fresh audit covers 270 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 uncertainty-aware rank aggregation

The selector now has a diagnostic uncertainty-aware rank ensemble. It averages within-window ranks from logistic, tree, and neural members, then subtracts a fixed penalty for cross-model rank dispersion. This is a practical uncertainty proxy inspired by [Confident Risk Premiums and Investments Using Machine Learning Uncertainties](https://academic.oup.com/rfs/article-abstract/39/5/1463/8287227), not a claim that the backtest has forecast confidence intervals.

The causal, global, and state routes produced 5, 4, and 5 qualified windows out of 108, with maximum streak 1. Contract violations were 0 and protected inputs were unchanged. The branch was rejected because it increased total hits without improving consecutive stability.

The fresh audit covers 267 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 RankGLU score-head control

The score head was changed to keep a direct linear scoring path and add a bounded gated interaction branch. This follows the ranking-focused design in [RankGLU](https://arxiv.org/abs/2606.08930), while using the existing 162-feature cache and prior-label training policy.

The causal, global, and state routes each produced 1, 0, and 1 qualified windows out of 108, with maximum streak 1 and zero contract violations. Protected inputs were unchanged. The branch was rejected because it did not improve consecutive stability.

The fresh audit covers 264 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue remains stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 nonlinear joint pair scorer

The joint pair stage was changed from logistic classification to a bounded ExtraTrees classifier over the same symmetric pair features. This tested nonlinear pair interactions directly while keeping the individual candidate prefilter, prior-label cutoff, full-universe cache, and final two-pick rule unchanged.

The replay produced causal/global/state 3/1/3 qualified windows, each with maximum streak 1 across 108 decisions. Every route had zero contract violations and unchanged protected inputs. The branch was rejected because its higher total causal and state counts did not produce a longer run.

The fresh audit covers 261 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The realized-label envelope still permits five or more consecutive two-winner windows in every market type, so the current issue is stable causal ranking and pair selection rather than source or candidate availability.

## August 30, 2026 full-feature univariate rank-lift control

The new factor-sort control used every feature in the 162-column full-universe cache. For each earlier window, it estimated the top-30 hit rate for five cross-sectional quantile bins, smoothed the estimates, selected the strongest 32 prior-only features, and applied their learned lifts to the current window.

The causal, global, and state routes each produced 1 qualified window out of 108, with maximum streak 1 and zero contract violations. The branch was rejected. The fresh audit covers 258 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false.

The realized-label envelope still permits five or more consecutive two-winner windows in every market type. This confirms that the current issue is not a lack of source files or unavailable winners. The selector still fails to retain both winners together in a stable causal way.

## August 30, 2026 candidate-identification control battery

The continuation tested five independent changes after the list-level ranking control failed. The multi-cutoff objective used top-2, top-5, top-10, and top-30 targets together, following [Differentiable Top-k Classification Learning](https://arxiv.org/abs/2206.07290). The hard-negative variant added prior labels just outside the top 30, following the controllable-hardness principle in [On the Theories Behind Hard Negative Sampling for Recommendation](https://arxiv.org/abs/2302.03472). The context variant added a current-window cross-sectional summary motivated by [A Deep Multi-Factor Framework for Cross-Sectional Stock Return Ranking via Market-State Attention Pooling](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6963093). The other two controls widened the individual candidate prefilter to 80 and aggregated six already-tested model families.

| Control | Causal | Global | State | Maximum streak | Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| Multi-cutoff top-k objective | 1 | 1 | 1 | 1 | Not promoted |
| Hard-negative multi-cutoff top-k | 0 | 2 | 1 | 1 | Not promoted |
| Cross-sectional attention context | 1 | 1 | 1 | 1 | Not promoted |
| 80-name individual prefilter | 2 | 1 | 2 | 1 | Not promoted |
| Broad rank ensemble | 2 | 1 | 2 | 1 | Not promoted |
| 72-window co-hit history | 0 | 0 | 0 | 0 | Not promoted |

All five controls covered 108 evaluated decisions, had zero contract violations, and preserved the protected inputs. The fresh audit covers 252 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false. The realized-label upper bound still permits five or more consecutive two-winner windows in every market type, so the data can contain the required winners but the causal selector still does not retain both reliably.

## August 30, 2026 list-based weekly ranking control

The new control treated each earlier week as a ranking list. It trained a small list-level scorer on prior winner lists and deterministic non-winner samples, with validation restricted to earlier windows. This directly tests whether the failure came from using point targets instead of a weekly ordering objective.

The full-universe replay produced causal/global/state 0/0/0 qualified windows, maximum streak 0, and zero contract violations. The branch was rejected. The fresh audit covers 237 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The exact five-week gate remains false.

The realized-label envelope still supplies a non-promotable upper bound of five or more possible consecutive two-winner windows in every market type. This keeps the current blocker precise: causal ranking and pair selection remain unstable even though the data can contain both winners. No candidate or external action was promoted.

## August 30, 2026 top-30 precision feedback for dynamic weighting

The dynamic ensemble was corrected to weight models by earlier top-30 accuracy rather than only the two final names. This better matches the actual success rule and uses no current or future labels. The direct full-universe control produced causal/global/state 4/3/4 qualified windows with maximum streak 1, identical to the fixed equal-rank ensemble.

The current audit covers 231 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The feedback change did not resolve the stable two-winner ranking problem.

## August 30, 2026 isolated cross-sectional price-rank control

The price-rank experiment was isolated from the added macro source. It changed only raw price signals to tie-aware ranks within each decision window. The direct full-universe ensemble produced causal/global/state 0/1/0 qualified windows with maximum streak 1, so price scaling was not the main cause of the ranking failure.

The current audit covers 234 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The remaining limitation is stable causal ranking of two winners.

## August 30, 2026 prior-score smoothing control

The equal-rank ensemble was smoothed with 20 percent of the prior decision's model score. This uses no future labels and targets week-to-week stability. The full-universe control produced causal/global/state 3/2/4 qualified windows with maximum streak 1, so it did not improve the fixed ensemble.

The current audit covers 225 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. Simple score persistence did not resolve the two-winner ranking problem.

## August 30, 2026 cross-sectional price-rank representation

The price features were ranked within each decision window and mapped to a stable range, following the approach described in [Empirical Asset Pricing via Machine Learning](https://doi.org/10.1093/rfs/hhaa009). This reduces scale changes across market periods while keeping the same full universe and source data.

The ranked-price equal-rank ensemble produced causal/global/state 0/1/0 qualified windows with maximum streak 1. It did not improve the raw-price ensemble. The current audit covers 228 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The five-week gate remains false.

## August 30, 2026 dynamic forecast-weight control

Published research on dynamic forecast averaging motivated a model that gives more weight to models with better earlier results. The direct full-universe control combined logistic, tree, and neural scores using only prior successful-week history. It produced causal/global/state 1/1/2 qualified windows with maximum streak 1, so it did not improve the equal-rank ensemble.

The current audit covers 222 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. Dynamic weighting did not resolve the stable two-winner ranking problem.

## August 29, 2026 continuation

## August 30, 2026 research-backed forecast ensemble

Reviewed the primary research paper [Stock return prediction: Stacking a variety of models](https://www.sciencedirect.com/science/article/pii/S0927539822000342), which studies combining forecasts out of sample. The direct equal-rank ensemble of logistic, tree, and neural individual models produced causal/global/state 4/3/4 qualified windows, with maximum streak 1. Feeding that ensemble into the pair model produced 0/0/0. No weights were tuned on current or future labels.

The fresh audit covers 219 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The ensemble improved total successful weeks but not consecutive stability, so the remaining limitation is causal ranking and pair selection at the current complete-label boundary.

The continuation audited 16 new top-50 diagnostic artifacts before selecting another strategy family. All 16 artifacts covered 107 evaluated windows from June 27, 2024 through August 13, 2026, recorded zero stored contract violations, preserved the protected inputs, and failed the active three-consecutive route and market-type gate.

| Diagnostic family | Best qualified count | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Full official-signal lift | 7 | 2 | Not promoted |
| Pair retention | 6 | 1 | Not promoted |
| Full bar-signal lift | 5 | 2 | Not promoted |
| Online feature-union specialist | 4 | 2 | Not promoted |
| Within-symbol self-history transition signature | 1 | 1 | Not promoted |

The strongest prior result was global full-official-signal lift at 7 qualified windows with only a two-window streak. The failure remains candidate identification: the candidate pool can contain both realized winners, but the selector does not retain both often enough.

An isolated forward refresh retrieved 3,027 of 3,042 baseline symbols for the August 26, 2026 through August 28, 2026 range. The August 28, 2026 session was excluded as incomplete. The trusted rebuild produced 120 valid windows, a latest complete label of August 27, 2026, and 2,797 common symbols in the latest decision window. The refreshed official top-50 baseline remained at 3 qualified windows and a longest streak of 1.

The new causal representation used 12 fixed bar features. It encoded each symbol's within-symbol percentile zones over prior observations, per-channel zone transitions, grouped transition tokens, recency-weighted prior hit rates, and a deterministic signature-diversity rule for the second pick. It covered 108 windows and produced 0 causal, 1 global, and 0 state qualified windows, with maximum streaks 0, 1, and 0. All contract, proxy, cutoff, and protected-input checks passed, so the result is a valid negative diagnostic rather than a failed implementation.

The top-50 evaluator and isolated refresh helper also received a verification repair. Their stale fixed-regime hash was replaced with the verified official v14 backtest hash. Later review corrections made the canonical baseline explicitly non-gating, wired the original promotion check to top 30, coupled gate success to protected hashes, and rejected writes to the official cache. Focused enforcement tests passed 5, 8, and 2 cases, the full historical private suite passed 99 tests with pre-existing `ResourceWarning` output, compilation passed, SQLite integrity returned `ok`, and public validation passed. v14 remains unchanged and all trade, broker, email, resend, scheduler, publication, and promotion gates remain closed.

### Additional top-30 continuation battery

The current continuation used the isolated refreshed cache with 120 valid windows and 108 evaluated decisions. It tested new candidate construction and learning families while preserving strict prior-label selection, exact-two distinct non-proxy picks, fixed market types, protected v14, and closed external-action gates.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Rank-profile shape | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |
| Per-symbol change-point signature | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |
| Full 95-signal rank forest | 5/108, max 1 | 3/108, max 1 | 3/108, max 1 | Not promoted |
| Top-400 union rank forest | 4/108, max 1 | 2/108, max 1 | 3/108, max 1 | Not promoted |
| Top-400 balanced probability forest | 1/108, max 1 | 2/108, max 1 | 1/108, max 1 | Not promoted |
| Top-400 hard-negative contrast | 3/108, max 2 | 3/108, max 1 | 3/108, max 1 | Not promoted |
| Top-400 balanced logistic | 2/108, max 1 | 0/108, max 0 | 1/108, max 1 | Not promoted |
| Top-400 pairwise rank learner | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |
| Point-in-time SEC-event logistic | 3/108, max 1 | 1/108, max 1 | 2/108, max 1 | Not promoted |
| SEC-event top-400 union logistic | 2/108, max 1 | 1/108, max 1 | 2/108, max 1 | Not promoted |
| Cross-candidate arm routing | 9/108, max 3 | 6/108, max 3 | 9/108, max 3 | Aggregate improvement only; per-type gate failed |

The cross-candidate result is not a promotion. Its aggregate streak is produced across mixed market states. Every market-type report still fails, with the strongest per-type result reaching maximum streak 1. An oracle over the 9 current arm pairs found 11 possible two-winner windows overall and no three-window per-market-type run.

The top-400 union measured the candidate-construction boundary. It contained all 30 realized winners in 84 of 108 windows, compared with 17 at top 200 and 0 at top 50. The raw universe feasibility oracle still permits a growth-like five-window witness and an oil-like six-window witness, so a strict data-level blocker is not established.

Parent verification passed 131 historical tests, compilation, SQLite integrity, public validation, whitespace, and exact protected-hash checks. The wider 181-test run had two unrelated missing-`agentmail` imports. All new diagnostics recorded zero contract violations, v14 remained unchanged, and no external action occurred.

### Self-history quantile rank continuation

The next representation used a top-800 union of all 95 current bar-signal ranks and added each symbol's empirical percentile within its own prior 24 observations. This is distinct from the earlier 12-feature change-point signature because it uses the full signal set and a nonparametric self-relative feature for every signal.

The replay covered 120 valid windows and 108 evaluated decisions. Causal routing produced 1 qualified window and maximum streak 1. Global and state routing produced 0 qualified windows and maximum streak 0. All four market-type cells failed, contract violations were 0, protected hashes were unchanged, and v14 remained unchanged. The artifact SHA-256 is `23c173a783f4f581eb8421209f15e0652dee2ae2894aa616fe5065616f8b3167`.

Focused tests passed 3/3 and compilation passed. The candidate was not promoted. The raw-universe feasibility blocker remains unestablished because growth-like and oil-like five-window opportunities still exist.

### Bayesian rank-bin top-400 continuation

The Bayesian follow-up estimated smoothed feature-bin likelihood ratios for realized top-30 membership over the top-400 union of all 95 current bar-signal ranks. It used only prior labels, fixed five-bin boundaries, and temporal decay.

The refreshed replay covered 120 valid windows and 108 evaluated decisions. Causal, global, and state routes each produced 0 qualified windows with maximum streak 0. Every market-type cell failed, contract violations were 0, protected hashes were unchanged, and v14 remained unchanged. The artifact SHA-256 is `443ecf0d0f12a8095bda0fec2d161109d6fea635e20e0c6823440a0afdd2a68d`.

The Bayesian candidate was not promoted. Expanded historical tests passed 137/137, compilation, SQLite integrity, public validation, and whitespace checks passed. The raw-universe feasibility blocker remains unestablished.

### Sparse adaptive top-800 lift continuation

The sparse adaptive lift candidate selected the strongest 12 of the 95 current bar-signal ranks using only prior top-30 membership and rank-severity lift, then scored a top-800 union of current signal ranks. This differs from the prior all-feature lift because feature selection is learned causally at each decision.

The refreshed replay covered 120 valid windows and 108 evaluated decisions. Causal, global, and state routes produced 2, 2, and 3 qualified windows, each with maximum streak 1. Every market-type cell failed, contract violations were 0, protected hashes were unchanged, and v14 remained unchanged. The artifact SHA-256 is `7ff2eeddfa2b814f839504ae28ca9449293c2e53fd7da5af79798ae017e1f241`.

The expanded historical suite passed 140/140 with expected ResourceWarning output. The candidate was not promoted. The formal feasibility blocker remains unestablished.

### Rank-trajectory top-800 continuation

The rank-trajectory candidate combined the current 95-signal cross-sectional rank vector with causal summaries of each symbol's prior rank persistence, drift, volatility, and top or bottom quintile behavior over 8 and 24 windows. It used a top-800 union candidate pool and a prior-label-only ridge scorer.

The refreshed replay covered 120 valid windows and 108 evaluated decisions. Causal, global, and state routes produced 4, 3, and 3 qualified windows with maximum streaks 2, 1, and 1. Causal market-type results were defensive 2/1, growth-like 0/0, oil-like 1/1, and transition 1/1. Every market-type gate failed. Contract violations were 0, protected hashes were unchanged, and v14 remained unchanged. The artifact SHA-256 is `b833b67cb99d0608f529d08acfea071fc9abc41883d4c16a6687eb834ef74d2a`.

The current-cache v14 control separately covered 120 windows and 107 evaluable decisions, with 3 qualified windows, maximum streak 1, and `pass=false`; its latest decision had one top-30 hit. Expanded historical tests passed 143/143, compilation, SQLite integrity, public validation, and whitespace checks passed. The candidate was not promoted.

### Random-Fourier top-800 continuation

The random-Fourier candidate applied a fixed label-free 96-component Fourier map to the top-800 union of all 95 current bar-signal ranks, then fit balanced logistic classifiers from prior top-30 membership labels.

The refreshed replay covered 120 valid windows and 108 evaluated decisions. Causal, global, and state routes each produced 0 qualified windows with maximum streak 0. Every market-type cell failed, contract violations were 0, protected hashes were unchanged, and v14 remained unchanged. The artifact SHA-256 is `e63fdd67205e1c46fe24e6fc71d4c756c4e21fd1f3fa45f93cc0ba1deceef684`.

Expanded historical tests passed 146/146, compilation, SQLite integrity, public validation, and whitespace checks passed. The candidate was not promoted. The raw-universe feasibility blocker remains unestablished.

### Extended top-800 causal battery and candidate envelope

The continuation then tested five additional causal top-800 selectors against the same isolated refreshed cache. Each selector used only prior labels, exact two distinct non-proxy picks, decision-date features, fixed market types, and closed external-action gates.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Top-800 ExtraTrees rank forest | 2/108, max 1 | 1/108, max 1 | 3/108, max 1 | Not promoted |
| Top-800 per-signal rank acceleration | 2/108, max 1 | 2/108, max 1 | 1/108, max 1 | Not promoted |
| Top-800 forward-return surprise ridge | 2/108, max 1 | 1/108, max 1 | 1/108, max 1 | Not promoted |
| Top-800 hard-negative contrast | 3/108, max 2 | 3/108, max 1 | 4/108, max 2 | Not promoted |
| Top-800 Bayesian rank-bin likelihood | 0/108, max 0 | 1/108, max 1 | 0/108, max 0 | Not promoted |

All five artifacts had zero contract violations, preserved the refreshed cache, database, dated-universe, and v14 hashes, and failed every route and market-type gate. The expanded relevant historical suite passed 161/161, SQLite integrity returned `ok`, public validation passed, and whitespace checks passed.

The non-promotable union across 60 clean current-cache route outputs contained both realized top-30 winners in 25 defensive windows with a maximum streak of 5, 15 growth-like windows with a maximum streak of 4, 13 oil-like windows with a maximum streak of 5, and 21 transition windows with a maximum streak of 6. The raw-universe oracle still permits a growth-like five-window witness. The precise current blocker is therefore candidate-family coverage and ranking, not proven data infeasibility. The envelope uses realized labels and cannot be promoted.

### August 30, 2026 full bar and SEC-event continuation

The next continuation completed a nonlinear direct-return forest and tested the full current bar-signal surface with point-in-time SEC-event features. Both used the refreshed 120-window cache, 108 evaluated decisions, exact-two distinct non-proxy top-30 picks, strict prior-label cutoffs, fixed market types, and closed external-action gates.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Top-800 forward-return-surprise ExtraTrees | 1/108, max 1 | 1/108, max 1 | 1/108, max 1 | Not promoted |
| Full bar plus SEC-event top-800 logistic | 2/108, max 1 | 1/108, max 1 | 4/108, max 1 | Not promoted |

The full bar plus SEC-event classifier had oil-like and growth-like results of 0/0 for every route. Contract violations were 0, protected inputs and v14 were unchanged, SQLite integrity returned `ok`, and the relevant historical suite passed 165/165. The direct-return artifact SHA-256 is `e9f4f876e19e56b3a8f69809e9ccf0fee1355634bd48a9f979ab48254e658871`; the full bar plus event artifact SHA-256 is `eafe3ac57545d908d2f2af3d9169484aef43443c50208976029e12e9826640f9`.

The updated non-promotable union across 66 clean current-cache route outputs contained both realized top-30 winners in 25 defensive windows with a maximum streak of 5, 16 growth-like windows with a maximum streak of 4, 13 oil-like windows with a maximum streak of 5, and 22 transition windows with a maximum streak of 6. The raw-universe feasibility oracle still permits a growth-like five-window witness, so the current evidence identifies candidate-family coverage and ranking as the blocker without proving that no future causal representation can succeed.

### August 30, 2026 raw path embedding and analog continuation

The continuation then tested the full 63-session decision-date log-return path as a causal sequence representation, followed by a nearest-positive path analog model. Both used the top-800 union candidate pool, prior top-30 labels only, exact-two distinct non-proxy picks, fixed market types, and closed external-action gates.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Full 63-session path embedding logistic | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |
| Nearest-positive path cosine analog | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |

Both artifacts had zero contract violations, unchanged protected inputs and v14, and complete 108-window coverage. The relevant historical suite passed 171/171, SQLite integrity returned `ok`, public validation passed, and whitespace checks passed. The path embedding artifact SHA-256 is `0b31bdf6a3ea603583e1869b2b3d0d9566a685ff9abf3578b4a0b6f5fd02984d`; the analog artifact SHA-256 is `bc5f6ef8e9760afb6f227868424378af65afead5949d57d3297bf1b9d175645b`.

The updated non-promotable union across 72 clean current-cache route outputs contained both realized top-30 winners in 26 defensive windows with a maximum streak of 5, 16 growth-like windows with a maximum streak of 4, 13 oil-like windows with a maximum streak of 5, and 22 transition windows with a maximum streak of 6. The raw-universe oracle still permits a growth-like five-window witness. This supports a candidate-family coverage and ranking blocker without proving that no future causal representation can succeed.

### August 30, 2026 graph diffusion and symbol-union continuation

The continuation tested a current-window similarity graph seeded by prior positive and negative top-30 prototypes, then a symbol-level ranker over the union of clean current-cache top-30 route outputs. The symbol-union selector used current 95-signal ranks plus arm-support provenance and a causal top-800 fallback only when the arm union was empty.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Top-800 positive-negative graph diffusion | 0/108, max 0 | 0/108, max 0 | 0/108, max 0 | Not promoted |
| Clean-arm symbol-union ranker | 2/108, max 1 | 1/108, max 1 | 2/108, max 1 | Not promoted |

The first symbol-union artifact emitted four warmup pair violations because the saved clean arms had no candidates at two early windows. A causal top-800 signal-union fallback corrected the issue; the final replay had 0 contract violations and 78 arm sources. The graph artifact SHA-256 is `6163b53de3ab6f9fee4ecb2782843c38d2b19d8efc2fb16c95f2226bb4827057`; the corrected symbol-union artifact SHA-256 is `c8ac22d548ef52803c6258534c69b5d2cdbb6a54ce8e779b19f190bddb26c2c9`.

The updated non-promotable union across 78 clean current-cache route outputs contained both realized top-30 winners in 28 defensive windows with a maximum streak of 5, 18 growth-like windows with a maximum streak of 5, 15 oil-like windows with a maximum streak of 6, and 22 transition windows with a maximum streak of 6. The raw-universe oracle and this envelope use realized labels, so neither is promotion evidence. Individual predictive routes still fail the five-week gate.

### August 30, 2026 complementary arm assembly continuation

The continuation then formalized a complementary-symbol assembler over the clean current-cache arm union. It estimated each arm's prior graded top-30 utility, scored symbols from the current arm provenance, rewarded arm complementarity, and used a causal top-800 signal-union fallback for empty warmup windows.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Complementary arm pair assembler | 2/108, max 1 | 2/108, max 1 | 2/108, max 1 | Not promoted |

The final artifact used 78 clean arms, had 12 fallback warmup windows, and recorded zero contract violations. The relevant historical suite passed 182/182, compilation, SQLite integrity, protected-hash checks, public validation, and whitespace checks passed. The artifact SHA-256 is `d3908c4256e0b7c917641b199d817d1f78938988ad3e539c85a10ca6f53ae32d`.

The updated non-promotable union across 81 clean current-cache route outputs contained both realized top-30 winners in 28 defensive windows with a maximum streak of 5, 18 growth-like windows with a maximum streak of 5, 15 oil-like windows with a maximum streak of 6, and 22 transition windows with a maximum streak of 6. The envelope uses realized labels, so it is a feasibility upper bound and not promotion evidence. Individual predictive routes still fail the original five-week gate.

### August 30, 2026 ordinal clean-arm union continuation

The continuation tested an ordinal clean-arm union ranker. It predicted graded realized top-30 rank severity from current signal ranks and arm-support provenance, using only earlier labeled windows. The first ExtraTrees implementation exceeded the runtime ceiling without producing an artifact. A deterministic weighted-ridge correction completed under the same target and contract.

| Diagnostic family | Causal result | Global result | State result | Decision |
| --- | --- | --- | --- | --- |
| Ordinal clean-arm union ridge | 3/108, max 1 | 2/108, max 1 | 3/108, max 1 | Not promoted |

The completed artifact had zero contract violations, unchanged protected inputs and v14, and SHA-256 `9e549f53b9e809eb791daa4063e63897f7735e4cab5322781da23a718826dd34`. The relevant historical suite passed 187/187, SQLite integrity returned `ok`, public validation passed, and whitespace checks passed.

The updated non-promotable union across 84 clean current-cache route outputs contained both realized top-30 winners in 28 defensive windows with a maximum streak of 5, 18 growth-like windows with a maximum streak of 5, 15 oil-like windows with a maximum streak of 6, and 22 transition windows with a maximum streak of 6. The envelope uses realized labels, so it is not promotion evidence. Individual predictive routes still fail the original five-week gate.

### August 30, 2026 formal historical-goal blocker audit

The final requirement-level audit evaluated the original contract, current predictive routes, candidate availability, and data boundary. Across 84 clean current-cache top-30 predictive routes, the maximum aggregate streak was 3 and the maximum per-market-type streak was 1. The latest complete label remained August 27, 2026, while the August 28, 2026 database session contained only 4 rows and was excluded.

The realized-label envelope contained both winners in maximum streaks of 5 defensive, 5 growth-like, 6 oil-like, and 6 transition windows. This is a non-promotable upper bound because it reads realized labels. It shows that raw candidate availability is not the blocker. The repeated precise blocker is causal ranking and pair selection at the current labeled boundary. The blocker audit artifact SHA-256 is `dd481b6a2ac241a4a7c3596e5712f26cb91b714fb67771518b79b2840742491f`.

The exact goal remains unachieved. The goal is blocked pending a new complete realized label or independently timestamped information surface. No gate was relaxed, and no model, trade, send, publication, scheduler, or v14 promotion occurred.

## Contract

The current goal requires two distinct suggestions in the realized top 30 for five consecutive forward windows. The promotion result is `pass=true` only when the longest qualified streak reaches five. No resend is authorized before that gate passes.

## Latest realized extension

- A bounded retry restored 217 of 218 missing symbols for the August 19, 2026 canonical session. One symbol returned no provider data and remains excluded rather than imputed.
- The canonical dated store now ends at August 20, 2026 with 2,034,082 bars. The repaired August 19, 2026 session has 3,184 bars and the August 20, 2026 session has 3,168 bars, so both are trusted under the local 11-session, 95% coverage rule.
- The current price-quality audit remains partially reconciled. It reports 92 raw extreme moves across 44 symbols, one corrected move, 39 excluded symbols, and one residual extreme move. No signal or selector promotion uses that residual data as resolved evidence.
- The new decision session August 13, 2026 received label session August 20, 2026. The official selector produced two distinct suggestions, but only one reached the realized top 30, so the window did not qualify.
- The refreshed v14 artifact evaluates 106 windows, has 3 qualified windows, a longest streak of 1, an ending streak of 0, and `pass=false`.

## What worked

- The replay uses a date-scoped historical IWB/IWM holdings proxy. Its cache is bound to the replay schema, signal schema, historical-universe hash, and corporate-action ledger hash.
- The default cache now also binds the canonical historical price-store path, content hash, row count, and maximum market session. This prevents a new bar from being hidden behind stale windows.
- The evaluator default now selects that canonical dated-universe store, so a low-level replay invocation does not silently fall back to the observed-universe database.
- The official feature set is point-in-time: 74 bar and price-volume signals plus 25 SEC EDGAR event-price signals.
- The evaluator enforces two distinct picks and scores them against realized forward ranks.
- The live prediction path is staged: 1,050 source profiles receive a cached mini screen, 200 finalists plus explicit exceptions produce 201 full-screen inputs, 100 reach the full screen, and at most 30 receive deep source review.
- The daily report now exposes exception presence, deep selection, cache-hit, fetch, and profile-refresh telemetry. The verified dry run selected 30 deep entries, served all 30 from cache, and requested no new source fetches. This improves observability without changing the ranking caps.
- An import-time delivery defect was corrected with a `__main__` guard and a regression test.
- The cross-sectional rank transform now uses deterministic NumPy sorting and reuses each current transformed matrix across candidates. This reduced the diagnostic runtime without changing the official result.

## What failed

| Experiment | Result | Decision |
| --- | --- | --- |
| v9 ridge baseline | 3 qualified windows, longest streak 1 | Historical baseline |
| v10 mean-rank ensemble | 3 qualified windows, longest streak 1 | Not promoted |
| v11 median and lower-quartile ensembles | 3 qualified windows, longest streak 1 | Not promoted |
| v12 top-30 vote ensemble | 3 qualified windows, longest streak 1 | Core baseline |
| v13 extended 19-signal bar set | 2 qualified windows, longest streak 1 | Not promoted; retained in schema-8 cache for diagnostics |
| v14 schema-8 core selector | 3 qualified windows, longest streak 1 | Official frozen selector |
| Symbol-prior diagnostic | 0 qualified windows, longest streak 0 | Not promoted |
| Feature-quality rank model | 0 qualified windows, longest streak 0 | Not promoted |
| Class-weighted feature model | 1 qualified window, longest streak 1 | Not promoted |
| Expanding technical selector | 1 qualified window, longest streak 1 | Not promoted |
| Regime-conditioned technical selector | 0 qualified windows, longest streak 0 | Not promoted |
| Qualified-rate, hit-count, rank selector | 3 qualified windows, longest streak 1 | Not promoted; tied v14 |
| Recent-five-rate-first selector | 2 qualified windows, longest streak 1 | Not promoted; regressed v14 |
| All 93 cached bar signals plus 25 SEC signals | 2 qualified windows, longest streak 1 | Not promoted; regressed v14 |
| Cross-sectional average-rank diagnostic | 2 qualified windows, longest streak 1 | Not promoted; regressed v14 |
| Best univariate `drawdown_63d` diagnostic | 5 qualified windows, longest streak 1 | Not promoted; retrospective audit |
| Retrospective `drawdown_63d` plus `downside_volatility_63d` rank pair | 4 qualified windows, longest streak 2 | Not promoted; selected after full-history inspection |
| Walk-forward compact rank-pair selector | 2 qualified windows, longest streak 1 | Not promoted; failed point-in-time improvement check |

## Prior conclusion, superseded October 9, 2026

The official v14 replay covers 106 windows with 99 promoted signals and 68 candidates. It uses a schema-8 cache that stores 93 bar signals, including 19 diagnostic additions, while the official selector promotes the proven 74-bar core plus 25 SEC signals. It produces 3 qualified windows, reaches a longest streak of 1, and remains `pass=false`. The historical price store currently ends at August 20, 2026, and the latest realized label is August 20, 2026. Later sessions are required before another forward window can be scored.

The failed experiments are retained as evidence and are not promoted. The next valid action is to append later realized sessions and rerun the canonical exact-two replay. No resend, trade, or other external action is authorized by this analysis.

## August 25, 2026 adaptive regime follow-up

The bounded follow-up tested whether market-state adaptation could improve the five-week gate without allowing future winners to define the state. All completed variants used chronological decisions, the existing realized top-30 labels, exact two distinct picks, and proxy exclusion.

| Diagnostic family | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Same-regime training | 2 | 1 | Not promoted |
| Cutoff-corrected mixture of base and alternate experts | 3 | 1 | Not promoted |
| Two-window hysteresis plus per-pick reliability | 3 | 1 | Not promoted |
| Common top-30-grade fallback | 0 | 0 | Not promoted |
| Fixed market-state factors | 0 | 0 | Not promoted |
| Regime-conditioned winner prototypes | 0 | 0 | Not promoted |
| Online target-mode selector | 1 | 1 | Not promoted |
| Bounded 16-candidate ridge family | 1 | 1 | Not promoted |
| Dated-membership inner predictor | 4 | 1 | Not promoted |
| Fixed-versus-membership outer ensemble | 2 | 1 | Not promoted |
| Regime-entry pair holdover | 1 | 1 | Not promoted |

The fixed regime mapping remains the best market-state candidate at 3 qualified weeks and a longest streak of 1. The official v14 artifact remains unchanged at 3 qualified weeks and a longest streak of 1. The adaptive result is not a five-week success, and no promotion or external action is authorized.

## August 25, 2026 nonlinear model round

The existing ridge family was measured first with an oracle envelope. The oracle is explicitly non-promotable because it uses each current label only to measure candidate upper bounds. The best fixed candidate reached a maximum streak of 2, while the per-window union across all 68 candidates reached 4, so the existing ridge family still cannot contain the requested five-week path.

| Diagnostic | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Ridge candidate oracle upper bound | 3 best candidate | 2 | Non-promotable feasibility bound |
| Regime-conditioned quantile hit-rate calibration | 1 | 1 | Not promoted |
| State-nearest winner prototypes | 0 | 0 | Not promoted |
| Market-context ExtraTrees | 3 | 1 | Not promoted |
| Market-context HistGradientBoosting | 1 | 1 | Not promoted |
| Prequential pooled conformal calibration | 3 | 1 | Not promoted |
| Pairwise diversity calibration | 3 | 1 | Not promoted |

Every completed nonlinear artifact covered 106 windows, had zero contract violations, equal cache-before/cache-after hashes, and an unchanged v14 hash. The fresh Sol review returned `RETHINK`: the goal remains unachieved, and repeated same-sample model selection creates post-selection risk.

## August 25, 2026 state-conditioned confirmation round

| Diagnostic | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Full-feature nearest historical winners | 0 | 0 | Not promoted |
| Same-regime technical-variant selector | 1 | 1 | Not promoted |
| Recent 36-window holdout of strongest completed models | No five-week run | No five-week run | Confirmation failed |

The confirmation round did not produce the requested five-week success. The official v14 result and all protected inputs remain unchanged. Future success requires a genuinely new predeclared candidate space or later realized sessions, not repeated selection from the same 106-window sample.

## August 25, 2026 regime-to-technical mapping oracle

All 6,561 fixed mappings from the four detected market regimes to the nine existing technical variants were evaluated as a label-informed upper bound. Zero mappings reached a five-week streak. The best mapping reached 3 qualified weeks and a longest streak of 1. This closes the current technical-family routing path without proving the broader objective.

## August 25, 2026 pair-specific co-hit continuation

The pair-level co-hit model used a fixed market-state candidate pool and learned joint outcomes from prior labeled windows. It produced 1 qualified week and a longest streak of 1 across 106 windows. The model is not promoted. The resumed blocked audit reset reference is August 25, 2026 18:09:42 CDT.

## August 25, 2026 forward-data boundary audit

Canonical bars were available through August 24, 2026, but the official cache could not label beyond August 20, 2026. A bounded refresh added 2,762 of 3,044 August 25, 2026 bars before rate limiting. The short-warmup current-cohort diagnostic reached a August 25, 2026 label but produced 0 qualified weeks. The exact task-written rows and metadata were rolled back, SQLite integrity passed, and the logical canonical store returned to its prior boundary.

## August 25, 2026 regime winner-frequency continuation

The regime-conditioned winner-frequency model blended prior same-regime top-30 occurrence with a fixed current technical score. It produced 1 qualified week and a longest streak of 1 across 106 windows. It was not promoted. The resumed reset reference remains August 25, 2026 18:09:42 CDT.

## August 25, 2026 adaptive-state and causal-meta continuation

The next bounded round tested three new leakage-safe families after the block and regime batteries failed:

| Diagnostic family | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Market-state adaptive blend and regime-block hold | 0 to 1 | 0 to 1 | Not promoted |
| Stock-level market-state analog KNN | 0 | 0 | Not promoted |
| Causal online selector over the 68-candidate ridge family | 1 to 3 | 1 | Not promoted |

The continuous-state child lane independently matched the official baseline at 3 qualified weeks and a longest streak of 1, with 32 expert switches and unchanged prefix results after future-label mutation. The block audit found no all-qualified oil-like, tech-like, defensive, mixed, or transition block of lengths 1 through 5. The causal ridge meta-selector corrected a double-warmup alignment defect, then covered all 106 windows and still reached only 3 qualified weeks with a longest streak of 1.

All parent-owned diagnostics kept exact-two distinct picks, excluded the proxy basket, preserved equal cache-before and cache-after hashes, and preserved the pinned v14 artifact. The current official label boundary remains August 20, 2026, with canonical bars through August 24, 2026. The five-week goal remains unachieved. No candidate was promoted, and no trade, email, scheduler, resend, or publication action occurred.

## August 25, 2026 trusted-session repair and new model battery

The stall audit found a replay implementation issue. Feature-history construction required raw sessions that the trusted-session audit had already excluded. Partial sessions on July 21, 2026, July 22, 2026, and July 31, 2026 reduced the late common universe from about 2,945 names to 469 and then 409. An isolated trusted-session rebuild restored about 2,900 late-window names without changing the canonical database, official cache, or v14 artifact.

The unchanged official selector still produced 3 qualified weeks and a longest streak of 1 on the repaired cache. A current-cohort trusted-session comparison also produced 3 and 1, so coverage collapse is a real correctness issue but not the sole prediction cause.

| Diagnostic family | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Factor-residual market-state scoring | 2 | 1 | Not promoted |
| Multi-horizon finite-state trajectory policy | 1 | 1 | Not promoted |
| Causal cross-candidate pair and score voting | 3 | 2 | Not promoted |
| State-conditioned MLP | 0 to 1 | 0 to 1 | Not promoted |
| State-conditioned pairwise XGBoost ranker | 0 to 1 | 0 to 1 | Not promoted |

All completed diagnostics used decision-time features and prior labels only, produced zero contract violations, and preserved the official v14 hash. The five-week goal remains unachieved. The trusted-session rebuild is retained as isolated diagnostic evidence only.

## August 25, 2026 signed SEC-event continuation

The event layer was tested with fixed signed theme weights and then with causal same-regime theme calibration. Earnings and transaction themes were treated as positive, financing and legal-risk themes as negative, and event recency was decayed before combining with price confirmation.

| Diagnostic | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Fixed signed event state routing | 1 | 1 | Not promoted |
| Causal adaptive event-theme lift | 0 | 0 | Not promoted |

Both policies covered 106 label-eligible windows after the causal prior-index correction. They produced zero contract violations and preserved the official v14 hash. The event ledger's `available_at` timestamps remain a source-quality limitation, and no event strategy reached the five-week gate.

## August 25, 2026 specialist-library and title-sentiment continuation

A predeclared library of 312 signed single-factor and fixed factor-pair rank rules was tested with global, same-regime, same-dwell, and state-nearest causal routing. The best causal policy produced 2 qualified weeks and a longest streak of 1.

The library's retrospective per-window union reaches 52 qualified windows and a maximum streak of 5. This is a label-informed feasibility envelope only. It is explicitly non-promotable because it chooses the current winning rule after observing the current label. No causal router reproduced that streak.

Raw SEC filing-title sentiment was also tested with event-only, blended, and state-routed price confirmation. These policies produced 0 to 1 qualified weeks and a longest streak of 1. The fresh Sol review returned `RETHINK`. No candidate was promoted.

## August 25, 2026 market-factor alignment continuation

The market-type hypothesis was tested directly with trailing 63-session exposure to oil, growth, and defensive proxy baskets. The active pre-week factor determined whether the selector favored aligned beta, factor-relative residual momentum, or a balanced combination.

| Policy | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Active-factor aligned beta | 0 | 0 | Not promoted |
| Factor-relative residual | 1 | 1 | Not promoted |
| Balanced aligned and relative score | 0 | 0 | Not promoted |

The policies covered 106 windows, selected exactly two non-proxy symbols, produced zero contract violations, and preserved all protected hashes. A fresh Sol review returned `RETHINK`. This family does not explain the five-week gap.

## August 25, 2026 calendar and specialist-meta continuation

The 312-rule specialist library was extended with month, quarter, calendar-plus-regime, state-nearest, state-regression, and score-shape meta routing. All 18 causal policies covered 106 windows and reached a maximum streak of 1.

The per-window union still reaches a five-week streak, but only by selecting the rule after observing each current label. It remains a retrospective feasibility envelope, not a strategy result. The fresh Sol review returned `RETHINK`, and no candidate was promoted.

## August 26, 2026 continuation audit

The local artifact inventory found no unreviewed passing historical diagnostic. The fresh random-month protocol remained `pass=false` at 3 qualified weeks and longest streak 1, the dated-membership variant reached 4 qualified weeks with longest streak 1, and the current-joint-state diagnostic reached 0.

An empirical-Bayes ordinal calibration lane improved proper probability scores slightly but produced 0 qualified weeks and longest streak 0 across 106 windows. The corrected specialist trajectory battery was independently rechecked across 2,756 specialist evaluations. All 26 causal policies had maximum streak 1; trajectory-nearest-5 reached 3 isolated qualified windows but no consecutive run.

The official data boundary remains canonical bars through August 24, 2026 and the latest realized label through August 20, 2026. The five-week goal remains active and unachieved.

## August 26, 2026 dated profile-source continuation

The local profile database contains dated daily snapshots and nightly forecast runs, but coverage begins only in July 2026. A fixed as-of-safe profile strategy was tested on the first five covered replay windows, using one-week, one-month, three-month, volatility, drawdown, breakout, and volume fields. Momentum, breakout, risk-adjusted, and reversal policies all produced 0 qualified weeks and no streak.

The richer nightly forecast path was corrected to strip `actual_*` fields rather than reject every row. Its safe mixed nightly/daily route still produced 0 qualified weeks across the same five windows. The source is retained as diagnostic evidence only because it has narrow coverage and does not improve the exact-two gate.

The nightly profile extension also tested dated target-upside, confidence, valuation, tangible-support, and forecast-consensus routes after stripping all `actual_*` fields. All nightly variants produced 0 qualified weeks across the same five covered windows. No profile-based strategy reached the five-week gate.

## August 26, 2026 remaining local-source audit

The local Google News discovery ledger was replayed with its existing price-plus-news walk-forward module. It produced 4 qualified windows and a longest streak of 1 across 107 evaluations. The module and records identify the timestamps as discovery metadata, not verified publication or pre-decision observation evidence, so the result is non-promotable.

Together with the dated profile, nightly forecast, SEC, price, factor, specialist, and random-month audits, this closes the currently available local data surfaces. No causal 5/5 result exists at the current August 20, 2026 label boundary.

## August 26, 2026 isolated forward-data boundary refresh

An isolated copy of the canonical price store received 3,042 of 3,044 available August 25, 2026 bars. The trusted-session rebuild accepted the new session for quality purposes, but the standard non-overlapping five-session weekly windows still end with decision session August 13, 2026 and label session August 20, 2026. The unchanged official selector and fixed market-state selector remain at 3 qualified weeks and longest streak 1.

The isolated refresh did not alter the canonical database, official cache, or v14 artifact. A later standard weekly decision requires additional realized sessions. The goal remains active and unachieved.

## August 26, 2026 CatBoost runtime attempt

A state-conditioned CatBoost rare-event classifier was started against the repaired trusted-session cache. It exceeded a ten-minute bounded runtime without producing an artifact, so no performance result is claimed. The process was terminated without changing official state. This architecture remains untested rather than failed on predictive evidence.

## August 26, 2026 online Hedge continuation

The 312-rule specialist library was also tested with multiplicative-weights Hedge updates from prior hit losses. Global and state-nearest Hedge routing produced 2 qualified weeks with a longest streak of 1, while same-regime Hedge produced 1 and 1. This did not improve the causal result and remains diagnostic-only.
## August 30, 2026 autonomous source expansion and continuation

The current causal blocker was attacked with a broader official information surface. Fourteen source families were researched. FINRA short interest, CFTC Commitments of Traders, and Treasury daily yields were materialized into a 120-window ledger with strict availability rules. FINRA was retained as diagnostic-only because the public archive can contain current revisions without historical vintages. CFTC and Treasury were used as causal lanes under conservative release cutoffs.

The new selector first combined raw source values with the existing clean arm union, then changed representation by using cross-sectional FINRA and SEC ranks plus macro-to-signal interactions. A separate continuous rank-severity regression battery tested ridge and a reduced ExtraTrees model.

| Diagnostic family | Qualified weeks | Longest streak | Decision |
| --- | ---: | ---: | --- |
| Raw CFTC, Treasury, and FINRA selector | 3 | 1 | Not promoted |
| Ranked source features plus SEC events | 4 | 1 | Not promoted |
| Ridge rank-severity regression | 4 | 1 | Not promoted |
| Reduced ExtraTrees rank-severity regression | 2 | 1 | Not promoted |

All source-expanded routes evaluated 108 windows, selected exactly two distinct non-proxy symbols, produced zero contract violations, and preserved the protected inputs. The post-expansion blocker audit covers 102 clean routes, with maximum aggregate streak 3 and maximum per-market-type streak 1. The realized-label envelope still reaches at least five in every market type, so the precise blocker is causal ranking and pair selection at the current complete-label boundary. No candidate, trade, send, scheduler action, or publication was promoted.
## August 30, 2026 SEC XBRL and source-expanded candidate identification

SEC XBRL Company Facts added a new symbol-level fundamental surface. The adapter used filed date plus one calendar day as the availability boundary and stored one payload hash per resolved CIK. It covered 1,602 candidate symbols and produced features for all 120 decision windows, with three unresolved cases recorded.

The raw XBRL composite improved the causal route to 5 qualified windows and a maximum streak of 2. Ranked XBRL, ridge, and reduced ExtraTrees variants did not improve that maximum. A separate candidate-identification sweep added top and bottom FINRA and XBRL source ranks to the clean arm union. Top/bottom 5 produced 3 qualified windows with maximum streak 1, top/bottom 10 produced 1/1, and top/bottom 20 produced 1/1 for each route.

All completed variants selected exactly two distinct non-proxy symbols, produced zero contract violations, and preserved the protected inputs. The post-XBRL blocker audit covers 126 clean routes. The maximum aggregate streak is 3 and the maximum market-type streak is 2. The realized-label envelope remains 5 defensive, 5 growth-like, 6 oil-like, and 6 transition. The precise blocker remains causal ranking and pair selection at the current complete-label boundary. No candidate or external action was promoted.
## August 30, 2026 source-expanded continuous regression

Continuous rank-severity regression was tested over the top and bottom five FINRA and SEC XBRL source-ranked candidates per source feature. Ridge produced causal/global/state 3/2/1 qualified-count/max-streak results. Reduced ExtraTrees produced 2/2/2. Both models kept exact-two selection, zero contract violations, and protected-input equality.

The updated blocker audit covers 132 clean routes. Maximum aggregate streak is 3 and maximum market-type streak is 2. The realized-label envelope remains 5 defensive, 5 growth-like, 6 oil-like, and 6 transition. The precise blocker remains causal ranking and pair selection at the current complete-label boundary. No candidate or external action was promoted.

## August 30, 2026 full-universe pair ranking and ALFRED expansion

The source-union candidate set was a genuine feasibility limit. Both realized top-30 winners were present in only 83 of 108 evaluated windows. The full-universe cache raised that recall to 108 of 108 windows, with 2,458 to 2,935 candidates per window after proxy exclusion. This removed a hard ceiling but did not solve ranking precision.

The pair selector was expanded with symmetric mean, minimum, absolute-difference, and product features; deterministic hashed negative sampling; an exact top-30 individual prefilter; full-universe bounded sampling; co-hit classification; weak-leg regression; rank-weighted co-hit regression; individual-score consensus; and prior-label membership feedback. The strongest full-universe co-hit result was global/causal/state 4/3/3 qualified windows, all with maximum streak 1. Rank-product reached 2/3/5, also with maximum streak 1. The weak-leg, feedback, consensus, tie-aware, ExtraTrees-prefilter, raw-source, and training-pool branches did not reach the active three-week gate.

The source surface was expanded beyond the three primary raw feeds with nine ALFRED vintage-bound macro series. The ledger fetched 1,080 decision-specific snapshots, uses a vintage one day before each decision session, and feeds 18 additional finite macro features into the raw full-universe cache. The ALFRED ledger hash is `ca956b1d05c12953af3f91260ffd87780a9c92f4543961503cdbbea01b5a36d5`; the resulting 180-feature full-universe cache hash is `e68d328402e298c620761066621c1728470b0da1303f19a35645eaaa7a4eec32`. The ALFRED-enhanced replay fell to 1 qualified window per route, so it remains a rejected diagnostic branch.

The fresh audit now covers 183 clean routes. Maximum aggregate streak is 3 and maximum market-type streak is 2. The realized-label envelope remains 5 defensive, 5 growth-like, 6 oil-like, and 6 transition. The current blocker is causal ranking and pair stability, not raw source availability or candidate-universe coverage. All completed branches preserved the exact-two distinct non-proxy contract, had zero contract violations, and preserved protected inputs. No candidate, trade, send, scheduler action, publication, or promotion was authorized.

## August 30, 2026 causal temporal-membership selector

A simple four-window prior top-30 membership score reached 3 qualified windows with a maximum streak of 2. This was a useful diagnostic because adjacent realized top-30 sets share an average of 1.69 names, but it was not treated as a forecast result.

The causal implementation added three lagged membership rates for each symbol. Each training row used only labels whose label session preceded that training window, and each current row used only prior windows. The first implementation was too slow because it recomputed the same history per row. Precomputing the maps preserved parity and made the full replay complete.

The resulting full-universe rank-product selector produced causal/global/state 1/1/0 qualified windows, with maximum streaks 1/1/0. It therefore did not improve the prior 2/3/5 rank-product result. The current audit covers 186 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The five-week gate remains false. No contract violation or protected-input change occurred.

## August 30, 2026 causal pairwise ranking selector

The pairwise branch changed the learning objective from predicting a pair label to ranking a positive co-hit pair above a non-co-hit pair. Each comparison used only earlier windows and deterministic negative pairing. The full-universe raw replay produced causal/global/state 0/0/0 qualified windows with maximum streak 0. It remained contract-clean but was weaker than the existing co-hit and rank-product branches.

The fresh audit covers 189 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The remaining limitation is causal ranking and pair stability at the complete-label boundary, not source absence or candidate-universe coverage.

## August 30, 2026 causal prototype individual prefilter

The prototype branch compared each current symbol with recent positive and negative feature centroids. This supplied a non-linear similarity prefilter while keeping the final pair objective and contract unchanged. The full-universe co-hit replay produced causal/global/state 1/1/1 qualified windows with maximum streak 1, so it was rejected as weaker than the logistic prefilter.

The fresh audit covers 192 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The remaining limitation is causal ranking and pair stability, not source absence, candidate-universe coverage, temporal features, pairwise ranking, or prototype similarity.

## August 30, 2026 research-backed nonlinear controls

The next model review used the peer-reviewed paper [Empirical Asset Pricing via Machine Learning](https://doi.org/10.1093/rfs/hhaa009), which emphasizes nonlinear tree and neural models for cross-sectional prediction. Direct ExtraTrees reached causal/global/state 0/2/0 qualified windows. A small early-stopped neural classifier reached 2/1/2 with maximum streak 2/1/2. Neural rank-strength regression reached 0/0/0.

The neural prefilter did not combine well with pair scoring. Pair co-hit reached 2/2/1 and rank-product reached 0/0/1. The direct binary neural control was the strongest new branch, but it did not reach the three-week gate. The current audit covers 210 clean routes, with maximum aggregate streak 3 and maximum market-type streak 2. The remaining limitation is causal ranking and pair stability, not source absence, candidate coverage, or lack of tested nonlinear models.

## August 30, 2026 full-rank neural return control

The neural target was changed from a top-30 yes-or-no label to a continuous rank value across the full label universe. This preserves ordering information for every stock while keeping the final success test unchanged. The full-universe replay produced causal/global/state 0/0/0 qualified windows with maximum streak 0, so the branch was rejected.

The current audit covers 213 clean routes. Maximum aggregate streak remains 3 and maximum market-type streak remains 2. The exact five-week gate remains false. The remaining limitation is stable causal ranking of two winners, not source absence, candidate coverage, or lack of nonlinear research.

## October 8, 2026 approved-map feasibility upper bound

The September 21, 2026 artifact tested whether the frozen approved set could contain two non-proxy members of the diagnostic realized top 30, without selecting symbols. It found 89 feasible decisions out of 111. The maximum consecutive feasible runs were 5 defensive, 4 growth-like, 6 oil-like, and 3 transition. It found no historical membership authority, and the expanded manifest had zero operator-confirmed and zero platform-verified symbols. This result bounds feasibility under the tested proxy inputs; it does not prove exact full-market membership, a predictive result, or historical Cash App availability.

Cash App's agreement permits the offered-security list to change at any time without prior notice. The frozen present-day approved CSV therefore cannot establish past availability. Keep the approved list, full-market target, and promotion gates unchanged. No candidate or external action was promoted. Sources: SRC-214 and SRC-215.

## October 8, 2026 offline report-path revalidation

The offline renderer, dry-run dispatch, auto-heal authorization, generator import-safety, and Yahoo source-guard suite passed 47 tests through the canonical runner with offline package resolution. Nine Cash App approval-policy checks passed. AgentMail calls are patched; the observed OSError retry messages came from simulated failure cases. The dispatch safety tests use temporary scripts and do not invoke the loaded LaunchAgent.

The live LaunchAgent remains idle after 15 runs with last exit 0. The latest report remains September 25, blocked by Cash App availability with zero delivery attempts. Report files, delivery markers, and dispatch-log hash remained unchanged. The runbook requires documented Yahoo express permission before generator dry runs, so no current render or delivery occurred. No external action or promotion happened. Source: SRC-216.

## October 8, 2026 private model and source-gate regressions

Six optional forecast-adapter tests passed with fake model outputs, including the opt-in-disabled behavior. Five Yahoo source-access guard tests passed with mocked provider functions, covering both the denied path and the separate Financial Datasets path. No model weights, inference, provider request, price refresh, or production forecast occurred. The tests do not establish prediction accuracy or promotion eligibility. Source: SRC-217.

## October 8, 2026 QuantConnect Cloud and local-download boundary

The earlier local-download pricing statement does not describe QuantConnect Cloud access. Current official pages describe a free Cloud US Equities path and a daily Coarse Universe for all U.S.-traded stocks. Local bulk download remains paid and requires the Security Master. The Coarse Universe may be a candidate for a broader U.S. market analysis, but it does not by itself establish the exact unchanged full-market target, Russell 3000 membership, or Cash App availability. No account or dataset was accessed. Source: SRC-218.

## October 8, 2026 exact-universe and platform-availability source screen

The public source screen did not identify a complete daily Russell 3000 membership-and-weight file with inactive-security history. LSEG's pages describe selected historical constituent products, typically quarterly in arrears, and the current reconstitution page provides dated change notices rather than the full daily roster. QuantConnect ETF holdings are not index membership, and its local bulk access is paid. Cash App's public product page directs users to search in the app; its agreement permits the offered list to change without notice. These pages do not establish past-date availability. This is a bounded public-source finding, not proof that no internal or account-specific record exists. No account, in-app lookup, provider request, data download, purchase, trade, send, scheduler change, or promotion occurred. Sources: SRC-219 and SRC-220.

## October 8, 2026 WRDS FTSE Russell catalog revalidation

The public WRDS catalog recheck confirms that the FTSE Russell US product already recorded in SRC-189 remains listed. It now also confirms the page was last updated September 10, 2026 and specifies no identifiers. The previous SRC-190 entry records a separate legacy sample whose coverage ends in 2017.

## October 8, 2026 public Russell change-file scope

Official LSEG pages make dated Russell 3000 additions and deletions lists publicly visible and describe quarterly IPO additions. They also describe a Daily Events Monitor, selected historical constituent and weight files updated quarterly in arrears, and subscriber access for full announcement versions. This is evidence that some dated changes are available. It does not establish a complete point-in-time Russell 3000 roster or full change history for every weekly decision, or inactive-security coverage. Do not treat these event lists as exact weekly membership. This finding does not claim that no complete history or service exists. No files were downloaded locally and no login, sample, account, data request, purchase, or contact occurred. The exact full-market target, frozen Cash App top-65, protected v14, and five-week promotion gate remain unchanged. Source: SRC-222.


## Current conclusion, October 9, 2026

Protected v14 remains at 106 windows, 3 qualified weeks, maximum streak 1, and `pass=false`. A same-window comparison evaluated the baseline and stable-support candidate on 110 common decision dates, with zero label-session mismatches, zero stored-rank mismatches, and zero contract violations.

| Route | Top-30 name hits | Both-pick windows | Maximum streak | Mean selected realized rank |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 27 | 3 | 1 | 1263.432 |
| Causal | 15 | 2 | 1 | 1305.741 |
| Global | 15 | 3 | 1 | 1294.455 |
| State | 21 | 2 | 1 | 1160.014 |

The state route improved mean realized rank but did not improve the name-hit or paired-window count. No candidate improved validated accuracy or passed the five-week gate. The market-type pair maximum was 1, with zero growth-like paired windows. This remains a diagnostic on the dated IWB/IWM proxy, not exact point-in-time full-market membership. See [SRC-226](source-register.md#src-226).

The current research inputs remain insufficient for a full-market promotion result: the latest complete label is September 18; September 22 fixed-cohort and broad-store row counts are unreconciled; and the date-bounded approval ledger is absent. QuantConnect entitlement and per-decision cutoff safety are unverified. The latest public-source screen found no ready no-account, no-purchase path for exact membership and daily labels; see [SRC-227](source-register.md#src-227). Keep the approved list and protected v14 unchanged. No provider request, account query, purchase, trade, send, scheduler change, or promotion occurred.
