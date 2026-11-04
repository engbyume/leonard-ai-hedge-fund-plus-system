# Forecast Model History and Status

Evidence date: October 9, 2026

This page tracks forecast-model components. It separates forecasts from language-model agents and candidate-selection models. A public model link, code path, or adapter test does not prove that a model produced a report or improved returns.

## Timeline

### August 8, 2026: Kronos retained as optional forecast evidence

The public source register first names Kronos as an optional financial forecasting model. The private report generator contains a Kronos loader and a direct yield call site. That confirms code wiring, not inference in a particular scheduled report. The public method treats forecasts as supporting evidence, not authorization. See SRC-002.

### September 26, 2026: TimesFM 3.0 research adapter

The private runtime contains an adapter for `google/timesfm-3.0-pytorch` behind an explicit non-production opt-in. The official [TimesFM 3.0 license](https://huggingface.co/google/timesfm-3.0-pytorch/blob/main/LICENSE) limits the model grant to non-commercial and non-production use. The canonical LaunchAgent does not set the opt-in. The canonical report generator defines TimesFM helper functions but has no direct call site for them. A separately registered private TimesFM analyst is gated by the opt-in; when disabled or when initialization fails, it returns neutral before price retrieval.

Five adapter contract tests use fake model outputs. They check the opt-in, batch API behavior, and runtime-path wiring. A separate disabled-path regression verifies that the private analyst does not call the price reader when the opt-in is absent. These six tests do not load model weights or evaluate forecast accuracy. No production TimesFM forecast or validated accuracy gain is established.

### October 3, 2026: Evaluation boundary

The model history does not establish full-market forecast accuracy. The latest complete label is September 18, the price stores end September 24, and the September 25 session is missing. The current 123-window IWB/IWM holdings proxy does not establish exact FTSE Russell membership or Cash App availability. No dated approval ledger exists, so no final pick or promotion is supported. See the [current progress report](../evidence/progress.md) and [selector results](../evidence/success-failure-analysis.md).

### October 9, 2026: Matched-window selector diagnostic

A stable-support selector was compared with its baseline on 110 common decision dates. The comparison had zero label-session mismatches, zero stored-rank mismatches, and zero contract violations. Baseline performance was 27 top-30 name hits and 3 both-pick windows. The causal, global, and state candidates had 15/2, 15/3, and 21/2; all had a maximum streak of 1. The state route improved mean realized rank, but paired-window accuracy and name-hit count did not improve. This is selector evidence, not a forecast-model result, promotion, or five-week pass. Protected v14 remains unchanged. See the redacted [progress comparison](../evidence/progress.md#october-9-2026---matched-window-candidate-comparison).

## How to read this history

- Forecast models estimate future prices. Their output is supporting evidence, not a recommendation, order, or approval.
- Analyst agents and candidate selectors are separate model layers.
- Selector experiments, baselines, failures, and results are documented in the [success and failure analysis](../evidence/success-failure-analysis.md).
- A model link, installed package, code path, or mocked test does not prove production use or an accuracy improvement.
- Record model version, source date, input window, seed, fallback, and failure state before making an accuracy claim.

See [source-register entries SRC-002 and SRC-184](../evidence/source-register.md) for the dated sources and limits.
