# SPEC-03 — ARGUMENT GRAPH (AIF-style Info / Inference / Conflict)

**Status:** DRAFT · **Owner:** ip-graph · **Source:** patala `machinelearning/research/patala_ml/aifgraph.py`

## What

Replace the flat `co_occurs_with` edges with a **typed argument graph** using AIF's three node types
instead of one generic "related" edge:

- **INFORMATION NODE** — a proposition/claim (textual assertion, resolvable to a passage)
- **INFERENCE NODE** — WHY proposition A supposedly licenses B (the scheme/move)
- **CONFLICT NODE** — WHY proposition X challenges Y (objection/rebuttal)

Plus our 16 typed relations from `docs/04-ontology.md` (negates, presupposes, is_cause_of,
tensions_with, ...).

## Why

`co_occurs_with` says "these two words appear in the same document" — it has no philosophical content.
The two-stage argument is full of *inferences* ("randomness → then evaluation → free will") and
*conflicts* ("compatibilism disagrees with libertarianism"). AIF separates proposition from inference
from conflict so the graph can represent **actual argument structure**, not term co-occurrence.

## The two-stage argument as an AIF graph (from our data)

```text
[INFO]  "Quantum events are genuinely indeterministic"   (grounded: Bell, EPR papers)
   │
   │ INFERENCE (TRANSCENDENTAL / ENTAILMENT)
   ▼
[INFO]  "Indeterminism provides the random 'chance' stage"  (two-stage premise 1)
   │
   │ INFERENCE (ANALOGY to biological variability: Operant Variability paper)
   ▼
[INFO]  "The evaluation/decision step adds the 'choice'"    (two-stage premise 2)
   │
   │ INFERENCE (REDUCTIO: without indeterminism no free will)
   ▼
[INFO]  "The two-stage model explains free will"            (the thesis)

[CONFLICT] "Compatibilism defines free will as acting on desires — tensions_with the
            two-stage (libertarian) model"   (grounded: the free-will papers)
```

## The 3 node types (adopted)

```python
@dataclass
class InfoNode:
    id, text, node_type="INFORMATION", passage_ids=[], role="claim", explicitness="EXPLICIT"

@dataclass
class InferenceNode:
    id, scheme (TRANSCENDENTAL|REDUCTIO|ANALOGY|ENTAILMENT|PRESUPPOSITION),
    premise_ids=[], conclusion_id, passage_ids=[]

@dataclass
class ConflictNode:
    id, text, a_id, b_id, kind ("objection"|"rebuttal"), passage_ids=[]
```

Every node resolves to `passage_ids` (our `data/extracted/*.txt` + the work they come from).

## Edge relation mapping (our ontology → AIF)

| Ontology relation | AIF node type it maps to |
|-------------------|--------------------------|
| presupposes | INFERENCE (PRESUPPOSITION) |
| is_cause_of | INFERENCE (ENTAILMENT) |
| negates | CONFLICT |
| tensions_with | CONFLICT |
| supports | INFERENCE |
| is_antidote_to | INFERENCE (REDUCTIO-style) |
| is_instance_of | INFORMATION (is-a) |

## Data model

New output `data/graph/argument.json`:
```json
{
  "information_nodes": [ {id,text,role,passage_ids,explicitness} ],
  "inference_nodes":   [ {id,scheme,premise_ids,conclusion_id,passage_ids} ],
  "conflict_nodes":    [ {id,text,a_id,b_id,kind,passage_ids} ]
}
```

## Build steps

1. Define the 3 dataclasses (port from patala `aifgraph.py`, simplified).
2. Hand-curate the two-stage argument skeleton (the INFO/INFERENCE/CONFLICT above) from the core works.
3. Anchor each node to `evidence_quote` + `passage_ids` (the actual extracted text).
4. Emit `data/graph/argument.json`.
5. Load into the networkx graph as typed subgraph.

## Acceptance

- [ ] `data/graph/argument.json` exists with all 3 node types
- [ ] Every node has ≥1 `passage_id` (real grounding, not invented)
- [ ] The two-stage thesis is represented as a resolvable argument chain
- [ ] The compatibilist conflict is present (not a one-sided graph)
- [ ] Mark `APPROVED` and fold into `docs/` when done
