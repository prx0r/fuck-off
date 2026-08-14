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

| XiaoConstantine/herdr-workflow | **CLONED** (2.2M) — event-sourced multi-agent workflow; agents propose immutable evidence, reducers own lifecycle |
| broomva/arcan | **CLONED** (4.7M) — tiny agent kernel, event sourcing done correctly |
| valkor-ai/loom | cloned local-only (Apache-2.0 open; gitignored) |
| ReinaMacCredy/maestro | cloned local-only (tracked sqlite has sk- strings; gitignored) |

| mntlra/knowledgeProvenance | **CLONED** (epistemic/) — PROV-K nanopubs: ReliableFact/ContrastingEvidence/InsufficientEvidence + trust. Validated: our ceilings map cleanly (validate-provenance.py) |
| prometheus-eval/cmu-paper-reviewer | **CLONED** (agent-runtime/) — 5-critical-issue paper reviewer (Apache-2.0) |
| gallantlab/literature-review-toolkit | **CLONED** (science/) — topic-agnostic literature review agent (MIT) |
| wan-huiyan/agent-review-panel | **CLONED** (agent-runtime/) — 16-phase adversarial review protocol (Phase 10 claim-verify, Phase 11 severity-verify, Phase 14 judge) |
