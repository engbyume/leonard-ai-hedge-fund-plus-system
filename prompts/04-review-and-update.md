# Review evidence and update the system

```text
Review the latest report, decision log, and benchmark observations before changing the system.

The root task parent defaults to GPT-6 Luna / max. Easy or routine work and all read-only work use Luna / max. Medium implementation uses GPT-6.1 Terra / medium. Hard, complex, or high-risk implementation uses GPT-6.1 Sol / medium. Ultra-complex implementation uses Sol / high only when estimated completion is under 10 minutes; at 10 minutes or more, or when duration is unknown, use Sol / medium. Astra requires an explicit current-task request. Keep final review acceptance with the Luna / max root. Verify the active model and effort from current-task runtime evidence.

Act as the parent coordinator. Use at most three bounded children and one delegation level. For a different child route, set `fork_turns: "none"` and pass `model` and `reasoning_effort` explicitly; include the full task scope. Use disjoint read-only research roles by default. When a bounded implementation would materially benefit from delegation, prefer one workspace-write child with an exact file scope. Group the five source lanes across no more than three researchers: Yahoo Finance with Reuters, X with CNBC, and MarketWatch with countercase review. Launch independent read-only researchers in parallel in one dispatch round when their scopes do not share state, then wait at one barrier before evidence reduction. Require each child to return a structured record with assigned lanes, query date, source statuses, URLs, evidence, conflicts, limitations, and a no-action declaration. Children may not trade, send, publish, invoke external actions, or edit shared state. Only the parent may make financial decisions or authorize an external effect. The parent owns evidence reduction, conflict resolution, integration, final diff inspection, and fresh verification. Child output is evidence, not proof. Serialize shared writes, finance, outreach, publication, and all other external effects.

Separate machine observations, user confirmations, public-source facts, inferences, and unverified claims. Do not rewrite prior observations to make a later result look better.

For each rule or prompt change, show:

- the advice or evidence that motivated the change
- the operator's decision
- the exact failure or risk the change addresses
- the smallest files or rules that need to change
- a counterexample that could make the new rule harmful
- the test, dry render, or readback that will verify it
- the date and next review condition

Pay special attention to momentum exhaustion. A large one-day move that dominates the positive five-day return is an outlier warning, not a strength score. Keep company-specific catalysts separate from price momentum and require a catalyst for an individual-stock thesis.

Audit the quantitative funnel before catalyst depth. Record the broad source count, the cached-quantitative mini-screen count, the observed full-screen input count after explicit exceptions, the 100-name full-screen finalist count, and the maximum 30-name deep-scan count. Confirm that the mini stage does not call catalyst or multi-source research, and that the full stage runs only on its bounded finalists. For each deep-scan name, verify Yahoo Finance, Reuters, X, CNBC, and MarketWatch source status, source-backed links, dates, positive and negative evidence, distinct source count, insider-selling rejection, persistence, confirmation, countercase, and invalidation. A foundation review must explain the operating reason for the move, not repeat an event label. X stays public and read-only. Record unavailable when dynamic or blocked, and never bypass access controls.

Check ETF card integrity. Every card must be a new non-held ETF candidate marked `new ETF monitor`. A shortage below three stays visible. A standalone held-ETF review must never fill a missing card.

Check the backtest contract. It must rank exactly two distinct stock suggestions against a fixed realized top-30 promotion target. Record top-30 hits and rate, whether both suggestions reached the top 30, the current and longest qualified streaks, and the five-consecutive-week pass result. Keep later realized leaderboards diagnostic only. Any refinement history must use a fixed pre-period variant or walk-forward training. Do not tune on future labels and call the result out-of-sample.

Audit raw and residual extreme price moves before promotion. Apply the dated point-in-time corporate-action ledger only at or before each cutoff, keep append-only source rows unchanged, exclude symbols with residual moves, and report the effective-date availability limitation.

Check performance integrity: one benchmark, one baseline, same dates, same cash-flow treatment, costs, drawdown, downside capture, and data freshness. If the baseline is missing, keep the claim unverified.

Check action integrity: no unmatched sells, no buys funded by unsettled proceeds, no unverified platform availability, and no external action without explicit authorization. Run the validator and a dry report after approved changes. Record failed ideas rather than deleting them.
```
