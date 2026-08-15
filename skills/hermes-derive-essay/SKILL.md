---
name: hermes-derive-essay
description: "Derive the essay anatomy (sections, argument moves, IPK refs) from a real scholarly book text using Hermes, then reduce with essay_ingest.EssayIngestor (the 9-stage pipeline). Use for essays-as-derivation-input on real sources like Ratié."
version: 1.0.0
author: agentgraph (ip-graph)
metadata:
  hermes:
    tags: [hermes, essay, ingest, derivation, patala, raite]
    related_skills: [hermes-generate-reduce, hermes-derive-enquiry]
    checkpoint: essay anatomy DERIVED by Hermes from the real book text, not hand-fed/regex
---

# Derive Essay Anatomy from a Real Text (Hermes-driven)

## When to use
- Ingesting a real scholarly essay/book as derivation-input (essays-as-derivation-input).
- Building an `EssayIngestor` from a real source (e.g. Ratié, *Le Soi et l'Autre*).

## The flow
1. **GENERATION:** Hermes reads the REAL book text (it has file access — pass the path, don't stuff
   contents) and outputs strict JSON anatomy:
   ```json
   {"title":"...","author":"...","sections":[
     {"id":"...","chapter":"...","ipk_refs":["1.2.1-2"],
      "argument_move":"thesis|rival|support|conclusion","text":"short theme"}]}
   ```
   Derive every field from the real text; empty `ipk_refs` if a chapter has none (never fabricate).
   Cover intro + chapters + conclusion.
2. **REDUCTION (.py):** extract JSON → `essay_ingest.EssayIngestor.structure(...)` → run the 9 stages
   (schema → mine claims → evidence → argument → crux → review → pedagogy → reactive).

## Anti-theatre
The anatomy must be DERIVED BY THE MODEL from the real book. No hand-fed chapter dicts, no regex parse.

## Reference implementation
`scripts/validate-essay-ingest.py` reads `recognition/books/Le-Soi-et-l-Autre-Ratie-2011.txt` (2.5MB French).
