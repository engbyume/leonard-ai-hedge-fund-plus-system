# Historical experiment history

The stock-selector experiments below are research records. A diagnostic result is not a promoted strategy, a portfolio return, or a live forecasting record. Results from different window sets are not directly comparable without aligning their decision and label dates.

## How the question developed

| Research question | Finding and limit |
| --- | --- |
| Can a historical replay avoid using later information? | The protected replay uses dated inputs and separates unknown later labels from negative outcomes. Its IWB/IWM holdings cohort is a proxy, not verified exact historical index membership or platform eligibility. |
| Does a wider candidate pool solve the problem? | Candidate retrieval and final pair selection are different stages. Wider diagnostic pools can reveal retrieval limits but cannot turn an unapproved security into an eligible selection. |
| Do different pair scorers produce stable results? | Multiple causal, global, and state-route experiments were recorded. Isolated hit counts did not establish the required stable five-week streak or a validated improvement over the protected baseline. |
| Is the approved working list large enough? | The September 2026 feasibility study found both realized top-30 names on the working list in 89 of 111 decisions. The maximum feasible consecutive runs differed by market type. This was an upper bound, not selector performance or proof of dated platform availability. |
| Does another forecast model prove improvement? | Loading a model, producing a finite forecast, or passing an adapter test is a runtime check. Promotion requires the same decision windows, labels, eligibility rules, and independent evaluation as the baseline. |

The [success and failure analysis](../evidence/success-failure-analysis.md) retains the dated experiment records and their separate windows. The [progress narrative](../evidence/progress.md) records later source and feasibility checks. The [model history](model-history.md) describes the forecast components and their status.

## Evaluation rules retained from the research

1. Use information available at the decision cutoff. Treat later labels as unknown until they are observable.
2. Record the candidate universe and its evidence. Keep historical holdings proxies and unverified platform availability labeled as such.
3. Compare candidates and baselines on the same decisions and labels. Report the number of qualified windows and the longest consecutive streak, not only a favorable aggregate.
4. Preserve failed experiments and the protected artifact. Do not promote a candidate solely because it improves one diagnostic or in-sample score.

The protected v14 result remains three qualified windows out of 106, longest streak one, with `pass=false`. See [evaluation and results](evaluation-and-results.md) for the distinction between this selector test and portfolio measurement.
