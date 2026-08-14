# INGESTION — source texts vs essays, and essays-about-source (the full picture)

*2026-08-14 · How we ingest THREE related things, and how they relate: (A) a huge source text (e.g.
IPVV, Tantrāloka), (B) an essay ABOUT a source (Ratié's *Le Soi et l'Autre* on the IPVV), (C) a
standalone essay. Each enters at a DIFFERENT layer and references the others through our existing
kernels. This is the full ingestion architecture.*

---

## THE THREE INPUT TYPES AND WHERE THEY ENTER

```text
(A) SOURCE TEXT (primary)          → enters at Layer 0-4 (raw → tokenization → claims)
    IPVV · Tantrāloka · the passage corpus
        │  this is the GROUND TRUTH (reality graph, KORAL)
        │
(B) ESSAY ABOUT A SOURCE (secondary) → enters at Layer 6 (commentarial) / Layer 5 (argument)
    Ratié on the IPVV · Torella on the Tantrāloka
        │  references the source's passages as EVIDENCE
        │  this is the INTERPRETATION (literature graph, KORAL)
        │
(C) STANDALONE ESSAY (scholarship) → enters at Layer 4-6 (argument/commentarial)
    a scholar's independent argument
        │  may reference multiple sources
        │  interpretation, not primary
```

**The KORAL two-graph rule (already proven):** the reality graph (A) and the literature graph (B/C)
are SEPARATE. An interpretation NEVER corrupts the primary source. A doctrinal reinterpretation flags
the interpretation, not the source.

---

## (A) HOW A HUGE SOURCE TEXT INGESTS

A large source text (thousands of passages) does NOT go through the essay-ingest stages. It uses the
**primary-source pipeline** (patala v2 LAYERS.yaml):

```text
Source (Bronze on R2, fingerprinted)
  → Tokenization (L0: the token floor — needs Vidyut)
  → DraftTranslation → Translation → TranslationProof (the non-aggregate vector)
  → Commentary (passage-local)
  → Argument (propositions → arguments → cruxes)
  → Synthesis
```

**The distinction:** a source text is the **ground truth** — its claims get SCHOLARLY_CORROBORATED by
the text itself. It's ingested vertically (raw → proof), each passage a node. This is the patala v2
spine; our `epistemic.py` + `translation.py` + `staleness.py` kernels are the substrate.

---

## (B) HOW AN ESSAY-ABOUT-A-SOURCE INGESTS (the key case)

An essay about the IPVV (Ratié) is **secondary scholarship**: its claims REFERENCE the primary
passages. It enters at the **commentarial layer (L6)** and its relationship to the source is:

```text
ESSAY (Ratié Ch4, IPK 1.5.11)
  │  claim: "experience is not construction"     ← this is Ratié's reading
  │  evidence: [IPK 1.5.11 passage]              ← references the SOURCE as evidence
  │  ceiling: SCHOLARLY_CORROBORATED (her reading, well-sourced)
  ▼
SOURCE passage (IPK 1.5.11)                       ← the GROUND TRUTH (reality graph)
  │  ceiling: SCHOLARLY_CORROBORATED (the text itself)
```

**The essay-ingest pipeline (ESSAY-INGEST.md) applies** — but with one crucial addition: every claim's
`evidence` links to a **SOURCE passage**, not just an essay chapter. The essay's claims are
`derived_from` source passages + reviewed against them (the review stage checks the essay's reading
against the primary text — does Ratié's claim actually follow from IPK 1.5.11?).

**The KORAL rule bites here:** Ratié's interpretation lives in the literature graph. If Ratié is
revised or re-read, HER claims are flagged — the source passage (IPK 1.5.11) is NOT corrupted.

---

## (C) HOW A STANDALONE ESSAY INGESTS

A standalone essay (no single source it's "about") enters at the **argument/commentarial layer**:
- mine its claims (with honest ceilings — its thesis is MACHINE_PROPOSED, its verbatim-cited sources
  are corroborated),
- build its argument graph (AIF),
- find its cruxes (internal tensions + cross-scholar tensions),
- review it (adversarial + citecheck — every citation must resolve to a REAL source, or it's a phantom).

It references whatever sources it cites (possibly many) as evidence, but it's not "about" one the way
Ratié is about the IPVV.

---

## THE KEY RELATIONSHIP: how source + essay + essay-about-source fit together

```text
                    SOURCE (IPVV)          ← the reality graph (ground truth)
                       │  ↑
      essay's claims derive_from + are reviewed against source passages
                       ▼  │
              ESSAY ABOUT SOURCE (Ratié)    ← the literature graph (interpretation)
                       │
      essays-about-source can be compared across scholars (claim-standardisation)
                       ▼
              COMPARISON / CRUX / SYNTHESIS ← where scholars diverge = research targets
```

**The full ingestion:** source text (vertical, ground truth) → essays-about-it (commentarial,
referencing source as evidence) → comparison/crux/synthesis (across scholars). Each layer uses the
proven kernels; the KORAL two-graph keeps reality and interpretation honest.

---

## HOW WE USE IT ALL (the pipeline end-to-end)

1. **Ingest the source** (IPVV) → canonical passages + translation proofs (ground truth).
2. **Ingest essays-about-it** (Ratié) → claims mined, evidence = source passages, reviewed against the
   source.
3. **Ingest standalone essays** → claims + arguments + cruxes, reviewed.
4. **Cross-scholar comparison** (`claim-standardisation.py`) → where scholars diverge = cruxes.
5. **The graph grows** — source + interpretations + comparisons, all KORAL-separated.
6. **Reactive** — source correction marks dependent essay claims stale (staleness.py).
7. **The organism + pedagogy** consume the grown graph — learners reconstruct the arguments.

---

## THE DISTINCTION IN ONE LINE

> A **source text** is ingested vertically as ground truth (raw → proof). An **essay about a source**
> is ingested at the commentarial layer, its claims deriving from + reviewed against the source's
> passages (KORAL-separated). A **standalone essay** enters at the argument layer. All three feed the
> same graph — and the KORAL two-graph keeps primary truth from being corrupted by interpretation.

## Proofs
- Essay ingest: `validate-essay-ingest.py` (8/8 on Ratié).
- Source/interpretation separation: `experiment-koral-twograph.py`.
- Claim ceilings: `validate-stack.py` (SOURCE vs INTERPRETATION distinct).
- Cross-scholar: `experiment-claim-standardisation.py`.
