# ip-graph — the agentgraph frontier lab for the Verified Epistemic OS

A **general epistemic graph engine** (claim / argument / evidence / review / immutable-artifact) that
turns corpora into a compiled, immutable read plane — generalizing across Sanskrit, Western philosophy,
and science. It is patala's second-generation kernel, and this repo is the **generalization test**
(it was born as the informationphilosopher knowledge graph).

## The integration (one line)

**patala PRODUCES (the translation factory DAG: SOURCE→T1→L0→L2→L200→C1). ip-graph VALIDATES + SERVES**
(the read plane, the organism, and the TranslationProof/validation kernels).

## Current verified state (2026-08-15)

| Metric | Value |
|---|---|
| Kernels (`lib/`) | **52** |
| Experiments | **97** |
| Theatre proofs | **84 = 38 PROVEN / 46 PROVEN-MECHANISM / 0 UNPROVEN** |
| Graph | **490 nodes / 6578 edges** |
| Corpus | 425 docs (6 html + 419 pdf) |
| Graduations | Doyle 14/14 · IPVV 18/18 · product stack 13/13 |
| Tantrāloka (canonical DAG) | SOURCE 4,624 · T1 264 · L0 1 |

## Build decision (SPEC-49, frozen)

Python factory + DuckDB → immutable R2 projections → Astro/JSON-LD (humans) + compiled agent bundles/MCP
(agents) + Postgres FTS first (Tantivy only if measured hot). Rust only as measured hot wheels.

## How to work here (read first)

1. **`AGENTS.md`** — the governing rules + anti-theatre doctrine. Read first.
2. **`NAVIGATION.md`** — the master index (resolve anything → location/script/how-to-run).
3. **`CANONICAL-HERMES-BUILD.md`** — how Hermes, kanban, skills, layers, and experiments fit together.
4. **`CONTEXT-REVIEW.md`** — the honest full state + the missing-work list.
5. **`DEV_PLAN.md`** — the executable roadmap.
6. **`handover/hermes/`** — the Hermes execution-kernel notes (calling convention, thesis).

**The one rule:** nothing is "real" because a file exists. It is real when it has a reproducible
pipeline, a clean input, a verifiable output, and a recorded epistemic ceiling. Hermes GENERATES, `.py`
REDUCES, kanban TRACKS the task queue, and the record (`state.json` + `layers/` + proofs) is the truth.
