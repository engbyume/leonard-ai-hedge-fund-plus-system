# Architecture

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

## Independent workflows

The standalone simulated app, the canonical scheduled report, and the offline historical replay are separate paths. Evidence from one path does not establish that another path ran or passed its gates.

- **Standalone simulated app:** performs a broad-market screen and hypothetical portfolio analysis. It does not prove Cash App availability, point-in-time membership, or historical eligibility.
- **Canonical scheduled report:** passes the source-permission gate before dispatch and report generation, then checks report rendering and Cash App availability. Email requires a separate authorization. A scheduled run or generated report does not prove delivery.
- **Offline historical replay:** keeps the Cash App top-65 frozen, uses prior-only inputs and labels, and selects exactly two distinct non-proxy names against the unchanged full-market realized top-30 target. Causal, global, state-route, and market-type gates must pass for five consecutive qualified weeks before promotion can qualify. Under approved-symbol scarcity, exactly five dated full-universe extras feed a prior-only ranking, and only the best one or two approved Cash App symbols can be selected. Unapproved extras stay diagnostic-only.

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
