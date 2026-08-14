# Information Philosopher — Ontology (concept + relation vocabulary)

This ontology defines the closed vocabulary for knowledge-graph construction from the
informationphilosopher corpus. Adapted from `emptiness-graph`'s 16 typed relations + patala's
term/theme model + the site's own navigation themes.

## 1. THEME CATEGORIES (top-level organization, ≈ patala layers / iwe categories)

From the site's nav + the corpus subject matter. Concepts can belong to MULTIPLE themes
(polyhierarchy — a concept like "entropy" is both physics and information).

| Theme | Focus |
|-------|-------|
| `free_will` | agency, freedom, responsibility, two-stage model |
| `determinism` | causal determinism, Laplace, necessity |
| `causality` | cause/effect, correlation, intervention |
| `quantum` | QM interpretation, measurement, superposition, entanglement |
| `information` | information theory, Shannon, bit, computation |
| `entropy` | thermodynamics, 2nd law, arrow of time |
| `mind` | consciousness, mental/physical, qualia |
| `chance` | probability, randomness, indeterminism |
| `knowledge` | epistemology, truth, belief, logic |
| `value` | ethics, meaning, purpose |
| `life` | biology, evolution, origin of life |

## 2. CONCEPT CATEGORIES (node types, ≈ instagraph `type` / patala concept kind)

| Category | Example nodes |
|----------|---------------|
| `concept` | free will, determinism, entropy, information, consciousness |
| `work` | "Einstein 1905 photoelectric paper", "Gödel's incompleteness theorem" |
| `author` | Einstein, Bell, Bohr, Planck, Dennett, Kane, Wheeler, Sperry, Deacon |
| `scientist` | specific scientist/physicist (subtype of author) |
| `philosopher` | specific philosopher (subtype of author) |
| `theory` | two-stage model, Copenhagen, pilot-wave, Many-Worlds |
| `problem` | mind-body problem, measurement problem, hard problem of consciousness |
| `experiment` | double-slit, Stern-Gerlach, EPR, Schrödinger's cat |
| `school` | compatibilism, libertarianism, determinism, indeterminism |

## 3. RELATION VOCABULARY (typed edges, ≈ emptiness-graph 16 relations)

Each edge is `(source CONCEPT, relation, target CONCEPT)` anchored to an evidence quote.

| Relation | Meaning | Example |
|----------|---------|---------|
| `negates` | directly contradicts / refutes | determinism negates free will (in libertarianism) |
| `presupposes` | A assumes B | two-stage model presupposes indeterminism |
| `is_cause_of` | A causes B | entropy is_cause_of arrow of time |
| `is_identical_to` | A = B (same concept) | information is_identical_to negentropy (Brillouin) |
| `defines` | A defines B | Shannon defines information |
| `supports` | A provides evidence for B | EPR supports non-locality |
| `tensions_with` | unresolved disagreement (NO forced reconciliation) | free will tensions_with determinism |
| `is_obstacle_to` | A blocks/prevents B | measurement is_obstacle_to wavefunction collapse-free view |
| `is_antidote_to` | A resolves/relieves B | two-stage model is_antidote_to the free-will paradox |
| `extends` | A generalizes B | information extends entropy (generalized) |
| `applies_method_of` | A uses B's method | Dennett applies_method_of engineering |
| `is_instance_of` | A is an example of B | indeterminism is_instance_of chance |
| `deconstructs` | A breaks down B | Kant deconstructs metaphysical free will |
| `reframes_as` | A recasts B | compatibilism reframes_as free will = acting on desires |
| `is_precursor_of` | A historically precedes B | Laplace is_precursor_of modern determinism |
| `opposes` | A is a school opposed to B | incompatibilism opposes compatibilism |

## 4. Evidence anchor discipline (critical — borrowed from darshana-graph)

- Every concept/edge MUST carry a verbatim `evidence_quote` (≤15 words) from the source text.
- Closed vocabulary only — anything outside is dropped (no invented relations).
- Confidence: `low` if not clearly asserted (implied/inference only).
- No self-referential edges (concept_a == concept_b dropped).
- Keep `source` (work/author) + `section` provenance on every object.

## 5. Output record shape (per fragment / per edge)

```json
{
  "id": "ip:concept:free_will",
  "label": "Free Will",
  "category": "concept",
  "themes": ["free_will", "determinism", "mind"],
  "definition": "The capacity of agents to choose among alternatives...",
  "aliases": ["freedom of the will", "free choice"],
  "evidence_quote": "the question of whether we are free",
  "source": {"work": "C_S_Lewis_Restoration_of_Man", "author": "C.S. Lewis"},
  "section": "solutions"
}
```

```json
{
  "id": "ip:edge:determinism-negates-free_will",
  "source": "ip:concept:determinism",
  "target": "ip:concept:free_will",
  "relation": "negates",
  "confidence": "high",
  "evidence_quote": "if every event is caused, no choice is free",
  "source": {"work": "...", "author": "..."}
}
```
