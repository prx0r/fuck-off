# VISION — THE QUESTION-GROWTH ENGINE (the pushing method as a learnable machine)

*2026-08-14. Inspired by the patala pushing method (research-library/pushing — SPEC-33..36) and its
core insight: **"the best questions are grown, not pre-written: if we record how questions grow, we can
learn the growth."** This is the abstract architecture for a machine that doesn't just answer questions
— it grows new ones from the graph's own tension.*

---

## THE PRIMA MATERIA (from the pushing method)

The Logicvid / Pushing method is a **graph-growth machine** with two loops:

```text
DECOMPOSITION   text → claims → definitions → dependencies → proof-or-boundary → GRAPH
QUESTION-GROWTH graph tension → paradox → hidden premises → branches → research → NEW GRAPH
```

Every session produces a structured record:

```text
QUESTION       the pressure point (mechanism-gap, crux, subversion, quantifier, register, root)
DISTINCTIONS   the text's terms separated
THEOREM        the boxed result
BOUNDARY       what has NOT been established (the honest limit)
NEXT_PRESSURE  the new question the text forces
PASSAGES       the cited passages
```

## THE ONE-LINE VISION

> **A machine that grows questions the way a text grows them: it hounds the graph with "why,"
> records each pressure-point as a structured record (question → theorem → boundary → next-pressure),
> and learns the growth — so it can predict the next question a graph's tension implies.**

## WHY IT'S POWERFUL (the abstract architecture)

1. **Questions are a first-class graph** — not search queries, but nodes in a growth tree. Each
   question has children (the next-pressure it forces) and honest boundaries (what's not established).

2. **Convergence = robustness** (the key insight from logicvid3): when the *same primitive* is reached
   from *many independent question-roots*, it's robust — not one fragile chain. This is a new kind of
   epistemic signal: `primitive_robustness = number of independent question-routes reaching it`.

3. **Learnable growth**: each PushingRecord is a supervised example
   `(question + passages → theorem → next_pressure)`. A model trained on real pushing sessions could
   predict the next pressure-point a text/graph implies — the "question-generation" that feeds both
   research (What-If Machine) and education (adaptive pedagogy picks the next hardest question).

4. **It connects everything we've built:**
   - research signal → the What-If Machine's Research-Value (a high-boundary question is a research gap)
   - learner confusion → the Co-Evolving Organism (a learner's next-question is a growth record)
   - curriculum → the education vision ("the learner reconstructs the argument the tradition grew")
   - comparative → the cross-tradition questionnaire (ask every text the same question-shapes)

## THE NOVEL MECHANISM: "QUESTION-SHAPE + PRIMITIVE-ROBUSTNESS"

```text
QuestionShape    ROOT | CRUX | MECHANISM_GAP | SUBVERSION | QUANTIFIER | REGISTER
PrimitiveRobustness(p) = # independent question-routes that reach primitive p
```

- **QuestionShape** classifies the pressure-point (predictable from question + passages).
- **PrimitiveRobustness** measures how many independent paths converge on a concept — a metric for
  "how load-bearing is this idea" that complements our counterfactual load-bearing score (a primitive
  reached many ways is foundationally robust).

## WHY START NOW

- The pushing sessions are **real, existing supervised data** (SPEC-33..36) — not synthetic.
- The graph-growth structure is **exactly** our epistemic graph + staleness + question tools.
- It gives the organism + education + research visions a **concrete growth engine** to build on.

## WHAT TO BUILD NEXT

1. **`lib/question_growth.py`** — PushingRecord datatype + the growth-graph builder + PrimitiveRobustness.
2. **Parse real pushing sessions** into PushingRecords (SPEC-33) → a real question-growth graph.
3. **Train a next-pressure predictor** on the records (learnable growth).
4. **Wire into pedagogy**: the learner's next interaction = the graph's next-pressure, not a fixed quiz.

See `SPEC-33..36` (the method) + `experiment-question-growth.py` (the prototype). This is the pushing
method turned from a scholarly practice into a machine — the "grown, not pre-written" question engine.
