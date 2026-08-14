# GRADUATION — the full organism test is real

*2026-08-14. The P0 milestone (HANDOVER §9 P0) is DONE: **`validate-graduation.py` — 14/14** on real
data. One claim now runs through the ENTIRE organism, and a premise mutation makes the WHOLE system
react. This is the anti-theatre proof that turns the lab into the kernel.*

---

## What was proven

The claim under test is a real one: **"The two-stage model explains free will as chance plus choice"**
(I5), on the real Doyle graph/argument/canonical-DAG. It is run through the whole organism:

| # | Stage | Kernel | What's asserted (REAL) |
|---|-------|--------|------------------------|
| 1 | Ingest | `epistemic.py` | I5 is honestly MACHINE_PROPOSED; ceiling invariant holds |
| 2 | Review | `review.py` + `scholar_review.py` | citecheck runs; thesis held in CORRECTION (not promoted — it asserts a collapse it doesn't prove) |
| 3 | **MUTATE** | `staleness.py` | retract the load-bearing premise I1 (QM indeterminism) → blast radius reaches I5 |
| 4 | Reactive | `staleness.py` | the essay's prose citing I5 is marked STALE; review_queue filed |
| 5 | Pedagogy | `pedagogy.py` | a learner who relied on I5 is re-examined: skill held, misconception recorded |
| 6 | Organism | `organism.py` | the learner's confusion enters the misconception graph (a signal, not noise) |
| 7 | Signed | signing (cosign-style) | the corrected re-release is signed + verifies; tampering detected |
| 8 | Invariant | `epistemic.py` | 0 real-graph edges exceed their ceiling (the honesty law survives the whole run) |

**14/14 checks pass.**

---

## Why this matters (the honest gap is now closed)

The theatre audit said: 24 experiments prove mechanisms on real data, but only `validate-stack.py`
proved a real pipeline. **That gap is now closed.** `validate-graduation.py` is the full-stack proof:
not a mechanism demo, not a toy-input demo — ONE claim through the whole organism, with a mutation
that forces every layer to react, while the epistemic invariant stays intact.

The stack is **genuinely wired**: a retraction at the physical layer propagates to the thesis, which
stales the essay, which re-examines the learner, which feeds the organism, which drives the signed
re-release — all on real data.

---

## The unifying picture

```
source (I1 QM indeterminism)
  → envelope (I5 honest MACHINE_PROPOSED)
  → review (held in CORRECTION — the anti-theatre gate)
  → [MUTATE: retract I1]
  → staleness blast-radius → I5 stale
  → reactive essay → prose marked stale
  → pedagogy → learner re-examined
  → organism → misconception = research signal
  → signed re-release (verifiable + tamper-detect)
  → invariant still holds (0 violations)
```

This is the "one graph" principle made real: correctness + staleness + scheduler + retrieval all flow
from ONE derivation graph, and the whole organism reacts to a single source change.

## Proof
- `scripts/validate-graduation.py` — 14/14, real data.
- Added to `run-tests.py` (full suite) + experiment matrix (52 → 53).
