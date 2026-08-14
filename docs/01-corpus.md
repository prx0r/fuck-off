# 01 — CORPUS (the source data)

*The cleaned informationphilosopher source corpus. Ground truth numbers verified 2026-08-14.*

## The corpus reality

The scraped site is ~97% broken HTML. The real value is the PDF library.

| Type | Raw count | Real content | Notes |
|------|-----------|--------------|-------|
| HTML | 1896 | 44 files in `data/raw/html_articles/` | 788 unique error pages quarantined in `data/raw/errors/` |
| PDFs | 437 | 419 in `data/raw/pdfs/` | the real value — curated primary papers |
| Images | 522 | 502 in `data/raw/images/` | supporting |

**Ground-truth usable corpus: 425 documents** (`data/corpus.jsonl`):
- 6 html + 419 pdf = 425
- Each record: `{id, title, kind, section, docname, text, version, layer, created_at}`

## Where things live

```
data/raw/            cleaned source
  html_articles/       real HTML (44 files), by section
  pdfs/                the PDFs (419), by section
  images/              images (502)
  errors/              quarantined error pages (788)
  MANIFEST.json        classified inventory
data/corpus.jsonl     ONE machine-readable corpus (425 records, versioned)
```

## The PDF library (the gold)

`data/raw/pdfs/solutions/` (most of the 419) is a primary-source library: Einstein, Bell, Bohm, Bohr,
Planck, Schrödinger, Mermin, Turing, Dennett, Sperry, Deacon, Landauer, Wheeler + free-will
philosophers (Kane, Mele, Strawson).

## Related
- Build: `scripts/clean-corpus.py` → `data/raw/`
- Docs: `04-ontology.md` (the concept vocab)
- Backup: R2 `r2:atlas-sources/informationphilosopher/`
