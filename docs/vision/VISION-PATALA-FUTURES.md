# VISION — PĀṬALA FUTURES (what we can build with everything we've proven)

*2026-08-14. Synthesizes everything we've VALIDATED — the epistemic engine, the algorithms we've
implemented and tested, the cloned repos, the arXiv mastery, and the Doyle-corpus experiments. Each
vision is concrete, mapped to layers, and grounded in what's already proven. The point: these aren't
speculative — each rests on a working implementation in this repo.*

---

## THE FOUNDATION WE'VE ALREADY PROVEN

Before the futures, the validated substrate (all working, tested):
- **Epistemic envelope** on 490 nodes / 6578 edges — invariant `authority(projection)<=authority(parent)`
  holds with 0 violations (physics corroborated, free-will thesis machine-proposed).
- **Canonical DAG** — 14-layer derivational chain PHYSICS→…→VALUE, validated, grounded in real works.
- **Argument graph** — AIF 6 info / 4 infer / 2 conflict for the two-stage thesis.
- **Retrieval algorithms implemented + tested on our data:** PathRAG flow-pruning, HippoRAG PPR,
  KG2Code executable queries, bounded context, stable-LCC.
- **Epistemic promotion** — herdr-style reducer + RKA blast-radius staleness, unified pipeline.
- **The generalization insight:** the data itself confirms physics=corroborated / thesis=machine-proposed.

**The strategic fact:** models are disposable compute; **the accumulated verified state is the durable
intelligence.** Everything below rests on making that verified state real, queryable, and self-maintaining.

---

# VISION 1 — "The Argument Map" (the flagship product)

> The product the arXiv + ecosystem research keeps pointing to: **the map of arguments humans have
> actually made** — not an encyclopedia, not a paper graph.

**What it is:** every contested question (`/free-will`, `/consciousness`, `/causality`, `/self`,
`/time`) becomes a **living argument object**:
```
QUESTION
 ├── positions (libertarianism, compatibilism, two-stage)
 ├── arguments (with premise→conclusion chains)
 ├── objections (AIF conflict nodes)
 ├── counterarguments
 ├── evidence (with epistemic ceilings: corroborated vs machine-proposed)
 ├── experiments
 ├── thinkers + historical development
 └── current frontier
```
Switch surfaces: `[Learn] [Explore] [Evidence] [History] [Debate] [Ask]`.

**What's proven:** our argument graph (AIF Info/Inference/Conflict) IS this structure; the epistemic
ceilings make it honest; KG2Code executable queries let agents navigate it.

**Layers:** 02 Epistemic Graph · 04 Argument Engine · 06 Retrieval · 07 Surfaces
**Build order:** extend argument.json → bounded-context retrieval → Astro pages per argument object.

---

# VISION 2 — "The General Epistemic Engine" (the architectural bet)

> Not "Pāṭala about Sanskrit" and not "Pāṭala about Information Philosopher." The **domain-agnostic
> engine** underneath multiple knowledge worlds.

**What it is:** one kernel (identity, provenance, passages, claims, evidence, arguments, review,
projection, retrieval) with pluggable domain ontologies:
```text
PĀṬALA ENGINE
 ├── Corpus layer    ├── Epistemic graph   ├── Argument engine
 ├── Review/gate     ├── Retrieval compiler ├── Agent API/MCP
 └── Education compiler
      ├── Sanskrit/Tantra     ├── Western philosophy     ├── Science
```
Same kernel · different corpus · different ontology extension · different UI projection.

**What's proven:** the Doyle corpus (information-philosopher) entered the same engine built for
Sanskrit — the epistemic envelope + DAG + argument graph all worked unchanged. The **generalization
test** is the 5 adapters (`import_openalex/s2orc/scifact/xaif/eleutheria`).

**Layers:** 00 Core · 01 Corpus · 08 Domain Expansions
**Build order:** the 5 import adapters → prove EleutherIA + SciFact + xAIF enter the same engine.

---

# VISION 3 — "Self-Maintaining Epistemic Graph" (the RKA/herdr synthesis)

> The graph that keeps itself honest — corrections propagate, staleness is filed, promotion is gated.

**What it is:** fully executable epistemic lifecycle:
```
agent output → evidence → review → canonical knowledge
        ↑                (herdr reducer: CORRECTION until evidence grounds)
        └── correction → blast-radius stale → review_queue (RKA)
```
A retraction at the physics floor auto-flags FREE_WILL and VALUE as `stale_dependency`, filed in a
review queue. Nothing is ever silently wrong.

**What's proven:** `experiment-herdr-review.py` (reducer keeps thesis in CORRECTION_REQUIRED) +
`experiment-rka-staleness.py` (PHYSICS retraction → 8 downstream stale) + `experiment-unified-epistemic.py`.

**Layers:** 03 Factory · 05 Review & Gate · 09 Live System
**Build order:** `lib/review.py` (reducer) + `lib/staleness.py` (blast-radius) → wire into the DAG.

---

# VISION 4 — "Executable Knowledge" (the KG2Code frontier)

> Agents don't get 40 MCP tools — they get a tiny graph-query language and write the plan; the engine
> executes truth-preserving code.

**What it is:**
```
resolve("Free Will") -> ip:concept:free_will
path(from=resolve("Quantum"), to=resolve("Free Will"), via=["presupposes"])
  .filter(review_state="accepted")
  .limit(12)
```
Verifiable traces, deterministic execution, agent does planning. This is our Bet 2 — now proven working
in `experiment-kg2code.py`.

**What's proven:** the executable DSL (resolve/neighbors/path/evidence) runs on our graph with verified
traces.
**Layers:** 06 Retrieval · 07 Surfaces (MCP)
**Build order:** promote the experiment to `lib/query.py` → expose over MCP → the agent surface.

---

# VISION 5 — "The Verified Corpus Engine" (science-scale)

> The substrate the AI-scientist convergence needs: persistent verified evidence, not just papers.

**What it is:** question-first scientific epistemic graph:
```
PAPER → CLAIM → EVIDENCE → EXPERIMENT → RESULT → SUPPORTS/FAILS → THEORY → CONTRADICTION → REPLICATION
```
Query: "strongest evidence that consciousness requires recurrent processing" → not 100 search results
but a structured claim↔evidence bundle with methods, sample sizes, replications, defeaters.

**What's proven:** SciFact ingest design (SPEC-07), claim↔evidence machinery designed, the epistemic
envelope gives the honest ceilings.
**Layers:** 01 Corpus · 02 Epistemic · 06 Retrieval
**Build order:** `import_scifact` adapter → evidence-retrieval benchmark against SciFact gold.

---

# VISION 6 — "Cross-Tradition Comparative Philosophy" (the killer feature)

> Not "Śiva = quantum mechanics." Structural comparison with explicit "analogy ≠ identity."

**What it is:** one substrate where arguments cross domains:
```
STRUCTURAL QUESTION: Does cognition require a persistent subject?
  INDIAN:    Utpaladeva · Dharmakīrti · Nyāya
  WESTERN:   Hume · Kant · Husserl
  COGNITIVE: predictive processing · global workspace
```
Compare claim structure, premises, target phenomenon, necessary commitments, defeaters — with
`analogy ≠ identity` discipline.

**What's proven:** the epistemic envelope + argument graph + the Doyle corpus (which naturally spans
free-will across philosophy/physics/neuroscience) is the seed.
**Layers:** 02 Epistemic · 04 Argument · 08 Domain Expansions
**Build order:** a `compare(question, [traditions])` query over the graph.

---

# VISION 7 — "The Autonomous Review Institute" (the meta-vision)

> The convergence thesis made real: persistent verified state as durable intelligence.

**What it is:** patala as an **autonomous research institute** — a swarm of agents propose, a
deterministic reducer gates, humans adjudicate, and the verified epistemic graph accumulates. Each
agent-run is a first-class, immutable, reviewable artifact (the universal schema from SPEC-09):
```
Task → Run → Agent → Artifact → Proposal → Review → Decision → (supersede)
```
Self-improvement is PR-based, not mutation (SPEC-12: "self-modification as PR rather than mutation").

**What's proven:** the universal schema matches our envelope; herdr's reducer + Vouch's gate are cloned
references.
**Layers:** 05 Review · 09 Live System
**Build order:** the reducer + review-event ledger → agent execution loop.

---

## THE STRATEGIC THROUGH-LINE

All seven visions are the same engine at different magnifications:
```
compile knowledge once
  → verified epistemic graph (honest ceilings)
  → self-maintaining (staleness + promotion)
  → executable retrieval (KG2Code / PathRAG / HippoRAG)
  → surfaces (Argument Map / comparative / agent API)
  → accumulates as durable intelligence
```

**The unifying bet:** patala is not a Sanskrit project and not a philosophy project. It is the
**verified-state substrate** that the self-improving-agent convergence depends on. Sanskrit is the
deepest vertical; the Doyle corpus is the generalization test; the Argument Map is the product; the
autonomous review institute is the end-state.

---

## PRIORITY ORDER (what to build first)

1. **Promote the proven experiments to `lib/`** — `review.py`, `staleness.py`, `query.py` (KG2Code),
   `retrieval.py` (PathRAG/HippoRAG). These are done-in-experiments, trivial to make real.
2. **The 5 import adapters** — the generalization test (VISION 2/5). Highest information value.
3. **`lib/query.py` over MCP** — executable knowledge (VISION 4), the agent surface.
4. **The Argument Map pages** — the product (VISION 1).
5. **Review-event ledger + agent loop** — the institute (VISION 7).

Each is mapped to layers in `STATE.yaml` and specced in `specs/`.
