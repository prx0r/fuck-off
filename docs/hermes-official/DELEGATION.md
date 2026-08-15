# Official Hermes Docs — Subagent Delegation (`delegate_task`)

*Imported 2026-08-15 from the official Hermes docs (hermes-agent.nousresearch.com/docs/user-guide/features/delegation). The `delegate_task` tool — child agents with isolated context + their own terminal sessions. Use for parallel review panels, counterfactual probes, and multi-file work. (For MANY durable cross-session tasks, use Kanban instead.)*

## What it is
`delegate_task` spawns child AIAgent instances with isolated context, inherited tools, and their own terminal sessions. Only the final summary enters the parent's context. `delegate_task` = a function call; Kanban = a durable work queue.

## Single / parallel
- Single: `delegate_task(goal="...", context="...")`
- Parallel batch: `delegate_task(tasks=[{goal,context},...])` — up to 3 concurrent children (default, configurable).
- Subagents KNOW NOTHING — the parent must pass everything they need in `goal`+`context` (they start with a fresh conversation). Full context in the call, or they fail.

## Key properties
- Each child gets its own terminal session; inherits parent's toolsets (model can't widen them).
- Leaf children CANNOT call: `delegate_task`, `clarify`, `memory`, `send_message`, `cronjob`. Orchestrator children retain `delegate_task` (bounded by `max_spawn_depth`, default 1 = flat).
- `max_iterations` (default 50) per child; no wall-clock timeout by default (opt-in `child_timeout_seconds`).
- Stall detection: progress-based monitor (450s idle / 1200s in-tool) interrupts frozen children; progressing children never touched.
- Background completions are durable (stored in `state.db`, restored after restart); a running child does NOT survive restart (becomes `unknown`).
- Only final summary enters parent context (token-efficient).

## Steering / monitoring
- Parent can `list` / `steer` / `stop` its own running children via `delegate_task`.
- `/agents` (TUI + CLI/gateway) shows the live subagent tree with per-branch cost/tokens, kill/pause.
- Live transcripts: append-only log per task at `<hermes_home>/cache/delegation/live/<delegation_id>/task-N.log` (+ `manifest.json`) — a full-fidelity operational record (= our run-provenance).

## Cost strategy
Frontier planner → inexpensive workers. Pin `delegation.model` to a cheap model (children are where tokens go); the parent stays on the frontier model. For quality-sensitive cards use kanban's per-task model override instead.

## Worktree isolation
`delegation.worktree_isolation: true` → each child gets its own git worktree + branch so parallel editors don't collide. Child result includes `worktree{path, branch, commits, dirty}`.

## vs `execute_code`
- `delegate_task` = full LLM reasoning loop, fresh context, all tools, parallel. Use for judgment tasks.
- `execute_code` = just Python code, no reasoning, 7 tools via RPC, single script, low cost. Use for mechanical multi-step pipelines.

## Config (`~/.hermes/config.yaml`)
```yaml
delegation:
  max_iterations: 50
  max_concurrent_children: 3
  worktree_isolation: false
  max_spawn_depth: 1        # 1=flat; 2=orchestrator children can spawn leaves
  model: "google/gemini-3-flash-preview"   # cheap worker model
  provider: "openrouter"
```

## The ip-graph use
Parallel adversarial review panels (each child reviews independently → synthesize), counterfactual
What-If probes in parallel, and multi-file graph work — each child gets a fresh context + full context in
the call. Live transcripts give us the run-provenance audit trail for free.
