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
  data/
    raw/             cleaned source (html_articles/ · pdfs/ · images/ · errors/ + MANIFEST.json)
    extracted/       plain text per doc (html/ · pdf/ · _ocr/)
    extracted_md/    markdown per doc (_errors/ = quarantined)
    graph/           graph outputs (graph.json · doc_graph.gexf · concepts.jsonl · works.jsonl)
    corpus.jsonl     ONE machine-readable corpus (425 versioned records)
  scripts/           the pipeline, dash-case names
  docs/              numbered concern docs (01-corpus … 05-performance)
  mcp/               future agent-tool layer
  AGENTS.md          the governing rules (read first)
  BUILDNOTES.md      the build history
  NAVIGATION.md      this file
  TODO.md            the live task tracker
```

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
| `BUILDNOTES.md` | full build history + decisions |
| `NAVIGATION.md` | this file |
| `TODO.md` | live task tracker |
| `docs/01-corpus.md` | the source data + ground truth |
| `docs/02-extraction.md` | the text pipeline |
| `docs/03-graph.md` | the graph output |
| `docs/04-ontology.md` | the concept + relation vocabulary (the graph contract) |
| `docs/05-performance.md` | the performance doctrine |
| `docs/ORIGINAL-README.md` | redirect stub (superseded) |
| `docs/ECOSYSTEM-INDEX.md` | consolidated reference index (repos/datasets/arxiv/agent infra) |
| `docs/ARXIV-INDEX.md` | canonical arXiv catalog (32 papers, by category) |
| `docs/GITHUB-INDEX.md` | canonical GitHub catalog (74 repos, by category + tier) |
| `docs/TESTING-VALIDATION-REPORT.md` | the test + validation results |

## Reference catalogs (machine-readable)
| File | What it is |
|------|------------|
| `data/references/arxiv.json` | 32 papers with id/url/title/category/status/note |
| `data/references/github.json` | 74 repos with owner/name/url/category/tier/note |

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
