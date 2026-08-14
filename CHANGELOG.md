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

## 2026-08-14 (cont.) — canonical arXiv reference index

### Added
- **`scripts/build-arxiv-index.py`** — generates the arXiv catalog from the survey specs.
- **`data/references/arxiv.json`** — machine-readable catalog (32 papers).
- **`docs/ARXIV-INDEX.md`** — readable, agent-navigable catalog organized into 7 categories:
  graph-reasoning (11), agent-rl (6), agent-memory (4), agent-eval (4), agent-orchestration (3),
  agent-frameworks (2), skills-datasets (2). Each entry: title · arxiv link · status (GAP/BET/
  VALIDATES/REFERENCE) · note.
- NAVIGATION.md wired to the index.

## 2026-08-14 (cont.) — GitHub reference index + full structure audit

### Added
- **`specs/SPEC-11-AGENT-MEMORY-SURVEY.md`** (from R2 `githubagent`, 1194 lines) — agent-memory /
  self-evolving systems. Key insight: what remains distinctly ours is the **epistemic kernel +
  rigorous promotion path (agent output → evidence → review → canonical knowledge)**.
- **`scripts/build-github-index.py`** — generates the GitHub catalog.
- **`data/references/github.json`** — machine-readable (74 repos: owner/name/url/category/tier/note).
- **`docs/GITHUB-INDEX.md`** — readable catalog, 10 categories + tier tagging (0=clone-first, 1=ingest,
  2=architecture, 3=watch).

### Structure audit (cleanliness + cross-references)
- Fixed NAVIGATION.md to list only real spec files (removed stale SPEC-04/05/06 entries).
- Fixed layers/07-surfaces.md dangling SPEC-05 ref → SPEC-00/09.
- Reconcile specs/README.md: SPEC-01/02/03 marked implemented; SPEC-04/05/06 clearly marked "planned,
  content covered elsewhere".
- ECOSYSTEM-INDEX.md updated with SPEC-10/11 sources + §7 agent-memory repos.

### Reference catalogs (canonical, machine-readable)
- `data/references/arxiv.json` (32 papers) + `docs/ARXIV-INDEX.md`
- `data/references/github.json` (74 repos) + `docs/GITHUB-INDEX.md`

## 2026-08-14 (cont.) — added loom (Huntley's Rust agent)
- Cloned `ghuntley/loom` → `ecosystem/agent-runtime/loom` (24M). **PROPRIETARY license** — reference/
  code-read only, do not reuse code.
- Added to GitHub index (75 repos, agent-runtime category, T3 watch) + agent-runtime README.

## 2026-08-14 (cont.) — agent-harness survey (SPEC-12) + small clones
- **`specs/SPEC-12-AGENT-HARNESS-SURVEY.md`** (from R2 `githubagent2`) — maestro, arcan, herdr-workflow,
  weft, looms, Dicklesworthstone flywheel. Red circles: **Herdr** (agents propose immutable evidence,
  reducers own lifecycle) + **Dicklesworthstone** (tiny composable tools).
- **Cloned (tracked):** herdr-workflow (2.2M), arcan (4.7M) → `ecosystem/agent-runtime/`.
- **Cloned (local-only, gitignored):** valkor-ai/loom (Apache-2.0), maestro (tracked sqlite w/ sk- strings).
- GitHub index: 75 → **79 repos**.

## 2026-08-14 (cont.) — third-party repo experiments
- Cloned + tested core patterns from cloned repos against our real data:
  - **herdr-workflow** (`experiment-herdr-review.py`) — reducer state machine keeps thesis claims in
    CORRECTION_REQUIRED, corroborated physics in ALIGNED.
  - **RKA** (`experiment-rka-staleness.py`) — blast-radius propagation: PHYSICS retraction flags 8
    downstream layers stale (FREE_WILL, VALUE) -> review_queue.
  - **Kappa** — grounding/contradiction (evidence-weights.json).
  - **nano-graphrag** (`experiment-nano-stable-graph.py`) — stable-LCC + GraphML determinism confirmed.
  - **unified synthesis** (`experiment-unified-epistemic.py`) — kappa+herdr+RKA in one pipeline.
- New clones: RKA (local-only 30M), Kappa (local-only 49M), nano-graphrag (tracked 3.3M).
- **`docs/EXPERIMENT-REPORT.md`** — consolidated results + what to adopt.
- NAVIGATION + CHANGELOG wired.
