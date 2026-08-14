# LAYER 01 — CORPUS & PROVENANCE

*Part of the `VISION-CHUNK-LAYER-MAP.md` spine (Chunk 2). Ingestion + clean corpus + provenance.*

## 1. What it is
The intake + clean layer: sources → canonical works/passages, with provenance and R2 backup. This is
the ONLY layer that's fully DONE.

## 2. Purpose
Turn raw scraped content into a clean, versioned, provenance-carrying corpus — the substrate every
other layer reads.

## 3. Data
- `data/raw/` — cleaned source (html_articles/ · pdfs/ · images/ · errors/)
- `data/extracted/` — plain text (425 docs)
- `data/extracted_md/` — markdown (426 active)
- `data/corpus.jsonl` — the ONE machine corpus (425 records, versioned)
- R2 backup: `r2:atlas-sources/informationphilosopher/`

## 4. Processes
```
scrape → inventory → clean → extract-html/pdf → to-md/jsonl → purge-errors → (ocr scanned later)
```

## 5. Implementations
- `scripts/inventory.py` · `clean-corpus.py` · `extract-html.py` · `extract-pdf.py`
- `to-markdown-jsonl.py` · `classify-errors.py` · `purge-errors.py` · `ocr-scanned-pdfs.py`

## 6. Docs
- `docs/01-corpus.md` · `docs/02-extraction.md`
- `specs/SPEC-00-INFRA-BUILD.md`

## 7. Current state
`DONE` (see `STATE.yaml`). 425 clean docs, versioned, R2-backed. Open: OCR the 8 scanned PDFs.
