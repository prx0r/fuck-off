---
name: hermes-derive-enquiry
description: "Derive enquiry-as-discovery structure (taxonomy -> theorem -> boundary -> frontier) from a real LOGICVID gold transcript using Hermes, then reduce with enquiry.EnquiryDiscovery. Use for the missing-gold work: turning live human curiosity into enquiry structure that feeds ontology/claims/gaps/pedagogy."
version: 1.0.0
author: agentgraph (ip-graph)
metadata:
  hermes:
    tags: [hermes, enquiry, logicvid, gold, curiosity, discovery]
    related_skills: [hermes-generate-reduce, hermes-derive-essay]
    checkpoint: DiscoveryProgressions DERIVED by Hermes from the real SPEC-40..48 gold, not hand-fed
---

# Derive Enquiry Structure from LOGICVID Gold (Hermes-driven)

## When to use
- Ingesting the LOGICVID gold (SPEC-40..48, SPEC-36, SPEC-3x-SESSION-Q1) — the live-human-curiosity exemplars.
- Turning an enquiry transcript into taxonomy → theorem → boundary → frontier for the enquiry organism.

## The flow
1. **GENERATION:** Hermes reads each gold transcript (via file path) and outputs strict JSON:
   ```json
   {"topic":"...","taxonomy":{"term":"definition"},"theorem":"...",
    "boundary":["what was NOT established"],"frontier":"the next open question?"}
   ```
   Rules: taxonomy = term distinctions the enquiry reveals (terms NOT equivalent); theorem = the claim it
   actually established; boundary = the honest limit (what it did NOT prove); frontier = the deepest next
   question (ending in ?). If a field is genuinely absent → empty, never fabricate.
2. **REDUCTION (.py):** extract the JSON, build `enquiry.DiscoveryProgression`, add to
   `enquiry.EnquiryDiscovery`, write `data/logicvid/enquiry-gold.json`, record `method` (hermes vs fallback).

## Anti-theatre
The progression must be DERIVED BY THE MODEL from the real gold text. Regex is only an honest fallback
(and each entry records its method). Never hand-feed the presence enquiry.

## Reference implementation
`scripts/ingest-logicvid-gold-enquiry.py` → `data/logicvid/enquiry-gold.json`
