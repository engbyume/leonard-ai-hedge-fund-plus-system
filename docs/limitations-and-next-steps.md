# Limitations and next steps

[Guide](guide.md) · [Evaluation](evaluation-and-results.md) · [Privacy boundary](privacy-and-publication.md) · [Source register](../evidence/source-register.md)

## What remains unproven

| Limit | Why it matters | Current boundary |
| --- | --- | --- |
| Historical Cash App membership | A stock in a market-data universe may not have been tradeable on the platform at a past decision. | The dated ETF-holdings cohort and a working list are research proxies. The expanded manifest has no verified operator or platform approval (SRC-010, SRC-015, SRC-019). |
| Full and licensed price coverage | Missing or inaccessible labels weaken a fair replay. | The local source has September 24 bars but no September 25 session. The registered path stops before Yahoo-backed refresh without documented express permission. A licensed source or documented permission is needed before that path can run (SRC-020, SRC-023). |
| Stable exact-pair accuracy | Isolated hits do not meet the promotion rule. | Protected v14 has longest streak one and `pass=false` on 106 windows (SRC-015). |
| Portfolio baseline and costs | A reported spread cannot prove an end-to-end return edge without comparable cash flows and costs. | The July 11 baseline is not independently archived; later public rows are limited comparisons (SRC-003, SRC-009). |
| Delivery content readback | A local preview or sent label does not prove the exact rendered body reached the recipient. | Metadata readback found a sent label, but the message body was not retrieved (SRC-012, SRC-014). |
| TimesFM 3 generalization and license | A successful load or diagnostic forecast does not establish production rights or accuracy gains. | Explicit non-production opt-in only; no promotion or production accuracy claim (SRC-018). |

## Next research steps

1. Establish a permitted, sufficiently complete dated price source and verify aligned labels before replay.
2. Obtain authoritative dated Cash App availability evidence, or keep availability unknown and all extra candidates diagnostic-only.
3. Compare each candidate with protected v14 on identical decisions, including route and market-type breakdowns, exact-two violations, and longest streak.
4. Reconstruct a comparable portfolio baseline with cash flows, costs, drawdown, and downside capture before claiming benchmark success.
5. Keep report previews separate from delivery. Verify rendered content and external readback only within a separately authorized send workflow.

No step above authorizes a trade, email, scheduler change, or model promotion.

[Back to guide](guide.md)
