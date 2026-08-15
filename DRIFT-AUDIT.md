# DRIFT-AUDIT — vision docs vs layers vs earlier nav docs vs reality

*2026-08-15. A line-by-line read of the vision docs, `layers/`, and the earlier docs indexed in
`NAVIGATION.md` (LAB-REVIEW, BUILT-BY-LAYER, DEV-PLAN-HONEST, MASTER-KNOWLEDGE-BASE, COHERENCE-AUDIT,
etc.) against what is actually built (52 kernels, 97 experiments, 84 proofs, 6578 edges). This is the
honest gap between the RECORD and REALITY.*

---

## 0. THE GROUND TRUTH (what is actually true right now — verified 2026-08-15)

52 kernels · 97 experiments · 84 theatre proofs (38 PROVEN / 46 MECHANISM / 0 unproven) · 490 nodes /
6578 edges · all 10 layers (00-09) VALIDATED · Phase 6 "USE the architecture" COMPLETE (all orphaned
kernels wired) · LOGICVID gold ingested (Hermes-driven) · ToG-2 + BKT + temporal-validity added.

---

## 1. THE LAYERS ARE A MIX — stale, accurate, and partial (read all 10)

Reading every `layers/00-09-*.md` in full, they do NOT uniformly say "to build." The drift is
**per-layer and uneven**:

| Layer | What the page says | Verdict |
|---|---|---|
| **L00 Core Engine** | envelope + ladder + 4-axis authority; **Implementations empty** | **STALE** — `epistemic.py`, `schema.py`, `certificate.py` built + validated; the "Implementations" section never filled in |
| **L01 Corpus & Provenance** | "the ONLY layer fully DONE"; `DONE` (425 docs, R2) | **ACCURATE** — corpus is done; though it omits the `source_registry`/`fts_search` kernels |
| **L02 Epistemic Graph** | `PARTIAL` — "edges are co_occurs_with, needs epistemic ceilings (SPEC-02) + typed relations (SPEC-03)" | **PARTIAL-STALE** — ceilings ARE now applied (nodes carry `epistemic_ceiling`); the typed-relation upgrade is the still-real part |
| **L03 Factory** | "to build `canonical-dag.yaml`" | **STALE** — `canonical-dag.yaml` + `validate-dag.py` exist (SPEC-01 IMPLEMENTED); also omits `translation.py`, `proof_generators`, `factory_pool`, `vidyut_l0` |
| **L04 Argument Engine** | "to build `argument.json`" | **STALE** — `argument.json` EXISTS (6 info nodes, real ceilings) + `essay_ingest.py`, `query.py` |
| **L05 Review & Gate** | **Implementations empty** | **STALE** — `review.py`, `scholar_review.py`, `integrity_gate.py`, `open_ended_evolve.py`, `skill_graph.py` built + validated |
| **L06 Retrieval Compiler** | "to build compiled bundles per entity" | **STALE** — `context_compiler.py` (12/12), `bundle_router.py` (16/16), `fts_search.py` (9/9), `retrieval.py` (PathRAG/HippoRAG/ToG-2) built |
| **L07 Surfaces** | `BUILT — SEO/Astro live (seo.py 13/13)` | **PARTIAL-ACCURATE** — SEO is live; but it omits the MCP/Worker which are BUILT-but-NOT-DEPLOYED (the real L07 gap) |
| **L08 Domain Expansions** | domain subclasses live OUTSIDE core | **ACCURATE — and the REAL empty layer**: `lib/domains/` does not exist (matches the L08 over-claim in the old state.json) |
| **L09 Live System** | `IN_PROGRESS — the loop (agent execution) is next` | **PARTIAL-STALE** — the map/STATE/specs exist (true); but the "agent execution loop" is now being BUILT (Hermes-as-driver, kanban, `/goal`) — the page predates it |

**Verdict:** L01 + L08 are accurate. L07 + L02 + L09 are partial. **L00, L03, L04, L05, L06 are STALE** —
they still say "(to build)" or empty for layers that are proven + wired. These five are the misleading
ones and must be regenerated to the built state (the Phase-0 work). L08's emptiness is a REAL capability
gap, not a doc lag.

---

## 2. THE COUNT DRIFT IS SEVERE AND SPANS EVERYWHERE

| File | Kernels | Tests | Experiments | Theatre |
|---|---|---|---|---|
| **REALITY** | **52** | (suite ~93 gates) | **97** | **84 (38/46)** |
| `state.json` (fixed) | 52 | 81 | 97 | 38/46 ✅ |
| `AGENTS.md` (fixed) | 52 | — | 97 | 38/46 ✅ |
| `BUILT-BY-LAYER.md` | **37** ❌ | 75/75 ❌ | 75 ❌ | 35/39 ❌ |
| `DEV-PLAN-HONEST.md` | **37** ❌ | 75/75 ❌ | — | 35 ❌ |
| `MASTER-KNOWLEDGE-BASE.md` | **25 / 17** ❌ | — | 63 ❌ | 31/27 ❌ |
| `COHERENCE-AUDIT.md` | 37 ❌ | 75/75 ❌ | 75 ❌ | 35/39 ❌ |
| `KERNELS-INDEX.md` | 52 ✅ | — | — | — |

**Verdict:** only `state.json` + `AGENTS.md` (which I corrected this session) + `KERNELS-INDEX` match
reality. Every prose inventory (`BUILT-BY-LAYER`, `DEV-PLAN-HONEST`, `MASTER-KB`, `COHERENCE-AUDIT`)
is 15-27 kernels behind and says 75/75 tests when the suite is far larger.

---

## 3. "BUILT-BY-LAYER" HAS STALE GAP CLAIMS (gaps that are now closed)

- It lists **`misconception.py` repair cascade** as the L09 gap — but `misconception.py` is BUILT + wired (9/9, Phase 6).
- It lists **"BKT/FSRS pedagogical policy"** as a gap — I just added **BKT (Bayesian Knowledge Tracing) to `pedagogy.py`** (validate-bkt 4/4) this session. Closed.
- It lists **context paging (gap A)** + **signed attestation (gap E)** — these ARE still real (not closed).
- It lists **"only scifact" adapter done** — still true (openalex/s2orc/xaif/eleutheria incomplete).

---

## 4. "DEV-PLAN-HONEST" PREMISES ARE SUPERSEDED

- It says **"STOP adding kernels, we're over-built in breadth (37 kernels), wire the real corpus."** The
  "over-built breadth" premise is **outdated**: Phase 6 already WIRED all the orphaned kernels into live
  paths. The record is 52 kernels, not 37. The honest next step is no longer "don't add kernels" — it's
  the wiring that is done + the record reconciliation.
- Its **Phase 1 "translate Tantrāloka from scratch"** is **SUPERSEDED** by
  `CANONICAL-TRANSLATION-ORCHESTRATION.md`: ip-graph no longer produces translations from scratch;
  patala's factory produces, ip-graph VALIDATES. So the Mona-Lisa plan's generation premise is void.

---

## 5. VISION vs BUILD — the real drift (not a doc lag)

`VISION.md` is a **general epistemic-graph engine across Sanskrit/Western-philosophy/science** with
domain extensions (`science/`, `philosophy/`, `sanskrit/`) proving the engine generalizes. Reality:
- The engine is proven on **two** domains (Doyle/Western + IPVV/Sanskrit) — the generalization test is
  halfway.
- **L08 `domains/` is EMPTY** — the actual domain-subclass extensions the vision centers on do not exist.
  The engine is general *in design* but not yet *demonstrated* across 3+ domains.
- So the **true open drift** is: the vision says "general engine," the build has a general core proven on
  2 domains but **no `domains/` layer**. This is a REAL capability gap, not a stale doc.

---

## 6. THE CURRENT-DIRECTION DRIFT (where the roadmap points vs where we are)

| Roadmap (docs) | Reality now |
|---|---|
| DEV-PLAN-HONEST: "translate Tantrāloka from scratch" | SUPERSEDED → patala factory produces, ip-graph validates |
| DEV_PLAN Phase 0: "reconcile the record" | still open (layers, GAPS, the prose inventories below) |
| DEV_PLAN Phase 7: LOGICVID gold → enquiry | DONE (Hermes-driven, 11 files) |
| new: ToG-2 / BKT / temporal-validity | DONE (added this session) |
| vision: general engine across domains | L08 `domains/` EMPTY — the real forward gap |

---

## 7. THE ACTION LIST (what to fix)

1. **Regenerate `layers/00-09-*.md`** to the BUILT state (Phase-0) — the most misleading artifact.
2. **Resync the prose inventories** to 52/97/84/6578: `BUILT-BY-LAYER.md`, `DEV-PLAN-HONEST.md`,
   `MASTER-KNOWLEDGE-BASE.md`, `COHERENCE-AUDIT.md`, `GAPS.md`.
3. **Update `BUILT-BY-LAYER.md`** — drop the closed gaps (misconception, BKT now built).
4. **Mark DEV-PLAN-HONEST's "translate from scratch" + "stop adding kernels" as SUPERSEDED** (canonical
   orchestration + Phase 6 wiring).
5. **The real forward work** (not a doc lag): **L08 domain-expansions** (`lib/domains/`) to actually
   realize the general-engine vision, plus the still-real gaps (gap A context paging, gap E signed
   attestation, the 3 needs-build products, corpus-wide IPVV graduation).
