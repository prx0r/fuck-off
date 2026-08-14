# SPEC-01 — CANONICAL DAG (the derivational layer chain)

**Status:** DRAFT · **Owner:** ip-graph · **Source:** patala `contracts/CANONICAL-DAG.yaml`

## What

Encode the information-philosophy thesis as a **directed dependency chain** where nothing is built
until its inputs are satisfied — exactly like patala's `SOURCE → T1 → L0 → … → C1 → THEME → ARGUMENT →
SYNTHESIS`. This turns our flat co-occurrence graph into a **derivational argument**, not a term map.

## Why

Our current graph (`data/graph/graph.json`) has only statistical `co_occurs_with` edges. It shows
*what topics appear together* but not *why one claim supports another*. The data's real structure is a
**thesis argument** (physics → information → free will → value). A CANONICAL-DAG captures that as an
auditable dependency chain — the single source of truth for what derives from what.

## The derived DAG (mapped from our actual corpus)

```yaml
version: 1
dependencies:
  # Layer 1 — the physics evidence floor (solutions/ PDFs: Bell, EPR, Boltzmann, Planck)
  PHYSICS:
    requires: [SOURCE]                 # the raw papers
  THERMODYNAMICS:
    requires: [SOURCE]                 # entropy, second law, Maxwell, Boltzmann
  # Layer 2 — information as the bridge (Landauer, Shannon, information-thermo)
  INFORMATION:
    requires: [THERMODYNAMICS]         # information↔entropy relation
  COMPUTATION:
    requires: [INFORMATION]
  # Layer 3 — the quantum/chance premise (measurement, indeterminism)
  INDETERMINISM:
    requires: [QUANTUM, PROBABILITY]   # QM foundations + chance
  QUANTUM:
    requires: [PHYSICS]
  PROBABILITY:
    requires: [PHYSICS, THERMODYNAMICS]
  # Layer 4 — the mind layer (consciousness, qualia, mind-body)
  MIND:
    requires: [INFORMATION]            # mind as information-processing
  # Layer 5 — the free-will thesis (two-stage model)
  FREE_WILL:
    requires: [INDETERMINISM, MIND]    # two-stage = chance + choice
  RESPONSIBILITY:
    requires: [FREE_WILL]
  # Layer 6 — value (the payoff)
  VALUE:
    requires: [FREE_WILL, LIFE]        # meaning/morality ground in agency
  LIFE:
    requires: [INFORMATION, THERMODYNAMICS]
  # Projections
  SYNTHESIS:
    requires: [FREE_WILL, VALUE]
  ESSAY:
    requires: [SYNTHESIS]
```

**Eligibility rule (patala):** a layer is eligible when all its `requires` are committed AND it has no
current committed object. Every claim in `FREE_WILL` must trace down to `PHYSICS` evidence.

## Key scholarly facts encoded (from our data)

- `THERMODYNAMICS` derives from the entropy/2nd-law papers (Boltzmann, Gibbs, Planck, Clausius).
- `INFORMATION` derives from `THERMODYNAMICS` — the corpus repeatedly ties info↔entropy (Landauer,
  "Information and Entropy in Quantum Theory").
- `FREE_WILL` (two-stage) requires BOTH `INDETERMINISM` (chance) AND `MIND` (the evaluation step) —
  this is Doyle's core thesis made explicit.
- `VALUE` requires `FREE_WILL` — meaning/morality presuppose genuine agency.

## Data model

A new file `data/graph/canonical-dag.yaml` (the single source of truth, like patala). Every layer maps
to `source_refs` (the actual papers/works in our corpus that ground it).

## Build steps

1. Create `data/graph/canonical-dag.yaml` from the above.
2. Map each DAG layer → the corpus works that ground it (via `data/corpus.jsonl`).
3. A `validate-dag.py` script checks: every layer's `requires` exist, no cycles, every committed object
   has all inputs committed.
4. Emit the DAG as a graph layer in `data/graph/graph.json` (new node type `layer`, edge `derives_from`).

## Acceptance

- [ ] `data/graph/canonical-dag.yaml` exists and validates (no cycles, all refs resolve)
- [ ] Each DAG layer has ≥1 grounding work from the corpus
- [ ] `derives_from` edges appear in the graph output
- [ ] Mark this spec `APPROVED` and fold into `docs/` when done
