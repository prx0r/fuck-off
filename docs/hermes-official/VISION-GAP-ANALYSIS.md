# Hermes Gold → Our Visions — what we're MISSING (feature → vision gap analysis)

*2026-08-15. Deep-dive of the official Hermes docs (`docs/hermes-official/`) against our four product
visions (`docs/vision/beyond-patala/`). The verdict: **our visions are the BRAIN; Hermes's automation
features are the LIMBS/autonomy we are largely NOT using.** Every vision compounds only when it RUNS
autonomously + remembers across sessions — which is exactly what the unused Hermes features provide.*

---

## The thesis

Our four visions (Verified-Statement-Marketplace, Co-Evolving Organism, What-If Machine, Self-Proving
System) are compositions of validated kernels (the 8 laws). But a composition of kernels is a *mechanism*,
not a *product*. What turns a mechanism into a compounding, autonomous product is the **execution,
delegation, memory, scheduling, and provenance substrate** Hermes ships natively — and we currently use
almost none of it beyond the basic `hermes chat` call. **That unused substrate IS the gold we're missing.**

---

## 1. Verified-Statement-Marketplace → MISSING: verification AT SCALE

| Hermes feature (official) | What it is | Why it's the missing gold |
|---|---|---|
| **Batch Processing** (`/docs/.../batch-processing`) | Run the agent across **hundreds/thousands of prompts in parallel**, structured ShareGPT trajectories, for evals/training | The marketplace moat = *Certification Weight* (kill-rate × consensus × load). Load needs verification at SCALE. Today we verify one claim at a time. Batch = the mutation-testing / adversarial-review at scale substrate. |
| **Subagent Delegation** (`delegation`) | `delegate_task` spawns parallel child agents (up to 3 default), orchestrator trees, live transcripts | The adversarial review PANEL (scholar_review) should be a parallel subagent panel, each child reviewing independently, then synthesized — not one sequential pass. |

## 2. Co-Evolving Epistemic Organism → MISSING: persistent learner MEMORY + continuous loop

| Hermes feature | What it is | Why it's the missing gold |
|---|---|---|
| **Persistent Memory** (`/docs/.../memory`) | `MEMORY.md`/`USER.md` bounded curated memory **across sessions** | The organism's learner-state must PERSIST across sessions to co-evolve. Today `pedagogy.py`/`LearnerState` is in-memory — it forgets every run. |
| **Memory Providers** (`/docs/.../memory-providers`) | pluggable external memory (Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover, Supermemory) for **cross-session user modeling** | The organism vision wants real learner modeling; these are purpose-built backends we're ignoring. |
| **Recurring Loops** (`/loop`) | timer-driven re-run in-session ("watch the queue / iterate-until-green") | The organism's flywheel should LOOP continuously (probe → learn → repair → re-probe). `/loop` or cron = the continuous driver. |
| **Cron** (`/docs/.../cron`) | scheduled autonomous jobs, attach skills, deliver anywhere | unattended organism feedback + overnight growth (we hand-rolled shell cron for the factory; Hermes cron is richer). |

## 3. What-If Machine → MISSING: parallel discovery + reactive hooks

| Hermes feature | What it is | Why it's the missing gold |
|---|---|---|
| **Subagent Delegation (parallel research)** | many counterfactual probes in parallel, each a fresh agent | What-If discovery = test many counterfactuals; delegation fans them out and synthesizes. |
| **Event Hooks** (`/docs/.../hooks`) | run custom code at lifecycle points (kanban_task_completed, blocked) | When a new crux/boundary is discovered, a hook can AUTOMATICALLY trigger the next counterfactual + downstream research (staleness→next-layer automation, our blast-radius made live). |

## 4. Self-Proving System → MISSING: real construction provenance + run traces

| Hermes feature | What it is | Why it's the missing gold |
|---|---|---|
| **Checkpoints / Rollback** (`/docs/checkpoints-and-rollback`) | auto-snapshot the working dir before file changes; `/rollback` | This is EXACTLY self-proving construction history — a signed, replayable record of every change the OS makes to itself. We have `design_provenance` nanopubs but not the live change-snapshot substrate. |
| **Live Transcripts** (delegation) | append-only, timestamped log of every subagent's tool calls/results | = run-traces / content-addressed operation record (our Gap D). The "how this was constructed" audit trail, for free. |
| **Context Files** (`.hermes.md`, `AGENTS.md`, `SOUL.md`) | auto-loaded project constitution | our `AGENTS.md` IS this — already wired, but we should use `.hermes.md` to inject the graph structure as the agent's standing context. |

---

## 5. Cross-cutting gold we're missing (powers ALL four)

| Hermes feature | What it is | Our gap |
|---|---|---|
| **Code Execution (`execute_code`)** | Hermes calls its OWN tools programmatically from Python, collapsing multi-step into one turn (7 tools via RPC, no reasoning) | THE hidden lever. We could drive the whole graph pipeline (compile → validate → record) as a Hermes `execute_code` script instead of hand-running each step. |
| **Provider Routing / Fallback / Credential Pools** | cost/speed/quality routing, failover, key rotation | our heavy Hermes use is single-provider, single-key, no failover — reliability + cost we're leaving on the table. |
| **MCP** | connect any MCP server (stdio/HTTP) | our read-plane design has MCP; we should expose the graph via Hermes MCP so the agent queries it directly. |
| **Plugins** | custom tools/hooks/context-engines without core changes | a clean place to ship `kanban_*`-style custom tools over our graph. |

---

## The one-line verdict

> **We're missing the AUTONOMY + MEMORY + PROVENANCE substrate.** Our kernels prove the visions on
> stand-in data; Hermes's batch-processing, delegation, persistent memory, loops, cron, hooks,
> checkpoints, and live-transcripts are the gold that makes them RUN, COMPOUND, and REMEMBER overnight.
> Start with: (1) `execute_code` to drive the graph pipeline, (2) delegation for the parallel review/
> counterfactual panels, (3) a memory-provider for the organism's learner-state, (4) event-hooks for
> staleness→downstream automation, (5) checkpoints for the self-proving construction record.

## Files
- The official features overview: `docs/hermes-official/` (KANBAN, GOALS) + the features/overview/loops/delegation references
- Our visions: `docs/vision/beyond-patala/`
- The kernels that power them: `lib/` (certificate, misconception, pedagogy, review, discovery, design_provenance)
