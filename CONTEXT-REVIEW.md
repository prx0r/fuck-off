# CONTEXT-REVIEW — the full honest state of ip-graph (agentgraph) + what's missing

*2026-08-15. Compiled by agentgraph from a parallelized read of NAVIGATION, TRACEABILITY, HANDOVER,
MASTER-KNOWLEDGE-BASE, STATE.yaml, state.json, KERNELS-INDEX, BUILT-BY-LAYER, COHERENCE-AUDIT,
BUILDNOTES, CHANGELOG, the specs, the experiment matrix, the theatre proofs, and the Tantrāloka build
area. Every count below was verified against the machine source (file/jsonls), not prose. This file is
the "everything I learned" review — a single dense reference + the explicit missing-work list.*

---

## 0. THE ONE-LINE (what this project actually is)

**ip-graph is the "agentgraph" frontier lab for the Verified Epistemic OS** — a domain-agnostic epistemic
graph engine (claim/argument/evidence/review/immutable-artifact). It is patala's second-generation
kernel and the generalization test across Sanskrit / Western philosophy / science. The integration
contract is: **patala PRODUCES (the translation factory DAG), ip-graph VALIDATES + SERVES (the read
plane + organism + validation kernels).**

---

## 1. VERIFIED GROUND TRUTH (the counts that are actually true right now — machine-verified 2026-08-15)

| Metric | Value | Machine source |
|---|---|---|
| Kernels in `lib/` | **52** | `ls lib/*.py` (exact) |
| Corpus records | **425** (6 html + 419 pdf) | `data/corpus.jsonl` (wc -l = 425) |
| Graph | **490 nodes / 6578 edges** | `data/graph/graph.json` |
| Experiments | **97** | `data/references/experiments.json` count=97 |
| Theatre proofs | **84 = 38 PROVEN / 46 PROVEN-MECHANISM / 0 UNPROVEN** | `data/references/theatre-proofs-all.json` |
| Graduation tests | Doyle 14/14 · IPVV 18/18 · product stack 13/13 | `scripts/validate-graduation*.py` |
| Tantrāloka SOURCE | 4,624 committed · 5,860 total kārikās · Āhnika 1 = 333 | e2e log + `data/tantraloka/root-verses.json` |
| Tantrāloka committed by layer | **264 T1 / 1 L0** (from the canonical factory DAG) | `corpus/organism.json` + e2e |
| Read plane (SPEC-49) | context_compiler 12/12 · fts 9/9 · bundle_router 16/16 · seo 13/13 | validate-* scripts |
| Repos cloned / catalog | 48 cloned / 99 cataloged | `data/references/github.json` |
| arXiv catalog | 32 | `data/references/arxiv.json` |
| Specs | 47 files | `specs/` |

**The single most important fact the record gets wrong:** `state.json` says 47 kernels / 81 tests, but
the true count is **52 kernels**. The entire prose layer (AGENTS.md, state.json, MASTER-KNOWLEDGE-BASE,
BUILT-BY-LAYER, COHERENCE-AUDIT, GAPS.md) lags the build.

---

## 2. THE ARCHITECTURE (what's actually built, per layer)

**All 10 layers (00–09) are VALIDATED**; L06/L07 additionally BUILT per SPEC-49. No layer is PRODUCTION.

- **L00 Core Engine** — `epistemic.py` (envelope + 4-axis authority + invariant), `schema.py`.
- **L01 Corpus & Provenance** — 425-doc corpus, source_registry, fts_search.
- **L02 Epistemic Graph** — 490/6578 graph + `canonical-dag.yaml`.
- **L03 Factory** — projection DAG + factory_pool + translation machinery (the moat).
- **L04 Argument Engine** — AIF argument graph + essay_ingest.
- **L05 Review & Gate** — scholar_review, integrity_gate, review reducers, open_ended_evolve.
- **L06 Retrieval Compiler** — context_compiler, fts, bundle_router, retrieval (PathRAG/HippoRAG/SAGE).
- **L07 Surfaces** — Astro (web/), edge worker, SEO, MCP (built, NOT deployed).
- **L08 Domain Expansions** — **EMPTY.** No `lib/domains/`. This is the false-VALIDATED layer.
- **L09 Live System** — organism, pedagogy, education, next_action, self_healing, agent_delivery.

**Phase 6 "USE the architecture" is COMPLETE (2026-08-14):** all ~25 previously-orphaned kernels are
now WIRED into live paths — validator stack onto the DAG (8/8), flywheels (9/9), read-plane retrieval
(9/9), scheduler bridge (5/5), organisms (7/7 each), and a genuine E2E on real DAG data (5/5).

**The integration seam (both sides):**
- **patala (agentpatala):** the write-side factory — SOURCE→T1→L0→L2→L200→C1 workers, object_registry
  (PG-backed), corpus_state 111-work ledger, the frozen L200/C1 specs, 71 translated works.
- **ip-graph (me):** read plane + organism + validation. `schema.py` collision forces SEPARATE PROCESSES.

---

## 3. THE TANTRĀLOKA ("Mona Lisa") HONEST STATE

- **Canonical orchestration decision (frozen):** translation runs through patala's deterministic
  `factory_scheduler.py` DAG (T1→ARGMAP→L0→L2→L200→C1). Hermes is a **generation kernel only**. The
  ip-graph per-verse Hermes runner was an **unplanned divergence and is KILLED**.
- **The gap between claim and canon:** the 34-verse `translations.jsonl` / 33 in the checkpoint were
  produced by the **KILLED bypass runner**, NOT the canonical argument-guided DAG. They are L2 *outputs*
  but not canonical DAG-committed objects. The truly canonical committed corpus is **264 T1 + 1 L0**,
  with **zero** ARGMAP / L2 / L200 / C1 from the factory yet.
- **The gold gap (the real problem):** the gloss scores **0.118** vs Dyczkowski — it misses the
  philosophical frame (self/object/luminous). The B4 **commentary-lift** reaches it, but the canonical
  fix (the **ARGMAP** step) has **zero committed objects**. Commentary-lift through real Hermes + ARGMAP
  are the open path to a real score.
- **Wiring status (green but not "production"):** `organism.json` has `verified: null`; `organs.json`
  `self_heal_step_recovered: false`; `scheduler-bridge.json` `eligible: false` (bridge knows the legal
  next action but eligibility not true) — the one-orchestrator principle is stated but not fully
  realized.

---

## 4. THE HONEST GAPS — WHAT IS MISSING (the deliverable of this review)

### 4A. THE RECORD IS STALE / CONTRADICTORY (fix first — the trust problem)

1. **Kernel count drift: 52 in `lib/` vs 47 in `state.json:5`/AGENTS.md, 37 in BUILT-BY-LAYER:28/COHERENCE:3, 25/17 in MASTER-KB.** Reconcile to **52** everywhere.
2. **KERNELS-INDEX table documents only 50 kernels — `commentary_lift.py` and `organism_factory_bridge.py` are MISSING from the table** despite being wired + validated. Add them.
3. **Edge count 6484 vs 6578.** Actual = 6578. Fix NAVIGATION.md:12,98, docs/03-graph.md:7, AGENTS.md:24.
4. **Experiment count 97 vs 75.** Fix BUILT-BY-LAYER:95, COHERENCE:3.
5. **Theatre totals drift (52/58/75/80/84).** Authoritative = **84 (38/46/0)**. Sync all prose.
6. **`state.json` L08 over-claims VALIDATED** — `lib/domains/` is EMPTY. Mark L08 accordingly.
7. **SPEC-01/02/03 still DRAFT** though fully implemented. Bump to IMPLEMENTED.
8. **GAPS.md is stale** — claims no projection compiler/retrieval/surfaces; all built. Rewrite.
9. **`layers/*.md` (00/03/04/05) say NOT_STARTED** while kernels exist. Regenerate.
10. **Gap B/C contradiction:** STATE.yaml marks execution_branching + deterministic_replay DISCOVERED; HANDOVER/MASTER-KB say BUILT. Decide + align.
11. **README.md is a 2-line placeholder** ("fuck-off / bounty chocolate bar"). Write a real one.
12. **3 competing layer taxonomies (00-09 / L00-10 / L00-12).** Pick ONE (the 10-layer decomposition).

### 4B. THE 2 THEATRE VALIDATORS (anti-theatre debt — must fix)

- `validate-provenance.py` — asserts are **hardcoded literals** (`emit_nanopub("I1","",... )`); does not assert on data-derived output.
- `validate-essay-ingest.py` — the Ratié essay is **injected as literals**, not read from a file.
- Rule: a validator is REAL only if the object it validates is **DERIVED from data**, not hand-typed. When in doubt mark **PROVEN-MECHANISM**.

### 4C. GOLD EXPERIMENTS / DATA NOT YET INGESTED (the moat gaps)

1. **The 63 L200 + 63 C1 IPVV golds are NOT bulk-ingested into the registry with Derivation edges.** This is the highest-leverage build (migration/shared `BUILD-IPVV-L200-C1-GOLD-INGEST.md`). Makes the moat real on real data.
2. **Live TranslationProof auditors are NOT wired** — xCOMET / MQM / OTTAWA / ByT5 / Heritage / Vidyut lattice. `translation.py.generate()` still **hand-fills from bool()**. SPEC-16 §30 `patala translate-proof` CLI doesn't exist.
3. **8 scanned PDFs un-OCR'd** (Stapp, 2×Culverwell, Quantum_Mechanics, Sperry1966, Watson, Wheeler, gabor1946) — blocks 100% corpus coverage. `scripts/ocr-scanned-pdfs.py` written, not run.
4. **Graph edges are still statistical `co_occurs_with`** — the typed-relation upgrade (negates/presupposes/is_cause_of/tensions_with) from docs/04-ontology not applied. Needs LLM tagging + verbatim `evidence_quote`.
5. **Import adapters: only scifact done.** openalex / s2orc / xaif / eleutheria incomplete (L01).
6. **LOGICVID gold (SPEC-40..48, the live-human-curiosity gold) not yet parsed into an enquiry graph** and not wired into pedagogy.
7. **The Mitchell/Mitra samgraha (391k bitext) + MITRA (1.74M S↔T↔C)** not ingested as benchmark/error-family validators (TRANSLATION-PRODUCTION T4).

### 4D. PRODUCT / CAPABILITY GAPS (from DEV_PLAN + state.json next steps)

- **The 3 v3 needs-build products** (Essay projection, Commentary, live Tokenization) — not built.
- **Read plane is BUILT but NOT DEPLOYED** — no `wrangler deploy` / Cloudflare Pages; Worker `/api/search` + `/mcp` not standing; FTS in DuckDB (local), not Postgres. SPEC-00 premise unmet until deployed.
- **Signed human attestation (Gap E)** — `human_authorize()` is a plain state flip; needs real crypto (ed25519/ecdsa), blocks any marketplace. **(critical before public authority)**
- **Context paging (Gap A)** — `context_compiler.py` does prose projection only; no lossless virtualization.
- **L08 domain expansions** — `lib/domains/` empty.
- **The 5 "missing" kernels (misconception, question_growth, enquiry, design_provenance, graph_stable) are ALL BUILT now (52 total).** Any doc still listing them as a gap is stale.

### 4E. FILES / ARTIFACTS MISSING OR BROKEN

- `lib/__pycache__/*.pyc` are untracked — add to `.gitignore`.
- **Uncommitted live work** (should be committed): `run-tantraloka-translation-parallel.py`, `translations.jsonl`, `translation-checkpoint.json`, and the Phase-6 outputs (dag-validation, flywheel, organism, organs{,2,3}, scheduler-bridge, iterations, e2e log).
- **Checkpoint skew:** `v103` is in `translations.jsonl` but not in `translation-checkpoint.json` `done` (34 vs 33); 6 records are buggy raw-reasoning captures (v100, v1000-1003, v1011).
- `experiments.json` and `theatre-proofs-all.json` are **dicts with a `count` field**, not bare lists — any script treating them as lists breaks.

---

## 5. HIGH-IMPORTANCE OPERATIONAL NOTES (read these or you'll repeat a mistake)

1. **The canonical translation path is patala's DAG — do NOT build another per-verse runner.** The ip-graph runner was killed for this reason. ip-graph's job is to VALIDATE the DAG's output and wire the crux compass, not to produce translations.
2. **`schema.py` collision:** ip-graph `lib/schema.py` vs patala `pipeline/schema.py` — **must run in separate processes.**
3. **Shared 4-core / 8GB / 2-agent box, NO swap.** ~2.5GiB available. Never bulk-load the 172MB registry in RAM; use `object_registry_pg.py` (streams/append). Background every long job (`setsid … &` + log). One heavy job at a time. Check `free -h` before launching anything heavy.
4. **Disk: volume at 97%** (2.1G free). External sources → R2, not local disk.
5. **The promotion gate:** a kernel is `INTEGRATED` only when **agentpatala** runs it on real Pāṭala data (real IPVV/gold via Hermes). Currently 10 integrated / 27 at frontier. agentgraph proves the mechanism; agentpatala makes it real.
6. **agentpatala's standing assignment (adjacent, non-overlapping):** make the R2 harvest factory-runnable — extract real verse text into `<work>.jsonl` (`sanskrit`/`source_sha256`) so `factory_batch._source_objects` can advance the 47k SOURCE. My proof generators then validate the output.
7. **RUNNING TESTS IS NOT WORK.** The suite is green. Run a gate only when code/data changed or a real claim is in doubt. Otherwise BUILD.
8. **Anti-theatre doctrine:** never hand-feed the object a validator claims to validate; never fabricate both sides of a comparison; mark PROVEN-MECHANISM when unsure. The manual data-flow read (Gate 3) is the only rigorous check.

---

## 6. RECOMMENDED NEXT WORK (my lane, in order)

1. **Phase 0 — reconcile the record** (4A): unify counts to 52/97/84/6578, add the 2 missing kernels to KERNELS-INDEX, fix state.json L08, bump SPEC-01/02/03, rewrite GAPS.md, regenerate layers/*.md, write a real README. *Everything else is untrustworthy until this matches reality.*
2. **Fix the 2 THEATRE validators** (4B) — make them data-derived.
3. **Commit the uncommitted Phase-6 + translation work** (4E) — after reconciling the checkpoint skew.
4. **Wire the crux compass + ARGMAP validation** into the Tantrāloka argument layer (the 0.118 fix path).
5. **Build the education/essay products** from the validated Tantrāloka corpus → `compile_interactions` → LearningClaims → read plane (the "X4" step).

*Shared-with-agentpatala coordination lives in `/root/projects/patala/migration/shared/`. This file could be mirrored there so both sides see the same honest record.*
