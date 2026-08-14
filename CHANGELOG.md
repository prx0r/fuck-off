# CHANGELOG

## 2026-08-14 — epistemic foundation + argument graph + experiments

### Added
- **`AGENTS.md`** — expanded to full governing doc: 21 operating axioms (process, data/safety,
  epistemic discipline, performance/infra, agent-optimization), naming standards, test/validation
  gates, anti-theatre doctrine.
- **`lib/epistemic.py`** — the epistemic kernel (SPEC-02): EPISTEMIC_RANK ladder, 4-axis Authority,
  `invariant_ok()`, per-type ceiling defaults (Eigenius-style "how it's known" axis).
- **`scripts/apply-epistemic-envelope.py`** — applied envelopes to all 490 nodes + 6484 edges:
  physics/info concepts → SCHOLARLY_CORROBORATED; free-will/value/mind thesis → MACHINE_PROPOSED;
  schools/contested → MACHINE_PROPOSED.
- **`scripts/audit-epistemic.py`** — invariant gate. **PASS, 0 violations** (authority(projection) <=
  authority(parent) holds everywhere).
- **`data/graph/epistemic-audit.json`** — machine-readable envelope audit.
- **`data/graph/canonical-dag.yaml`** + **`scripts/validate-dag.py`** (SPEC-01) — the 14-layer
  derivational chain PHYSICS→THERMODYNAMICS→INFORMATION→COMPUTATION→QUANTUM→PROBABILITY→INDETERMINISM→
  MIND→LIFE→FREE_WILL→RESPONSIBILITY→VALUE→SYNTHESIS→ESSAY, all source_refs grounded. **PASS, no
  cycles, no undefined deps.**
- **`scripts/build-argument-graph.py`** + **`data/graph/argument.json`** (SPEC-03) — AIF argument graph:
  6 info + 4 inference + 2 conflict nodes for the two-stage thesis, evidence-anchored, honest ceilings.
- **`scripts/experiment-evidence-weights.py`** + **`data/graph/evidence-weights.json`** — Kappa-style
  probe: grounding, support vs contradiction, section diversity per concept.

### Key experimental finding
The data independently confirms the epistemic split: grounded physics/info concepts (information,
quantum, entropy, causality) show high support and **zero contradiction**; thesis concepts (value, mind,
free_will, consciousness, agency) show **pure contradiction, zero support** despite high grounding —
they are pervasive but proposed. This validates SPEC-02's ceiling assignment as *data-driven*, not
imposed.

### Docs
- `DEV_PLAN.md` — the executable roadmap (Phase 0 foundations → generalization test → surfaces → live).

### Specs imported (canonical)
- `specs/SPEC-00-INFRA-BUILD.md` (from R2 `performancedoyle`)
- `specs/SPEC-07-ECOSYSTEM-SURVEY.md` (from R2 `gitclone`)
- `docs/vision/VISION.md` (the founding vision)

## 2026-08-14 (cont.) — arxiv graph-reasoning review + bounded-context experiment

### Imported
- **`specs/SPEC-08-GRAPH-REASONING-SURVEY.md`** (from R2 `arxivgraph`, 1467 lines) — 37 graph-reasoning
  architectures. Key conclusions: don't choose one GraphRAG algorithm — build a stable epistemic graph
  with **pluggable retrieval**; the 4 things to pinch (GFM-RAG graph abstraction, ToG-2 alternating
  text↔graph search, PathRAG/SubgraphRAG bounded context, Graphiti/AriGraph epistemic-vs-event split);
  2 bets (hypergraphs internally, executable graph queries via KG2Code).
- **`GAPS.md`** — honest gaps list (typed relations, review chain, retrieval, surfaces, domains, OCR,
  agent loop + the SPEC-08 pinches not yet adopted + datasets not ingested).

### Added
- **`scripts/peer-review-arxiv.py`** + **`data/graph/arxiv-review.json`** — cross-referenced 17 key
  architectures vs our engine. Result: 11 GAP, 2 BET, 3 VALIDATES, 1 REFERENCE. The validations
  (SubgraphRAG, LightRAG, LLM-Wiki) confirm our compiler + bounded-context doctrine; the bets
  (hypergraph Argument, KG2Code executable queries) are the frontier.
- **`scripts/experiment-bounded-context.py`** — PathRAG-style bounded-context retrieval. Tested on
  `free_will`/`determinism`: retrieves the argument chain I2→I5 + evidence quotes + conflicts, capped
  to token_budget. Working.

### Findings
- The 3 underestimated architectures are **G-reasoner, LLM-Wiki, KG2Code** — together they point to:
  compile once → represent structurally → learn/search efficiently → agents navigate via small
  deterministic ops → retain provenance + self-correction as first-class state. This converges on our
  generalized-engine architecture.
- Our argument graph's multi-premise/defeater structure is naturally **hypergraphic** (validates the
  hypergraph bet).

## 2026-08-14 (cont.) — full test suite + real bug fix

### Added
- **`scripts/run-tests.py`** — the reproducible validation+experiment suite (8 tests). Result: **8/8 PASS**.
- **`scripts/experiment-context-coverage.py`** — bounded-context stress test across all 31 concepts.
- **`docs/TESTING-VALIDATION-REPORT.md`** — full results (gates, evidence-weights, coverage, peer review).
- `data/graph/test-results.json` · `context-coverage.json` — machine-readable results.

### Bug found & fixed (by testing)
- **`mind_body` concept was isolated (0 edges)** though the corpus has 44 "mind-body" + 13 "mind/body".
- Root cause: `norm()` strips punctuation to spaces, so `"mind-body"` → `"mind body"`, but the lexicon
  key `"mind-body"` (hyphenated) was matched un-normalized → never matched.
- Fix: normalize the lexicon key in `find_concepts` too.
- **Impact:** edges 6484 → **6578** (+94); mind_body 0 → 94 edges; context coverage 97% → **100%**.

## 2026-08-14 (cont.) — agent-orchestration survey + organized ecosystem index

### Imported
- **`specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md`** (from R2 `agenticref`, 1510 lines) — runtimes
  (Restate/DBOS/Temporal/Hatchet), protocols (MCP/A2A/MCP Gateway/GitSkills), and the **universal
  schema** (PROJECT→KNOWLEDGE/WORK/EXECUTORS/OUTPUT, Task→Run→Agent→Artifact→Proposal→Review→Decision).
  Key: keep a cheap single-host runtime today; the universal schema's Review/Decision/Supersede matches
  our epistemic envelope.

### Added
- **`docs/ECOSYSTEM-INDEX.md`** — the consolidated, agent-navigable reference index for ALL ecosystem
  entries (tier-0 clones, datasets, arXiv architectures, agent infra) with 1-line "what it is + why".
- **`ecosystem/`** — organized clone directory with 7 categories (epistemic, compilers, argumentation,
  science, philosophy, retrieval, agent-runtime), each with a README explaining what belongs there + why.

## 2026-08-14 (cont.) — frontier-agent survey (SPEC-10)

### Imported
- **`specs/SPEC-10-FRONTIER-AGENT-SURVEY.md`** (from R2 `frontieragent`, 869 lines) — the agent
  research watchlist (Sakana, Prime Intellect, Jiayi Pan, Neubig, Yao, Packer, Muhan Zhang, Khattab,
  METR, ...) + the **convergence thesis**: agents move to foundation-model + learned computation policy +
  graph memory + verifier + experience archive → self-improvement. Strategic implication: **persistent
  verified state is the durable intelligence; models are disposable compute.**

### Added
- `docs/ECOSYSTEM-INDEX.md` §6 — the people/labs watchlist + convergence (consolidated).
