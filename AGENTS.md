# Repository operating rules

This repository is a public, personal documentation and orchestration layer. Keep private runtime state outside the checkout.

## Source of truth

- Public architecture, prompts, schemas, and redacted evidence live here.
- A user's private runtime is the local source for live account state and credentials.
- Public claims require a source register entry and a date.
- Historical evidence is never silently rewritten after a later result becomes available.

## Safety

- Never commit credentials, cookies, API keys, account identifiers, raw emails, broker exports, or private filesystem paths.
- Never place a live trade or send an external message from a dry-run workflow.
- Require explicit operator confirmation before any external action.
- Treat platform availability as unverified until the operator confirms it.
- Every proposed sell must have a corresponding buy or a documented, approved proceeds-hold instruction.
- A momentum spike is not durable momentum. Review breadth, late-week behavior, and the largest-up-day share.

## Agent infrastructure gate

- **BEFORE WORK STARTS:** Before planning, selecting tools, delegating, editing files, or taking external action, run a visible preflight audit of expected length and detail, subtasks and dependencies, uncertainty, risk, shared-write or external overlap, and parallelism value. Record the objective, invariants, evaluation, pass condition, correction budget, side-effect gate, compatible skills, topology, model lane, and verification gates.
- **WHEN THE TASK CHANGES:** If a new requirement, file, dependency, tool, error, risk, side effect, or subtask appears, stop and rerun the full audit. Update skills, topology, model, evaluation, and release gates before continuing. Never continue under a stale plan.
- Run the active runtime's skill-routing procedure at both gates. Select and fully read the smallest complete compatible skill set, then reroute when the task changes.
- Apply codex-recursive-self-improvement after each task and material action. Record not promoted when no reusable lesson exists.
- On any ctx_* call failure or timeout, use the active Lean CTX skill helper. Its native mode must support authorized writes. Read mode is only for inspection. Read back before mutation and verify afterward.
- For any substantive task with two or more independent subtasks, parallel dispatch is the default: launch up to three bounded children in one round with disjoint scopes, then wait at one parent barrier. Use parallel research, implementation slices, test runs, and audits when they do not share state. Do not serialize independent work merely for convenience.
- The parent must choose each child's access before dispatch, keep one delegation level, and own integration, financial decisions, external effects, diff review, and final verification. Use one writer for shared files or shared state, and keep parallel writers limited to exact disjoint file sets with parent-owned checks.
- Use the active runtime's configured orchestration and review infrastructure when it is healthy. Keep shared writes, finance, outreach, publication, and irreversible actions single-writer and parent-verified.

### Task model routing

- The root task parent defaults to `gpt-6-luna` / `max`. Easy or routine work and every read-only child use Luna / max.
- Medium implementation uses `gpt-6.1-terra` / `medium`.
- Hard, complex, or high-risk implementation uses `gpt-6.1-sol` / `medium`.
- Ultra-complex implementation uses Sol / high only when the estimated completion time is under 10 minutes. At 10 minutes or more, or when duration is unknown, use Sol / medium.
- Astra is not an automatic complex-work route. Use it only when the user explicitly requests it for the current task.
- For a different child route, use `collaboration.spawn_agent` with `fork_turns: "none"`, explicit `model` and `reasoning_effort`, and the complete scoped task. Full-history forks inherit the parent's route.
- Use `sol_advisor_luna_foreman` at Luna / max only for at least three dependent scopes or explicit bounded supervisor work.
- If the native tool cannot set or expose the requested model and effort, do the work directly instead of guessing. Never send read-only work to Terra, Sol, or Astra.
- The selected role describes the requested route. Report the serving model only when current-task runtime metadata confirms it.
- Keep external actions and shared writes parent-owned. Keep account-quota and reserve rules separate from model selection.

### Autonomous goal-blocker recovery

- Before using goal status blocked, verify the goal tool's separate recurrence rule and inspect the existing checkpoint, logs, errors, source availability, tools, and authorized UI paths.
- Try safe local or read-only alternatives that fit the existing research authorization. Keep the original acceptance contract and continue useful independent work.
- A failed approach or exhausted correction count ends that method, not the goal. Record the dependency, attempts, observed results, remaining user-owned action, and whether useful authorized work remains.
- Ask only for an actual user decision, missing access or credentials, paid data, consent, purchase, trade or broker write, external send, scheduler change, publication, destructive action, or another required human decision.
- Do not infer data-source permission from availability or configuration. Preserve licensing, provider, finance, and external-action rules.
- For work across chats, compare the live goal and latest user request directly. Treat archived prompts, titles, and summaries as historical context. Claim that a goal restarted only after a live readback confirms an active status and matching objective. If the goal controls lack edit or resume, record the gap in the current checkpoint. Do not falsify completion or create a duplicate goal to bypass it; continue only work authorized by the current request.

### Blocker report contract

- Cite observed evidence and name the exact acceptance condition that it prevents.
- List safe recovery paths tried and their observed results.
- State any remaining user-owned action and whether independent authorized work can continue.
- Use task-level `needs_replan` when a method fails but useful work remains. Use goal status `blocked` only when the goal tool's own criteria are met and no safe, useful progress remains.
- Before claiming human intervention is required, check ordinary authorized UI paths and safe local remedies.

### Context-check cadence

- If the current user instruction suspends context monitoring, do not run /status or context_snapshot.py, do not pause work, and do not hand off because of context. Keep account-quota rules active.
- Otherwise use a same-chat live meter when the host returns one. If unavailable, use the documented helper only with a verified active thread ID. Label its result as a recorded-request snapshot, not live context; it excludes later tool output.
- Missing or non-live context data does not stop ordinary work. Pause only a decision that requires a current threshold and request a live number only for that decision.
- When monitoring is active and a handoff is needed, reuse a matching destination. It waits until the parent verifies destination readiness and matching goal, then the source archives itself. Confirm a terminal source turn before destination work.

## Evidence

Record benchmark, dates, cash-flow treatment, costs, return method, drawdown, and data freshness with every performance comparison. Use redacted percentages in public files. Label user reports, machine observations, inferences, and verified public sources separately.

## Changes

## Storage and artifact efficiency

- Prefer existing canonical outputs and update them in place. Create persistent files only when they support the requested result or audit.
- Keep ordinary work autonomous. A direct request authorizes the reversible local edits and checks needed to complete it. Do not pause for command-by-command approval or create a persistent `GATES.md` for routine work. Use a ledger only when a long or multi-branch task materially benefits from durable coordination; it tracks progress and does not grant permission.
- Keep routine evidence in the task context or existing checkpoint. Use one scratch location and remove task-created ledgers and logs after verification when they are not required evidence.
- Set a practical durable-file and scratch budget for long-running work. Keep decision records compact; avoid duplicate datasets, raw tool transcripts, and one file per routine step.
- Use one task-scoped scratch location. Remove only temporary files created by the current task after verifying final outputs and references.
- Preserve canonical inputs, protected data, dated evidence, user-maintained files, and verified goal checkpoints. Do not prune pre-existing history without explicit authorization.
- For long-running AIHF work, reuse canonical data and the latest verified checkpoint. If a run exceeds its storage budget, stop adding artifacts and report the largest new outputs.

Make the smallest change that fulfills the request. Add a dated entry to `CHANGELOG.md` for meaningful system changes and update the appropriate evidence or decision-log entry. Run `python3 scripts/validate_repo.py` before publishing.
