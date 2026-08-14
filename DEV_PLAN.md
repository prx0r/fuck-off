# DEV PLAN — from vision to working epistemic engine

*2026-08-14. The executable roadmap. Synthesizes: `docs/vision/VISION.md` (the why), 
`VISION-CHUNK-LAYER-MAP.md` (the structure), `specs/SPEC-00..07` (the how), and the ecosystem survey.
Ordered by the patala-derived priority: **foundations first, prove generalization early.***

## How to use
Each task maps to a Layer (see `STATE.yaml`). A task is DONE only when it passes its acceptance gate and
`STATE.yaml` + `CHANGELOG.md` are updated. Tasks are ordered by dependency + excitement-to-effort ratio.

---

## PHASE 0 — FOUNDATIONS (the epistemic kernel)

### 0.1 Epistemic envelope (Layer 00) — SPEC-02
Every graph object carries `epistemic_ceiling` + 4-axis `authority` + `review_state` + the invariant
`authority(projection) <= authority(parent)`.
- [ ] `lib/epistemic.py` — ladder + Authority dataclass + invariant check
- [ ] Rebuild graph.json with envelopes
- [ ] `audit-epistemic.py` — invariant across all edges (a violation = bug)

### 0.2 Stable IDs + content-addressing (Layer 00) — SPEC-00 §2
SHA-256 identities for works/passages/entities/relations/artifacts.
- [ ] ID scheme: `ip:work:<sha>` · `ip:passage:<sha>` · `ip:concept:<slug>` · `ip:rel:<sha>`
- [ ] content-addressed artifact store

### 0.3 Incremental build (Layer 03) — SPEC-00 §4
Replace full-rebuild with hash-driven incremental.
- [ ] hash each source doc → rebuild only changed → propagate staleness (RKA idea)

---

## PHASE 1 — THE GRAPH (make it truthful)

### 1.1 Typed relations (Layer 02) — SPEC-03
Upgrade `co_occurs_with` → the 16 ONTOLOGY relations (negates, presupposes, is_cause_of, tensions_with...).
- [ ] seed typed edges for the two-stage argument + compatibilist conflict (hand-curated, evidence-anchored)
- [ ] each edge: `evidence_quote` + `passage_ids` + `epistemic_ceiling`

### 1.2 Canonical DAG (Layer 03) — SPEC-01
`data/graph/canonical-dag.yaml`: PHYSICS→INFO→INDETERMINISM→FREE_WILL→VALUE + validator.
- [ ] write the DAG, map layers→works, `validate-dag.py`

### 1.3 Argument graph (Layer 04) — SPEC-03
AIF Info/Inference/Conflict for the two-stage thesis.
- [ ] `data/graph/argument.json`

---

## PHASE 2 — GENERALIZATION TEST (the exciting bet)

### 2.1 The 5 adapters (Layer 01) — SPEC-07
`ExternalRecord → CanonicalCandidate → Validation → Proposal → AcceptedObject`.
- [ ] `import_scifact()` — real scientific claim↔evidence gold
- [ ] `import_xaif()` — real argument graphs (ARG Tech)
- [ ] `import_eleutheria()` — free-will philosophy (validates domain generalization)
- [ ] `import_openalex()` · `import_s2orc()` — bibliography layer

> **The bet:** if Doyle + SciFact + xAIF + EleutherIA all enter the same engine, the abstraction is real.

### 2.2 Evidence weighting (Layer 02) — Kappa-style
Supporting vs contradicting evidence, grounding + diversity, NOT one mushy score.
- [ ] `grounding_score` + `contradiction` separation per concept

---

## PHASE 3 — SURFACES (make it real)

### 3.1 Projection compiler (Layer 06) — SPEC-00
Per-entity static JSON/MD/HTML/bundles → R2 immutable.
### 3.2 Astro site (Layer 07)
Argument objects as living pages.
### 3.3 API + MCP (Layer 07)
Workers on /api /search /mcp; thin MCP adapter.

---

## PHASE 4 — LIVE SYSTEM (Layer 09)
Agent loop: pick chunk → layer → state → advance → update STATE.yaml. Staleness tracking.

---

## Experimentation note (current mode)
We are in **experimental time** — the point is to play with architecture and test the generalization
bet, not to gold-plate. Highest excitement-to-effort right now:
1. **0.1 epistemic envelope** (foundation, small, transformative)
2. **1.1 typed relations** on the two-stage argument (the moat)
3. **2.1 scifact adapter** (the generalization bet — most exciting)

See `STATE.yaml` for live status. See `specs/` for each piece's design.

---

## PHASE 5 — PATALA FUTURES (from VISION-PATALA-FUTURES.md)

The seven visions reduce to a clear build order. Promote the proven experiments to real libraries first.

### 5.1 Promote experiments → lib/ (fastest wins, already proven)
- [ ] `lib/review.py` — herdr-style reducer state machine (from `experiment-herdr-review.py`)
- [ ] `lib/staleness.py` — RKA blast-radius propagation (from `experiment-rka-staleness.py`)
- [ ] `lib/query.py` — KG2Code executable graph queries (from `experiment-kg2code.py`)
- [ ] `lib/retrieval.py` — PathRAG + HippoRAG retrieval (from experiments)

### 5.2 The generalization test (highest info value)
- [ ] `import_openalex/s2orc/scifact/xaif/eleutheria` adapters → same engine

### 5.3 The agent surface
- [ ] `lib/query.py` over MCP → executable knowledge (VISION 4)

### 5.4 The product
- [ ] Argument Map pages: `/free-will`, `/consciousness`, ... (VISION 1)

### 5.5 The end-state
- [ ] Review-event ledger + agent execution loop (VISION 7 Autonomous Review Institute)

See `docs/vision/VISION-PATALA-FUTURES.md` for full detail per vision.
