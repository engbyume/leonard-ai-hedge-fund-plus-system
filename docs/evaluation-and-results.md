# Evaluation and results

[Guide](guide.md) · [Methodology](evidence-methodology.md) · [Results table](../evidence/weekly-checkpoints.csv) · [Source register](../evidence/source-register.md)

Two different evaluations appear in this project. **Portfolio comparison** asks how an account performed against a chosen benchmark. **Historical selector accuracy** asks whether two dated research picks later appeared in the full-market top 30. A positive result in one does not prove the other.

## Portfolio comparison

For a fair SPY comparison, declare the start date and return method, align market closes, and state how cash flows, dividends, costs, taxes, and cash were handled. The public CSV contains redacted percentages, not balances or order values.

| Published observation | Portfolio | SPY | Spread | Limit |
| --- | ---: | ---: | ---: | --- |
| August 5, 2026, month | 1.81% | 2.95% | -1.14 percentage points | Archived checkpoint |
| August 10, 2026 report, latest 21 sessions | 2.49% | 2.87% | -0.38 percentage points | Market closes through August 7; pending contribution excluded |
| August 10, 2026 report, open-position comparison | 4.09% | 4.25% | -0.16 percentage points | Starts with confirmed positions, not a verified July 11 trial baseline |

These rows do not establish durable benchmark outperformance. The July 11 trial-start baseline, complete cash-flow treatment, costs, drawdown, and downside capture are still missing (SRC-003, SRC-009). The user's earlier belief of about 3% outperformance remains an unverified hypothesis (SRC-008).

## Historical selector contract

1. At each decision date, build the approved Cash App-only top-65 candidate scope from information available then.
2. Select exactly two distinct approved non-proxy names. If approved names are scarce, add exactly five dated full-universe candidates for diagnosis and rank only the best one or two approved names by prior-only causal score. Fewer than two approved names cannot form a qualifying pair. Unapproved extras never become approved by appearing in that diagnostic list.
3. Compare the selected pair with the later realized **full-market** top 30. A week qualifies only if both names are present.
4. Keep the strict prior-label cutoff, causal, global, state-route, and market-type checks. Evaluate candidate and baseline on identical decision and label sessions.
5. Require five consecutive qualified weeks before promotion. Record all failed windows and contract violations.

> **Current protected result:** On September 28, 2026, v14 reports three qualified weeks across 106 evaluated windows. The longest qualified streak is one; `pass=false`. The simple exact-pair hit fraction is 3/106, about 2.83%, on this artifact's own window set. This is not a portfolio return or a forecast-error score (SRC-027).

### Point-in-time safeguards

The official v14 artifact uses a dated research cohort derived from IWB and IWM holdings snapshots. Each decision uses the latest snapshot strictly before the decision session. This is an ETF-holdings proxy, not exact historical index membership or proof of Cash App tradeability. It retains 74 bar and price-volume signals and 25 dated SEC event signals. The SEC inputs require source-backed timestamps at or before the decision cutoff; current sector and market-cap metadata stay out of the official replay (SRC-027).

The later label is the adjusted-close return at the exact fifth subsequent trusted market session. Rows without a later label are excluded from training and realized-rank scoring, rather than treated as misses. A cached window is bound to its price-store and dated-universe inputs so new bars cannot silently reuse an old evaluation. These controls reduce look-ahead risk, but provider records without a publication timestamp and historical platform membership still limit what the replay can prove.

The September 21 approved working-list audit found both realized top-30 names in its 677-name list in 89 of 111 decisions. Maximum feasible runs were five defensive, four growth-like, six oil-like, and three transition. This is a **feasibility ceiling**, not achieved accuracy or proof of dated Cash App availability. Growth-like and transition could not reach five consecutive feasible decisions on that boundary (SRC-010, SRC-031).

## Evidence grades

The [source register](../evidence/source-register.md) labels machine observations, user reports, public sources, and inferences. Historical notes explain why a branch was tested; the protected artifact and comparable replay outputs determine whether it passed. No diagnostic has been promoted on the evidence published here.

[Back to guide](guide.md)
