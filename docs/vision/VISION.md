# VISION — the epistemic graph engine (across knowledge worlds)

**Status:** CANONICAL VISION · **Owner:** ip-graph · **Date:** 2026-08-14
**How to use:** this is the *vision*. It decomposes into chunks → layers → tasks via
`VISION-CHUNK-LAYER-MAP.md` (the mechanism). Read this for the *why*; read that for the *how to build*.

---

## THE ONE GLOBAL VISION

> **A general epistemic graph engine** — Pāṭala architecture stripped down and rebuilt as a cleaner,
> faster **second-generation knowledge compiler** that operates across multiple knowledge worlds
> (Sanskrit philosophy, Western philosophy, science, consciousness). The engine is the product; any
> single domain (including Information Philosopher) is a proving ground.

**The anti-goal:** NOT "Pāṭala, but about Information Philosopher." NOT a generic encyclopedia. NOT
another paper graph. The engine is **domain-agnostic epistemic infrastructure**, and this repo
(`fuck-off`/ip-graph) is its **first generalization test** — the place Pāṭala learns to operate outside
Sanskrit.

> *"If the architecture works equally well on Abhinavagupta, Bell, Dennett and Shannon, you've
> discovered something considerably more valuable than another philosophy website."*

---

## THE THREE GRAPHS (do not collapse them)

| Graph | Content | Status |
|-------|---------|--------|
| **Bibliographic** | paper · author · institution · citation · journal · date | solved elsewhere (OpenAlex, Semantic Scholar, Crossref) — **ingest** |
| **Semantic** | concept · entity · method · experiment · theory · phenomenon | partially solved |
| **Epistemic** ⭐ | claim · argument · evidence · objection · defeater · replication · interpretation · confidence · review · disagreement · synthesis | **the one we own** |

The differentiator is the **argument/evidence layer** — not "Kant influenced Hegel" but:

```text
Hume claim H183
   ├─ warrant / evidence / depends_on
   ▼
causal inference position
   ├─ challenged_by → Kant K92  (with argument structure)
   ├─ reframed_by → Russell R18
   └─ related modern evidence
```

---

## THE ENGINE / DOMAIN SEPARATION

```text
             PĀṬALA KNOWLEDGE ENGINE
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
   Sanskrit        Philosophy       Science
   / Tantra        / Ideas          / Evidence
```

```text
core/
  identity · provenance · passages · claims · evidence · arguments · relations
  reviews · projections · retrieval · search · MCP · publication
domains/
  indian-philosophy/  western-philosophy/  physics/  consciousness/  biology/
```

**Domain-agnostic canonical core:** Source · Work · Passage · Entity · Claim · Relation · Argument ·
Evidence · Interpretation · Review · Decision · AgentRun · Artifact

**Domain extensions (NOT in core):**
```text
sanskrit/    Manuscript · Reading · Translation · Commentary
science/     Experiment · Dataset · Method · Measurement · Replication
philosophy/  Position · Objection · ThoughtExperiment · ArgumentForm
```

---

## THE CROSS-DOMAIN MEETING (the killer feature)

One substrate where arguments cross domains. Free will already spans metaphysics, mind, physics,
quantum, information theory, neuroscience, moral responsibility:

```text
          FREE WILL
       ┌───────┼────────┐
       ▼       ▼        ▼
  philosophy physics neuroscience
       │       │        │
  compat.  indeterm.  Libet-style
       │       │        evidence
       └───────┼────────┘
               ▼
         CRUX STRUCTURE
```

**Cross-tradition comparison (scholarly, not dumb analogy):**
```text
STRUCTURAL QUESTION: Does cognition require a subject that persists across representations?
  INDIAN:     Utpaladeva · Dharmakīrti · Nyāya
  WESTERN:    Hume · Kant · Husserl
  COGNITIVE:  predictive processing · global workspace · self-model theory
```
with explicit "analogy ≠ identity" discipline.

---

## THE PRODUCTS

### 1. The map of arguments humans have actually made
`/consciousness` `/free-will` `/causality` `/self` `/time` `/knowledge` `/information` — each a living
**argument object**: question → positions → arguments → objections → counterarguments → evidence →
experiments → thinkers → history → frontier, with `[Learn][Explore][Evidence][History][Debate][Ask]`.

### 2. Argument search (the differentiator)
```text
illusionism
  CLAIMS AGAINST:
   A1 phenomenal certainty objection
   A2 meta-problem circularity objection
   A3 introspective datum argument
  FOR EACH: evidence · proponent · strongest formulation · responses · counter-responses ·
            unresolved cruxes · primary sources
```
Validated by AKASE (2026) + the 2026 KG systematic review.

### 3. A scientific Pāṭala (question-first, not ingest-everything)
```text
PAPER → CLAIM → EVIDENCE → EXPERIMENT → RESULT → SUPPORTS/FAILS → THEORY → CONTRADICTION → REPLICATION
```
"Science is infinite — don't ingest it all." Use **question-first expansion** from natural seeds:
information, entropy, quantum foundations, causality, free will, consciousness, computation, life.

---

## THE PRODUCT HIERARCHY

```text
PĀṬALA ENGINE
 ├── Corpus layer
 ├── Provenance layer
 ├── Epistemic graph
 ├── Argument engine
 ├── Review/gate system
 ├── Retrieval compiler
 ├── Agent API/MCP
 └── Education compiler
      ├──────┬──────┬──────┐
      ▼      ▼      ▼      ▼
   Pāṭala  Ideas  Science  (worlds)
  Sanskrit  Explorer
```
Same kernel · different corpus · different ontology extension · different UI projection.

---

## THE DEEPER STRATEGIC IMPLICATION

Use this repo to discover the boundary between **Pāṭala-specific intellectual work** and **general
epistemic infrastructure**. If you can ingest Information Philosopher → Bell → contemporary science
with the SAME provenance/argument/evidence/review/immutable-artifact/agent-retrieval primitives you
developed for the IPVV, **the underlying system is the actual project**. Pāṭala Sanskrit becomes your
deepest, hardest first vertical — not the architectural boundary.

---

## RESEARCH VALIDATION (2026 landscape)

- The 2026 systematic review of 102 scholarly-KG studies: the unsolved problem is **bridging
  inter-document graphs with deep intra-document structure** — exactly the claim→evidence→argument→
  synthesis layer. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0306457326002335))
- **PhilKG (2025)**: 140k-node philosophy KG from SEP, LLM extraction + verification. Shows generic
  philosophy KG is no longer a differentiated product.
- **EleutherIA**: ~19k nodes / 44k edges / 69k passages on ancient free-will philosophy, typed
  ontologies, agentic GraphRAG.
- Scientific KGs + LLMs as infrastructure for AI-driven discovery.
  ([OUP](https://academic.oup.com/nsr/article/13/8/nwag140/8507209))
- **AKASE (2026)**: argumentation KGs for search over arguments, multi-agent deliberation.
  ([openwebsearch](https://openwebsearch.eu/akase-results/))

---

## THE ONE-SENTENCE CARRY-FORWARD

> Build a **general epistemic-graph engine** (claim/argument/evidence/review/immutable-artifact) that
> works across Sanskrit, Western philosophy, and science; treat Information Philosopher as the
> generalization test; make the *map of arguments humans have actually made* the product.
