# VISION — THE SELF-PROVING SYSTEM (the OS that can prove why it is the way it is)

*2026-08-14. Grounded in our validated capabilities: EXPERIMENT-MATRIX (maps experiment→repo→vision→layer),
nanopub provenance (portable, signed), signed Merkle roots (tamper-evident), schema compiler
(single-source), knowledgeProvenance (multi-source assertions), the docs/axioms themselves.*

---

## THE EMERGENT SYNERGY

We already track, in a machine-readable matrix, which repo contributed which mechanism, which paper
justified which design, which experiment validated which law. And we have the machinery to sign + version
any object. **Nobody has combined these into the system auditing its own construction.**

## THE IDEA

> **A system that can produce a signed, verifiable provenance record of ITS OWN code, design decisions,
> and reasoning** — so every behavior resolves to a claim with evidence, exactly as it does for the
> scholarship it manages.

Concretely:
```
"why does the reducer block promotion?"
  → resolves to: herdr-workflow (source) + experiment-herdr-review (evidence) + the
    epistemic invariant (reason) — all signed + versioned
```

## WHY THIS IS THE DEEPEST LONG-TERM MOAT

Every other moat (corpus, ontology, data) can eventually be copied or scraped. **A system's
self-provenance cannot be copied** because it's the *history of its own construction* — the decisions,
the evidence, the validated experiments, the reasons. It's like the difference between a painting and
the *provenance chain* that proves it's authentic — except here the "painting" is the whole system and
the provenance is machine-verifiable.

Three compounding properties:
1. **Verifiability** — you can ask "why is X the way it is?" and get a signed, evidence-backed answer.
2. **Trust-by-construction** — the system is auditable top to bottom; it doesn't *ask* you to trust it,
   it *shows* you why.
3. **Self-improving** — as it evolves, every change adds to the provenance chain, making the whole
   system *more* auditable over time, not less.

## THE FLYWHEEL

```
  every decision signed + evidence-backed → system is fully auditable
        ↑                                            ↓
  more confidence → more adoption → more use → more decisions made
        ↑                                            ↓
  richer provenance chain ← every new decision adds evidence
```

The flywheel is **trust compounding on itself**: each verified decision makes the system more
trustworthy, which attracts more use, which produces more decisions, which thickens the provenance.

## THE FUTURE MOAT (given where AI is going)

As AI systems become ubiquitous, **the distinguishing question becomes "can I trust this system — and
can it prove why it deserves trust?"** A self-proving system is the answer:

- **For agents**: they can *verify* the substrate they build on (trust-by-construction).
- **For humans**: they can *audit* the reasoning (no black box).
- **For the system itself**: it applies its own epistemic machinery to its own design — the ultimate
  dogfood, and the strongest proof the machinery is real.

## THE NOVEL MECHANISM: "DESIGN-PROVENANCE NANOPUB"

A concrete mechanism: every design decision is itself a claim, exported as a nanopub:

```
design_nanopub {
  decision: "reducer blocks promotion until evidence",
  derived_from: [herdr-workflow@sha, epistemic-invariant@sha],
  evidence: [experiment-herdr-review@result, mutation-testing@killrate],
  review: [cross-review@consensus, human-adjudication@id],
  signed: {root: merkle, cert: scholar-review-certificate},
  timestamp: ...,
  supersedes: <prior design decision>
}
```

The EXPERIMENT-MATRIX already gives us the `derived_from` + `evidence` links. We add signing + the
supersession chain, and the system becomes self-proving.

## WHY START NOW

- The matrix + nanopub + signed-root machinery are **already built** — this is composition, not invention.
- It's the **only moat that compounds purely through continued activity** — every decision you make
  today becomes part of the un-copyable provenance chain.
- It makes patala itself the **first complete application** of the Verified Epistemic OS.

## WHAT TO BUILD NEXT

1. **`lib/design_provenance.py`** — turn design decisions + the experiment matrix into signed nanopubs.
2. **The self-audit experiment** — pick 3 of our own design decisions, emit their provenance nanopubs,
   and verify they resolve (like any scholarly claim).
3. **The trust-by-construction demo** — "why does the reducer block?" resolves to a signed evidence chain.

See `docs/vision/VISION-UNCONSIDERED-FRONTIERS.md` (VISION F system self-provenance) + the
EXPERIMENT-MATRIX + signed-corpus experiments — this vision makes self-provenance the compounding moat.
