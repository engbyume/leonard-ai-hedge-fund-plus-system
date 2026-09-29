# Limitations and next steps

[Guide](guide.md) · [Evaluation](evaluation-and-results.md) · [Privacy boundary](privacy-and-publication.md) · [Source register](../evidence/source-register.md)

## What remains unproven

| Limit | Why it matters | Current boundary |
| --- | --- | --- |
| Historical Cash App membership | A stock in a market-data universe may not have been tradeable on the platform at a past decision. | The dated ETF-holdings cohort and a working list are research proxies. The expanded manifest has no verified operator or platform approval (SRC-010, SRC-027, SRC-031). |
| Full and licensed price coverage | Missing or inaccessible labels weaken a fair replay. | The local source ends on September 24, 2026. Yahoo refresh remains blocked without express permission. No alternative has been selected or verified against the exact local symbol/session cohort (SRC-035, SRC-038). |
| Stable exact-pair accuracy | Isolated hits do not meet the promotion rule. | Protected v14 has longest streak one and `pass=false` on 106 windows (SRC-027). |
| Portfolio baseline and costs | A reported spread cannot prove an end-to-end return edge without comparable cash flows and costs. | The July 11 baseline is not independently archived; later public rows are limited comparisons (SRC-003, SRC-009). |
| Delivery content readback | A local preview or sent label does not prove the exact rendered body reached the recipient. | Metadata readback found a sent label, but the message body was not retrieved (SRC-012, SRC-014). |
| TimesFM 3 generalization and license | A successful load or diagnostic forecast does not establish production rights or accuracy gains. | Explicit non-production opt-in only; no promotion or production accuracy claim (SRC-030). |

## Dated price-source screen

This documentation-only screen uses vendor pages and terms dated September 28, 2026. It does not authorize an account, data request, purchase, or source change. No option has been checked against every symbol and session in the existing 3,182-symbol store and dated cohort. Keep the unverified expanded manifest diagnostic-only.

| Provider | Documented fit | Remaining gate |
| --- | --- | --- |
| Tiingo EOD | Individual Power is listed at $30 per month, with 60+ years of history, adjusted prices for splits and dividends, and stated limits of 110,125 unique symbols per month and 100,000 requests per day. | API use is internal-use only. Starter and trial plans cannot persist data; paid-plan data must be deleted after cancellation or downgrade. Documentation describes delisted support for unrecycled symbols and warns some may lack prices. Verify full cohort coverage, retention, and any public-output rights before use (SRC-038). |
| Nasdaq Sharadar SEP | Premium daily EOD prices and corporate actions include adjusted and unadjusted series for 20,000+ active and delisted U.S. companies, with history from 1998. | Price and order-form terms require account access. Verify the exact license and derived-output rights before use (SRC-038). |
| Alpaca Basic | Free plan documentation describes 7+ years of historical bars, up to 200 requests per minute, multi-symbol queries, `adjustment=all`, and historical SIP data older than 15 minutes. | API authentication is required. No account or access is authorized, and documentation does not establish full delisted-symbol coverage or fit to this cohort (SRC-038). |
| Alpha Vantage | Daily Adjusted documents 25+ years of split and dividend adjusted history. | Full history is a premium feature; the standard tier allows 25 requests per day. Full-cohort and delisted coverage are unverified (SRC-038). |
| Massive | Historical aggregates begin in 2003 and the adjustment flag adjusts prices for splits. | The current price contract also includes dividend adjustments. Terms restrict derived investment strategies without a separate license, so this is not an equivalent replacement as documented (SRC-038). |

## Next research steps

1. Obtain operator authorization for a source and tier. Before any request, verify its rights, retention limits, adjusted-price method, and coverage for the exact stored symbols and required historical sessions. Then refresh an isolated candidate, preserve prior rows, and verify a complete aligned label before replay.
2. Obtain authoritative dated Cash App availability evidence, or keep availability unknown and all extra candidates diagnostic-only.
3. Compare each candidate with protected v14 on identical decisions, including route and market-type breakdowns, exact-two violations, and longest streak.
4. Reconstruct a comparable portfolio baseline with cash flows, costs, drawdown, and downside capture before claiming benchmark success.
5. Keep report previews separate from delivery. Verify rendered content and external readback only within a separately authorized send workflow.

No step above authorizes a trade, email, scheduler change, or model promotion.

[Back to guide](guide.md)
