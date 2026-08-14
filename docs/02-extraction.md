# 02 — EXTRACTION (text pipeline)

*Turning the raw corpus into plain text + markdown + one JSONL. Ground truth verified 2026-08-14.*

## Pipeline

```text
raw/ (HTML+PDF)
  → extract-html.py   (HTML → clean text)
  → extract-pdf.py    (pdftotext → text; 8 scanned flagged)
  → data/extracted/        (plain .txt per doc)
  → to-markdown-jsonl.py   (txt → markdown + corpus.jsonl)
  → classify-errors.py + purge-errors.py  (quarantine error pages)
  → data/extracted_md/ + data/corpus.jsonl
```

## Outputs (ground truth)

| Output | Count | Location |
|--------|-------|----------|
| Plain text | 425 | `data/extracted/{html,pdf}/` |
| Markdown (active) | 426 | `data/extracted_md/{html,pdf}/` |
| Quarantined error pages | 24 | `data/extracted_md/_errors/` |
| Machine corpus (versioned) | 425 | `data/corpus.jsonl` |

> Note: 426 active md vs 425 corpus records — the extra 1 is an `index` page that exists as markdown
> but is excluded from the corpus (it's a navigation index, not a document).

## The 8 scanned PDFs (need OCR — deferred)

No text layer; `pdftotext` yields nothing. Use `scripts/ocr-scanned-pdfs.py` (`ocrmypdf --force-ocr`):
- `introduction/Stapp_Copenhagen_Interpretation.pdf`
- `solutions/Culverwell1890.pdf`
- `solutions/Culverwell1894.pdf`
- `solutions/Quantum_Mechanics_Thermodynamics_Strong_Cosmological_Principle.pdf`
- `solutions/Sperry1966Chicago.pdf`
- `solutions/Watson_Behaviorism.pdf`
- `solutions/Wheeler.pdf`
- `solutions/gabor1946.pdf`

## Related
- Scripts: `extract-html.py`, `extract-pdf.py`, `to-markdown-jsonl.py`, `classify-errors.py`,
  `purge-errors.py`, `ocr-scanned-pdfs.py`
