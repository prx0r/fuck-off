# SPEC-20 — EDUCATION + ORGANISM (the learner & the sensor)

*2026-08-14. Builds out patala's education + organism visions using our experimental stack. Validated
by `scripts/validate-education-organism.py` (9/9) + `experiment-evolving-memory.py` (Layer 09
procedural memory). Test suite 28/28.*

---

## The vision (from patala's docs)

- **Education:** an intelligent tutoring system over the epistemic graph — the learner manipulates the
  same propositions/evidence/arguments scholars use. *Education is a projection of the graph, never a
  separate knowledge base.* (PATALA-EDUCATION-SYNTHESIS.md)
- **Organism:** the consumer app as a **sensor** for what humans fail to understand — building a demand
  + misconception graph. (patalaorganism.md)

---

## What we built

### `lib/education.py` — the learning layer
- **`LearningClaim`** — a derived-from-graph objective (epistemic ceiling, prerequisites, source_refs).
  *Validated: interaction compiler emits LearningClaims from the two-stage argument.*
- **`MasteryEvidence`** — learner response records (BKT/FSRS inputs, never defining the layer).
- **`compile_interactions()`** — the interaction compiler: scholarly object → LearningPacket
  (LearningClaims + 6-interaction vocabulary + distractors + progression + epistemic ceiling).
- **`wrong_answer_to_neighbor()`** — THE MOAT: a wrong answer resolves to a **known epistemic neighbor**
  classified in the failure taxonomy (rival_proposition, scope_inflation, wrong_technical_sense...),
  NOT an LLM-invented distractor. *Validated: compatibilism → rival_proposition.*
- **Counterfactual / crux primitive (PremiseRetract):** "what if this premise is false?" — retract I2 →
  I5 loses support → I2 is load-bearing. *Validated: teaches structure, not trivia.*

### `lib/organism.py` — the sensor layer
- **`UserKnowledgeState`** — per-user epistemic state (concept mastery, arguments understood, known
  confusions). *Validated: correct→mastery up, wrong→mastery down.*
- **`MisconceptionGraph`** — the demand graph: Confusion misreads Claim · Objection attacks Premise,
  with learner-count and top-misconception ranking. *Validated: records + feeds the flywheel.*
- **`experiment-evolving-memory.py`** — dream-cycle consolidation → procedural memory (agent improves
  across sessions).

---

## The design law (enforced)

> Education is a projection of Pāṭala objects — every LearningClaim resolves DOWNWARD to canonical
> scholarly objects; nothing is invented for education that isn't derived from the graph.

## The flywheel (validated end-to-end)
```
epistemic graph → LearningClaims → interactions → learner responses → misconception data
→ better pedagogy → hard distinctions → scholar questions → corrections → better graph
```
And the killer property: scholar corrections auto-propagate to mark stale the educational explanations
that depend on a changed claim (our reactive-essay + RKA staleness machinery repurposed).

## Build order (from the gold doctrine — 20 golds, not 10k)
1. ✅ LearningClaim + MasteryEvidence + interaction compiler + wrong-answer→neighbor (this spec)
2. ✅ UserKnowledgeState + MisconceptionGraph (this spec)
3. ✅ Counterfactual/crux primitive (PremiseRetract)
4. Next: BKT/FSRS learner-state → pedagogical policy → the 4 modes (DISCOVER/LEARN/PRACTICE/STUDY)

## Moats (from the vision, now partially built)
1. **Scholarly** — sources + provenance (have it)
2. **Machine** — benchmarks + adversarial fixtures (mutation-testing gives this)
3. **Pedagogical** — diagnostic interactions + misconception graph (built)
4. **Language** — Sanskrit alignment + pronunciation + term-sense (Vidyut)
