---
name: hermes-generate-reduce
description: "The core ip-graph execution pattern: HERMES for GENERATION, .py for REDUCTION. Use for any work where a model must derive structure from real source text (enquiry-discovery, essay anatomy, translation, commentary, cruxes) and a deterministic kernel must then validate/aggregate it."
version: 1.0.0
author: agentgraph (ip-graph)
metadata:
  hermes:
    tags: [hermes, execution, generation, reduction, anti-theatre, patala]
    related_skills: [hermes-derive-enquiry, hermes-derive-essay, hermes-derive-translation]
    checkpoint: the object under test is DERIVED from real data by the model, then reduced by .py
---

# Hermes for Generation, .py for Reduction

## The rule (non-negotiable)

> **HERMES for GENERATION. `.py` for REDUCTION.**
> - GENERATION (translation, commentary, essays, cruxes, enquiry-discovery, new pushing) → `hermes chat` (agentic).
> - REDUCTION (review, staleness, evidence, gates, epistemic, aggregation, validation) → deterministic `.py`.

Never fake generation with regex or hand-fed literals. A validator is REAL only if the object it
validates is **DERIVED from the data by the model**, then reduced by Python.

## Why (the failure this prevents)

Blind `hermes -z` is a one-shot text model with **no file access** (~3.8% yield on translation). The
regex/parse path silently hand-feeds or pattern-matches instead of deriving. Both are THEATRE. The
correct path: **Hermes reads the real file itself (it has full filebase access) and derives**, `.py`
reduces.

## How to call (the wrapper)

`lib/hermes_exec.py` — agentic `hermes chat`, runs through the **patala profile** (skills + MCP load):

```python
from hermes_exec import agentic
out = agentic(system, user, cwd="<repo>", max_turns=8)   # model text
# then .py parses/validates/aggregates `out`
```

- Model + provider passed explicitly (`-m deepseek-v4-flash --provider opencode-go`), never rely on `HERMES_MODEL`.
- **Hermes has full read/edit filebase access** — pass FILE PATHS, let Hermes read them itself. Do NOT
  stuff file contents into the prompt (that is the blind-`-z` mistake; blows ARG_MAX, hides context).
- You can delegate real work: Hermes can read + generate + WRITE files; `.py` gates the result.

## The reduce step (always)

After Hermes returns, `.py` must:
1. Extract the final JSON robustly (last brace-balanced object — the agentic output has reasoning + answer).
2. Validate the shape.
3. Feed the derived object into the real kernel (`enquiry.EnquiryDiscovery`, `essay_ingest.EssayIngestor`, ...).
4. Record provenance (method = hermes vs fallback) — never claim more than happened.

## Worked examples in this repo
- `scripts/ingest-logicvid-gold-enquiry.py` — Hermes derives DiscoveryProgressions from the LOGICVID gold.
- `scripts/validate-essay-ingest.py` — Hermes reads the real Ratié book and derives the essay anatomy.
- `scripts/validate-provenance.py` — .py REDUCTION over real graph data (no hand-fed literals).

## Where Hermes is applicable (more places to apply)
- Translation (the canonical path uses Hermes as the generation kernel only — `patala factory_scheduler`).
- Commentary / commentary-lift (B3 → B4 reaching the philosophical frame).
- Crux mining (the pushing-miner crux compass — Hermes reads pushing sessions).
- Enquiry-discovery (LOGICVID gold → taxonomy/theorem/boundary/frontier).
- Essay anatomy / essay-as-derivation-input.
- New question generation (the question-growth engine target).
