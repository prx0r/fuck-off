# THE GLOBAL VISION → CHUNKS → LAYERS MAP (deterministic, top-down)

*2026-08-14. THE way the whole vision decomposes. Read from the top down: **ONE global vision → a
fixed set of CHUNKS → each chunk lands deterministically on ONE Layer → and the Layer is where you find
the implementation, tools, docs, and live state.***

> **The direction:** this file goes **vision-first** (top-down). `NAVIGATION.md` goes
> **implementation-first** (bottom-up). They meet at the LAYER — the deterministic anchor where a
> vision chunk becomes buildable and its state is tracked. `STATE.yaml` is the live tracker.

---

## THE ONE GLOBAL VISION

> **A general epistemic graph engine** — a domain-agnostic knowledge compiler producing immutable,
> addressable read artifacts across Sanskrit philosophy, Western philosophy, and science. The engine
> (claim/argument/evidence/review) is the product; Information Philosopher is the first generalization
> test. (Full vision: `docs/vision/VISION.md`.)

---

## THE CHUNKS (each is a distinct part of the one vision)

The vision decomposes into **10 chunks**, each building ONE Layer (patala-style numbering):

```
GLOBAL VISION
 ├─ CHUNK 1  The Engine Core     ──►  Layer 00  Core Engine
 ├─ CHUNK 2  The Corpus          ──►  Layer 01  Corpus & Provenance
 ├─ CHUNK 3  The Epistemic Graph ──►  Layer 02  Epistemic Graph
 ├─ CHUNK 4  The Factory         ──►  Layer 03  Factory (compiler)
 ├─ CHUNK 5  The Argument Engine ──►  Layer 04  Argument Engine
 ├─ CHUNK 6  The Review System   ──►  Layer 05  Review & Gate
 ├─ CHUNK 7  Retrieval/Compiler  ──►  Layer 06  Retrieval Compiler
 ├─ CHUNK 8  The Surfaces        ──►  Layer 07  Surfaces (Astro/API/MCP)
 ├─ CHUNK 9  The Domains         ──►  Layer 08  Domain Expansions
 └─ CHUNK 10 The Live System     ──►  Layer 09  Live System
```

*(The 12-layer map exists in patala; for this leaner second-gen engine we use 10 layers — the
governance, organism, and economics concerns fold into Core + Live System.)*

---

## THE DETERMINISTIC CHUNK → LAYER MAP

| Chunk | The vision chunk | Lands on Layer | What the Layer is | Implementation anchor |
|---|---|---|---|---|
| **1 Engine Core** | domain-agnostic object envelope, identity, provenance | **00 Core Engine** | the shared epistemic kernel | `specs/SPEC-02-epistemic-envelope.md` |
| **2 The Corpus** | sources → canonical works/passages, R2 backup | **01 Corpus & Provenance** | ingestion + clean corpus | `data/corpus.jsonl` + `scripts/` |
| **3 Epistemic Graph** | concept/entity/relation graph with ceilings | **02 Epistemic Graph** | the knowledge graph | `data/graph/graph.json` |
| **4 The Factory** | the DAG compiler (physics→…→value) | **03 Factory** | the derivational compiler | `specs/SPEC-01-canonical-dag.md` |
| **5 Argument Engine** | claims→arguments→evidence (AIF) | **04 Argument Engine** | the argument graph | `specs/SPEC-03-argument-graph.md` |
| **6 Review System** | review events, authority, adjudication | **05 Review & Gate** | epistemic gates | `specs/SPEC-02-epistemic-envelope.md` |
| **7 Retrieval Compiler** | compiled agent bundles + search | **06 Retrieval Compiler** | precomputed read artifacts | `specs/SPEC-00-INFRA-BUILD.md` |
| **8 The Surfaces** | Astro site + API + MCP | **07 Surfaces** | read surfaces | `specs/SPEC-05-surfaces.md` |
| **9 The Domains** | domain ontology extensions | **08 Domain Expansions** | world-specific subclasses | `docs/vision/VISION.md` §engine/domain |
| **10 Live System** | state, staleness, docs-in-sync | **09 Live System** | orchestration + projection | `STATE.yaml` + this map |

---

## THE DETERMINISTIC FLOW (how a vision chunk becomes buildable)

```text
VISION CHUNK         LAYER               NAVIGATION              PROGRESS
   (this map)    layers/NN-*.md       resolves impl/tools      STATE.yaml
       └─►   └─►            └─►  live state slot
```

An agent does this:
1. **Pick a VISION CHUNK (1-10)** from this map.
2. **GO TO its Layer page** (`layers/NN-*.md`) — its deterministic home.
3. **NAVIGATION.md** resolves the implementation + docs + tools for that layer.
4. **READ the layer's "current state"** — the live progress.
5. **ADVANCE the work** → update the layer's state in `STATE.yaml`.

---

## THE MACHINE-RESOLVABLE FORM (VISION-CHUNKS.json)

```json
{
  "global_vision": "general epistemic graph engine across Sanskrit/Western-philosophy/science",
  "chunks": [
    {"chunk":1, "name":"Engine Core",     "layer":"00", "doc":"layers/00-core-engine.md",     "spec":"specs/SPEC-02-epistemic-envelope.md"},
    {"chunk":2, "name":"The Corpus",      "layer":"01", "doc":"layers/01-corpus-provenance.md","spec":"specs/SPEC-00-INFRA-BUILD.md"},
    {"chunk":3, "name":"Epistemic Graph", "layer":"02", "doc":"layers/02-epistemic-graph.md",  "spec":"specs/SPEC-01-canonical-dag.md"},
    {"chunk":4, "name":"The Factory",     "layer":"03", "doc":"layers/03-factory.md",          "spec":"specs/SPEC-01-canonical-dag.md"},
    {"chunk":5, "name":"Argument Engine", "layer":"04", "doc":"layers/04-argument-engine.md",  "spec":"specs/SPEC-03-argument-graph.md"},
    {"chunk":6, "name":"Review System",   "layer":"05", "doc":"layers/05-review-gate.md",      "spec":"specs/SPEC-02-epistemic-envelope.md"},
    {"chunk":7, "name":"Retrieval Compiler","layer":"06","doc":"layers/06-retrieval-compiler.md","spec":"specs/SPEC-00-INFRA-BUILD.md"},
    {"chunk":8, "name":"The Surfaces",    "layer":"07", "doc":"layers/07-surfaces.md",         "spec":"specs/SPEC-05-surfaces.md"},
    {"chunk":9, "name":"The Domains",     "layer":"08", "doc":"layers/08-domain-expansions.md","spec":"docs/vision/VISION.md"},
    {"chunk":10,"name":"Live System",     "layer":"09", "doc":"layers/09-live-system.md",      "spec":"specs/SPEC-06-live-system.md"}
  ],
  "deterministic": "each chunk builds exactly ONE layer; progress tracked per-layer via STATE.yaml"
}
```

---

## HOW IT MEETS NAVIGATION (the two directions, one anchor)

```text
TOP-DOWN (this file):      GLOBAL VISION → 10 CHUNKS → each → ONE LAYER
BOTTOM-UP (NAVIGATION.md): any file/tool → resolve → ONE LAYER → impl/docs/state
                               ↓  both meet at the LAYER  ↓
                        layers/NN-*.md  =  the deterministic anchor
```

The vision chunks top-down into layers; navigation resolves bottom-up back to layers. They agree at the
layer page — where "what this vision chunk needs" and "what this layer implements" are the same thing.
Progress is tracked per-layer, deterministically, in `STATE.yaml`.
