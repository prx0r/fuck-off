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

## 2026-08-14 (cont.) — read arXiv papers + implement core algorithms
- Read the actual papers (not just surveys): PathRAG, HippoRAG, KG2Code (full), ToG-2, SubgraphRAG,
  G-reasoner, HyperGraphRAG (abstracts).
- **Implemented + tested on our graph:**
  - `experiment-pathrag.py` — flow-based pruning (α=0.7, early-stop θ), path reliability, ascending path prompting
  - `experiment-hipporag.py` — Personalized PageRank retrieval (found hub-bias: Value/Information over-rank)
  - `experiment-kg2code.py` — executable graph-query DSL (resolve/neighbors/path/evidence) with verifiable traces
- **`docs/ALGORITHMS.md`** — granular findings + what to adopt (PathRAG→L06, HippoRAG→L06, KG2Code→L06/L07,
  ToG-2 alternating→L06 trace, HyperGraphRAG→L04).
- NAVIGATION + CHANGELOG wired.

## 2026-08-14 (cont.) — patala futures visions
- **`docs/vision/VISION-PATALA-FUTURES.md`** — 7 concrete, evidence-grounded visions synthesizing
  everything validated: (1) The Argument Map [flagship product], (2) General Epistemic Engine,
  (3) Self-Maintaining Epistemic Graph, (4) Executable Knowledge [KG2Code], (5) Verified Corpus Engine
  [science], (6) Cross-Tradition Comparative Philosophy, (7) Autonomous Review Institute.
- Priority order: promote proven experiments to lib/ → 5 import adapters (generalization test) →
  KG2Code query over MCP → Argument Map pages → review ledger + agent loop.
- NAVIGATION + CHANGELOG wired.

## 2026-08-14 (cont.) — staleness & performance engineering for the futures
- **`specs/SPEC-13-STALENESS-PERFORMANCE.md`** — for each of the 7 patala futures, the concrete staleness
  mechanism (borrowed + verified from cloned repos: RKA review_queue/blast-radius, herdr reducer/
  invalidation_rules/FindingStatus, arcan event-sourcing, nano-graphrag content-addressing) and the
  performance optimization (SPEC-00 compile-once, PathRAG/HippoRAG retrieval), each with justification.
- Unifying thesis: staleness-walk = dependency-graph = incremental-rebuild = retrieval index — one graph.
- specs README + NAVIGATION + CHANGELOG wired.

## 2026-08-14 (cont.) — frontier layer-by-layer builds for patala
- Read all 13 of patala's layer docs (00-12) + the CORE-BIBLE vision.
- **`specs/SPEC-14-FRONTIER-LAYER-BUILDS.md`** — for each patala layer, the most frontier-optimized build
  using our papers (SPEC-08) + cloned repos (SPEC-07/09/11/12) + proven experiments:
  - 00 Governance → Stencila schema contract
  - 01 Ingestion → 5-adapter generalization test (RKA backends)
  - 02 Atlas → nano stable-LCC content-addressing
  - 03 Factory → canonical DAG = staleness+rebuild engine (RKA)
  - 04 Evidence → verifier ensemble + conformal abstention
  - 05 Research → herdr reducer + KG2Code executable ArgumentSynthesis
  - 06 Commentarial → KORAL two-graph + verifier ensemble
  - 07 Verification → two-plane + conformal + PathRAG
  - 08 Human Authority → herdr/Vouch gate
  - 09 Organism → Graphiti + pyBKT + KST (Q-variable)
  - 10 Surfaces → Argument Map over compiled projections (KG2Code/PathRAG/HippoRAG)
  - 11 Org/Economics → arcan event-sourcing + publication gate
  - 12 Live System → epistemic work queue + RKA staleness + STATE.yaml
- Frontier thread: epistemic honesty (SPEC-02/herdr/RKA) + compile-once (SPEC-00/KG2Code) — one graph.
- specs README + NAVIGATION + CHANGELOG wired.

## 2026-08-14 (cont.) — FRONTIER-MAP: lib/ kernels + layer validations
- **`docs/process/FRONTIER-MAP.md`** — implementation map + todos per patala layer.
- **Promoted experiments → `lib/`:** `lib/review.py` (herdr reducer), `lib/staleness.py` (RKA
  blast-radius + review_queue + incremental rebuild order), `lib/query.py` (KG2Code DSL),
  `lib/retrieval.py` (PathRAG + HippoRAG).
- **Layer 03+05 validation** (`validate-layer03-05.py`): 12/12 pass — staleness reaches FREE_WILL/VALUE,
  rebuild order correct, reducer gates promotion honestly.
- **Layer 10 retrieval comparison** (`validate-layer10.py`): PathRAG + KG2Code retrieve the target;
  **HippoRAG PPR is hub-biased (Value/Information dominate)** — a verified finding requiring
  query-relevance reweighting.
- Test suite now 10/10 pass.

## 2026-08-14 (cont.) — complete product pipeline (SPEC-15/16/17 → SPEC-18)
- Imported + saved SPEC-15 (review), SPEC-16 (translate), SPEC-17 (githubs) from R2.
- **Built 3 product kernels (validated 11/11):**
  - `lib/translation.py` — TranslationProof, non-aggregate audit vector + dimension-specific publication gate
  - `lib/scholar_review.py` — adversarial review panel, anti-groupthink, CiteCheck phantom detection
  - `lib/schema.py` — Stencila-style single-source schema compiler (claim/evidence/argument)
- **`specs/SPEC-18-COMPLETE-PIPELINE.md`** — the full pipeline (textual/epistemic/work substrates →
  TranslationProof → claim/argument/evidence → review → projection → education).
- `scripts/validate-products.py` (11/11) added to test suite (now 11 total tests... will confirm).

## 2026-08-14 (cont.) — cloned + validated 4 more high-value repos
- **Cloned (tracked, clean):** `mntlra/knowledgeProvenance` (748K, PROV-K nanopubs), `cmu-paper-reviewer`
  (3.6M), `literature-review-toolkit` (11M), `agent-review-panel` (13M).
- **Validated knowledgeProvenance** (`validate-provenance.py`, 4/4): our epistemic ceilings map cleanly
  to PROV-K nanopub types (SCHOLARLY_CORROBORATED → ReliableFact, MACHINE_PROPOSED → UncertainFact) with
  content-addressed ids + provenance — the outward serialization for Layer 02/04.
- **agent-review-panel**: extracted its 16-phase protocol (Phase 10 claim-verify, Phase 11 severity-verify,
  Phase 14 judge) — directly enhances our `lib/scholar_review.py`.
- GitHub index 79 → **83 repos**. Test suite now **12/12**.

## 2026-08-14 (cont.) — more subsystem tests (KORAL, communities, generalization)
- **`experiment-koral-twograph.py`** (Layer 06): reality-vs-literature two-graph validated — a
  literature reinterpretation stays in literature (reality untouched); a reality retraction cascades
  up into interpretations. Enforces PRIMARY≠INTERPRETATION.
- **`experiment-communities.py`** (Layer 02): community detection on our concept graph independently
  discovered 3 emergent clusters that MATCH our epistemic split — (0) physics/info/mind,
  (1) free-will/determinism/agency, (2) consciousness/mind-body/qualia. Structural confirmation of
  the hand-curated themes.
- **`experiment-generalization.py`** (Layer 08/domain): the engine's core (envelope, schema, reducer)
  applies UNCHANGED to an EleutherIA-style ancient free-will domain — only ontology extends. The
  generalization bet validated; `agency`+`determinism` are shared cross-link concepts.
- Test suite 12 → **15/15 pass**.

## 2026-08-14 (cont.) — Doyle experiments (SPEC-19): crux compiler, mutation testing, signed corpus, reactive essay
- Imported **SPEC-19-DOYLE-EXPERIMENTS.md** (16 experiments) from R2; the thesis: Pāṭala as
  Bazel/Nix+Git+CI+review applied to epistemic objects.
- **Crux compiler** (`experiment-crux-compiler.py`): isolates the minimal divergence between
  compatibilism and the two-stage thesis — INDETERMINISM being necessary for free will.
- **Epistemic mutation testing** (`experiment-mutation-testing.py`): 100% verifier kill-rate across
  all 3 operators. The process EXPOSED a real weakness (flip_ceiling 0%) and guided the fix
  (corroboration-record check) — mutation testing works.
- **Signed corpus root** (`experiment-signed-corpus.py`): Merkle root fingerprints the whole epistemic
  state; any mutation changes the root (tamper-evident).
- **Reactive essay** (`experiment-reactive-essay.py`): source retraction propagates to mark 5/5 prose
  sentences stale (reactive documents).
- Test suite 15 → **19/19 pass**.

## 2026-08-14 (cont.) — cloned + tested instagraph, seventeen-centuries, PathRAG, graphiti
- **Cloned (clean, tracked):** instagraph (520K), seventeen-centuries (6MB), PathRAG (2.1M), graphiti (30M).
- **Graphiti temporal model** (`experiment-graphiti-temporal.py`): valid_at/invalid_at/episodes gives
  replayable temporal truth — validated as Layer 09 organism/user-knowledge temporal layer.
- **instagraph**: our graph.json already uses its exact Node/Edge schema (validates our choice).
- **PathRAG**: confirmed the real code's flow (keyword→entity→context) matches our lib/retrieval.py.
- GitHub index 83 → **87 repos**. Test suite 19 → **20/20**.

## 2026-08-14 (cont.) — SciFact generalization adapter + sage-wiki
- **Cloned:** allenai/scifact (528K, claim/evidence gold), xoai/sage-wiki (30M, graph-as-compile-output).
- **`experiment-import-scifact.py`** (the generalization bet): a real SciFact-format claim enters our
  engine — envelope (contradicted→MACHINE_PROPOSED), schema validation OK, review reducer blocks it
  (CORRECTION_REQUIRED). Proven: Doyle (philosophy) + SciFact (science) share ONE engine.
- Test suite 20 → **21/21 pass**.

## 2026-08-14 (cont.) — VISION: the Verified Epistemic OS (unifying the arsenal)
- **`docs/vision/VISION-VERIFIED-EPISTEMIC-OS.md`** — the visionary synthesis: patala as the
  Verified Epistemic OS where every genius repo is a component. 8 unifying laws (epistemic honesty,
  deterministic promotion, self-maintaining staleness, temporal truth, publishable provenance,
  executable retrieval, reactive documents, verified self-knowledge) + the work-substrate synthesis
  (loom state + maestro card.yaml + herdr reducer + arcan event-sourcing).
- **`experiment-verified-lifecycle.py`** (flagship): ONE claim runs through all 8 laws — proposed →
  herdr-gated → RKA-flagged-stale → graphiti-temporally-stamped → knowledgeProvenance-nanopub →
  KG2Code-queried → prose-marked-stale → Merkle-signed. Proves the OS coheres.
- Test suite 21 → **22/22 pass**.
