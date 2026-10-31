# Evidence methodology

## Measurement contract

Use one benchmark, one declared start date, one return method, and consistent treatment of cash flows. The default example uses SPY as the investable proxy for the S&P 500. A valid comparison should identify whether it is time-weighted or money-weighted, how deposits and withdrawals are handled, and whether transaction costs, taxes, dividends, and cash are included.

The public table reports percentage returns and spreads only. `spread = portfolio return - benchmark return` for the same period.

## Historical selector accuracy

For historical selection diagnostics, exact-pair hit rate is `qualified windows / evaluated windows`. A window qualifies only when both distinct non-proxy picks land in the realized full-market top 30. Preserve the Cash App top-65 prefilter, strict prior-label cutoff, route and market-type checks, and exact-two selection.

Compare candidate accuracy only on identical decision and label sessions. Report route-level results and the longest consecutive qualified streak. This diagnostic is separate from portfolio returns and cannot replace the five-consecutive-week promotion gate.

## Evidence labels

- `machine_observed`: extracted from an archived report or deterministic run.
- `user_confirmed`: explicitly supplied by the operator, such as a purchase or rejection.
- `public_source`: supported by a public URL.
- `inference`: a reasoned interpretation that is not directly proven.
- `unverified`: a claim that needs a baseline, readback, or source before it can be measured.

## Momentum and catalyst evidence

An individual-stock candidate needs a company-specific catalyst with a date or persistence window, supporting evidence, a countercase, and an invalidation signal. Momentum is evaluated using all five daily returns, green/red breadth, late-versus-early momentum, and the largest positive day's share of the positive five-day move.

Use this catalyst record for every serious candidate:

- `source`: the exact outlet name and a direct or clearly labeled public URL. Required lanes are Yahoo Finance, Reuters, X, CNBC, and MarketWatch.
- `date`: the publication timestamp and analysis date. Do not use an undated item as current proof.
- `source_status`: `available`, `unavailable`, or `not_scanned`, with a short reason. A failed fetch is a data-quality result.
- `source_backed_evidence`: the headline or fact supported by the link. Keep positive and negative evidence separately and record the distinct source count.
- `persistence`: the expected duration of the operating effect and the evidence for that duration.
- `confirmation`: the next observable result that would strengthen the thesis.
- `countercase`: the strongest supported reason the apparent catalyst may fail or already be priced in.
- `invalidation`: the observable condition that ends the thesis.

Run quantitative triage first. Move the full approved stock profile set through a cached-quantitative mini screen that uses only stored returns, volatility, drawdown, volume, consistency, breadth, and exhaustion fields. Pass 200 mini finalists plus explicit held or foundation exceptions to the richer full profile and sector screen, retain 100 full-screen finalists, and cap the five-lane deep source screen at 30 names. The current run had 201 full-screen inputs because the held-symbol exception was outside the 200 mini finalists. Foundation names consume slots inside the deep cap, so a small configured cap can review fewer than all five. Their analysis must connect the observed move to an operating or expectation mechanism supported by public evidence. An earnings or investor-day label alone is not an explanation. Treat X as a public read-only search surface. If it is dynamic or blocked, record `unavailable`. Never bypass login, CAPTCHA, access control, or rate limits.

If the largest positive day contributes 60% or more of the positive five-day move, reject the candidate from the weekly replacement watchlist as a concentration and exhaustion risk. The 60% threshold is a hard exclusion in this system, not a reason to increase confidence.

## ETF monitor evidence

Every delivered ETF card must cover a new non-held ETF candidate and must be marked `new ETF monitor`. A held ETF cannot fill an empty slot. If fewer than three new candidates pass the screen, report the delivered count and the shortage.

## Top-30 two-pick evaluation

The approved historical source is a derived adjusted-close store filtered by dated BlackRock IWB and IWM holdings snapshots. Each decision uses the latest holdings snapshot strictly before that session because the archived snapshots do not provide publication timestamps. This is a dated ETF-holdings proxy, not exact FTSE Russell membership, historical listing or delisting evidence, or historical Cash App availability. The current official replay uses 74 bar and price-volume features available through each decision session. It also uses 25 SEC EDGAR features only for source-backed, point-in-time eligible records whose accepted, published, and filing timestamps are all valid and no later than 15:59:59.999999 America/New_York on the decision session. The SEC event-price interactions are computed only after that cutoff filter, from same-cutoff event and price features. Current sector and market-cap metadata and discovery-only Google News records remain excluded. The replay rejects globally incomplete sessions against a local 11-session baseline at a 95% coverage threshold, and it retains the full decision feature universe even when a later label is unavailable.

Corporate actions are handled through a dated point-in-time ledger without rewriting append-only source rows. A matched action factor is applied only to bars on or after its effective date and only when that date is at or before the relevant cutoff. Symbols with residual extreme moves remain excluded. In the current artifact, six action boundaries are matched, four retained-symbol boundaries are applied, 39 symbols remain excluded, and one residual extreme move remains after one corrected move, so the current price-quality status is `partially_reconciled`. The latest audit reports 92 raw extreme moves across 44 symbols. The effective-date boundary is a conservative availability proxy because provider action records do not include publication timestamps. The default window-cache receipt binds the replay schema, signal schema, dated-universe content hash, and corporate-action ledger content hash. A ledger-only change invalidates the default cache and requires an explicit rebuild before reuse.

Recent candidate-identification diagnostics preserve this contract while comparing materially different causal representations. The nine-source cache adds vintage macro, insider filings, institutional holdings breadth, and fails-to-deliver features only when their source hashes and decision cutoffs match. A temporal-context test follows the time-aware framing in [Prospective Learning](https://openreview.net/forum?id=XEbPJUQzs3&noteId=dvgkjWAUlf), and the source-block graph test gives each source block equal distance influence before the peer search. These are diagnostic branches until they improve the realized top-30 route and market-type gates. A source count or lower token cost does not prove better candidate identification.

The anchor-stable pair control is also diagnostic. It fits separate pair models in chronological early, middle, and recent environments, then subtracts a fixed instability penalty from the mean score. The fit uses only labels available before each decision. It cannot change the exact two-pick contract, the realized top-30 test, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

The dynamic Bradley-Terry control is also diagnostic. It follows the time-varying pairwise ranking direction in [Nonparametric Estimation in the Dynamic Bradley-Terry Model](https://proceedings.mlr.press/v108/bong20a.html). It compares prior top-30 symbols with prior non-top-30 symbols, weights each comparison by prior-window distance, and estimates symbol strengths without reading the current label. It cannot change the exact two-pick contract, the Cash App-only top-65 scope, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

Kernel Rank Centrality is also diagnostic. It follows the pairwise rank-centrality and dynamic spectral directions in [A Statistical Convergence Perspective of Algorithms for Rank Aggregation from Pairwise Data](https://proceedings.mlr.press/v32/rajkumar14.html) and [A Spectral Approach for the Dynamic Bradley-Terry Model](https://arxiv.org/abs/2307.16642). It converts strictly prior weighted comparisons into a normalized transition graph and uses stationary scores. It cannot change the exact two-pick contract, the Cash App-only top-65 scope, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

HodgeRank is also diagnostic. It uses the same strictly prior pair comparisons but fits symbol potentials by weighted least squares over pairwise residuals, following the HodgeRank direction in [A Statistical Convergence Perspective of Algorithms for Rank Aggregation from Pairwise Data](https://proceedings.mlr.press/v32/rajkumar14.html). It cannot change the exact two-pick contract, the Cash App-only top-65 scope, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

The artifact-policy tournament is diagnostic. It selects among completed, independently generated policies using only their earlier hit fractions, following the walk-forward model-selection principle in [Model Assessment and Selection under Temporal Distribution Shift](https://proceedings.mlr.press/v235/han24b.html). It cannot use the current label, change the exact two-pick contract, expand beyond the Cash App-only top-65 scope, or weaken any route, market-type, or five-consecutive-week gate.

Feature-BTL least squares is also diagnostic. It follows the feature-informed pairwise ranking direction in [A Graph Theoretic Approach for Preference Learning with Feature Information](https://proceedings.mlr.press/v244/saha24a.html). It fits only strictly prior feature differences and cannot change the exact two-pick contract, the Cash App-only top-65 scope, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

Context-aware HGB is also diagnostic in the artifact-policy layer. Its completed policy artifact can be compared with other completed policies using only earlier hit fractions, but adding it cannot change the exact two-pick contract, the Cash App-only top-65 scope, the route gates, the market-type gates, or the five-consecutive-week promotion gate.

Current-cache arm consensus is also diagnostic. It counts support from completed, protected current-cache arm outputs without reading the current label. Hash-prefiltered arm discovery is a runtime optimization only; it does not change candidate scope, gate definitions, or the no-action policy.

The candidate-prefilter audit separates retrieval from pair ranking. It records how many realized top-30 winners enter the fixed top-65 pool and whether the pair stage fails when both are reachable. It is diagnostic only and cannot relax the Cash App-only scope, exact-two contract, route gates, market-type gates, or five-consecutive-week promotion gate.

At each dated cutoff, rank candidates using only information stored at or before that cutoff and select exactly two distinct stock suggestions. Use the exact fifth later trusted market session, and its adjusted-close return from the decision session, as the later diagnostic label. Rank the full label-eligible snapshot by that realized return. Record the target top-30 hits, hit rate, and whether both suggestions reached the realized top 30 for every window. A week qualifies only when both suggestions have labels and both realized ranks are 30 or better. The current v14 schema-8 derived subset remains partially reconciled under the active point-in-time policy because one residual extreme move remains after ledger correction and exclusions; earlier historical entries retain their prior limitations.

Track the ending consecutive qualified streak and the longest qualified streak. The quality gate passes only when the longest streak reaches five consecutive qualified weeks. Report the pass or fail result directly. Do not describe fewer than five consecutive qualified weeks as a pass.

Realized leaderboards are diagnostic only. They cannot become an input to an earlier forecast. The current ridge selector trains and chooses among 64 ridge configurations plus four label-free consensus candidates only from completed prior windows whose label session is strictly before the current decision session. A bounded refinement history can compare fixed scoring variants declared before the validation period and walk-forward variants trained only on completed prior windows. Record each variant, training policy, validation windows, result, and production selection. Do not tune on future labels and then describe that result as out-of-sample proof.

## Benchmark interpretation

One positive spread is not proof of a durable edge. The evidence should show multiple checkpoints, market direction, drawdown, downside capture, and data quality. A neutral or zero spread may be low-information if the report was incomplete, reset, or produced on a non-comparable date.

## Evidence gaps

If the baseline is missing, say so. If the broker value is pending, say so. If a platform is not independently confirmed, retain `Manual Cash App search required` or the equivalent status. If a sale is recorded without a paired buy, block publication and correct the plan before delivery.
The August 30, 2026 source expansion is diagnostic and does not change the official v14 selector. Fourteen official source families were researched. FINRA short-interest files, CFTC historical COT files, and Treasury daily yield feeds were materialized into a separate ledger for all 120 windows. FINRA current archive revisions are excluded from promotion. CFTC records use a conservative four-calendar-day release cutoff, and Treasury records use a one-calendar-day availability lag. Raw and cross-sectional-ranked source vectors, point-in-time SEC events, ridge rank-severity regression, and reduced ExtraTrees rank-severity regression were evaluated against the unchanged exact contract.
The SEC XBRL Company Facts diagnostic lane was added on August 30, 2026 for symbols in the clean candidate-arm union. Each fact uses filed date plus one calendar day as a conservative availability rule. The lane records CIK resolution, payload hashes, unresolved symbols, and 120-window feature coverage. It remains diagnostic-only because the public Company Facts payload does not provide the acceptance-time vintage needed to prove the exact historical state of every fact. Source-expanded candidate pools add top and bottom source ranks to the clean arm union, but only the unchanged exact top-30 five-week contract can support promotion.

The SEC Forms 3, 4, and 5 overlay is a separate diagnostic source. It uses the public submissions endpoint, records accession IDs, and uses `acceptanceDateTime` at or before `15:59:59.999999 America/New_York` on each decision session. Filing date is a fallback only when acceptance time is absent. Form 4/A and other amendments remain separate observations. The overlay adds eight cross-sectional ranked filing-activity features to the fixed 168-feature Cash App cache. It failed the unchanged gate and cannot be promoted without a new immutable vintage policy and a successful causal replay.

The historical selector excludes unknown later labels by default. A training row is eligible only when its later label exists; an unavailable label is not a negative. This default is required for all future selector comparisons. The flag and artifact metadata remain explicit so older replays can be audited without rewriting historical evidence.

The candidate-identification battery now includes a decision-time peer graph. Each window is robustly scaled across its available symbols. Each symbol receives features from its eight nearest current-window peers, including a local centroid, a residual from that centroid, local dispersion, and local density. The graph uses no later labels. Peer graphs are precomputed once per fixed cache so replay speed does not change the model or the cutoff policy.

The battery also records reachable top-30 recall. Ordinary recall uses all realized top-30 labels in the label universe. Reachable recall uses only realized winners that are present in the approved candidate map for that decision window. This is a diagnostic distinction. It does not relax the exact two-pick or five-consecutive-week rule. Source-blocked reciprocal-rank fusion uses only source blocks and past quality history. It is not treated as a calibrated probability, and its constants are fixed before replay.

The peer graph, matured peer history, source-blocked reciprocal-rank fusion, rank-quantile HGB, and graph hard-negative controls remain diagnostic. The best new downstream result did not extend the maximum streak. Current Cash App availability and historical Cash App membership remain unverified until an in-app check or an authoritative historical platform record is available.

Temporal contrastive candidate identification is also diagnostic. It compares each current symbol with positive and negative feature centroids from strictly earlier labeled windows, weights those comparisons by current-context similarity and age, and excludes unknown later labels. It must use only the current decision features before the label is read. The exact two-pick contract, realized top-30 test, and five-consecutive-week gate remain unchanged.

Market-type group-robust logistic training is diagnostic. It uses the existing prior-only training rows and updates group weights from past log loss for the observed market-type groups. It cannot use the current label, change the candidate pool, or weaken the exact two-pick and five-consecutive-week gates. A clean replay is required before any future promotion decision.

Temporal model tournaments are diagnostic. They may choose among existing causal scorer families using only earlier labeled precision. A minimum history and fixed tie order are required. The current decision and its label must be excluded from model choice. The tournament cannot weaken the exact two-pick or five-consecutive-week gates.

## Full-universe pair diagnostics

The pair research cache can use the complete decision universe after protected proxy exclusion. This is separate from the source-union candidate mode. The full-universe mode is required when a source-union recall audit shows that a realized winner is absent before model selection. The cache records candidate mode, source representation, feature profile, tie-aware ranking, and all input hashes.

Pair training uses causal rolling windows only. Positive co-hit pairs are retained. Large-universe negative classes use deterministic hashed sampling. Pair features are symmetric, and the final decision still selects exactly two distinct non-proxy symbols. Optional rank-product, weak-leg, consensus, ExtraTrees, and historical-membership feedback variants remain diagnostic until they pass the unchanged consecutive gate.

The source surface now includes nine ALFRED vintage series. Each response is cached at a vintage one calendar day before the decision session. This avoids same-day publication ambiguity and keeps the macro features separate from the current label. The ALFRED lane is diagnostic until its vintage and revision behavior remain stable across future refreshes.

Temporal membership features are also diagnostic. For each target window, the selector may use prior top-30 membership rates over three trailing horizons. A training row may use only earlier windows whose label sessions precede that row's decision session. A current decision may use only prior windows. The lag maps are precomputed for parity and speed. They cannot change the exact-two or five-consecutive-week promotion gate.

Pairwise ranking is diagnostic. It compares a positive co-hit pair against a non-co-hit pair from an earlier window and fits on signed symmetric-feature differences. The current result did not improve the gate. A failed ranking branch cannot become a production path without a complete replay and the unchanged consecutive qualification gate.

Prototype similarity is diagnostic. It compares current symbols with recent positive and negative feature centroids from prior windows. It cannot replace the exact two-pick contract or the unchanged five-consecutive-week gate.

Nonlinear individual models are diagnostic. The current research control uses a small early-stopped neural classifier and a bounded ExtraTrees classifier. The model family is motivated by peer-reviewed cross-sectional asset-pricing research, but every candidate still requires the same walk-forward replay and consecutive gate.

Full-rank targets are diagnostic. They preserve the relative rank of every labeled stock during training instead of treating all stocks outside the top 30 as identical. The final decision still uses the exact realized top-30 rule and the unchanged five-consecutive-week gate.

Forecast ensembles are diagnostic. The current ensemble averages the ranks from logistic, tree, and neural individual models with equal weights fixed before evaluation. It does not use current or future labels to tune those weights. The final decision still requires the exact two-pick and consecutive-week gates.

Dynamic forecast weights are diagnostic. The current control uses only each model's earlier successful-week history to set later weights. The current week is excluded from the weight calculation. The result remains subject to the exact two-pick and five-consecutive-week gates.

Dynamic model feedback may use earlier top-30 accuracy to set later weights. This feedback is calculated only after the earlier label is available before the later decision. It is diagnostic and cannot weaken the exact two-pick or five-consecutive-week gates.

Price-rank controls must be isolated from other new sources when measuring their effect. The current control uses no ALFRED features, so its result measures price representation only. It remains diagnostic and cannot weaken the exact gates.

Score smoothing is diagnostic. The current control blends each model score with the previous decision's score using a declared weight. It uses no current or future labels and cannot weaken the exact two-pick or five-consecutive-week gates.

Price rank normalization is diagnostic. Each price signal may be ranked across the current decision universe and mapped to a stable range before training. Ties receive equal values. This transformation does not change the realized top-30 test or the two-pick safety rules.

List-based ranking is diagnostic. A training list may represent one earlier decision window, with the realized top-30 members receiving the positive mass and deterministic earlier non-winners supplying the comparison set. The scorer must validate only on earlier labeled windows, and the final decision must still select exactly two distinct names using the unchanged realized top-30 and five-consecutive-week gates. A list-level objective cannot turn realized labels into a current-week input.

Multi-cutoff top-k ranking is diagnostic. A weekly training list may contribute separate top-2, top-5, top-10, and top-30 probability targets. The final test remains top-30 membership for exactly two picks. The objective can emphasize retrieval depth, but it cannot weaken the prior-label cutoff or the five-consecutive-week gate.

Hard-negative sampling is diagnostic. A bounded share of each training list may use the closest prior-label ranks outside the top 30, while the remaining negatives use stable hash sampling. Hardness is fixed before the current label is read, and the sampler must retain all prior top-30 positives. This improves the training question without converting future ranks into current inputs.

Cross-sectional context is diagnostic. A current-window context may summarize the full available universe with deterministic average, dispersion, and attention-weighted values. The summary is computed from features available at the decision cutoff. It cannot use the later label, and the final two-pick and five-week gates remain unchanged.

Candidate-pool width is diagnostic. The individual prefilter may be widened before joint pair scoring to test whether one winner is discarded too early. The width is recorded in the artifact, and the final selection still requires exactly two distinct names in the realized top 30.

Broad rank aggregation is diagnostic. Multiple separately fitted causal models may contribute within-window ranks before the final two names are selected. The member list, training policy, and prior-label rule must be recorded. Aggregation cannot turn a failed route into promotion evidence without the unchanged consecutive gate.

History length is diagnostic. A longer prior-label window may be tested against the same feature cache and selection rule. The comparison must change only the number of earlier eligible windows, record the window count, and keep the same exact-two, realized top-30, and five-consecutive-week requirements.

Univariate rank-lift scoring is diagnostic. For each earlier window, a feature may be converted to cross-sectional quantile bins and scored by the prior top-30 hit lift of each bin. Feature selection, smoothing, and bin definitions must use only earlier labeled windows. The final decision still requires exactly two distinct names in the realized top 30 and the unchanged five-consecutive-week gate.

Nonlinear joint pair scoring is diagnostic. A bounded tree model may score symmetric features for candidate pairs after an individual prefilter. The pair labels must come only from earlier realized top-30 membership, and the final selection must still contain exactly two distinct non-proxy names. A higher total hit count is not sufficient; consecutive route and market-type gates remain mandatory.

Residual gated score heads are diagnostic. A direct linear score may be combined with a bounded multiplicative branch to add controlled feature interactions. The head must train only on earlier labels, record its bottleneck and gate strength, and remain subject to the same exact-two and five-consecutive-week gates.

Uncertainty-aware rank aggregation is diagnostic. Cross-model rank dispersion may act as a conservative uncertainty proxy when the member models use the same prior-label boundary. The penalty and member list must be fixed before replay. This proxy cannot weaken the exact-two or five-consecutive-week gates and must not be described as a formal confidence interval unless interval coverage is separately proven.

Individual pairwise ranking is diagnostic. Each prior top-30 winner may be compared against bounded negatives from the same earlier window, with the learned comparison direction applied to the current universe. The negative budget, hardness rule, rank weights, and recency weights must be fixed before the current label is read. The final selection remains exactly two distinct names in the realized top 30.

Online expert weighting is diagnostic. Expert weights may be updated after each earlier label using exponential loss updates. The update history must be restricted to completed prior windows, and the learning rate and lookback must be fixed before replay. The weighted score remains subject to the exact-two and five-consecutive-week gates.

Weekly rank-correlation training is diagnostic. A model may optimize centered agreement between its current-window scores and earlier realized rank severity, with a separate top-30 membership term. The ranking loss must use only earlier labels, and the final decision remains exactly two distinct names in the realized top 30 across the unchanged five-week gate.

Direct top-30 membership voting is diagnostic. Multiple causal rankers may cast one vote for each stock in their current top 30, with a declared deterministic tie-breaker. Votes must be based on current features and prior-trained models only. The final selection remains exactly two distinct non-proxy names, both judged against realized top-30 membership.

Cash App-only historical scope is diagnostic. The approved 700-row Cash App CSV is the source for the research allowlist. Normalize tickers, remove known non-stock instruments and protected proxies, and intersect the result with each historical feature window before model fitting. The list does not prove historical Cash App availability, so the scope must remain labeled diagnostic-only. The candidate-pool width may be 50 or 65, but realized success remains exactly two distinct picks in the full label-ranked top 30.

FINRA daily short-sale volume is diagnostic. Use the consolidated daily file for the latest trade date strictly before each decision session. Record the original response hash and exclude files marked `Updated`. Derived ratio, mean, shock, exempt-ratio, and log-volume features cannot support promotion until the archive's historical revision behavior is independently vintage-safe.
