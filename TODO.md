# IP-GRAPH — TODO / STATUS

Track the informationphilosopher → knowledge-graph pipeline. Legend: `[x]` done · `[ ]` open ·
`[~]` in progress.

## Pipeline stages
- [x] **Inventory** — classify all 1896 HTML + 437 PDFs by section + quality
- [x] **Clean corpus** — separate real HTML/PDFs/images; quarantine errors → `data/raw/`
- [x] **Extract HTML** — real pages → plain text
- [x] **Extract PDF** — pdftotext → plain text (8 scanned flagged)
- [x] **To markdown + jsonl** — 452 docs → `data/extracted_md/` + `data/corpus.jsonl`
- [x] **Classify errors** — precise error-page detection (26 true error pages)
- [x] **Purge errors** — quarantine to `_errors/`; clean corpus.jsonl → **425 records**
- [x] **Build graph** — deterministic graph from clean corpus (**490 nodes, 6484 edges**)
- [x] **Restructure** — patala-style: data/ scripts/ docs/ separation, dash-case scripts, numbered docs
- [x] **Reconcile numbers** — all docs updated to ground truth (425 / 6+419 / 24 / 490 / 6484)

## Open items (priority order)
- [ ] **OCR the 8 scanned PDFs** — add their text so 100% coverage (see `docs/02-extraction.md` for
  the list). Tool: `scripts/ocr-scanned-pdfs.py` (`ocrmypdf --force-ocr`).
- [ ] **Upgrade graph edges** — replace `co_occurs_with` with typed relations from
  `docs/04-ontology.md` (needs LLM tagging, e.g. darshana-graph `tag_corpus.py` pattern).
- [ ] **Attach evidence quotes** — verbatim `evidence_quote` per concept/edge (ontology requires it).
- [ ] **iwe markdown graph export** — fragments + concept `.md` files for browsing + MCP agents.
- [ ] **Visualization** — pyvis/HTML or Gephi-ready export of `data/graph/graph.json`.
- [ ] **Re-scrape broken pages** — the ~788 quarantined error pages could be re-fetched if the site
  returns real content.
- [ ] **Build the agent MCP layer** — populate `mcp/` with agent tools over the graph (per
  `docs/05-performance.md` doctrine).

## Decisions pending
- [ ] Primary graph format (iwe markdown vs instagraph JSON vs patala registry)
- [ ] LLM vs deterministic extraction for typed relations
- [ ] Relation vocabulary finalization (`docs/04-ontology.md` is the draft)
