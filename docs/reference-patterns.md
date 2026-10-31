# Reference Repository Patterns

Initial review: October 3, 2026; rechecked: October 7, 2026

This page records a read-only review of official repository pages. It summarizes documented architecture and safety patterns. It is not a ranking, benchmark, or independent validation. No source code, model weights, data, or dependency was copied into this project.

## Finance research systems

### Upstream AI Hedge Fund

The upstream project describes itself as an educational research proof of concept and says it does not place trades. Its repository also documents investor-agent roles and runtime API requirements. This project uses those as reference points for its research-only scope and operator gates; it does not vendor the upstream code. [Repository README](https://github.com/virattt/ai-hedge-fund).

### Microsoft Qlib

Qlib documents a quant-research pipeline covering data processing, model training, backtesting, and analysis across signal, risk, portfolio, and execution layers. The useful documentation pattern is to state each stage and its evidence boundary. This project keeps its own models and data separate from Qlib. [Repository README](https://github.com/microsoft/qlib).

### QuantConnect LEAN

LEAN describes an event-driven, modular algorithmic-trading engine. Its README presents local backtesting and live execution as separate commands. This project follows the documentation distinction between a local dry run and an external action. The canonical pipeline does not integrate LEAN. A separate no-order Cloud date probe is recorded in SRC-196 and SRC-199. [LEAN README](https://github.com/QuantConnect/Lean).

## General agent workflow

### LangGraph

LangGraph describes infrastructure for long-running, stateful workflows, including durable execution, human oversight, and persistent memory. This project records state in versioned context and evidence documents, with explicit approval before external actions. It does not depend on LangGraph. [Repository README](https://github.com/langchain-ai/langgraph).

## How these references inform this project

- Keep public method, private runtime, and operator state in separate layers.
- State data sources, dates, assumptions, and limitations beside each result.
- Keep forecasts and agent analysis separate from approval or execution.
- Preserve dry-run, validation, and external-action steps as distinct states.
- Record failed approaches and their limits without presenting them as successful strategies.

These patterns improve documentation and auditability. They do not validate the AIHF strategy or its performance.

## Sources

- [Upstream AI Hedge Fund](https://github.com/virattt/ai-hedge-fund)
- [Microsoft Qlib](https://github.com/microsoft/qlib)
- [QuantConnect LEAN](https://github.com/QuantConnect/Lean)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- See [source-register entries SRC-185 and SRC-198](../evidence/source-register.md) for the dated sources and recheck limits.

## October 3 live recheck

The official repository pages were read again during the completion audit. The Qlib summary now stays with the documented data, model, and backtest stages. The LEAN summary distinguishes the canonical pipeline from the separate Cloud probe. These references remain architecture guidance, with no imported code or performance claim.


## October 7, 2026 official repository recheck

### OpenBB Open Data Platform

The current OpenBB repository is under openbq-org. Its README describes an open data layer for licensed and public sources, exposed through Python, Excel, MCP, and REST surfaces, with a Workspace UI documented separately. It also states that data may be inaccurate and trading involves risk. This is a pattern for separating data access, user surfaces, and source limits; Leonard does not integrate OpenBB. [OpenBB README](https://github.com/openbq-org/OpenBB).

### OpenAI Agents SDK

The official SDK README groups agent instructions, tools, guardrails, handoffs, sessions, tracing, and human-in-the-loop steps. Its guardrails documentation distinguishes checks around function tools from handoff checks. This is a pattern for naming workflow gates, not evidence that Leonard uses the SDK or has equivalent runtime controls. [OpenAI Agents SDK README](https://github.com/openai/openai-agents-python) and [guardrails documentation](https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md).

### Rechecked workflow patterns

- Qlib documents qrun as a configured dataset, training, backtest, and evaluation workflow, alongside a modular code interface for custom research.
- LEAN presents lean backtest and lean live as separate commands, which keeps local evaluation distinct from external execution.
- LangGraph describes durable execution, human oversight, persistent state, and tracing for long-running workflows.

These are maintainer-described documentation patterns, not performance evidence. No code, data, model weights, dependency, or service was copied. See source-register entry SRC-206.
