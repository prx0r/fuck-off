# SPEC-02 — EPISTEMIC OBJECT ENVELOPE (the status ladder)

**Status:** DRAFT · **Owner:** ip-graph · **Source:** patala `source-evidence/schema/derived_scholarly_object.py`

## What

Give every object in our graph (concept, edge, claim, work) the **same epistemic envelope**:
`id · layer · derived_from · source_refs · epistemic_ceiling · review_state · authority`. Plus the
**4-axis authority** and the invariant `authority(projection) <= authority(parent)`.

## Why

Our current graph asserts edges as if they were facts ("Information → Value"). But the data mixes
**established physics** (entropy, QM — solid) with **a speculative thesis** (free will as two-stage —
proposed). Without an epistemic status, the graph is epistemically dishonest: it can't distinguish
"Bell proved non-locality" from "free will requires indeterminism." This envelope fixes that — it's the
difference between a real epistemic tool and a fanfic map.

## The epistemic status ladder (adopted from patala)

```python
EPISTEMIC_RANK = {
    "MACHINE_PROPOSED": 0,               # max for a machine — our default
    "ENGINEERING_VALIDATED": 1,          # deterministic verifier passed
    "SCHOLARLY_CORROBORATED_PRELIMINARY": 2,
    "SCHOLARLY_CORROBORATED": 3,         # found in multiple independent sources
    "INDEPENDENT_REVIEWED": 4,           # a live independent reviewer
    "ADJUDICATED": 5,                    # human adjudication only
}
```

## The 4-axis authority (never one scalar)

```python
Authority(
    generation="MACHINE_PROPOSED",    # deterministic/engineering
    evidence="MACHINE_PROPOSED",      # scholar-corpus corroboration
    review="NOT_REVIEWED",            # only a human can raise this
    publication="PRIVATE",
)
```

**The invariant:** `authority(projection) <= authority(parent)`. A downstream object never exceeds the
epistemic status of what it's derived from. If we later correct the physics grounding, every claim built
on it drops its ceiling automatically.

## How this maps to OUR data

| Object | Epistemic ceiling (sensible default) |
|--------|----------------------------------------|
| Work node (a paper) | `SCHOLARLY_CORROBORATED` if published/peer-reviewed; `ENGINEERING_VALIDATED` if an archived paper |
| Concept "entropy" | `SCHOLARLY_CORROBORATED` (established science) |
| Concept "free_will" | `MACHINE_PROPOSED` (philosophical, contested) |
| Edge "thermodynamics → information" | `ENGINEERING_VALIDATED` (Landauer's principle, published) |
| Edge "indeterminism → free will" | `MACHINE_PROPOSED` (the two-stage thesis, not settled) |
| Edge "free_will → value" | `MACHINE_PROPOSED` (speculative) |

The **invariant does real work here**: it guarantees the free-will chain can NEVER be marked
corroborated just because the physics under it is — the thesis layer stays honestly `MACHINE_PROPOSED`.

## Data model

Every concept/edge in `data/graph/graph.json` gains:
```json
{
  "id": "ip:concept:free_will",
  "label": "Free Will",
  "type": "concept",
  "epistemic_ceiling": "MACHINE_PROPOSED",
  "authority": {"generation":"MACHINE_PROPOSED","evidence":"MACHINE_PROPOSED","review":"NOT_REVIEWED","publication":"PRIVATE"},
  "source_refs": ["ip:doc:pdf/solutions/Free_Will.pdf"],
  "evidence_quote": "...",
  "review_state": "GENERATED"
}
```

## Build steps

1. Add the ladder + Authority to a `lib/epistemic.py` module.
2. Rebuild `data/graph/graph.json` with each object carrying the envelope.
3. Assign `epistemic_ceiling` per object type (sensible defaults; refine by source quality).
4. `audit-epistemic.py`: verify the invariant (`authority(projection) <= authority(parent)`) across all
   edges — a violation is a bug.

## Acceptance

- [ ] Every node + edge in graph.json has the full envelope
- [ ] The invariant holds across all edges (audit passes)
- [ ] Physics edges outrank thesis edges (entropy > free_will ceiling)
- [ ] Mark `APPROVED` and fold into `docs/` when done
