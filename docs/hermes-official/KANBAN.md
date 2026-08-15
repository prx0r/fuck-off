# Official Hermes Docs — Kanban (Multi-Agent Board)

*Imported 2026-08-15 from the official Hermes documentation (hermes-agent.nousresearch.com/docs/user-guide/features/kanban). This is the tool's own reference for the durable multi-agent task board we use to drive work. For the two-sided narrative, see the Kanban tutorial; this is the reference.*

## What it is
Hermes Kanban is a **durable task board** shared across Hermes profiles: every task is a row in `~/.hermes/kanban.db`; every worker is a full OS process with its own identity; handoffs are rows anyone can read/write. Use it for work that crosses agent boundaries, survives restarts, or needs human input. NOT for short one-call reasoning (that's `delegate_task`).

## Two surfaces (same DB)
- **Agents drive via `kanban_*` tools** — `kanban_show/list/complete/request_review/request_changes/block/heartbeat/comment/attach/create/link/unblock`. Dispatcher spawns workers with these in-schema; workers call tools, NOT the CLI.
- **You drive via CLI** — `hermes kanban …`, `/kanban …`, or the dashboard.

## Core concepts
- **Board** — a standalone queue (own SQLite DB + workspaces + dispatcher). One per project/repo/domain. `hermes kanban boards create <slug> --name "..." --switch`.
- **Task** — row with title, body, assignee (a profile), status (`triage|todo|ready|running|blocked|review|done|archived`), tenant, idempotency key.
- **Link** — parent→child dependency; dispatcher promotes `todo→ready` when all parents done.
- **Comment** — the inter-agent protocol; workers read the full thread on spawn.
- **Workspace** — `scratch` (ephemeral, deleted on complete), `dir:<path>` (shared dir, preserved), `worktree` (git worktree for coding).
- **Dispatcher** — long-lived loop (default tick 60s, runs inside the gateway) that reclaims stale claims, promotes ready tasks, claims, and spawns profiles. After `failure_limit` (default 2) consecutive spawn failures → auto-block.
- **Tenant** — soft namespace within a board.

## Dispatcher / gateway
- Default: `kanban.dispatch_in_gateway: true` — runs in the gateway. If the gateway is up, ready tasks get picked up next tick. Without a gateway, `ready` tasks wait.
- Quick start: `hermes kanban init` → `hermes gateway start` → `hermes kanban create "..." --assignee <profile>` → `hermes kanban watch`.

## The worker lifecycle (auto-injected, nothing to install)
1. On spawn: `kanban_show()` to read the task + comment thread.
2. `cd $HERMES_KANBAN_WORKSPACE`, do the work via terminal/file tools.
3. `kanban_heartbeat(note=...)` during long ops (at least once/hour if >1h, or the dispatcher reclaims after ~4h).
4. Finish with `kanban_complete(summary="...", metadata={...})` or `kanban_block(reason=...)`. Exiting 0 without a terminal board call = `protocol_violation`.

Recommended `metadata` for engineering tasks: `{changed_files, verification, dependencies, blocked_reason, retry_notes, residual_risk}` — enough for the next reader to answer "what changed / how verified / what unblocks / what risk remains."

## Skills per task
Attach specialist skills to a specific task (not the profile): `--skill <name>` (CLI) or `kanban_create(..., skills=[...])` (orchestrator). Worker spawns with them loaded on top of the auto-injected kanban guidance.

## Goal-mode cards (`--goal`)
Runs the worker in a Ralph-style continuation loop: after each turn an auxiliary judge checks the output against the card title+body (acceptance criteria) and keeps going until the judge agrees, the worker terminates, or the budget runs out (which blocks the card for human review). Use `--goal` for open-ended "keep going until X is true" cards; the body must be explicit acceptance criteria.

## Orchestrator behavior
A well-behaved orchestrator **decomposes the goal into tasks, links them, assigns each to a profile, and steps back** — it does not do the work itself. It uses `kanban_create` (fan out), `kanban_link` (deps), `kanban_comment`. Decide design decisions (naming, schema, format) up front and stamp them into every child body (workers can't see siblings).

## Boards (multi-project)
- Per-board isolation is absolute: separate SQLite DB, workspaces, logs; workers see only their board (`HERMES_KANBAN_BOARD`).
- `hermes kanban boards create/list/switch/show/rename/rm`.

## Config (under `kanban:` in `~/.hermes/config.yaml`)
- `auto_decompose: true` (dispatcher runs the decomposer on Triage tasks — drops a one-liner, walks away).
- `orchestrator_profile`, `default_assignee`, `auto_subscribe_on_create`, `done_sub_retention_days`.
- Aux models: `auxiliary.kanban_decomposer`, `auxiliary.triage_specifier`.

## Swarm
`hermes kanban swarm "goal" --worker PROFILE:TITLE[:SKILL,SKILL] --verifier V --synthesizer S` — parallel workers → verifier → synthesizer as a linked task graph.

## The key rule for ip-graph
Kanban is the **task board (what to do next), not the truth.** The durable truth is `state.json` + `layers/` + the proofs. A task is done only when it ships a real, verified artifact AND the record reflects it.
