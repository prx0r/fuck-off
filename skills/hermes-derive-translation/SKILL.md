---
name: hermes-derive-translation
description: "Derive a real from-scratch translation of a Sanskrit karika (and commentary-lift) using Hermes as the generation kernel, then compute TranslationProof with .py. Use for the canonical translation moat — Hermes produces, ip-graph validates."
version: 1.0.0
author: agentgraph (ip-graph)
metadata:
  hermes:
    tags: [hermes, translation, sanskrit, proof, validation]
    related_skills: [hermes-generate-reduce, hermes-derive-enquiry, hermes-derive-essay]
    checkpoint: translation DERIVED by Hermes from the real Sanskrit, proof computed on real output
---

# Derive a Translation (Hermes) + Validate (TranslationProof)

## When to use
- Translating a Sanskrit kārikā from scratch (the moat).
- Producing a commentary-lift (B3 gloss → B4 commentary reaching the philosophical frame).
- Any place `TranslationProof` needs a REAL model output, not hand-filled fields.

## The flow
1. **GENERATION:** Hermes translates the verse (agentic, reads the repo/skills). Output JSON:
   `{"translation":"...","terms":{"term":"sense"},"contested":"..."}`.
   See `lib/hermes_exec.translate_karika()` for the reference.
2. **REDUCTION (.py):** compute the 11-dimension `TranslationProof` on that REAL output
   (`lib/translation.py`) — never hand-fill from bool().

## The canonical orchestration rule
The ORCHESTRATOR is patala's deterministic `factory_scheduler.py` DAG (T1→ARGMAP→L0→L2→L200→C1);
Hermes is the **generation kernel only**. ip-graph VALIDATES (TranslationProof / three-version /
commentary_lift). Do NOT build a parallel per-verse runner.

## Reference
`lib/hermes_exec.py` · `lib/translation.py` · `tantraloka/CANONICAL-TRANSLATION-ORCHESTRATION.md`
