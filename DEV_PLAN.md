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

## PHASE 3 — SURFACES (make it real) — the read plane (SPEC-49, THE remaining build)

**The build decision (SPEC-49):** Python factory + DuckDB → immutable R2 projections → Astro (humans,
JSON-LD) + compiled agent bundles/MCP (agents) + **Postgres FTS first, Tantivy only if profiled hot.**
Rust = compiled wheels only when measured hot. **Start here: the projection compiler** (everything
reads from it).

### 3.1 Projection compiler (Layer 06) — SPEC-00 §25 steps 6-10, SPEC-49  [P0]
The single highest-leverage build. Python/DuckDB turns canonical graph → immutable per-entity
JSON/MD/HTML/bundles, content-addressed to R2. One agent question = one request. Perf contract:
reading-route JS <10KB, HTML <100KB, LCP <1s, new doc must NOT rebuild whole corpus.

### 3.2 Search (Layer 06) — Postgres FTS first [P0]
`tsvector`/`tsquery` + `pg_trgm` for free, consistent search in the canonical DB. Benchmark it.
**Only if profiled hot** swap in Tantivy (Rust wheel, like paper-qa). This is the SPEC-49 decision
point — record the measurement.

### 3.3 Compiled agent bundles + MCP (Layer 06/07) — SPEC-00 §15, §16  [P0/P1]
`/bundle/{id}` = entity+positions+relations+evidence+disagreements+provenance in ONE request, with
`?view=compact&budget=2000|8000|32000&depth=0|1|2`. MCP = thin Streamable-HTTP adapter, ~8 tools
(resolve/search/get/context/trace/compare/neighbors/evidence), NOT 70 micro-tools.

### 3.4 Astro site (Layer 07) — SPEC-00 §24, §17  [P1]
0-JS reading pages, Preact islands only, **semantic HTML + JSON-LD + `<link rel="canonical">`**.
One canonical URL per entity (`/concept/free-will` + `.json` + `.md` + `/api/...`) — unifies the human,
search-engine, agent, and API graphs. This is the agent-SEO layer.

---

## PHASE 4 — LIVE SYSTEM (Layer 09)
Agent loop: pick chunk → layer → state → advance → update STATE.yaml. Staleness tracking.

---

## Experimentation note (current mode)
The **machine side is done and proven** (55/55 tests, IPVV graduation 18/18 on real corpus, v3 product
stack 13/13). We are now in **build mode on the read plane** (SPEC-49): the projection compiler +
Postgres-FTS search + compiled agent bundles/MCP + Astro/SEO. Priority (from `state.json`):
1. **P0 — projection compiler** (Layer 06) — unblocks agent bundles, Astro, MCP, SEO all at once
2. **P0 — Postgres-FTS baseline** (Layer 06) — the SPEC-49 Tantivy decision point
3. **P0 — compiled agent bundles** (Layer 06) — one request per agent question
4. **P1 — Astro + JSON-LD/SEO + MCP** (Layer 07) — the human + agent + search surfaces

See `state.json` (machine) + AGENTS.md §1.5 (human) for exact counts. See `specs/SPEC-49` for the build
decision.

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
