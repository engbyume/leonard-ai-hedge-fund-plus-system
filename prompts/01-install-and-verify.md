# Install and verify public components

```text
You are installing optional, public components for the AI Hedge Fund Plus System. Inspect the host before installing anything. Show me the proposed packages, versions, licenses, storage needs, Python compatibility, GPU requirements, and network access for each component.

Use the public links in integrations/tools.md. The relevant components are the Agent Skills format, Kronos, yfinance, and the configured broker-readback or delivery providers. Do not download private skills, arbitrary code, model weights, cookies, credentials, or account exports. Do not use a third-party repository as a source of truth when its license or compatibility is unclear.

Installing a market-data client does not grant rights to automate data collection. Check the source's current terms and documented permission or use a licensed alternative before any automated refresh. If the access basis is unclear, stop that source-dependent step and report the gap.

Install only compatible components after the compatibility report is complete. Record exact versions and a fallback for each missing or failed component. Run a non-network import or version check where possible, followed by a small deterministic smoke test. Never call a broker, email provider, or trade endpoint during this prompt.

Create a private runtime/model-registry.yml with provider, version, seed, input requirements, output status, fallback, and license notes. Run the repository validator and report every failure. A failed model installation must result in a labeled baseline or missing value, never a fabricated forecast.
```
