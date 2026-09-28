# Successes and failures

[Guide](guide.md) · [Timeline](timeline.md) · [Evaluation](evaluation-and-results.md) · [Limitations](limitations-and-next-steps.md)

Here, **success** can mean a safety or data-quality control worked. It does not mean the portfolio beat SPY or the historical selector passed promotion. Each item is dated and tied to the [source register](../evidence/source-register.md).

## Controls that worked

| Date | Observed result | Scope of the evidence |
| --- | --- | --- |
| August 3, 2026 | A concentrated five-day price move was treated as an exhaustion warning. The reviewed candidate was removed from the eligible replacement watchlist. | Candidate-screen correction, not a future-return result (SRC-004). |
| September 21, 2026 | The aligned-label replay reported zero exact-two contract violations across 111 evaluated decisions. | Historical diagnostic contract only; no five-week pass (SRC-019). |
| September 22, 2026 | A no-send report preview rendered with zero delivery attempts and zero proposed actions. | Local dry-run and focused tests, not proof of an external delivery (SRC-012). |
| September 26, 2026 | The Yahoo permission gate stopped the registered path before refresh, report, and delivery. | A dated safety stop; it also left that run without a new report (SRC-020). |

## Hypotheses that failed or remain open

| Hypothesis or aim | Observed result | Decision |
| --- | --- | --- |
| The protected v14 selector meets five consecutive qualified weeks. | Three qualified windows in 106, longest streak one, `pass=false` on September 28 (SRC-015). | Keep v14 protected; do not promote. |
| More dated signals or a different selector automatically improves exact-pair accuracy. | Evaluated diagnostic routes did not establish a validated improvement on shared decisions (SRC-011, SRC-018). | Retain failed branches as evidence. |
| Five extra full-universe names solve approved-symbol scarcity. | A literal diagnostic branch introduced exact-two violations; an approved-fill branch preserved the contract but did not pass the gate (SRC-019). | Keep extras diagnostic-only and availability approval separate. |
| The portfolio has a demonstrated long-run benchmark edge. | The August 10 month and open-position spreads were negative, and the reported trial-start baseline is missing (SRC-003, SRC-009). | Do not claim durable outperformance. |
| A sent label proves the exact report body arrived. | The scheduled report had a sent-label metadata match, but the body was not retrieved (SRC-014). | Treat exact content delivery as unverified. |

The [decision log](../evidence/decision-log.md) preserves why rules changed. The [evaluation page](evaluation-and-results.md) defines the different denominators behind these observations.

For the deeper selector sequence, read the [historical experiment history](experiment-history.md).

[Back to guide](guide.md)
