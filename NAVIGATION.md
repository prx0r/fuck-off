# IP-GRAPH — MASTER NAVIGATION (resolve anything)

*2026-08-14 (restructured to patala conventions). The canonical index for the informationphilosopher →
knowledge-graph project. For a human, a coding agent, or Hermes. Every resource resolves to: **what it
is · where it lives · which script built it · how to run it · key doc.** Read `AGENTS.md` (rules) and
`BUILDNOTES.md` (history) first.*

---

## 0. THE ONE-LINE

> Scraped info-philosophy site → cleaned corpus → **490-node, 6484-edge knowledge graph** of the
> free-will / determinism / quantum / information / entropy / mind / chance network.

---

## 1. THE LAYOUT

```
/mnt/HC_Volume_106427611/ip-graph/
  data/              all CONTENT
    raw/             cleaned source (html_articles/ · pdfs/ · images/ · errors/ + MANIFEST.json)
    extracted/       plain text per doc (html/ · pdf/ · _ocr/)
    extracted_md/    markdown per doc (_errors/ = quarantined)
    graph/           graph outputs (graph.json · doc_graph.gexf · concepts.jsonl · works.jsonl)
    references/      machine catalogs (arxiv.json · github.json)
    corpus.jsonl     ONE machine-readable corpus (425 versioned records)
  lib/               the reusable CODE KERNELS (epistemic · review · staleness · query · retrieval)
  scripts/           the pipeline + experiments + validations, dash-case names
  docs/              concern docs (01-05) + reference indexes + process/ + vision/ + reports/
  specs/             SPEC-00 … SPEC-14 (designs; 00 = CANONICAL infra build)
  layers/            00-09 the layer deep-pages (what/purpose/impl/current-state)
  ecosystem/         third-party clones, organized by category
  skills/            reusable agent skills (vcreate/ — backward-delivery planning)
  mcp/               future agent-tool layer
  AGENTS.md          the governing rules (read first)
  BUILDNOTES.md      the build history
  NAVIGATION.md      this file
  TODO.md            the live task tracker
  DEV_PLAN.md        the executable roadmap
  GAPS.md            known holes
  CHANGELOG.md       change log
  STATE.yaml         live per-layer tracker
  VISION-CHUNK-LAYER-MAP.md + VISION-CHUNKS.json   the vision→layer decomposition
```

### The code kernels (`lib/`) — reuse, don't rebuild
| Kernel | What it is | Layer |
|--------|-----------|-------|
| `lib/epistemic.py` | envelope + 4-axis authority + invariant | 00 |
| `lib/review.py` | herdr reducer state machine | 05/08 |
| `lib/staleness.py` | RKA blast-radius + review_queue + rebuild order | 03/12 |
| `lib/query.py` | KG2Code executable graph queries | 10 |
| `lib/retrieval.py` | PathRAG + HippoRAG retrieval | 10 |

### The layers (`layers/00-09-*.md`) — the deterministic anchors
Each layer page: what it is · purpose · data · processes · implementations · current state.
Tracked live in `STATE.yaml`. Decomposed from the vision in `VISION-CHUNK-LAYER-MAP.md`.

| Layer file | Focus | Layer file | Focus |
|-----------|-------|-----------|-------|
| `layers/00-core-engine.md` | envelope+schema substrate | `layers/05-review-gate.md` | review + adjudication |
| `layers/01-corpus-provenance.md` | ingestion + R2 | `layers/06-retrieval-compiler.md` | read artifacts |
| `layers/02-epistemic-graph.md` | KG + DAG | `layers/07-surfaces.md` | Astro/MCP (DISCOVERED) |
| `layers/03-factory.md` | staleness + compiler | `layers/08-domain-expansions.md` | generality |
| `layers/04-argument-engine.md` | AIF + crux | `layers/09-live-system.md` | meta-layer + organism |

---

## 2. THE PIPELINE (scripts, in dependency order)

| Script | What it does | Output |
|--------|--------------|--------|
| `inventory.py` | classify every file by section + quality | `docs/reports/inventory.json` |
| `clean-corpus.py` | separate real HTML/PDFs/images; quarantine errors | `data/raw/` + `MANIFEST.json` |
| `extract-html.py` | HTML → clean text | `data/extracted/html/` |
| `extract-pdf.py` | PDF → text (pdftotext) | `data/extracted/pdf/` |
| `to-markdown-jsonl.py` | txt → markdown + corpus.jsonl | `data/extracted_md/` + `data/corpus.jsonl` |
| `classify-errors.py` | precise error-page detection | stdout list |
| `purge-errors.py` | quarantine error pages; clean corpus.jsonl | `_errors/` + clean `data/corpus.jsonl` |
| `build-graph.py` | build the graph from clean corpus | `data/graph/*` |
| `ocr-scanned-pdfs.py` | OCR the 8 scanned PDFs | `data/extracted/pdf/_ocr/` |

**Re-run order:** inventory → clean → extract → to-md → classify → purge → build. To rebuild just the
graph after adding text, run `build-graph.py`.

---

## 3. THE DATA

| Data | Where | Built by |
|------|-------|----------|
| Clean source corpus | `data/raw/` | clean-corpus |
| Plain text (425) | `data/extracted/` | extract-html, extract-pdf |
| Markdown (426 active) | `data/extracted_md/` | to-markdown-jsonl, purge-errors |
| Quarantined errors (24 md / 788 raw) | `data/extracted_md/_errors/` + `data/raw/errors/` | purge-errors, clean-corpus |
| Machine corpus (425) | `data/corpus.jsonl` | to-markdown-jsonl, purge-errors |
| Graph (490 nodes / 6484 edges) | `data/graph/graph.json` | build-graph |
| Gephi export | `data/graph/doc_graph.gexf` | build-graph |
| Concept / work records | `data/graph/concepts.jsonl` · `works.jsonl` | build-graph |

---

## 4. THE DOCUMENTS

| Doc | What it is |
|-----|------------|
| `AGENTS.md` | governing rules — read first |
| `LAB-REVIEW.md` | state of the lab (proven/exploratory/next) |
| `HANDOVER.md` | session state + where to continue |
| `TRACEABILITY-MAP.md` | the traceability root (everything → vision + layer) |
| `migration/v2/README.md` | the PROVEN v2 — patala spec ↔ our implementations (handoff) |
| `migration/v2/PUSHING-ORGANISM-ESSAYS.md` | logicvid + organism + essays-as-machine |
| `migration/v2/ESSAY-INGEST.md` | the 9-stage essay-as-derivation-input pipeline |
| `migration/v2/INGESTION-ARCHITECTURE.md` | source-text vs essay-about-source vs standalone |
| `migration/v2/GRADUATION.md` | the full organism test is real (one claim, whole stack, 14/14) |
| `KERNELS-INDEX.md` | the reusable kernels (reuse map) |
| `MASTER-KNOWLEDGE-BASE.md` | the synthesized master reference (17 kernels · 51 experiments · 32 arXiv · 99 repos · 46 specs) |
| `BUILDNOTES.md` | full build history + decisions |
| `NAVIGATION.md` | this file |
| `TODO.md` | live task tracker |
| `docs/01-corpus.md` | the source data + ground truth |
| `docs/02-extraction.md` | the text pipeline |
| `docs/03-graph.md` | the graph output |
| `docs/04-ontology.md` | the concept + relation vocabulary (the graph contract) |
| `docs/05-performance.md` | the performance doctrine |
| `docs/performanceagent.md` | agent/human speed deep-dive (frameworks, runtimes, formats, stacks) |
| `docs/ORIGINAL-README.md` | redirect stub (superseded) |
| `docs/ECOSYSTEM-INDEX.md` | consolidated reference index (repos/datasets/arxiv/agent infra) |
| `docs/ARXIV-INDEX.md` | canonical arXiv catalog (32 papers, by category) |
| `docs/GITHUB-INDEX.md` | canonical GitHub catalog (74 repos, by category + tier) |
| `docs/TESTING-VALIDATION-REPORT.md` | the test + validation results |
| `docs/EXPERIMENT-REPORT.md` | third-party repo experiments (herdr/RKA/kappa/nano-graphrag) |
| `docs/EXPERIMENT-MATRIX.md` | the full experiment tracking matrix (29, by vision/layer/source) |
| `docs/ALGORITHMS.md` | granular arXiv-algorithm implementations (PathRAG/HippoRAG/KG2Code) |
| `docs/process/FRONTIER-MAP.md` | per-layer implementations, todos, validations |
| `skills/vcreate/SKILL.md` | vcreate: backward-delivery planning (the reverse-chaining skill) |
| `skills/theatre-check/SKILL.md` | theatre-check: the verifiable-proof anti-theatre skill |
| `docs/vision/beyond-patala/THESIS-REVERSE-DELIVERY.md` | the reverse-delivery thesis |

## Vision docs
| Doc | What it is |
|-----|------------|
| `docs/vision/VISION.md` | the founding vision (general epistemic engine) |
| `docs/vision/VISION-PATALA-FUTURES.md` | 7 concrete, evidence-grounded futures for patala |
| `docs/vision/VISION-VERIFIED-EPISTEMIC-OS.md` | the unified Verified Epistemic OS (8 laws) |
| `docs/vision/VISION-UNCONSIDERED-FRONTIERS.md` | the unconsidered frontiers (6 novel directions) |
| `docs/vision/beyond-patala/` | the product visions (marketplace · organism · what-if · self-proving) |
| `docs/vision/beyond-patala/VISION-VERIFIED-STATEMENT-MARKETPLACE.md` | verification as an economic good (Certification Weight) |
| `docs/vision/beyond-patala/VISION-COEVOLVING-EPISTEMIC-ORGANISM.md` | learning loops back into scholarship (Misconception Likelihood) |
| `docs/vision/beyond-patala/VISION-WHAT-IF-MACHINE.md` | counterfactual as discovery (Research Value Score) |
| `docs/vision/beyond-patala/VISION-SELF-PROVING-SYSTEM.md` | the OS proves its own construction (Design-Provenance nanopub) |
| `docs/vision/beyond-patala/VISION-QUESTION-GROWTH-ENGINE.md` | the pushing method as a learnable question-growth machine |
| `docs/LOGICVID-GOLD-EXEMPLARS.md` | the live human-curiosity gold (markers + how to use as gold) |
| `docs/vision/beyond-patala/VISION-ENQUIRY-DISCOVERY-ORGANISM.md` | the enquiry-as-discovery organism (questions reveal topic structure) |
| `docs/EXPERIMENT-REPORT.md` | third-party repo experiments (herdr/RKA/kappa/nano-graphrag) |
| `docs/EXPERIMENT-MATRIX.md` | the full experiment tracking matrix (29, by vision/layer/source) |
| `docs/ALGORITHMS.md` | granular arXiv-algorithm implementations (PathRAG/HippoRAG/KG2Code) |

## Reference catalogs (machine-readable)
| File | What it is |
|------|------------|
| `data/references/arxiv.json` | 32 papers with id/url/title/category/status/note |
| `data/references/github.json` | 89 repos with owner/name/url/category/tier/note |
| `data/references/experiments.json` | 29 experiments mapped to layer/source/vision/kernel/status |

## Ecosystem clones (organized)
`ecosystem/{epistemic,compilers,argumentation,science,philosophy,retrieval,agent-runtime}/` — each
category has a README explaining what belongs there + why. See `docs/ECOSYSTEM-INDEX.md`.

## Specs (designs — become live docs when implemented)

| Spec | Topic |
|------|-------|
| `specs/SPEC-00-INFRA-BUILD.md` | **CANONICAL** master infra build (read architecture) |
| `specs/SPEC-01-canonical-dag.md` | the derivational layer DAG |
| `specs/SPEC-02-epistemic-envelope.md` | epistemic status ladder + authority |
| `specs/SPEC-03-argument-graph.md` | AIF Info/Inference/Conflict graph |
| `specs/SPEC-07-ECOSYSTEM-SURVEY.md` | third-party repos/datasets/benchmarks (CANONICAL) |
| `specs/SPEC-08-GRAPH-REASONING-SURVEY.md` | arXiv graph-reasoning architectures (CANONICAL) |
| `specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md` | runtimes/protocols/universal schema (CANONICAL) |
| `specs/SPEC-10-FRONTIER-AGENT-SURVEY.md` | people/labs to track + the convergence (CANONICAL) |
| `specs/SPEC-11-AGENT-MEMORY-SURVEY.md` | agent memory / self-evolving systems (CANONICAL) |
| `specs/SPEC-12-AGENT-HARNESS-SURVEY.md` | agent-harness repos (CANONICAL) |
| `specs/SPEC-13-STALENESS-PERFORMANCE.md` | staleness + performance for the futures (CANONICAL) |
| `specs/SPEC-14-FRONTIER-LAYER-BUILDS.md` | frontier build for all 13 layers (CANONICAL) |
| `specs/SPEC-15-PATALA-REVIEW.md` | scholar review survey (CANONICAL) |
| `specs/SPEC-16-PATALA-TRANSLATE.md` | translation subsystem survey (CANONICAL) |
| `specs/SPEC-17-PATALA-GITHUBS.md` | textual/identity/provenance survey (CANONICAL) |
| `specs/SPEC-18-COMPLETE-PIPELINE.md` | complete product pipeline (CANONICAL) |

## Governance / planning
| File | What it is |
|------|------------|
| `DEV_PLAN.md` | the executable roadmap (Phase 0 → generalization → surfaces → live) |
| `GAPS.md` | honest known holes (mapped to layer + spec) |
| `CHANGELOG.md` | change log |
| `STATE.yaml` | live per-layer tracker |

---

## 5. HOW TO RUN

```bash
cd /mnt/HC_Volume_106427611/ip-graph
# verify corpus integrity
python3 -c "import json; [json.loads(l) for l in open('data/corpus.jsonl')]; print('corpus OK')"
# verify graph integrity
python3 -c "import json; g=json.load(open('data/graph/graph.json')); print(len(g['nodes']),'nodes',len(g['edges']),'edges')"
# rebuild the graph
python3 scripts/build-graph.py
# OCR the 8 scanned PDFs (background)
nohup python3 scripts/ocr-scanned-pdfs.py > /tmp/opencode/ocr.log 2>&1 &
```

---

## 6. THE ONTOLOGY (`docs/04-ontology.md`)

- **Themes:** free_will, determinism, causality, quantum, information, entropy, mind, chance, knowledge,
  value, life
- **Concept categories:** concept, work, author, scientist, philosopher, theory, problem, experiment,
  school
- **16 typed relations:** negates, presupposes, is_cause_of, is_identical_to, defines, supports,
  tensions_with, is_obstacle_to, is_antidote_to, extends, applies_method_of, is_instance_of,
  deconstructs, reframes_as, is_precursor_of, opposes
- **Evidence anchor discipline:** every object carries a verbatim `evidence_quote`; closed vocab only;
  no invented relations; self-referential edges dropped.

---

## 7. THE PERFORMANCE DOCTRINE (`docs/05-performance.md`)

From patala. **Compute on write, immutable versioned URLs, one-request agent bundles, Astro static +
Cloudflare Workers/Hyperdrive/R2, ETags from hashes, Rust only for hot kernels.** See the doc for the
full 10 rules.

---

## 8. RELATED RESOURCES

- Cloned KG tools: `/mnt/HC_Volume_106427611/kg-tools/{instagraph,iwe,seventeen-centuries}`
- patala graph machinery: `/root/projects/patala/machinelearning/research/patala_ml/`
- darshana-graph (text→graph): `/mnt/HC_Volume_106427611/patala-ingest/clones/darshana-graph/`
- R2 backup of source: `r2:atlas-sources/informationphilosopher/`
