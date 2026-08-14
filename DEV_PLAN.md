# DEV PLAN — from vision to working epistemic engine (CURRENT, post-audit)

*2026-08-14. The executable roadmap, refreshed after the 4-agent completeness audit. This replaces the
stale pre-audit plan. It reflects what's ACTUALLY built (40 kernels, 83 experiments, 82/82 tests), the
honest gaps the audit found, and the correct build order. A task is DONE only when it passes its gate +
`STATE.yaml` + `CHANGELOG.md` are updated.*

---

## THE HONEST STATE (verified by the 4-agent audit, not the docs)

| Metric | Value | Notes |
|---|---|---|
| Kernels (`lib/`) | **40** | all pure mechanisms except `hermes_exec` (real `hermes -z` execution) |
| Experiments | **83** | 41 validate + 42 experiment/audit |
| Tests | **82/82** | fixed the 4 failures (graph ceilings, state drift) |
| Theatre (strict data-flow) | **19 REAL / 21 SYNTHETIC / 1 THEATRE** | the "34 PROVEN" marker count is inflated |
| Kernels w/o real-data validator | ~24 | the biggest anti-theatre gap |
| Docs-referenced kernels that DON'T exist | **5** | `misconception`, `question_growth`, `enquiry`, `design_provenance`, `graph_stable` |
| L08 domain-expansions | **EMPTY** | claimed VALIDATED but vision-only |
| Dead clones | 15 of 47 | cloned, unused |
| Unused external assets | pushing sessions (now wired), Ratié chapters, IPVV essays | |

**The 3 honesty problems (worse than missing code):**
1. `layers/*.md` is stale — says NOT_STARTED for built layers.
2. Two competing layer taxonomies (00-09 spine vs L00-L12 kernel-grouping) contradict across COHERENCE-AUDIT / BUILT-BY-LAYER / KERNELS-INDEX.
3. GAPS.md is stale (claims no projection compiler/surfaces — they're built).

---

## PHASE 0 — RECONCILE THE RECORD (do FIRST — everything else rests on it)

### 0.1 Fix the stale docs (cheap, unblocks trust) [P0]
- [ ] Regenerate `layers/*.md` to match reality (L00-L07+L09 BUILT/PARTIAL, L08 EMPTY).
- [ ] Reconcile the layer taxonomy — pick ONE (the 00-09 spine) and rewrite COHERENCE-AUDIT /
      BUILT-BY-LAYER / KERNELS-INDEX / state.json to match.
- [ ] Resync GAPS.md (drop the "no read plane" claims).
- [ ] Bump SPEC-01/02/03 from DRAFT → IMPLEMENTED (they ARE implemented).

### 0.2 Fix the failing/weak validators [P0]
- [ ] `validate-provenance.py` — the one THEATRE case (reads data, asserts on hand-fed constants). Rewrite
      to assert on data-derived output.
- [ ] Add real-data validators for the ~24 kernels that lack one (education, pedagogy, organism,
      organism_loop, agent_delivery, evolve, certificate, discovery, essay_ingest, evidence_ledger,
      alignment_flywheel, integrity_gate, next_action, vidyut_l0, verification_ensemble, translation_variant,
      open_ended_evolve, self_healing, skill_graph, ingestion_organism, scholar_review).
- [ ] `validate-essay-ingest.py` — header claims "real Ratié, 8/8" but the essay is hand-fed. Either read
      the real Ratié chapter or mark PROVEN-MECHANISM.

### 0.3 Index + validate `hermes_exec.py` [P0]
- [ ] It's the real execution path but has NO validator and is the 40th kernel not fully tracked.
- [ ] Build `validate-hermes-exec.py` (a real `hermes -z` call that returns the expected token).

### 0.4 STEAL from `hound` (scabench-org, cloned) — iteration-verified confidence [P1]
Hound's `DynamicNode` carries `observations` (verified) vs `assumptions` (unverified) + `iteration: int`
(how many passes confirmed a claim). That's a stronger epistemic signal than our binary ceiling:
- [ ] Extend `lib/epistemic.py` / `lib/evidence_ledger.py` with **iteration-verified confidence** — a claim
      confirmed across N independent passes is more trustworthy than one at the same ceiling.
- [ ] The **scout/strategist split** (cheap model explores, heavy model reasons) as a cost-efficiency
      extension to `next_action` — currently we don't split exploration vs deep reasoning.

---

## PHASE 1 — THE 5 MISSING KERNELS (docs reference them, they don't exist)

### 1.1 `lib/misconception.py` — the repair cascade [P1, closes Frontier C + the organism's closing edge]
`MisconceptionLikelihood = f(cluster_size, persistence, ambiguity_signal, novice_rate)` → cross threshold →
source flagged for scholar review → RKA propagate fix → confusion measured to dissolve.

### 1.2 `lib/question_growth.py` — Question-Growth Engine [P1]
The question tree + PrimitiveRobustness (currently only `experiment-question-growth.py`). Wire the 35
pushing sessions' cruxes as the growth seeds.

### 1.3 `lib/enquiry.py` — Enquiry-Discovery Organism [P1]
DiscoveryProgression (taxonomy→theorem→boundary→frontier) from the LOGICVID gold + pushing cruxes.

### 1.4 `lib/design_provenance.py` — Self-Proving full form [P2]
Every design decision → signed nanopub (the design-decision provenance, extends `system_provenance`).

### 1.5 `lib/graph_stable.py` — stable-graph (Co-Evolving Organism) [P2]
The stable-graph projection for the organism.

---

## PHASE 2 — CLOSE THE SECURITY + PRODUCT GAPS

### 2.1 Gap E — signed human attestation [P1, before any marketplace]
Replace plain `human_authorize()` with a cryptographic `HumanAttestation{actor, action, target_revision,
scope, timestamp, signature}`. Reuse `system_provenance` cosign-style signing.

### 2.2 Gap A — context paging [P1]
Lossless context virtualization over the compiled bundles (the agent read-plane is incomplete without it).

### 2.3 L08 domain-expansions — build the EMPTY layer [P1]
The pluggable-domain abstraction: `domains/science/`, `domains/philosophy/`, `domains/sanskrit/` subclass
modules over the core envelope. This makes "generalization" code, not a statement.

### 2.4 The L03 needs-build products [P1]
- Commentary (passage-local) — the missing spine step.
- Live Tokenization (vidyut cheda data download).

---

## PHASE 3 — THE MONA LISA: TANTRĀLOKA (the canonical full-stack test)

### 3.1 The sources are wired (done) [DONE]
`ingest-tantraloka-root.py` (5,860 kārikās), Dyczkowski vols, `pushing_miner.py` (35 sessions → cruxes).

### 3.2 Wire the crux compass into the organism [P0, the highest-value next build]
- [ ] The pushing-miner cruxes (TĀ 1/52-55 reflexivity) feed the Tantrāloka argument + crux layers.
- [ ] Replace the hand-fed Tantrāloka validators with real ones: translation (via `hermes_exec`),
      argument (auto-mine from the root), vs-Dyczkowski (already fixed to extract real text).

### 3.3 Run the FULL stack on real Tantrāloka [P0]
- [ ] theme cluster → essay (auto-mined) → education → pedagogy → products, all on real data.
- [ ] The from-scratch translation via `hermes_exec` (real model output, not hand-fed).

---

## PHASE 4 — DEPLOY + COMPLETE THE READ PLANE

### 4.1 Deploy the surfaces [P1]
- [ ] `astro build` → Cloudflare Pages (the static site is built, never deployed).
- [ ] Stand up the Worker (`edge/worker.js` + `wrangler.toml`) with R2+KV.
- [ ] Add `/api/search` + `/mcp` (Streamable HTTP) endpoints to the live Worker.

### 4.2 The 5 import adapters [P2]
- [ ] openalex / s2orc / xaif / eleutheria (only scifact done) — completes the generalization test.

---

## PHASE 5 — THE ORGANISM AT REAL SCALE

### 5.1 The self-executing agent loop [P0]
`next_action` (decide) + `hermes_exec` (execute) + `agent_delivery` (gate) wired into the `ingestion_organism`
refinery — the real autonomous loop, not the mechanism demo.

### 5.2 Real consumer data [P1]
The organism's fuel. Stand up the surfaces so real learners probe → misconception graph → re-prioritize.

### 5.3 The product surfaces (mechanism → product) [P2]
- Verifier-strength ledger (marketplace) · question-growth UI · enquiry-discovery UI.

---

## THE BUILD ORDER (why)

1. **Phase 0 first** — reconcile the stale docs + fix the theatre validators. Nothing else is trustworthy
   until the record matches reality.
2. **Phase 1 (missing kernels)** — `misconception.py` closes the organism's flywheel; the others are
   docs-promised.
3. **Phase 2 (security + products)** — gap E before any marketplace; L08 is the empty layer.
4. **Phase 3 (Tantrāloka)** — the canonical proof, now that the crux compass is wired.
5. **Phase 4 (deploy)** — make the read plane live.
6. **Phase 5 (real scale)** — the agentic loop + real consumer data.

**The honest one-line:** the machine is real (82/82) but the RECORD of it is not (stale docs, two
taxonomies, 21 synthetic validators over-marketed as real). Fix the record (P0), build the 5 missing
kernels + the empty L08 (P1-2), prove it on Tantrāloka with real Hermes execution (P3), deploy (P4), then
let real consumers drive the organism (P5).

## Proofs / resolution
- What's real: `BUILT-BY-LAYER.md` (but stale numbers), `scripts/audit-theatre-dataflow.py` (the strict gate)
- What's honest: the audit findings above (4 parallel agents)
- The Mona Lisa: `tantraloka/` (README + OPERATIONAL-PLAN + the 6 validators)
- The real execution: `lib/hermes_exec.py`
- The crux compass: `lib/pushing_miner.py` + `scripts/validate-pushing-miner.py` (7/7)
