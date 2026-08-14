# SPEC-18 — COMPLETE PIPELINE BUILD (the Pāṭala products)

*2026-08-14. Synthesizes SPEC-15 (Scholar Review), SPEC-16 (Translation), SPEC-17 (GitHubs/textual)
into the complete, implementable pipeline + products. Built from the surveys' frontier insights.
Each product maps to a layer and is validated by `scripts/validate-products.py` (11/11 pass).*

---

## THE ONE PIPELINE (all three surveys converge on one kernel)

```text
                    PĀṬALA CANONICAL KERNEL
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
 TEXTUAL SUBSTRATE    EPISTEMIC SUBSTRATE   WORK SUBSTRATE
 Text-Fabric (slots)  Eigenius (ceilings)   Hermes/Herdr
 CTS (identity)       nanopub (provenance)  Task/Run/Event
 SARIT/TEI            PROV-K
       │
       ▼  OCR/HTR: Kraken · eScriptorium
   Witness → Reading → Passage
       ▼  Vidyut (Sanskrit mechanics)
   TranslationProof          ← LIB/build (Layer 03)
       ▼
   Claim → Argument → Evidence → Crux   ← schema-compiled (Layer 00)
       ▼  xAIF · nanopub · RO-Crate
   REVIEW (adversarial panel + citecheck)  ← LIB/build (Layer 08)
       ▼
   ACCEPTED SCHOLARLY OBJECT
       ▼
   PROJECTION COMPILER (HTML · JSON · SQLite · TEI · API · MCP)
       ▼
   AGENTS → EDUCATION COMPILER (Engram-style)
```

---

## The three products, built

### PRODUCT 1 — TranslationProof (Layer 03) — `lib/translation.py` ✓ VALIDATED

**The frontier move (SPEC-16):** NO single aggregate score. A vector:
```text
SOURCE_COVERAGE 0.99 · TARGET_GROUNDING 0.96 · MORPHOLOGY PASS · SYNTAX PASS
NEGATION PASS · MODALITY PASS · TERM_CONSISTENCY WARN · ENTAILMENT WARN
XCOMET PASS · PARALLEL_WITNESS CONFLICT · HUMAN_REVIEW PENDING
```
**Publication gate:** `BLOCKED` unless all hard dimensions PASS; reason is dimension-specific
(`PARALLEL_WITNESS_CONFLICT`), not a mushy score.

**Proof generators (from SPEC-16):** ByT5-Sanskrit, Sanskrit Heritage, Vidyut, + skrutable.
**Auditors (intentionally redundant):** xCOMET, GemSpanEval, OTTAWA (omission/addition), entailment,
term consistency, MQM error vocabulary. No single one decides.

### PRODUCT 2 — Adversarial Scholar Review (Layer 08) — `lib/scholar_review.py` ✓ VALIDATED

**The frontier move (SPEC-15):** review as auditable *process*, not a score.
- **Adversarial panel** — N independent reviewers debate; a judge delivers the verdict.
- **Anti-groupthink** — dissent is reported, never forced into consensus.
- **CiteCheck** — every citation verified; phantom/hallucinated citations flagged (SPEC-15 §19).
- **Findings lifecycle** — OPEN → RESOLVED/REJECTED/OPEN_CRUX; open cruxes never hidden.
- **Reviewer-of-reviewer** is required (not optional) + security (peer review is gameable — audit it).

### PRODUCT 3 — Schema Compiler (Layer 00) — `lib/schema.py` ✓ VALIDATED

**The frontier move (SPEC-17 §15):** one YAML schema source → compiled validators. Kills the
SCHEMA-AUDIT divergence (claim/evidence/argument defined once).
- Canonical schemas for claim/evidence/argument with `epistemic_ceiling` enums.
- Full Stencila would also emit TS/Python/Rust/JSON-LD bindings + C2PA Content Credentials (signed
  provenance distinguishing *provenance integrity* from *scientific correctness*).

---

## The textual substrate (SPEC-17) — to build next

**Text-Fabric pattern:** `TextPosition` is the primitive; annotation layers (word/lemma/sentence/
entity/variant/syntax) reference it. Don't make every annotation own text. This is our L0 substrate.
- **CTS/CapiTainS** for citable passage identity.
- **Saktumiva** for witness/variant/collation.
- **SARIT/TEI** as the Indic compatibility target.
- **Vidyut** for Sanskrit mechanics (do not rebuild).

---

## Validation status
| Product | Kernel | Layer | Validation |
|---------|--------|-------|-----------|
| TranslationProof | `lib/translation.py` | 03 | ✓ 5/5 (vector + gate) |
| Scholar Review | `lib/scholar_review.py` | 08 | ✓ 4/4 (panel + citecheck) |
| Schema Compiler | `lib/schema.py` | 00 | ✓ 2/2 (single-source) |
| **run-tests.py now 11/11** | | | validate-products added |

## Build order (from the surveys' highest-value discoveries)
1. ✅ TranslationProof + Scholar Review + Schema Compiler (this spec, validated)
2. Text-Fabric textual substrate (TextPosition primitive) — next
3. Stencila full schema→bindings compiler
4. Engram education compiler (dependency learning)
5. Datasette read-plane + RO-Crate publication

## Highest-value discoveries to adopt (SPEC-17)
Text-Fabric (textual substrate) · Stencila (schema+provenance) · Saktumiva (collation) · Engram
(education) · Gallant toolkit (literature review) · Datasette (read-plane) · RO-Crate (publication) ·
PROV-K/knowledgeProvenance (provenance) · CapiTainS/CTS (identity) · TeamTat (adjudication).

See `docs/process/FRONTIER-MAP.md` for the per-layer tracking.
