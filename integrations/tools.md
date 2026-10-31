# Public tools and integrations

The links below cover skills, repositories, and provider capabilities used or referenced by the documented workflow. They do not grant this repository permission to download, authenticate, send, trade, or scrape anything. Check each project's current license and terms before use.

| Tool or source | Link | Role | Status |
| --- | --- | --- | --- |
| Agent Skills | https://agentskills.io/ | Portable `SKILL.md` format and progressive disclosure | Required reference |
| Kronos repository | https://github.com/shiyu-coder/Kronos | Financial K-line forecasting used by the private runtime when available | Used, with deterministic fallback |
| Upstream AI Hedge Fund | https://github.com/virattt/ai-hedge-fund | Public research-agent reference for the private runtime | Used as reference |
| yfinance | https://github.com/ranaroussi/yfinance | Market-price and history adapter | Used by the private runtime |
| SnapTrade | https://docs.snaptrade.com/docs/account-data | Account details, positions, and balances API | Capability reference only; user-account linkage is not verified here (SRC-270) |
| AgentMail | https://agentmail.to/ | Approved report-delivery provider | Used by the private runtime when enabled |

## Installation policy

The replication prompts must inspect the host before installing. Install only compatible components, keep Kronos behind a feature flag, record versions, and provide a deterministic fallback. Never place keys in this file or in a public configuration example.
