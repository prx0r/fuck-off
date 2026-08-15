# CANONICAL HERMES BUILD — how it all fits together (Hermes · kanban · skills · layers · experiments)

*2026-08-15 · agentgraph (ip-graph). THE mental model for how Hermes, kanban, skills, the build, and
the experiments relate. Read this if you're confused about which tool does what. It is the canonical
answer to: "which parts use kanban? how does that relate to our experiments/build/layers?"*

---

## 1. THE FIVE LAYERS OF THE SYSTEM (and the tool for each)

| Concern | Tool | What it is |
|---|---|---|
| **1. Execution (do the work)** | **Hermes** | The agent that GENERATES (translations, commentary, cruxes, enquiries, essays, new text). Runs through the `patala` profile, has full filebase access. |
| **2. Reduction (verify the work)** | **`.py` kernels** | Deterministic REDUCTION: review, staleness, evidence, gates, epistemic envelope, aggregation, validation. `lib/` = the 52 kernels; `scripts/validate-*.py` = the gates. |
| **3. Task tracking (what to do next)** | **Kanban** | A SQLite task board (`hermes kanban`, board `ip-graph`). Tracks the WORK QUEUE — what needs doing, who, status. **This is the "what are we working on" layer.** |
| **4. Reusable instructions** | **Skills** | `skills/` (vcreate, theatre-check, hermes-generate-reduce, hermes-derive-*). Packaged how-to's Hermes loads via `--skills`. |
| **5. State (what's built / proven)** | **Layers + state.json + experiments** | `layers/00-09` = what's BUILT per layer. `state.json` = machine counts. `data/references/experiments.json` + `theatre-proofs-all.json` = what's PROVEN. |

---

## 2. WHERE KANBAN FITS (and where it does NOT)

**Kanban tracks the WORK QUEUE — the tasks, not the content.** It answers "what should we build / fix /
run next, and is it done?" It does NOT store knowledge, it does NOT prove anything, and it is NOT the
source of truth for what's built.

```
Hermes (executes a task)      ─┐
.py kernels (reduces/gates it) ├─  a TASK on the KANBAN board
Skills (tells Hermes HOW)      ─┘        │
                                        v
                        KANBAN (task: ready → claimed → done)
                                        │  (marks the task finished)
                                        v
         LAYERS/state.json/experiments (the durable record of WHAT EXISTS + WHAT'S PROVEN)
```

- A **task** (kanban) is short-lived: it moves ready → claimed → done.
- The **build/layers/state/experiments** are long-lived: they record what actually exists and what's
  proven. They only change when a task actually ships a verified artifact.
- **Kanban ≠ the build.** The build is the code + data + proofs. Kanban is just the tracking board.

### The relationship in one line
> **Kanban = the "to do" board. Hermes = the worker. `.py` = the verifier. Skills = the worker's
> playbook. Layers/state/experiments = the ledger of what's actually built and proven.**

---

## 3. THE DATA FLOW (how a task becomes a proven artifact)

1. **A task is created** on the kanban (e.g. "ingest LOGICVID gold → enquiry").
2. **Hermes executes the generation** (reads real files itself via the patala profile) — HERMES lane.
3. **`.py` reduces** — validates, aggregates, gates the output — PYTHON lane.
4. **The artifact is committed** to `data/` and the counts are updated in `state.json` + the docs.
5. **The task is marked done** on the kanban.

**Anti-theatre invariant:** a task is "done" only when (a) the object was DERIVED from real data by
Hermes (or a proven deterministic kernel), (b) a `.py` gate passed, and (c) the record (state/layers/
experiments) reflects it. Running tests to look busy is not a task.

---

## 4. HOW THE CURRENT PIPELINE USES IT (concrete)

| Active task | Hermes lane (generation) | `.py` lane (reduction) | Kanban |
|---|---|---|---|
| LOGICVID gold → enquiry | Hermes reads each SPEC-40..48 gold and derives taxonomy/theorem/boundary/frontier | `enquiry.EnquiryDiscovery` aggregates → `data/logicvid/enquiry-gold.json` | `t_ec7b4506` (ready) |
| Ratié essay anatomy | Hermes reads `Le-Soi-et-l-Autre-Ratie-2011.txt` and derives sections/argument/IPK | `essay_ingest.EssayIngestor` runs the 9-stage pipeline | `t_d8848963` (ready) |
| Reconcile the record | (none — deterministic) | update `state.json`, `AGENTS.md`, `KERNELS-INDEX`, `GAPS`, `README` | `t_dd877db2` (ready) |
| prove provenance | (none — deterministic) | `validate-provenance.py` asserts on real `argument.json` data | `t_091111d1` (done ✅) |
| Hermes skills docs | (none — docs) | create `skills/hermes-*.SKILL.md` + wire into NAVIGATION | `t_62bc8de1` (ready) |

---

## 5. THE CANONICAL RUNBOOK (autonomous overnight = the whole loop, unattended)

The **autonomous overnight runner** is a single script that loops the data flow: for each task on the
board, Hermes derives (generation), `.py` reduces (gate), the record is updated, the task is marked
done — all backgrounded with a log, one heavy job at a time (the 8GB/2-agent constraint).

It is launched with:
```bash
setsid nohup python3 scripts/run-overnight-autonomous.py > /tmp/overnight.log 2>&1 &
```
Poll: `tail /tmp/overnight.log` + `hermes kanban list`. Kill by PID, never `pkill`.

---

## 6. THE KEY RULES (so you never get confused again)

1. **Hermes does the thinking/generating; `.py` does the checking.** Never fake generation with regex.
2. **Hermes reads files itself** (full filebase access) — pass paths, not stuffed contents.
3. **Kanban is the to-do board, not the truth.** The truth is `state.json` + `layers/` + the proofs.
4. **A layer/experiment changes only when a task ships a verified artifact.**
5. **One heavy job at a time** on the shared box; background everything long; kill by PID.
6. **Running tests is not a task.** A task must build or fix something real.
7. **The schema.py collision** — ip-graph `lib/schema.py` and patala `pipeline/schema.py` in separate processes.
8. **Verify the record after every change** — counts must match reality (52 kernels / 97 experiments / 84 proofs).

## Files
- This mental model: `CANONICAL-HERMES-BUILD.md`
- The calling convention: `handover/hermes/HERMES-CALLING.md`
- The wrapper: `lib/hermes_exec.py` · the skills: `skills/hermes-*`
- The task board: `hermes kanban` (board `ip-graph`) · the record: `state.json`, `layers/`, `KERNELS-INDEX.md`
