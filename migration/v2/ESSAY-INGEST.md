# ESSAY-INGEST — the deep architecture (essays as derivation input)

*2026-08-14 · How we structure essay ingest, and WHY each stage uses the kernel it does. This is the
design reasoning, not just the mechanism. The essay is NOT read — it is ingested through our existing
epistemic pipeline, becoming canonical objects. `lib/essay_ingest.py` + `validate-essay-ingest.py`
prove it on real Ratié data (8/8).*

---

## THE CORE DECISION: essays go through the pipeline, not a separate reader

A scholarly essay (Ratié, Torella, Dyczkowski) is a **dense bundle of machine-derivable objects**:
thesis-moves, source-cited claims, argument moves, scholar disagreements (cruxes), verbatim quotes.
Treating it as "text to read" wastes 90% of it. Treating it as **derivation input** means every stage
uses a PROVEN kernel we already built — no new essay machinery, just wiring.

**The reasoning:** we already proved (with theatre proofs) that our kernels handle claims, arguments,
evidence, review, cruxes, pedagogy. An essay is just a *structured bundle of those objects*. So essay
ingest = **the pipeline applied to a structured document**, not a new subsystem. This is the "one
graph" principle: scholarship, benchmark, education, assessment all derive from the same objects.

---

## THE 9 STAGES (each → kernel → why)

### STAGE 0 — Source
- **Kernel:** corpus ingestion (R2, `01-corpus.md`)
- **Why:** raw essay (Ratié txt/pdf) → Bronze on R2, fingerprinted (incipit/explicit/hash). Same as any
  source. The essay is a *publication*, not an epistemic verdict — its ceiling is set by later stages.

### STAGE 1 — Structure (schema-compile the anatomy)
- **Kernel:** `lib/schema.py` (the single-source schema compiler)
- **Why:** an essay has a known anatomy (book → chapters → sections → IPK kārikās → argument-move).
  We schema-compile that anatomy once, then validate any essay against it. This is the anti-theatre
  contract: an essay that doesn't fit the schema is flagged, not silently parsed. (The Ratié breakdown
  already gives us this anatomy — chapters, sections, IPK refs, "maps to framework.")

### STAGE 2 — Mine claims
- **Kernel:** `lib/epistemic.py` (the envelope)
- **Why:** from each section's argument-move we extract thesis/premise/conclusion claims. The envelope
  keeps **SOURCE-SAYS ≠ SCHOLAR-RECONSTRUCTS ≠ PĀṬALA-INFERS** distinct via `epistemic_ceiling`: a
  verbatim Ratié claim = SCHOLARLY_CORROBORATED; our reconstruction = MACHINE_PROPOSED. This is the
  honest ceiling — we never inflate an essay's thesis into fact.

### STAGE 3 — Evidence
- **Kernel:** `lib/translation.py` pattern + `experiment-signed-statement.py` (signing)
- **Why:** every mined claim carries its verbatim quote + source ref (IPK kārikā, chapter). This is
  grounded, source-linked, and (in production) signed — the same content-addressing we proved. A claim
  without a quote is a phantom (caught at Stage 6).

### STAGE 4 — Argument graph (AIF)
- **Kernel:** `lib/review.py` + `lib/scholar_review.py`
- **Why:** the essay's moves become AIF Info/Inference/Conflict nodes. This is exactly the argument
  structure we proved in `validate-stack.py` (real reducer gates). The essay's thesis → supporting
  moves → the load-bearing premises.

### STAGE 5 — Crux detection
- **Kernel:** `experiment-crux-compiler.py` (minimal divergence)
- **Why:** where scholars disagree (Ratié camatkāra vs Solms pleasure), the crux-compiler finds the
  minimal load-bearing divergence. This is the **honest tension preserved** — the essay doesn't flatten
  disagreement; the machine surfaces it as a first-class crux (research target + comparison unit).

### STAGE 6 — Review
- **Kernel:** `lib/scholar_review.py` (adversarial panel + citecheck)
- **Why:** the mined claims are adversarially reviewed: cross-review (survives only if confirmed),
  citecheck (no phantom citations — every source_ref must resolve to a real chapter/kārikā). This is
  the anti-theatre gate: an essay's claims must be REAL, not invented.

### STAGE 7 — Organism (optional but powerful)
- **Kernel:** `lib/organism.py` + `lib/organism_loop.py`
- **Why:** readers probe the essay-derived graph; their confusions reveal ambiguity in the original
  essay/source. This makes the essay a **living object** — it improves as readers engage, not a dead
  PDF.

### STAGE 8 — Pedagogy
- **Kernel:** `lib/pedagogy.py` + `lib/education.py`
- **Why:** the mined structure (claims, argument moves, crux) IS the pedagogical progression. A learner
  reconstructs the argument the scholar (Ratié) made — the wrong-answer→epistemic-neighbor moat applies
  directly. The essay's structure becomes the curriculum.

### STAGE 9 — Reactive
- **Kernel:** `lib/staleness.py` (blast-radius)
- **Why:** the essay is a **projection** of the source (IPK 1.5.11 etc). If a source kārikā is re-read
  or corrected, the blast-radius marks the essay's dependent sections stale → re-review. This is the
  "executable corrections" principle: scholarship changes → essays update, not silently drift.

---

## THE REASONING SUMMARY

| Stage | Kernel | Why this kernel |
|-------|--------|----------------|
| Structure | `schema.py` | anatomy is a contract, not free text |
| Claims | `epistemic.py` | honest ceilings, SOURCE≠SCHOLAR≠PATALA |
| Evidence | `translation.py`/signing | grounded + signed, no phantoms |
| Argument | `review.py` | AIF, real reducer gates |
| Crux | `crux-compiler` | minimal divergence, tension preserved |
| Review | `scholar_review.py` | adversarial + citecheck |
| Organism | `organism.py` | readers improve the essay |
| Pedagogy | `pedagogy.py` | structure = curriculum |
| Reactive | `staleness.py` | essay is a projection, updates on source change |

**The unifying insight:** every stage reuses a PROVEN kernel. We're not building "essay reading" — we're
applying the pipeline we already have to a structured document. The essay becomes derivation input, and
its content (claims/arguments/cruxes) feeds the same graph that serves review, comparison, research,
education, and the organism. This is the "one graph" principle made literal for the scholarly essay
corpus.

## Proof
- `validate-essay-ingest.py` — 8/8 on real Ratié data (structure→claims→evidence→argument→crux→review→
  pedagogy→reactive).
- `lib/essay_ingest.py` — the kernel.
- Theatre: added to `theatre-check-all.py` (PROVEN on real essay data).
