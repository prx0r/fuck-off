# IP-GRAPH — BUILDNOTES (full build history)

*Every step taken to turn the scraped informationphilosopher.com corpus into a knowledge graph.
Read this before `NAVIGATION.md`. For the agent governing rules, read `AGENTS.md` first.*

---

## 1. Context

The user scraped `informationphilosopher.com` (the full site — the **only copy**, backed up to R2 at
`r2:atlas-sources/informationphilosopher`). They wanted a **knowledge graph** of the information-
philosophy network (free will, determinism, causality, quantum, information, entropy, mind, chance).
The `patala` project (`/root/projects/patala`) is the architectural template.

---

## 2. The corpus reality (the key discovery)

**~97% of the scraped HTML is broken** (Apache "Bad Request" error pages saved as content).

| Type | Raw | Real | Location |
|------|-----|------|----------|
| HTML | 1896 | 44 in `data/raw/html_articles/` | 788 error pages in `data/raw/errors/` |
| PDFs | 437 | 419 in `data/raw/pdfs/` | the real value |
| Images | 522 | 502 in `data/raw/images/` | supporting |

**Ground-truth clean corpus: 425 documents** (6 html + 419 pdf). The `solutions/` PDFs are a curated
primary-source library (Einstein, Bell, Bohm, Planck, Schrödinger, Mermin, Turing, Dennett, Sperry,
Deacon, Landauer, Wheeler + free-will philosophers).

---

## 3. Build history (each step)

| Step | Script | Result |
|------|--------|--------|
| Inventory | `inventory.py` | classified all files; wrote inventory report |
| Clean | `clean-corpus.py` | `data/raw/` separated; errors quarantined |
| Extract HTML | `extract-html.py` | real pages → text |
| Extract PDF | `extract-pdf.py` | pdftotext → text (8 scanned flagged) |
| To md+jsonl | `to-markdown-jsonl.py` | 452 docs → md + corpus.jsonl |
| Classify errors | `classify-errors.py` | 26 true error pages (false positives excluded) |
| Purge errors | `purge-errors.py` | 24 error pages → `_errors/`; clean corpus.jsonl → 425 |
| Build graph | `build-graph.py` | **490 nodes, 6578 edges** from 425 clean docs |
| OCR (deferred) | `ocr-scanned-pdfs.py` | not run — see TODO |

---

## 4. The graph

- **490 nodes, 6578 edges**
- Node types: 425 works, 31 concepts, 18 authors, 11 themes, 3 schools, 2 problems
- Schema: instagraph `KnowledgeGraph` `{metadata, nodes, edges}`
- Edge relationships: `discusses`, `authored_by`, `co_occurs_with`, `belongs_to`
- **Limitation:** edges are `co_occurs_with` (statistical). Next: typed relations per
  `docs/04-ontology.md` (needs LLM tagging).

---

## 5. Design decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Graph format | instagraph JSON (primary) | simple, visualizable |
| Extraction | deterministic (offline) | no API key, fast, reproducible |
| Ontology | closed vocabulary | prevents invented relations |
| Error handling | quarantine, never delete | reviewable, safe |
| Corpus format | single versioned corpus.jsonl | one machine-readable source |
| Architecture template | patala NAVIGATION.md + atlas-performance.md | proven patterns |
| Structure | data/ scripts/ docs/ separated, dash-case scripts, numbered docs | patala discipline |

---

## 6. Performance doctrine (from patala, for serving the graph)

Sourced from `patala/docs/vision/atlas/atlas-performance.md` + `atlas-cloudflare-edge-layer.md`.
Full 10 rules in `docs/05-performance.md`. Summary: **compute on write, immutable versioned URLs,
one-request agent bundles, Astro static + Cloudflare Workers/Hyperdrive/R2, ETags from hashes, Rust
only for hot kernels.**

---

## 7. References / source code consulted

| Source | What it gave us |
|--------|-----------------|
| `patala/AGENTS.md` | agent governing doc pattern (one rule, axioms, navigation) |
| `patala/NAVIGATION.md` | master-index / layer model |
| `patala/docs/process/README.md` | data/code/docs separation + reusable inventory |
| `patala/machinelearning/research/patala_ml/*.py` | graph-building algorithms |
| `patala/docs/vision/atlas/atlas-performance.md` | the 35-point performance doctrine |
| `patala/docs/vision/atlas/atlas-cloudflare-edge-layer.md` | the Cloudflare stack |
| `patala/docs/atlas-contracts/read-api.md` | the read-API grammar ("mommyspeed") |
| `/mnt/HC_Volume_106427611/kg-tools/instagraph` | instagraph KnowledgeGraph schema |
| `/mnt/HC_Volume_106427611/kg-tools/iwe` + `seventeen-centuries` | markdown-graph format |
| `/mnt/HC_Volume_106427611/patala-ingest/clones/darshana-graph` | closed-vocab LLM tagging |

---

## 8. Known gaps / next steps

1. **OCR the 8 scanned PDFs** (`scripts/ocr-scanned-pdfs.py`).
2. **Typed relations** — upgrade `co_occurs_with` → ONTOLOGY relations (LLM-tagged).
3. **Evidence quotes** — attach verbatim `evidence_quote` per concept/edge.
4. **iwe markdown graph export** — for browsing + MCP agents.
5. **Visualization** — pyvis/HTML or Gephi export.
6. **Re-scrape broken pages** — the ~788 quarantined error pages could be re-fetched.

See `TODO.md` for the live tracker.
