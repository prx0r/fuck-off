# THE ORGANISM OPERATING MODEL — how it grows, teaches, ingests, publishes, and stays durable/secure

*2026-08-14. A zoom-out on the Verified Epistemic Organism as a LIVING system (patala v3 framing, now
made concrete against everything we actually built). This is the operating manual: how the organism
evolves with consumers, teaches, auto-ingests Sanskrit, translates, publishes essays — all tracked,
versioned, agentic, durable, and secure. Grounded in the kernels + SPECs, not aspiration.*

---

## THE ONE PICTURE — the organism has a circulatory system

```text
        ┌──────────────────────────── INGEST (the food) ────────────────────────────┐
        ▼                                                                           │
  Sanskrit work → R2 Bronze → SOURCE → Tokenization(vidyut) → DraftTranslation      │
        → Translation → TranslationProof → Commentary → Argument → Synthesis        │
        │                                                                           │
        ▼                                                                           │
  ┌─ THE EPISTEMIC GATE (the immune system) ─────────────────────────────────────┐ │
  │  epistemic(ceiling) · review(herdr) · scholar_review(citecheck) ·            │ │
  │  evidence_ledger(typed+kind) · integrity_gate(tri-state+primary) ·           │ │
  │  verification_ensemble(RefChecker+GraphCheck) · translation_variant(3-ver)   │ │
  └──────────────────────────────────┬───────────────────────────────────────────┘ │
        │                            │                                              │
        ▼ projection compiler        ▼ read plane                                  │
  Context bundles ──────────→ Astro/JSON-LD (humans) · bundles/MCP (agents)        │
        │                                                                           │
        ▼                                                                           │
  ┌─ THE ORGANISM LOOP (the senses — growth) ───────────────────────────────────┐   │
  │  consumers probe → MisconceptionGraph → confusion=research signal            │   │
  │  → next_action (calculate) → DeliveryLoop (budget+human gate)                │   │
  │  → source-repair → RKA propagate → better teaching → more learners           │──┘
  └──────────────────────────────────────────────────────────────────────────────┘
        │
        ▼ self-prove + sign (Vision F)
  system_provenance · certificate · signed Merkle root · evidence ledger
```

**The one law that makes it an organism, not a database:** *learners are sensors* (SPEC-21). Their
attempts to understand become measurements of the research object itself. The consumer loop feeds BACK
into the graph — that closed edge is what makes it a living organism.

---

## 1. HOW IT AUTO-INGESTS + TRANSLATES (the food → the spine)

The primary-source spine (`migration/v2/LAYERS.yaml` + `INGESTION-ARCHITECTURE.md`):

| Step | Kernel | Status |
|------|--------|--------|
| Source → R2 Bronze (fingerprinted) | `source_registry.py` (fojin pattern) | BUILT |
| Tokenization (L0, SLP1 via vidyut) | `vidyut_l0.py` | BUILT (9/9) |
| Translation | `translation.py` (draft) | BUILT |
| **TranslationProof** (non-aggregate, the moat) | `translation.py` + `translation_variant.py` | **PROVEN** |
| Commentary | (passage-local) | **NEEDS-BUILD** |
| Argument → Crux → Synthesis | `review.py` + crux-compiler | PROVEN |

**Key doctrines:**
- **Proof-carrying, not equivalent** (GEM 5.4): a translation can't be *proven equal* to the source, but it CAN be made **proof-carrying** — an 11-dim vector (`SOURCE_COVERAGE … HUMAN_REVIEW`), gate BLOCKS on any failing hard dim, never a scalar. (SPEC-16)
- **Three-version = scholarship** (GEM 5.1, `translation_variant.py`): N independent translations → where they agree is the HARD CORE, where they differ is the interpretation-space, the adjudication is the commentary. Honest pairwise-Jaccard score, not a vibe.
- **Source-vs-reception KORAL separation**: the reality graph (source) is never corrupted by interpretation (Ratié). `epistemic.py` enforces `authority(projection) <= authority(parent)`.
- **Intermediate representation** (SPEC-16): Sanskrit → morphology → ANVAYA (canonical prose order) → semantic propositions → English. (Not yet a kernel — a gap.)

---

## 2. HOW IT PUBLISHES ESSAYS (the reproductive system)

`lib/essay_ingest.py` — the 9-stage essay-as-derivation-input pipeline (each stage a proven kernel):
structure(schema) → mine claims(epistemic) → evidence(source_registry) → argument(AIF) → crux →
review(scholar_review+citecheck) → organism → pedagogy → **reactive**.

**Reactive documents (Law 7)** are the reproductive mechanism: prose is compiled from epistemic objects
with a dependency manifest (`Paragraph P7 depends_on [C18, C22, ARG9, E71]`). A source retraction
propagates `E71 STALE → C22 STALE → ARG9 STALE → P7 STALE → essay section 3 NEEDS_REBUILD`. **Prose is a
projection that recompiles; it never silently contains a refuted claim.**

---

## 3. HOW IT TEACHES + GROWS WITH CONSUMERS (the senses + reproduction)

**The teaching loop (SPEC-20/29, the motherlode):**
```
epistemic graph → LearningClaim → compile_interactions() → LearningPacket
   → learner answers → MasteryEvidence → mastery_reducer() → LearnerState
   → next_interaction() (targets the WEAKEST skill) → repeat
```
- **`wrong_answer_to_neighbor` is THE moat** (SPEC-23): a wrong answer resolves to a *known epistemic
  neighbor* (rival_proposition, scope_inflation, defeated_inference…), never an LLM-invented distractor.
  Unscrapeable + self-improving + domain-portable.
- **Education is a projection of the graph**, never a separate KB (SPEC-20). Every LearningClaim resolves
  downward to canonical objects.

**The co-evolving flywheel (SPEC-21/23, the deepest synergy — how it GROWS):**
```
more learners → more structured misconception data → sharper ambiguity detection
      ↑                                                       ↓
better explanations ← repaired sources ← scholars fix what learners reveal
      ↑                                                       ↓
more learners understand ← better teaching from repaired sources
```
- **MisconceptionGraph** with magic edges `Confusion──misreads──Claim · Objection──attacks──Premise ·
  Question──about──Concept`.
- **The repair cascade is the missing piece**: `MisconceptionLikelihood = f(cluster_size, persistence,
  ambiguity_signal, novice_rate)` → cross threshold → source flagged for scholar review → RKA propagates
  the fix → confusion measured to dissolve. *This kernel (`misconception.py`) is the biggest unbuilt
  gap — the flywheel's closing edge.*
- **Anti-indoctrination safeguard**: priority = α(demand) + β(epistemic importance) + γ(scholar) +
  δ(graph impact); repeated failure tests "is pedagogy bad? OR is the claim bad? OR is the source
  ambiguous?" (users = falsification pressure, not cheerleaders).

---

## 4. HOW IT DECIDES + STAYS AGENTIC (the nervous system)

**`next_action.py` (GEM 12.3)** — the deterministic scheduler: `P(v) = w1·D + w2·B + w3·U + w4·Q + w5·R − w6·C`
(downstream load, betweenness, uncertainty, question demand, review deficit, minus cost). **CALCULATES,
not LLM-guesses** what the organism works on next. All 6 inputs feed from other kernels.

**`agent_delivery.py`** — the gated delivery loop:
- `TaskContract` (maestro) + `RunBudget` (token/tool-call governor, the safety cap) + `ContextRoute`
  (loom context routing).
- Output is always a **proposal** with `gate="BLOCKED"`; **`human_authorize()` is the ONLY path to
  canonical truth** (herdr). Machines propose, reducers gate, humans adjudicate.

---

## 5. HOW IT STAYS DURABLE + VERSIONED + SECURE (the skeleton + skin)

**Durable:**
- **Staleness = the dependency graph** (SPEC-13): correctness (blast-radius), performance (incremental
  rebuild), and retrieval are ONE traversal. A change flags every dependent → review_queue → rebuild.
- **Temporal truth (Law 4)**: accepted state reduces to a **signed Merkle root**; what was accepted at
  any past time is replayable (`valid_at/invalid_at` + episodes).
- **Content-addressing (SHA-256)** everywhere: immutable versioned URLs (`/concept/free-will/v17` →
  `logical_id → version → sha256 → R2 object`), ETags, dedup.

**Secure / trustworthy:**
- **`integrity_gate.py`** (EleutherIA): tri-state `CLEAN/DEMOTED/EXCLUDED` persisted + **enforced at
  retrieval** (excluded never reaches the agent); **primary-source hard gate** — a synthesis needs ≥1
  CLEAN primary citation or it FAILS.
- **`evidence_ledger.py`** (GEM 6.5 + fojin): typed evidence events + `confidence_kind` — **incomparable
  numbers are never compared** (an import_flag "1.0" is NOT an expert "1.0").
- **`system_provenance.py`** (Vision F): the OS signs its OWN kernels — `why(reducer)` resolves to
  experiment+layer+vision; tamper-detect; signed Merkle root. **The project is the first complete
  application of the OS.**
- **`certificate.py`**: Certification Weight (kill×consensus×load×time) — the marketplace economics.

---

## 6. THE HONEST GAP (what's the flywheel waiting for)

**The organism's machinery is real (71/71 tests, 34 PROVEN on real data).** The honest gaps:

1. **`misconception.py` repair cascade** — the flywheel's closing edge (misconception → source-repair)
   is the biggest unbuilt piece. The loop is *conceptual*, not wired.
2. **BKT/FSRS pedagogical policy** — `next_interaction()` is a weak heuristic, not the full
   DISCOVER/LEARN/PRACTICE/STUDY engine.
3. **The 3 needs-build products**: Commentary, Tokenization (full vidyut cheda), Essay projection.
4. **Gaps A-G**: signed HumanAttestation (E, critical for the marketplace), context paging (A),
   content-addressed run-traces (D), workspace isolation (F), local-first nodedb (G), and execution
   branching/replay (B/C — exist as experiments, not wired kernels).
5. **No consumer data yet** — no real learners, so the misconception flywheel's fuel is prospective.
6. **The corpus-wide graduation** — only ONE real IPK claim is proven end-to-end, not a full IPVV pass.

---

## THE DEEPEST ZOOM-OUT

The organism is a **self-referential epistemic instrument** (OWN-VISION-MAP): it consolidates its own
knowledge, tests its own foundations, learns from its own learners, defends its own positions, traces
its own history, and proves its own construction. The read plane made it *servable*; the GEM builds
(source_registry, integrity, evidence_ledger, flywheel, next_action, vidyut) made it *durable + secure +
agentic*. 

**What would make it complete:** close the 3 loops (misconception→repair, BKT/FSRS policy, corpus-wide
graduation) and wire gaps A-E. Then the organism is a genuinely **self-improving, self-trusting,
self-proving, self-teaching** system that grows with every learner and every source it ingests.

## Proofs / resolution
- Teach/grow: `lib/{education,pedagogy,organism,organism_loop}.py` + SPEC-20/21/23/28/29
- Ingest/translate/publish: `lib/{translation,translation_variant,essay_ingest,vidyut_l0,source_registry}.py` + SPEC-16/17/18/19
- Agentic/durable/secure: `lib/{next_action,agent_delivery,staleness,integrity_gate,evidence_ledger,system_provenance,certificate}.py` + SPEC-13/32
- Vision: `docs/vision/VISION-VERIFIED-EPISTEMIC-OS.md`, `OWN-VISION-MAP.md`, `docs/vision/beyond-patala/`
