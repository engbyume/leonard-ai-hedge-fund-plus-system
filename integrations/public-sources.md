# Public source register for the system

| Source | Why it matters | How it is used |
| --- | --- | --- |
| Agent Skills specification | Defines the portable skill boundary | The repository exposes `skills/atlan-scale/SKILL.md` |
| Kronos repository | Documents the public financial model used by the private runtime when available | Forecast evidence with a deterministic fallback |
| Upstream AI Hedge Fund | Demonstrates a public multi-agent research project | Reference for agent roles and research composition |
| yfinance repository | Documents the market-data adapter used by the private runtime | Current market history and price readback |
| SnapTrade Account Data docs | Describe account details, positions, and balances for connected accounts | Capability reference only; this repository makes no claim about a user's account link (SRC-270) |
| AgentMail | Documents the delivery provider used by the private runtime when enabled | Report delivery only |

All live market, company, account, and provider data must be sourced and dated at runtime. Static links do not make current data current.
