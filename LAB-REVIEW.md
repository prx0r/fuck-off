# LAB-REVIEW — the state of the lab (what's real, what's exploratory, what's next)

*2026-08-14. The agent's starting point for "what have we actually built and what's worth doing next?"
This is our own anti-theatre review applied to the lab: every experiment categorized by patala layer +
vision, honest status (VALIDATED vs EXPLORATORY vs DISCOVERED), and a prioritized explore-next list.
Machine form: `data/references/experiments.json`. Read `AGENTS.md` (axioms) + `NAVIGATION.md` (index)
first.*

> **The one rule (our own):** a mechanism is not PRODUCTION because we demoed it. Most here are
> VALIDATED (prototype-level). Only honest statuses count. (patalamix review, SPEC-32.)

---

## 0. WHAT'S GENUINELY PROVEN (VALIDATED — in the test suite, gates pass)

41 experiments run; **21 PASS** in the authoritative suite (38/41 validations), the rest are
exploratory. The proven core:

| Capability | Kernel | Layer | What's proven |
|-----------|--------|-------|---------------|
| Epistemic envelope + invariant | `epistemic.py` | L00 | 0 violations; eigenius-order-preserving |
| Schema compiler | `schema.py` | L00 | single-source validation |
| Graph + DAG + themes | (data) | L02 | 490 nodes, communities match epistemic split |
| Provenance (nanopubs) | (validate-provenance) | L02 | ceiling→PROV-K |
| Staleness (RKA blast-radius) | `staleness.py` | L03 | PHYSICS retraction flags 8 layers |
| Counterfactual engine | `discovery.py` | L03 | THERMODYNAMICS most load-bearing |
| Crux compiler | (experiment) | L04 | indeterminism-necessity is the crux |
| Review reducer + cross-review | `review.py`,`scholar_review.py` | L05/08 | thesis stays CORRECTION; bias-robust |
| Mutation-testing (verifier self-audit) | (experiment) | L07 | 100% kill-rate |
| Retrieval (PathRAG/HippoRAG/KG2Code) | `retrieval.py`,`query.py` | L10 | PathRAG+KG2Code win; HippoRAG hub-bias |
| Education (learning claims) | `education.py` | L09 | wrong-answer→epistemic-neighbor |
| Organism (misconception graph) | `organism.py` | L09 | the demand sensor |
| Pedagogy (adaptive) | `pedagogy.py` | L09 | MasteryEvidence→reducer→next-interaction |
| Agent-delivery (contracts/gates) | `agent_delivery.py` | L09 | context-routing, budget, human gate |
| Evolution (MAP-Elites) | `evolve.py` | ALL | 6 niches, gen2 improves |
| Incremental (Salsa) | (experiment) | L03 | O(1) update, reuse-on-change |
| Execution branching + replay | (experiment) | L09 | checkpoint/branch/rollback + causal trace |
| Signed statements | (experiment) | L12 | sign+verify+tamper-detect |

---

## 1. BY PATALA LAYER (where the work lives)

| Layer | Built kernels | Status | Notes |
|-------|--------------|--------|-------|
| 00 Core | epistemic, schema | VALIDATED | envelope + schema compiler |
| 01 Corpus | (adapters) | VALIDATED | import_scifact; 5-adapter set incomplete |
| 02 Epistemic | (graph, provenance, certificate) | VALIDATED | graph + nanopubs + certification-weight |
| 03 Factory | staleness, discovery | VALIDATED | blast-radius + counterfactual + incremental |
| 04 Argument | (crux, rival) | VALIDATED | crux-compiler + justified-wins |
| 05 Research | review | VALIDATED | reducer + self-improve-as-PR |
| 06 Commentarial | (KORAL) | VALIDATED | reality vs literature separation |
| 07 Verification | (mutation-testing) | VALIDATED | self-auditing verifier |
| 08 Human Authority | scholar_review | VALIDATED | cross-review + bias-robust |
| 09 Organism/Education | education, organism, organism_loop, pedagogy, agent_delivery | VALIDATED | the deepest cluster (8 experiments) |
| 10 Surfaces | query, retrieval | VALIDATED | KG2Code + PathRAG/HippoRAG |
| 12 Live System | (merkle, reactive, signed) | VALIDATED | signed corpus + reactive docs + causal-operational graph |

---

## 2. BY VISION (the products we're building toward)

| Vision | Built mechanisms | Status |
|--------|-----------------|--------|
| Verified Epistemic OS | the 8 laws (all validated) | the substrate exists |
| Verified-Statement-Marketplace | certificate, signed-statement, discovery | mechanisms validated; no marketplace |
| Co-Evolving Epistemic Organism | organism, pedagogy, bkt, organism_loop | the loop works (human-gated) |
| What-If Machine | counterfactual, crux | discovery signal validated |
| Self-Proving System | signed-corpus, causal-operational | provenance validated |
| General Engine | import adapters (SciFact) | generalization proven, adapters incomplete |

---

## 3. EXPLORATORY (validated logic, not in the suite — RUN)

These are the original discovery experiments, now consolidated into kernels; keep as reference but the
kernels are canonical:
`herdr-review, rka-staleness, kg2code, pathrag, hipporag, context-coverage, nano-stable-graph,
unified-epistemic, counterfactual-engine, rival-argument, certification-weight, bkt-mastery,
signed-statement, communities` (all have PASS status logic; the kernels supersede them).

---

## 4. THE REVIEW CRITIQUES (what our reviewers told us — track these)

From **patalamix (SPEC-32)** + earlier reviews:
- **Honest statuses** (DONE was theatre) → adopted: DISCOVERED/PROTOTYPED/VALIDATED/INTEGRATED/PRODUCTION.
- **Real MAP-Elites** (behavioral niches + cost/latency) → adopted.
- **7 missing gaps**: A context-paging · B execution-branching · C deterministic-replay · D content-
  addressed run-traces · E signed-human-auth · F workspace-isolation · G local-first-workstation.
  B/C now built (`execution-replay`). E (signed attestation) is the next critical one.
- **5th graph** (causal-operational) → built.
- **The killer milestone**: ONE IPVV claim through the whole stack (source→translation→proof→
  proposition→argument→review→attestation→synthesis→essay→education→agent-bundle), then mutate the
  source and watch the organism react. Not yet done — this is the real graduation test.

---

## 4.5 THEATRE AUDIT (honest — which validators test real data vs synthetic demo)

This is our anti-theatre review applied to the validators themselves (2026-08-14):

| Validator | Real data? | Verdict |
|-----------|-----------|---------|
| `validate-stack.py` | **YES** — real graph + argument + DAG + reducer + invariant | **REAL** (the graduation test, 9/9) |
| `validate-dag.py` | YES — real canonical-dag.yaml | REAL |
| `validate-provenance.py` | YES — real argument ceilings → PROV-K | REAL |
| `validate-layer03-05.py` | YES — real DAG + argument | REAL |
| `validate-layer10.py` | YES — real concept graph | REAL (PathRAG/KG2Code) |
| `validate-education-organism.py` | partial — real argument + synthetic learner | MIXED |
| `validate-kernels.py` | partial — real graph for query/retrieval; synthetic for certificate/discovery | MIXED |
| `validate-products.py` | partial | MIXED |
| `validate-evolve.py` | **NO** — hardcoded STRATEGIES fitness dicts | SYNTHETIC (proves mechanism, not integration) |
| `validate-agent-delivery.py` | **NO** — mock contract + mock agent | SYNTHETIC |
| `validate-organism-loop.py` | **NO** — simulated question/variants | SYNTHETIC |
| `validate-pedagogy.py` | **NO** — synthetic learner + mock fixtures | SYNTHETIC |

**The honest truth (and the v2/migration critique):** the lab has proven the MECHANISMS, but only
`validate-stack` + a few prove them on the REAL patala pipeline. The pedagogy/organism/evolution
validators demonstrate the mechanism on toy inputs — they don't prove it's wired into the real kernel.
**The fix is not more docs; it's the graduation test** (real data through real kernels), which
`validate-stack.py` starts and the full "one claim through the whole stack" completes.

---

## 5. WHAT'S WORTH EXPLORING NEXT (prioritized, agent-actionable)

**P0 — the graduation test** (highest value, per patalamix #15):
Build ONE claim end-to-end through the whole stack on real evidence (start with our two-stage free-will
argument as the stand-in for IPVV), then mutate a premise and verify the whole organism reacts
(staleness→reactive essay→pedagogy regeneration→signed re-release). This is what turns the lab into
the kernel.

**P1 — close the review gaps:**
1. **Signed human attestation** (gap E) — replace plain `human_authorize()` with a signed
   HumanAttestation (cosign-style). Before any "marketplace" or public authority.
2. **Context paging** (gap A) — lossless context virtualization for agent runs.
3. **The remaining 3 import adapters** (OpenAlex, S2ORC, xAIF) — finish the generalization test.

**P2 — deepen what's promising:**
- **Cross-graph queries** — combine epistemic + causal-operational graphs ("why do we believe X AND why
  did we act on it?").
- **The flywheel demo** — connect organism-loop + pedagogy + evolution end-to-end: a learner's confusion
  → gap → intervention → improvement → fewer confusions (measure the loop closing).
- **MAP-Elites on a real translation task** (patalamix EXP-43) — literalness×intervention grid, 100
  candidates, see if distinct useful niches survive.

---

## 6. HOW TO USE THIS (for an agent)

1. Read `AGENTS.md` (axioms) → `NAVIGATION.md` (index) → this file (state of the lab).
2. To find what's proven: §0. To find a layer: §1. To find a vision: §2.
3. To decide what to build: §5 (prioritized explore-next).
4. Before claiming "done": run `scripts/run-tests.py` (must pass) + reconcile `STATE.yaml` honestly.
