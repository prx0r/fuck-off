# Official Hermes Docs — imported reference (driving autonomous agents)

*2026-08-15. The OFFICIAL Hermes Agent documentation (hermes-agent.nousresearch.com), imported into
ip-graph so the smart-Hermes-agent driving pattern is grounded in the tool's actual reference — not just
patala's internal notes (which live in `handover/hermes/`).*

## The docs

| File | Official page | What it covers |
|---|---|---|
| **`KANBAN.md`** | `/docs/user-guide/features/kanban` | the durable multi-agent task board: boards, tasks, links, comments, workspaces, dispatcher/gateway, worker lifecycle, `kanban_*` tools, skills-per-task, `--goal` cards, orchestrator behavior, swarm |
| **`GOALS.md`** | `/docs/user-guide/features/goals` | `/goal` (Ralph loop): persistent single-session goals, completion contracts, `/subgoal`, quality gates, parking on background processes, judge/turn-budget, config |
| **`DELEGATION.md`** | `/docs/user-guide/features/delegation` | `delegate_task`: child agents with isolated context + own terminals, parallel batches, orchestrator trees, live transcripts, worktree isolation |
| **`VISION-GAP-ANALYSIS.md`** | (synthesis of all) | **what Hermes GOLD we're MISSING vs our four product visions** — the autonomy/memory/provenance substrate (batch, delegation, memory, loops, cron, hooks, checkpoints, execute_code) that makes the visions run + compound |

## How this drives our autonomous work (the mental model)

- **Kanban** = the board of MANY tasks (the "what to do next" queue). Each card → its own worker process.
  This is what the `ip-graph` board tracks.
- **`/goal`** = ONE continuing task in a session (iterate until done).
- **Kanban card + `--goal`** = a card that keeps iterating to its acceptance criteria (strongest for
  autonomous overnight: judge + deterministic quality gate).
- **Swarm** = parallel workers → verifier → synthesizer as a linked graph.

**The ip-graph rule (anti-theatre):** Kanban is the task board, NOT the truth. The durable truth is
`state.json` + `layers/` + the proofs. A task is done only when it ships a real, verified artifact and
the record reflects it.

## Related
- patala's Hermes execution-kernel notes + calling convention: `handover/hermes/`
- Our derived-work skills: `skills/hermes-*`
- The wrapper: `lib/hermes_exec.py` (agentic `hermes chat -p patala`)
