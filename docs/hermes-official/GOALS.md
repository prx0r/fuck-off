# Official Hermes Docs — Persistent Goals (`/goal`)

*Imported 2026-08-15 from the official Hermes documentation (hermes-agent.nousresearch.com/docs/user-guide/features/goals). The Ralph-loop "keep a goal alive across turns until it's achieved" primitive — the single-session driver (vs kanban's many-task board).*

## What it is
`/goal <text>` gives Hermes a **standing objective that survives across turns.** After every turn a lightweight judge model checks whether the goal is satisfied; if not, Hermes feeds a continuation prompt back into the same session and keeps working — until achieved, paused/cleared, or the turn budget runs out.

## Goals vs Kanban (the sharp boundary)
- **`/goal` is single-session.** The loop feeds continuation prompts back into THIS conversation. Never creates a kanban card, never assigns work to another profile, never fans out.
- **Kanban is a board of many tasks.** Each card is dispatched to its own worker process with its own session; cards/deps/assignees/handoffs live on the board.
- Overlap: a kanban card with `--goal` runs the same Ralph engine *inside that one card's worker session* — borrows the engine, not the board.

| You want | Reach for |
|---|---|
| Keep iterating on one task in this chat | `/goal <text>` |
| Many independent tasks w/ deps, handoffs, profiles | Kanban (`hermes kanban create …`) |
| One card that keeps iterating to acceptance | kanban card with `--goal` |

## Commands
`/goal <text>` (set + kick off) · `/goal draft <text>` (draft a completion contract) · `/goal show` · `/goal`/`/goal status` · `/goal pause` · `/goal resume` · `/goal clear` · `/goal wait <pid> [reason]` · `/goal unwait` · `/goal gate add <cmd>` / `gate list` / `gate remove N` / `gate clear`. Works identically on CLI and every gateway platform.

## Completion contracts (make "done" precise)
Five optional fields — `outcome` (the end state), `verification` (test/command that PROVES it), `constraints` (what must not regress), `boundaries` (scope), `stop_when`. When set, the judge decides `done` only when the verification criterion is met with concrete evidence (command result / file excerpt / test output), not a loose "looks done." Two ways: `/goal draft <text>` (Hermes drafts it) or write inline with `field: value` lines (`verify: pytest tests passes`).

## `/subgoal` (add criteria mid-goal)
Append extra acceptance criteria without resetting the loop; the judge must satisfy the original goal AND every subgoal before `done`.

## Quality gates (deterministic, stronger than the LLM judge)
`/goal gate add <command>` — a shell command that must exit 0 before the goal can complete. Each turn: gates run BEFORE the judge; a red gate = deterministic evidence the goal isn't done (no judge call; the failure tail becomes the continuation prompt). Gates have 3 retries / 5-min timeout; exhausting them auto-pauses the goal. Gates + contract compose (gates run first).

## Parking on background processes (automatic)
Every turn the judge sees the agent's live background processes. If progress is genuinely gated on one, the judge returns `wait` and the loop **parks** (no judge call, no turn consumed) until it exits / pattern matches / a time delay passes, then resumes. `/goal status` shows `⏳ Goal (parked …)`. Manual override: `/goal wait <pid>` / `/goal unwait`.

## Behavior details
- **Judge**: conservative; marks done only when the response explicitly confirms completion / deliverable produced / unachievable (done-with-block-reason). Strict JSON verdict: `{"verdict":"done|continue|wait","reason":...}`.
- **Fail-open**: if the judge errors → `continue` (a broken judge never wedges progress); the turn budget is the real backstop.
- **Turn budget**: default 20 continuation turns (`goals.max_turns` in config). On hit → auto-pause with instructions.
- **User messages always preempt** the loop.
- **Persistence**: goal state in `SessionDB.state_meta` → survives `/resume` and context compression.
- **Judge model**: `auxiliary.goal_judge` (default = main model); route to a cheap fast model to save cost.

## Config (`~/.hermes/config.yaml`)
```yaml
goals:
  max_turns: 20
auxiliary:
  goal_judge:
    provider: openrouter
    model: google/gemini-3-flash-preview
```

## The key rule for ip-graph
Use `/goal` for ONE continuing task in a session; use Kanban for many parallel tasks / the board. For autonomous overnight work, a kanban card with `--goal` + a completion contract + a quality gate is the strongest pattern (judge + deterministic gate).
