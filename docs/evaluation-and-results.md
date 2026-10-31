# Evaluation and results

This page separates portfolio outcomes from the historical stock-selector experiment. They answer different questions and do not share a success rate.

## Portfolio comparison

The [checkpoint table](../evidence/weekly-checkpoints.csv) contains redacted percentage observations. A benchmark comparison needs aligned dates, a declared return method, and explicit treatment of cash flows, dividends, costs, and cash. An unverified starting baseline or incomplete cash-flow record limits what the table can establish. The [measurement method](evidence-methodology.md) describes these limits.

## Historical stock selector

The protected v14 artifact evaluated 106 decision windows. Three qualified, the longest consecutive streak was one, and the recorded five-week gate was `pass=false`. A qualifying pair consists of two distinct selected stocks that both appear in the later realized full-market top 30 under the experiment's rules. This is a research outcome, not a portfolio return or proof of future performance.

On 110 matched decision dates, the recorded baseline produced 27 top-30 name hits and three qualifying two-pick windows. The causal, global, and state-route candidates recorded 15/2, 15/3, and 21/2 respectively. Each route's longest qualifying streak was one. These matched-window diagnostics did not improve validated accuracy or pass the promotion gate. See [progress](../evidence/progress.md) and the [success and failure analysis](../evidence/success-failure-analysis.md) for scope and evidence.

## What the evidence cannot establish

- The historical cohort uses dated IWB and IWM holdings as a proxy. It is not verified exact Russell 3000 membership or dated Cash App eligibility.
- The price stores and labels have documented coverage gaps. Missing or untrusted observations are not evidence of successful predictions.
- A simulation, a rendered report, a delivered email, and a broker action are separate events. A pass in one path does not establish success in another.
- Backtest selection and repeated tuning can overstate performance. Compare strategies on the same decision dates, enforce information-availability cutoffs, and report holdouts separately.

Read the [source register](../evidence/source-register.md), [decision log](../evidence/decision-log.md), and [measurement method](evidence-methodology.md) before relying on a result.
