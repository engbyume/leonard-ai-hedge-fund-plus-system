# Leonard: AI Hedge Fund Plus System

**Purpose:** Leonard is a personal, educational system for AI-assisted investment research. This public repository contains its method, portable prompts, source rules, and redacted evidence. The private runtime holds live data and account state. The repository name remains `ai-hedge-fund-plus-system`, and the public Skill remains [`atlan-scale`](skills/atlan-scale/SKILL.md).

> **Status, September 28, 2026:** The protected v14 historical selector has **not** passed its five-consecutive-qualified-week gate. Its current artifact records three qualified weeks in 106 evaluated windows and a longest streak of one. No validated accuracy improvement or promotion is claimed. See [evaluation and results](docs/evaluation-and-results.md) and the [source register](evidence/source-register.md).

## Explore

| Start with | Then read |
| --- | --- |
| [Documentation guide](docs/guide.md) | A route through the linked pages |
| [Visual and text system map](docs/system-map.md) | How sources, research, gates, reports, and evidence connect |
| [Progression timeline](docs/timeline.md) | Dated changes and corrections |
| [Model history](docs/model-history.md) | Agent roles, optional Kronos forecasts, v14, and diagnostic models |
| [Historical experiments](docs/experiment-history.md) | The research questions and representative failed branches |
| [Evaluation and results](docs/evaluation-and-results.md) | What the numbers measure and what they cannot prove |
| [Successes and failures](docs/successes-and-failures.md) | Observed controls, rejected hypotheses, and open claims |
| [Limitations and next steps](docs/limitations-and-next-steps.md) | Open data, availability, and delivery questions |

## Use the public method

Clone the repository, run `python3 scripts/validate_repo.py`, then follow the [reproduction guide](docs/reproduction.md). The guide links to the prompts for preference intake, dry-run research, review, and redacted evidence import. Optional model or provider installation needs its own license and access check.

## Safety and scope

This is **not financial advice**. A forecast or watchlist is research, not a trade instruction. External email, broker actions, and scheduler changes require separate operator authorization and verification. Public documentation excludes credentials, account identifiers, raw emails, broker exports, private prompts, and private home paths. See [privacy and publication](docs/privacy-and-publication.md).

Leonard is an independent personal project. The `atlan-scale` name describes a local context-layer Skill and does not claim affiliation with Atlan or any linked provider. Original repository material is MIT licensed; linked projects retain their own terms. See [third-party notices](THIRD_PARTY_NOTICES.md).
