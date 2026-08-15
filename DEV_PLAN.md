# DEV PLAN — from vision to working epistemic engine (REV 2, post-translation-audit)

*2026-08-14. Rev 2. This plan was validated item-by-item against actual code (anti-theatre, verified by
execution, not docs) AND updated for the single most important finding: **the canonical translation
orchestration is patala's `factory_scheduler` DAG, not ip-graph's per-verse Hermes runner.** Read the
canonical note (`tantraloka/CANONICAL-TRANSLATION-ORCHESTRATION.md`) before any translation work. A task
is DONE only when it passes its gate + `STATE.yaml` + `CHANGELOG.md` are updated.*

---

## 0. THE CHANGE THAT REWRITES THE PLAN (read first)

**The translation runner ip-graph built (`run-tantraloka-translation*.py`) was an UNPLANNED DIVERGENCE
that bypassed patala's mature argument-guided factory DAG.** It is KILLED. The canonical path (verified,
and how IPVV was actually built):

```
patala/pipeline/factory_scheduler.py  (deterministic DAG controller — THE orchestrator)
   → T1 → ARGMAP → L0 → L2 → L200 → C1   (argument-guided; L2 requires L0+ARGMAP)
   → uses Hermes as the GENERATION KERNEL ONLY (batch calls, not per-verse)
   → commits versioned objects to the registry (JSONL now, PG next)
ip-graph VALIDATES + SERVES: TranslationProof / three-version / commentary_lift / read plane
```

**Why not redo the factory on the Hermes/kanban stack (the question):** Hermes is the execution kernel,
NOT the orchestrator (`handover/hermes/CANONICAL.md:7-8,54`); eligibility must be deterministic Python
(`hermespatala-architecture-review.md:142-144`); there are TWO DAGs, not interchangeable. So
`factory_scheduler.py` (deterministic Python) owns orchestration; Hermes kanban is only the execution
fabric. ip-graph's `next_action`/`factory_pool` are a duplicate "shadow task system" to route back
through patala's scheduler.

**Files:** `tantraloka/CANONICAL-TRANSLATION-ORCHESTRATION.md` (the canonical decision, full justification,
run commands) · `patala/pipeline/factory_scheduler.py` (the controller) · `contracts/CANONICAL-DAG.yaml`
(the DAG) · `handover/hermes/CANONICAL.md` (Hermes thesis).

---

## THE HONEST STATE (verified by execution, 2026-08-15 Rev 3 — counts reconciled)

| Metric | Value | Notes (verified) |
|---|---|---|
| Kernels (`lib/`) | **52** | `ls lib/*.py` — exact. `state.json`/AGENTS.md still say 47 (STALE — fix Phase 0) |
| Missing kernels | **0** | all 5 built (misconception, question_growth, enquiry, design_provenance, graph_stable) |
| Experiments | **97** | `data/references/experiments.json` count=97 |
| Theatre proofs | **84 = 38 PROVEN / 46 PROVEN-MECHANISM / 0 UNPROVEN** | `data/references/theatre-proofs-all.json` (authoritative) |
| Graph | **490 nodes / 6578 edges** | `data/graph/graph.json` (NOT 6484) |
| Corpus | **425** records (6 html + 419 pdf) | `data/corpus.jsonl` |
| THEATRE validators still to fix | **2** | `validate-provenance.py` (hardcoded asserts); `validate-essay-ingest.py` (hand-fed essay) |
| KERNELS-INDEX gap | **2 kernels missing from the table** | `commentary_lift`, `organism_factory_bridge` — both wired+validated, not indexed |
| L08 domain-expansions | **EMPTY** | no `lib/domains/`; `state.json` OVER-CLAIMS L08 as VALIDATED (fix Phase 0) |
| Tantrāloka (canonical DAG committed) | SOURCE 4,624 · **T1 264 · L0 1 · ARGMAP 0 · L2 0 · L200 0 · C1 0** | the 34-verse `translations.jsonl` = KILLED bypass runner, NOT canonical (see §3) |
| Registry backend | JSONL → **PG (flip LIVE in factory_loop.sh)** | `PATALA_REGISTRY_PG=1`, JSONL export after each pass |
| LOGICVID gold → enquiry | **NOT INGESTED** | `lib/enquiry.py` + `validate-enquiry.py` are HAND-FED the presence enquiry, not parsed from the real SPEC-40..48 gold |

**The 3 honesty problems (still true, now fully evidenced):**
1. `layers/*.md` stale — layers 00/03/04/05 say NOT_STARTED while kernels exist.
2. **THREE** competing taxonomies (00-09 spine / L00-10 / L00-12), with conflicting kernel→layer
   assignments (e.g. `review.py` = L04 in COHERENCE-AUDIT but L05 in KERNELS-INDEX; `query.py` = L06 vs
   L10; `scholar_review.py` = L05 vs L08; `next_action.py` = L09 vs L12).
3. GAPS.md stale (claims no projection compiler/surfaces — they're built); `state.json` over-claims L08.

---

## PHASE 0 — RECONCILE THE RECORD (do FIRST — everything else rests on it)

### 0.1 Fix the stale docs [P0] — VERIFIED STALE, all confirmed
- [ ] Regenerate `layers/*.md` to reality (00/03/04/05 are BUILT, not NOT_STARTED). Evidence:
  `layers/00-core-engine.md:33`, `layers/03-factory.md:25`, `layers/04-argument-engine.md:28`,
  `layers/05-review-gate.md:27` all say NOT_STARTED while `lib/{epistemic,factory_pool,proof_generators,review}.py` exist.
- [ ] Reconcile the layer taxonomy — pick ONE (the 00-09 spine). Evidence: 3 schemes conflict —
  `COHERENCE-AUDIT.md:21-32` (L00-10), `BUILT-BY-LAYER.md:16-25` (L00-10), `KERNELS-INDEX.md` (L00-12),
  `state.json` (L00-09). Rewrite to match.
- [ ] Resync GAPS.md. Evidence: it claims "no projection compiler/retrieval/surfaces" but
  `lib/{context_compiler,retrieval,seo,bundle_router}.py` all exist + validate.
- [ ] Fix `state.json:42` over-claim (L08 VALIDATED, but no `lib/domains/` — it's EMPTY).
- [ ] Bump SPEC-01/02/03 DRAFT → IMPLEMENTED. Evidence: still `**Status:** DRAFT` at `SPEC-01:3`,
  `SPEC-02:3`, `SPEC-03:3`, but `validate-dag.py` + `lib/epistemic.py` + argument graph all exist.

### 0.2 Fix the failing/weak validators [P0] — VERIFIED, numbers corrected
- [ ] `validate-provenance.py` — THEATRE confirmed. It reads data but all 4 `check()` asserts are
  hardcoded literals (e.g. `emit_nanopub("I1","","SCHOLARLY_CORROBORATED",...)`). Rewrite to assert on
  data-derived output. Evidence: `scripts/validate-provenance.py:71-72`.
- [ ] `validate-essay-ingest.py` — hand-fed confirmed. Essay injected as literals
  (`ing.structure("Le Soi et l'Autre", "Isabelle Ratié", [...])`), no file read. Either read real Ratié
  or mark PROVEN-MECHANISM. Evidence: `scripts/validate-essay-ingest.py:20-42`.
- [ ] **CORRECTED**: the "~24 kernels lack validators" / "21 named" list is STALE — 0 kernels lack any
  validator ref; only 16 lack a DEDICATED one (aggregate-covered); 18/21 named already have validators.
  Remaining truly-weak: `certificate`, `discovery`, `scholar_review` (covered only by aggregate
  `validate-kernels.py`).

### 0.5 THE ARCHITECTURE RULE [VERIFIED DONE for hermes/translation]
- [x] `hermes_exec.py` uses agentic `hermes chat` (not blind `-z`). Evidence: `lib/hermes_exec.py:41`.
- [x] `translation.py.generate()` calls Hermes. Evidence: `lib/translation.py:74`.
- [ ] `pushing_miner.py` add Hermes for NEW pushing generation — VERIFIED still open (zero hermes refs
      in `lib/pushing_miner.py`, pure regex). Correctly unchecked.

### 0.6 Peer-review-driven builds [VERIFIED — some superseded by the canonical decision]
- [ ] ~~Parallel factory worker pool~~ → **SUPERSEDED**: the DAG controller is patala's `factory_scheduler`
      (already parallel via `FACTORY_PARALLEL`). ip-graph's `factory_pool` is a shadow system to route back.
- [ ] Per-work translation-state FSM — route ip-graph's `next_action` through patala's `corpus_state`
      (`organism_factory_bridge.py` exists, 6/6).
- [ ] Argument-IR depth (CP4) — still real (nyayagate/crux_engine/ARG golds).
- [x] `misconception.py` repair cascade — DONE (9/9). Evidence: `lib/misconception.py`,
      `scripts/validate-misconception.py`.

---

## PHASE 1 — THE 5 MISSING KERNELS [ALL DONE — 2026-08-14] ✅

The docs-referenced kernels that "don't exist" were all built this session (REV 2 → current):
- [x] `lib/misconception.py` — the repair cascade (9/9). Evidence: `scripts/validate-misconception.py`.
- [x] `lib/question_growth.py` — the Question-Growth Engine (7/7). `validate-question-growth.py`.
- [x] `lib/enquiry.py` — the Enquiry-Discovery Organism (13/13). `validate-enquiry.py`.
- [x] `lib/design_provenance.py` — the Self-Proving full form (8/8). `validate-design-provenance.py`.
- [x] `lib/graph_stable.py` — the stable-graph projection (8/8). `validate-graph-stable.py`.

Kernel count now **52**. All registered in `KERNELS-INDEX.md`.

**Next:** the "missing kernels" gap is CLOSED. The record-consistency work (Phase 0: fix stale layers,
the 3-taxonomy conflict, GAPS, `state.json` L08 over-claim) and the 2 THEATRE validators are the remaining
Phase-0/trust items.

---

## PHASE 2 — CLOSE THE SECURITY + PRODUCT GAPS

### 2.1 Gap E — signed human attestation [P1] — VERIFIED MECHANISM-ONLY (not the crypto Gap E)
`lib/agent_delivery.py:93` `human_authorize()` is a plain state flip. `lib/patala_product.py:24` +
`system_provenance.py` use **plain SHA-256 with hardcoded secrets** (no ed25519/ecdsa/private-key).
Must become a real `HumanAttestation{actor, action, target_revision, scope, timestamp, signature}`.

### 2.2 Gap A — context paging [P1] — VERIFIED ABSENT
No `context_paging`/`virtualiz` anywhere. `context_compiler.py` only does prose projection.

### 2.3 L08 domain-expansions [P1] — VERIFIED ABSENT
No `lib/domains/`. This makes "generalization" code, not a statement.

### 2.4 L03 needs-build products [P1]
Commentary (passage-local) + live Tokenization (vidyut cheda data).

---

## PHASE 3 — THE MONA LISA: TANTRĀLOKA (REVISED for the canonical decision)

### 3.1 The sources are wired [DONE] — VERIFIED 5,860 kārikās
`scripts/ingest-tantraloka-root.py` → `data/tantraloka/root-verses.json` = exactly 5,860. Confirmed.

### 3.2 Wire the crux compass into the organism [P0] — STILL-OPEN
- [ ] The pushing-miner cruxes (TĀ 1/52-55 reflexivity) feed the Tantrāloka argument + crux layers.
- [ ] Replace hand-fed Tantrāloka validators with real ones.

### 3.3 Run the FULL stack on real Tantrāloka [P0] — **REVISED — premise invalidated**
- ~~translation via `hermes_exec` / per-verse from-scratch~~ → **WRONG / SUPERSEDED.** The canonical
  approach is patala's `factory_scheduler` DAG (argument-guided T1→ARGMAP→L0→L2→L200→C1). `ip-graph`
  must VALIDATE (TranslationProof/three-version/commentary_lift), not produce.
- [x] The canonical DAG is LIVE: `factory_scheduler --works tantraloka` producing T1 (164) → L0 → ARGMAP → L2.
- [ ] After the DAG produces L2, VALIDATE with `lib/translation.py` (TranslationProof) + `translation_variant`
      (three-version vs Dyczkowski) + `commentary_lift` (B3→B4). This is ip-graph's real Phase-3 job.
- [ ] theme cluster → essay → education → pedagogy → products, on real data.

---

## PHASE 4 — DEPLOY + COMPLETE THE READ PLANE

### 4.1 Deploy the surfaces [P1] — VERIFIED BUILT, NOT DEPLOYED
`web/` Astro built (`web/dist/` populated) + `edge/worker.js` + `wrangler.toml` (R2 `SITE`, KV, `/api/*`,
`/mcp` Streamable-HTTP 8-tools) all EXIST. NOT deployed (no wrangler publish; only local `astro preview`).
- [ ] `wrangler deploy` → Cloudflare Pages.
- [ ] Stand up the Worker + `/api/search` + `/mcp` endpoints.

### 4.2 The 5 import adapters [P2] — only scifact done.

---

## PHASE 5 — THE ORGANISM AT REAL SCALE

### 5.1 The self-executing agent loop [P0] — VERIFIED NOT WIRED
`ingestion_organism.py` imports only `next_action`/`source_registry`/`integrity_gate` — NOT
`hermes_exec` or `agent_delivery`. `refine()` just appends layer-name strings. The loop is a mechanism
stub. Wire `next_action` (decide) + real factory (execute) + gate (verify) — routing through patala's
scheduler.

### 5.2 Real consumer data [P1] — the organism's fuel.
### 5.3 Product surfaces [P2].

---

## PHASE 6 — USE THE ARCHITECTURE (wire the orphaned kernels) [THE BIG ONE — 2026-08-14]

*Added by the 3-agent architecture audit: ~52 kernels exist and validate, but only ~13 are wired into
any live path, and NONE into patala's production factory. The GEM/vision/clone machinery is OVER-PROVEN
and UNDER-FED: validators prove a machine, not a corpus. This phase makes the validated architecture
USED, not just proven — the same disease the translation divergence had, now fixed.*

### The audit result (verified by execution — see Proofs)
- **USED (13, ip-graph-internal only):** `integrity_gate`, `next_action`, `vidyut_l0`,
  `translation_variant`, `proof_generators`, `projection_dag`, + the read-plane kernels
  (`context_compiler`, `seo`, `bundle_router`, `fts_search`, `translation`, `commentary_lift`).
- **ORPHANED / VALIDATED-ONLY (16+):** `alignment_flywheel`, `verification_ensemble`, `open_ended_evolve`,
  `self_healing`, `skill_graph`, `structure_recall`, `ingestion_organism`, `iteration_confidence`,
  `canonical_contracts`, `factory_pool`, `organism_factory_bridge`, `misconception`, `question_growth`,
  `enquiry`, `design_provenance`, `graph_stable` — each has a passing validator but is referenced nowhere else.
- **CLONED-UNUSED (~30/48 repos):** paper-qa, pyBKT, graphiti, KAG, storm, salsa, cosign, scifact, the
  agent-runtime set — no kernel, no validator, dead clones.
- **The over-built layer:** the provenance/certification/signed-root substrate (`system_provenance`,
  `design_provenance`, `graph_stable`, `evidence_ledger`, `verification_ensemble`, `certificate`) is fully
  built but NOTHING compounds on it.

### 6.1 Wire the VALIDATOR STACK onto the running Tantrāloka DAG [P0 — DONE 2026-08-14]
`scripts/validate-tantraloka-dag.py` (8/8) wires `verification_ensemble` + `evidence_ledger` +
`integrity_gate` + `source_registry` onto the DAG's real committed T1/L0. The verifier moat is LIVE.
Output: `tantraloka/corpus/dag-validation.json`.

### 6.2 Wire the FLYWHEEL kernels into the organism / read plane [P1 — DONE 2026-08-14]
- `run-tantraloka-flywheel.py` (9/9): organism + pedagogy + misconception + question_growth + enquiry +
  design_provenance close the learner→repair→dissolve loop on real DAG data.
- `run-readplane-retrieval.py` (9/9): query (KG2Code) + retrieval (PathRAG/HippoRAG) + structure_recall
  (SAGE) serve the real read-plane graph.
- `run-tantraloka-organs.py` (7/7): self_healing + alignment_flywheel.
- `run-tantraloka-organs2.py` (7/7): skill_graph + iteration_confidence + canonical_contracts.
- `run-tantraloka-organs3.py` (9/9): open_ended_evolve + lightrag_compare + cognee_compare + graph_stable.

### 6.3 Route ip-graph's organisms through patala's factory [P1 — DONE 2026-08-14]
- `run-tantraloka-scheduler-bridge.py` (5/5): organism ranks by next_action, delegates to patala's
  corpus_state (ONE orchestrator).
- `run-tantraloka-organism.py` (7/7): ingestion_organism + factory_pool run the refine chain, routed
  through patala (ip-graph = SENSOR/decision, patala = EXECUTOR).

### 6.4 Promotion gate: every kernel wired = USED, not just VALIDATED [P0 — DONE 2026-08-14]
All 25 previously-orphaned/validated-only kernels are now USED in live paths (KERNELS-INDEX WIRED list).
Phase 6 COMPLETE.

---

## THE BUILD ORDER (Rev 3)

1. **Phase 0 first** — reconcile the record: counts to 52/97/84/6578, add `commentary_lift` +
   `organism_factory_bridge` to KERNELS-INDEX, fix state.json L08 over-claim + 47→52, rewrite GAPS.md,
   regenerate layers/*.md, bump SPEC-01/02/03 DRAFT→IMPLEMENTED, write a real README. Nothing is
   trustworthy until the record matches reality.
2. **Fix the 2 THEATRE validators** (`validate-provenance.py`, `validate-essay-ingest.py`) — make them
   data-derived (never hand-fed). Same phase as record reconciliation.
3. **Phase 7 — LOGICVID gold → enquiry** (the missing gold): parse the real SPEC-40..48/SPEC-36 gold
   transcripts into `DiscoveryProgression`s (taxonomy→theorem→boundary→frontier) + question-growth trees,
   DERIVED from the gold text. Replaces the hand-fed `validate-enquiry.py`. Feeds ontology/claims/gaps/
   pedagogy with real human-curiosity structure. [2026-08-15 in progress]
4. **Phase 3 + 6.1 (Tantrāloka)** — the canonical DAG (patala) produces; ip-graph wires the VALIDATOR
   STACK onto its real output + the crux compass (ARGMAP is the 0.118 fix path). The moat.
5. **Phase 6.2-6.3 (done)** + route organisms through patala's scheduler (one orchestrator).
6. **Phase 4 (deploy)** — read plane live (R2/CDN, Worker /api+/mcp); coordinate with agentpatala's
   openpatala surface.
7. **Phase 2 (security)** — Gap E signed attestation before marketplace; L08 domains.
8. **Phase 5 (real scale)** — X4 education/essay products off the validated corpus → learner data → organism.

**The honest one-line (Rev 3):** the machine is real (52 kernels, 97 experiments, 84 theatre proofs
38/46/0) and the translation path is CORRECT (patala's argument-guided DAG, PG-backed). The next
frontier is NOT more kernels — it is (a) reconcile the record to reality, (b) fix the 2 THEATRE
validators, (c) ingest the LOGICVID gold into the enquiry organism (missing gold), then (d) use the
validated Tantrāloka corpus to build real products and let the canonical DAG produce through ARGMAP.

## Proofs / resolution
- The canonical translation decision: `tantraloka/CANONICAL-TRANSLATION-ORCHESTRATION.md`
- The controller: `patala/pipeline/factory_scheduler.py` · the DAG: `contracts/CANONICAL-DAG.yaml`
- The Hermes thesis: `handover/hermes/CANONICAL.md`
- The record: `BUILT-BY-LAYER.md` (stale), `COHERENCE-AUDIT.md`, `KERNELS-INDEX.md`, `state.json`
- The Mona Lisa: `tantraloka/` (README + OPERATIONAL-PLAN)
- The kernels: `lib/` (52)
- The architecture audit: 3 parallel agents (GEM usage / vision-vs-built / clone-integration) —
  the "USED / VALIDATED-ONLY / ORPHANED / CLONED-UNUSED" classification, Phase 6 above
- The real execution: `lib/hermes_exec.py` · the crux compass: `lib/pushing_miner.py`
