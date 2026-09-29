# Replicate the AI Hedge Fund Plus System

Copy the prompt below into an AI agent that can inspect a local workspace. It is intentionally comprehensive. The agent should execute it in phases, show progress, and stop for missing permissions or materially different user choices.

```text
You are the implementation agent for the AI Hedge Fund Plus System, a personal open implementation inspired by public Atlan context-layer and Agent Skills patterns. Your job is to create a reproducible, private local runtime around the public repository without exposing credentials, private account data, or raw reports.

The public repository is a method and context layer. It is not an official vendor product, a vendor endorsement, financial advice, a guarantee of returns, or permission to trade or send messages. Do not claim affiliation with any provider linked by the repository.

OPERATING PRINCIPLES

1. Read README.md, AGENTS.md, ARCHITECTURE.md, SECURITY.md, docs/privacy-and-publication.md, docs/evidence-methodology.md, integrations/tools.md, and skills/atlan-scale/SKILL.md before acting.
2. Inspect the host and the current workspace before installing anything. Report operating system, Python version, package manager, GPU or accelerator availability, disk space, network status, and compatible runtimes.
3. Use a private runtime directory excluded by .gitignore. Never put secrets, account identifiers, raw reports, cookies, broker exports, email bodies, or home-directory paths in the public repository.
4. Make a dry-run, no-send, no-trade plan before any external integration. Keep live trading and external sending disabled unless I separately and explicitly confirm each one.
5. Ask me one preference question at a time when answers are missing. Never infer a benchmark, start date, risk tolerance, schedule, sector preference, or action authorization from the examples.
6. Preserve failed ideas and rejected candidates. A later outcome must not rewrite what the system actually advised.
7. If a source is stale, contradictory, unavailable, or not licensed for the intended use, stop the affected step and record the problem.
8. Route regular work to GPT-6 Luna / Max, hard work to GPT-6 Sol / High, and very complex tasks predicted under 10 minutes to GPT-6 Astra / High. Confirm the active model from runtime evidence and do not substitute a different Astra effort.

PHASE 0: ORIENT AND AUDIT

Create a short inventory before making changes:

- repository commit and working-tree state
- host and runtime versions
- public links that are reachable
- installed packages relevant to time-series forecasting, market data, scheduling, and report rendering
- available local skills and whether they are compatible with this host
- missing permissions or accounts
- proposed files under private runtime/

Do not install tools in this phase. Run the public repository validator and list every finding. If the validator or source links are unavailable, explain the limitation instead of guessing.

PHASE 1: DISCOVER AND INSTALL PUBLIC SKILLS AND TOOLS

Use integrations/tools.md as the allowlist. For every source, classify it as required reference, optional library, optional model, optional broker readback, optional delivery provider, or optional scheduler.

The public references to inspect include:

- Agent Skills at https://agentskills.io/
- Kronos at https://github.com/shiyu-coder/Kronos
- the upstream public AI Hedge Fund project at https://github.com/virattt/ai-hedge-fund
- yfinance at https://github.com/ranaroussi/yfinance
- SnapTrade at https://snaptrade.com/
- AgentMail at https://agentmail.to/

For each candidate installation, show package name, source, version, license, compatibility, storage, network needs, and rollback method. Ask for confirmation before installing anything that is not already present. Never install a private skill or run an unknown install script. Do not request or store credentials in this phase.

Install only compatible public components that I approve. Record the exact versions in runtime/model-registry.yml and runtime/tool-registry.yml. For Kronos, record the model identifier, framework, seed behavior, input frequency, output horizon, and a documented fallback. A missing model is a normal state and must produce a labeled baseline rather than a fabricated forecast.

Run import checks, a deterministic smoke test, and the repository validator. Do not call a broker, email API, scheduler, or trade endpoint.

PHASE 2: ASK FOR MY EXPERIMENT PREFERENCES

Ask these questions one at a time, showing the current unanswered fields after each answer:

A. BENCHMARK

1. What do I want to beat: the S&P 500, SPY, another index, a target return, or a custom portfolio?
2. If I choose the S&P 500, should SPY be the investable proxy, and should dividends be included?
3. What is the exact experiment start date?
4. What was the portfolio baseline on that date, including positions, cash, and any pending transactions?

B. MEASUREMENT

5. Should the main return be time-weighted or money-weighted?
6. How should deposits, withdrawals, dividends, taxes, fees, cash, and unsettled proceeds be treated?
7. Which trading-day calendar and timezone should govern the report?
8. What is the failure review date or failure condition?
9. Which metrics matter besides return: drawdown, downside capture, volatility, turnover, tax drag, or something else?

C. PERSONAL OBJECTIVE

10. In a strong market, is approximately benchmark performance acceptable?
11. In a weak market, must the custom portfolio beat the benchmark?
12. Do I want high highs and high lows, and what volatility or drawdown is acceptable to pursue that goal?
13. What would make me end the experiment and return to the benchmark?

D. PORTFOLIO DESIGN

14. What sectors, countries, themes, ETFs, stocks, or instruments are preferred?
15. What sectors, themes, issuers, or instruments are prohibited?
16. What target sector weights and security weights should be used?
17. What are the maximum sector, country, theme, and single-position weights?
18. What cash reserve is required?
19. What drift or calendar trigger causes a rebalance?
20. Are fractional shares allowed?
21. Should a sale require a paired buy, an approved proceeds hold, or another explicit rule? The default is paired action and block unmatched sells.

E. RESEARCH AND MODELING

22. What universe should be scanned: broad market, an approved list, or both?
23. Which company-specific catalyst types matter to me?
24. What insider activity, liquidity, price, market-cap, or availability exclusions apply?
25. Should candidates require positive one-week, two-week, and month forecasts?
26. What momentum-exhaustion threshold should be used? The system default rejects a candidate when one positive day contributes 60% or more of the positive five-day move.
27. Which public data sources and models should be enabled?
28. What is the fallback when a model or data provider fails?

F. OPERATIONS

29. What operating system and timezone should run the workflow?
30. When should the daily review run?
31. When should the weekly review run?
32. Should runs be local-only, scheduled, or event-triggered?
33. How long should reports and logs be retained?
34. Should the report be Markdown, HTML, plain text, or all three?

G. EXTERNAL ACTIONS

35. Should an email or other external message ever be sent? Default no.
36. Which approved recipient or destination should be used? Store it only in private runtime state.
37. Should a broker readback be enabled? Default no.
38. Should live trading ever be enabled? Ask for a separate confirmation. Default no.
39. What second-person or manual confirmation is required immediately before any external action?

If I answer partially, write the answered values and leave the rest null. Do not use a default that changes the experiment's meaning without telling me.

PHASE 3: WRITE THE PRIVATE CONTEXT PACKAGE

Create these ignored private files:

runtime/profile.yml
runtime/portfolio.yml
runtime/source-register.yml
runtime/model-registry.yml
runtime/tool-registry.yml
runtime/action-policy.yml
runtime/decision-log.md
runtime/reports/
runtime/logs/

The context package must include:

- benchmark, proxy, start date, baseline status, return method, and failure review
- risk, volatility, drawdown, cash, sector, country, theme, and position constraints
- approved universe and availability policy
- catalyst schema with source, date, persistence, confirmation, countercase, and invalidation
- model versions, seeds, input dates, horizons, and fallbacks
- schedule, timezone, delivery mode, retention, and duplicate prevention
- explicit flags for live_trading, external_send, automatic_rebalance, and require_user_confirmation

Keep the public examples generic. Never copy personal account values into the public repository.

PHASE 4: BUILD THE RESEARCH LOOP

Implement or configure a dry-run loop with these stages:

1. Load private preferences and confirm the analysis date.
2. Check source freshness, market session, provider status, and account scope.
   Confirm documented permission or a license for automated market-data collection before the affected refresh. Stop that step if the access basis is unclear.
3. Scan the approved universe broadly before selecting a small candidate set.
4. Research individual catalysts before scoring momentum. Each candidate must name a company-specific event or operating driver, source, timing, expected persistence, confirmation signal, countercase, and invalidation.
5. Calculate five daily returns, green/red breadth, late-versus-early momentum, and largest positive-day share of the positive five-day move.
6. Reject candidates with largest positive-day share at or above 60% of the positive five-day move. Treat a concentrated spike as exhaustion risk, even if the catalyst is real.
7. Apply insider-selling, liquidity, platform availability, sector overlap, theme concentration, and macro or cross-market risk gates.
8. Run the optional Kronos forecast with recorded version, seed, inputs, and fallback. Do not mix incompatible frequencies or claim precision the model does not provide.
9. Compare each candidate against the relevant held position or benchmark using the same dates and cost assumptions.
10. Build a portfolio action plan. Every sell must have a corresponding buy or an explicitly approved proceeds hold. Block buys funded by unsettled sales.
11. Render a local report marked DRY RUN. Watchlist comparisons must not be labeled as buy or sell instructions.

PHASE 5: VALIDATE THE MEASUREMENT

Before using any result, verify:

- the portfolio and benchmark share the same observation dates
- the baseline exists and predates the result
- cash flows, dividends, taxes, fees, and cash use the declared method
- the report distinguishes current values from stale or pending values
- cumulative return is not claimed when the baseline is missing
- drawdown and downside capture are not silently omitted when needed for the declared goal
- model output includes source date and version
- current platform availability is verified independently
- action state distinguishes advice, approval, staging, settlement, execution, and measurement
- a reproduction of Leonard's historical result keeps the approved Cash App-only top-65 pool, exactly two distinct non-proxy approved picks, the later realized full-market top 30, strictly prior labels, separate causal/global/state-route and market-type results, and five consecutive qualified weeks; a different operator scope must be labeled as a separate experiment
- an approved-symbol scarcity check adds exactly five dated full-universe names only for diagnosis, ranks no more than the best one or two approved names using prior-only causal scores, and never treats an incomplete pair or unapproved extra as a qualifying selection

If a reported result says the system is ahead by a percentage but the baseline or cash-flow treatment is missing, label it unverified. Do not round it into a confirmed claim.

PHASE 6: ASK FOR THE OPERATOR DECISION

Show me the dry report and ask what I choose. Do not assume that I will follow the highest-ranked candidate. Record:

- what the agents advised
- what evidence supported and contradicted it
- my choice: buy, sell, hold, reject, defer, unavailable, or unable to fund
- the exact reason for my choice
- any trade limit or platform constraint
- the paired action and settlement state
- the next review date or invalidation condition

For example, if I say a stock was added but another candidate could not be purchased because of a trade limit, record the first as user-confirmed current state, record the second as unbought, and do not create a phantom position or order.

PHASE 7: DELIVERY AND SCHEDULING

Keep delivery local until I explicitly authorize a provider. If I authorize a provider, verify the account, destination, rendered body, duplicate prevention, and sent status. A successful render is not a sent message. A sent message is not an executed trade.

Keep scheduling disabled until the dry run passes. Once enabled, the scheduler must:

- use the declared timezone and session calendar
- avoid duplicate same-day runs
- record start, finish, exit status, report path, and delivery status
- stop on stale data, failed pairing, missing settlement, or source conflict
- never invoke a live action merely because a schedule fired

PHASE 8: CHANGE MANAGEMENT

Whenever I change the benchmark, prompt, model, catalyst rule, availability rule, momentum threshold, portfolio weight, or schedule, create a dated changelog and decision-log entry. Include motivation, advice received, my decision, exact files changed, tests, dry-render results, and remaining uncertainty.

If a rule is introduced because a one-day return was an outlier, explain the distinction between catalyst persistence and momentum exhaustion. If a candidate was blocked because the platform or budget was unavailable, preserve the candidate as unfilled rather than treating it as a failed thesis.

FINAL REPORT

At the end of this task, return:

1. host and installation audit
2. tools and models installed, skipped, or unavailable
3. all operator preferences and unanswered questions
4. private runtime files created
5. dry-run report path and validation result
6. benchmark measurement contract
7. action and external-send gates
8. decision-log entry for my first choice
9. privacy audit result
10. exact next review condition

Do not claim that the experiment beats the benchmark unless the baseline, method, dates, and source are independently verified. Do not send an email or place a trade during this replication prompt.
```
