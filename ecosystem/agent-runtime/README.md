# agent-runtime/ — durable-execution runtimes

Only add when the single-host boundary hurts (SPEC-09). See `../../docs/ECOSYSTEM-INDEX.md` §4.

| Runtime | Why |
|---------|-----|
| Restate (restatedev/restate) | distributed stateful actors + durable calls (rank 1) |
| Temporal (temporalio/temporal) | mature durable execution (rank 3; we already run it) |
| DBOS (dbos-inc) | durable execution on Postgres (rank 2) |
| Hatchet (hatchet-dev/hatchet) | queue/scheduling (rank 4) |

**Today:** keep it cheap — Hermes Kanban + SQLite + MCP + git worktrees. Do NOT adopt a distributed
runtime yet.

| ghuntley/loom | Huntley's Rust AI coding agent (PROPRIETARY — code-read reference only; NOT for reuse) |
