# Model and strategy history

[Guide](guide.md) · [Timeline](timeline.md) · [Evaluation](evaluation-and-results.md) · [Source register](../evidence/source-register.md)

Leonard combines **agent research**, **forecast evidence**, and a **historical selector**. An agent is a role that gathers or weighs evidence. A forecasting model estimates a future path. The selector ranks candidates for a dated historical decision. None of these is an order executor.

## The layers

| Layer | Role | What is verified |
| --- | --- | --- |
| Research agents | Review fundamentals, technical behavior, sentiment, catalysts, and risk; a portfolio role combines the findings. | The upstream AI Hedge Fund project provides the original agent-workflow reference. Leonard adds its own gates and evidence records. |
| Kronos | Optional price-path forecast evidence. | The public interface links to Kronos. A missing dependency can leave a dry report without a fresh forecast; a rendered report alone does not prove model use. |
| Protected v14 | Official historical replay baseline, using 74 bar and price-volume signals plus 25 dated SEC event signals. | The current artifact identifies a walk-forward ridge selector, 99 official features, 106 evaluated windows, and `pass=false` (SRC-027). |
| Diagnostic selectors | Test alternative ranking, grouping, market-state, pair, and support methods against the same strict contract. | Tested alternatives in the dated notes did not establish a five-week pass or a validated improvement over protected v14 (SRC-011, SRC-030, SRC-031). |
| TimesFM 3 | Separate time-series forecasting experiment, not an LLM. | Current private adapter names version 3.0.1 and the public checkpoint; use requires explicit non-production opt-in. It has not earned production use or an accuracy claim (SRC-030). |

## Task model routing

Task routing selects the language model that performs the research or code work. It is separate from the forecasting model that estimates a price path.

| Task class | Preferred model | Effort |
| --- | --- | --- |
| Regular or bounded work | GPT-6 Luna | Max |
| Hard, complex, or high-risk work | GPT-6 Sol | High |
| Very complex work expected under 10 minutes | GPT-6 Astra | High |

The active model must be checked from current-task runtime evidence. A saved preference or role file is not proof that a running session uses that route. The current routing preference is operator-directed and dated in the [source register](../evidence/source-register.md) (SRC-037).

## Why v14 is protected

The historical selector must choose **exactly two distinct, non-proxy stocks** from the approved Cash App top-65 research scope. It is scored against the realized **full-market** top 30 after the decision. Training and route choices may use only labels that were known before that decision. Causal, global, state-route, and market-type checks stay visible. A candidate model is promoted only after the original five-consecutive-qualified-week gate and the other required comparisons pass. See [evaluation and results](evaluation-and-results.md).

The September 28 artifact reports three qualifying windows in 106 evaluations, but they do not form a five-week streak. Changing the target to a smaller market list or treating an unverified availability manifest as approved would change the question rather than improve the selector.

The [historical experiment history](experiment-history.md) groups the diagnostic families by question and explains why isolated gains were not enough.

## What the experiments taught

- **Extra features are not automatic gains.** Historical branches added dated market, filing, and peer information. The evaluated branches could lose qualified pairs even when their data lineage improved.
- **Pair quality is the bottleneck.** A method can rank one strong name and still fail the exact-two full-market target.
- **Availability is a separate fact.** A dated research universe or spreadsheet does not prove a stock was Cash App tradeable at the decision time.
- **A live model is not a validated model.** Loading TimesFM 3 or rendering a forecast does not establish better accuracy on the shared historical decisions.

Earlier private Skill snapshots list several language-model fallbacks. Their exact adoption dates and per-run model use were not verified, so this page does not assign them a performance history.

[Back to guide](guide.md)
