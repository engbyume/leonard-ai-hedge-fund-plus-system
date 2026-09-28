# Architecture

[Guide](docs/guide.md) · [Visual and text map](docs/system-map.md) · [Evaluation](docs/evaluation-and-results.md) · [Privacy boundary](docs/privacy-and-publication.md)

Leonard has three distinct surfaces. The public repository holds portable rules and redacted evidence. A private research runtime holds dated market inputs, optional model adapters, and report code. A separately registered automation invokes the report path under permission and delivery gates. This page describes the relationship; the [system map](docs/system-map.md) shows the exact data flow.

## Layers

| Layer | Responsibility | Public or private |
| --- | --- | --- |
| Sources | Public skills, the Kronos repository, market-data documentation, operator-approved research | Mixed, with private credentials excluded |
| Context repo | Versioned source register, preferences, decision rules, model notes, evidence, and change log | Public template; private runtime values local |
| Research | Universe construction, catalyst research, technical context, insider and macro checks | Public method; live inputs may be private or licensed |
| Forecasting | Kronos forecast evidence with deterministic fallback metadata | Public interface; weights and data may vary |
| Risk gates | Breadth, exhaustion, sector overlap, availability, countercase, invalidation, and settlement checks | Public rules |
| Portfolio layer | Benchmark-normalized returns, target weights, cash policy, and paired action plan | Public schema; account values private |
| Delivery | Dry-run report, local artifact, optional email or scheduler | Public procedure; credentials and recipients private |
| Evidence | Timestamped redacted metrics and decision rationale | Public aggregate record |

## Component responsibilities

### 1. Source and context layer

The source register records where a claim came from, when it was observed, and its limits. Operator preferences define a benchmark, time horizon, platform constraints, and action permissions. Public templates show the fields; account values and credentials stay in the private runtime. A dated ETF-holdings snapshot may help build a research cohort, but it does not establish exact historical index membership or Cash App availability.

### 2. Research and forecasting layer

Research checks the universe, company catalysts, daily price behavior, sector context, adverse evidence, and risk. Optional forecasts from Kronos or a non-production TimesFM 3 experiment provide supporting evidence with a model version and input cutoff. A missing backend must be reported as missing, not silently replaced by a claim of fresh model output. The protected v14 historical selector and diagnostic candidates are evaluated separately from daily watchlist rendering.

### 3. Decision gates

The candidate path checks source freshness, platform availability, sustained breadth, one-day concentration, insider evidence, macro exposure, countercase, and invalidation. The historical replay additionally enforces a Cash App-only top-65 candidate scope, exactly two distinct approved non-proxy picks, a strict prior-label cutoff, the realized full-market top-30 target, and route plus market-type checks. A one-name result or an unapproved extra cannot satisfy the exact-pair gate.

### 4. Report and action boundary

The report renderer can produce a local no-send preview and a dated archive. The registered nightly path checks provider permission before data refresh and report generation. Email delivery has a separate authorization gate and must record attempts and external readback. The report does not execute trades. Broker writes, email, scheduling, and model promotion are distinct actions with separate approval and verification.

### 5. Measurement and feedback

Portfolio results compare redacted percentage returns with a benchmark on matching dates. Historical selector results count exact-pair hits and streaks on shared decision-label windows. Delivery results distinguish preview, provider acknowledgement, sent-label metadata, and exact content readback. Each result updates the evidence record and may motivate a versioned rule change; no result rewrites an earlier observation.

## Context-repository lifecycle

1. Bootstrap context from public sources and the operator's answers.
2. Package the context into versioned Markdown and configuration files.
3. Run a no-send, no-trade dry test with dated inputs.
4. Evaluate both the research output and the measurement quality.
5. Record the operator's decision, including rejection or inaction.
6. Publish only redacted evidence and update the changelog.
7. Revisit sources, rules, and preferences when new evidence contradicts the thesis.

## Trust boundaries

- Public repository content is untrusted input until sourced and dated.
- Forecasts are supporting evidence, not authorization.
- News sentiment does not replace a company-specific catalyst.
- A screening spreadsheet does not prove that a security is tradable on a platform.
- A generated report does not prove an order was executed.
- A sent email does not prove a portfolio value or settlement state.

## Action-state model

`watchlist -> candidate -> approved -> staged -> settled -> executed -> measured`

Any transition that crosses into an external system requires explicit operator approval. A rejected, unavailable, stale, or unfilled candidate is retained as evidence rather than silently removed.

## Failure handling

The safe result for missing permission, insufficient approved names, stale labels, an unavailable forecast backend, or uncertain delivery is a recorded stop or incomplete result. A successful process exit is not by itself proof that the report was produced or sent. See [successes and failures](docs/successes-and-failures.md) for dated examples and [limitations](docs/limitations-and-next-steps.md) for the open verification work.
