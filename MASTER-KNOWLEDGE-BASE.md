# MASTER-KNOWLEDGE-BASE — everything we've built, in one authoritative reference

*2026-08-14. A synthesized master reference of the **Verified Epistemic OS** lab. This condenses the
full state — 17 kernels, 51 experiments, 32 arXiv papers, 99 repo catalog (41 cloned), 46 specs, 10
visions, 11 layers — into one agent-loadable map. Use this to know WHAT exists and WHERE before
building. Ground-truth counts verified against `data/references/*.json`, `lib/`, `scripts/`,
`specs/`. Honest statuses only — nothing claimed beyond what's proven.*

---

## 0. THE PROJECT IN ONE PARAGRAPH

The `ip-graph` lab evolved from a **knowledge graph** into the **Verified Epistemic OS** — a
domain-agnostic engine (pāṭala's 2nd-gen kernel) where machines propose, reducers gate, humans
adjudicate, staleness propagates, truth is signed + replayable, agents navigate via executable
queries, learners drive pedagogy, and questions grow new knowledge. It proves these mechanisms on the
Doyle corpus before the IPVV graduation test. The core philosophy: honest statuses, no theatre, one
derivation graph = correctness + staleness + scheduler + retrieval.

---

## 1. THE 17 KERNELS (`lib/`) — what each does

| Kernel | Core mechanism | Layer | Invariant/gate |
|--------|---------------|-------|----------------|
| `epistemic.py` | EpistemicEnvelope + 4-axis Authority + `invariant_ok` | L00/L01 | projection ceiling ≤ parent |
| `schema.py` | single-source schema compiler | L00 | every object validates against one schema |
| `review.py` | herdr reducer state machine | L05/L08 | nothing promotes without evidence; only human→ADJUDICATED |
| `scholar_review.py` | adversarial panel + citecheck + anti-groupthink | L08 | citation must resolve; blocking finding blocks |
| `staleness.py` | blast-radius + review_queue + rebuild order | L03/L12 | retraction flags all downstream stale |
| `query.py` | KG2Code executable graph-query DSL | L10 | deterministic verifiable trace |
| `retrieval.py` | PathRAG flow + HippoRAG PPR | L10 | (HippoRAG is hub-biased — known finding) |
| `translation.py` | TranslationProof 11-dim audit vector | L03 | publication blocked on any hard-dim fail |
| `certificate.py` | Certification Weight (compounding) | L02 | factors from validated subsystems |
| `discovery.py` | Research Value Score | L03 | value = load-bearing × weak-verified × contested |
| `education.py` | LearningClaim + wrong_answer_to_neighbor | L09 | education is a projection of the graph |
| `organism.py` | UserKnowledgeState + MisconceptionGraph | L09 | consumer = sensor for comprehension failure |
| `organism_loop.py` | 10-stage consumer→research machine | L09 | agents propose; human_authorize = only path to truth |
| `pedagogy.py` | live adaptive pedagogy (mastery reducer) | L09 | targets weakest skill |
| `evolve.py` | MAP-Elites evolution (Pareto incl. cost) | L05 | only better+distinct candidates promote |
| `agent_delivery.py` | task contract + budget + context routing | L09 | human gate for canonical truth |
| `essay_ingest.py` | 9-stage essay-as-derivation-input | L04-09 | essay = derivation input, not dead prose |

**The 5 architecturally load-bearing mechanisms:**
1. **Epistemic ceiling invariant** (`epistemic.py`) — the honesty law making the graph real, not a
   hallucination dump. 0 violations across the real graph.
2. **Human publication gate** (herdr) — in review/organism_loop/agent_delivery/evolve: agents propose,
   only humans authorize canonical truth.
3. **DAG staleness / blast-radius** (`staleness.py`) — the self-maintaining property; source change →
   downstream flagged → rebuild order.
4. **Review reducer + anti-groupthink panel** — deterministic evidence-gated promotion, bias-robust
   (37.1% reviewer bias survived).
5. **Education/organism moat** — wrong-answer→known-neighbor, mastery-reducer targeting weakest skill;
   closes consumer→research→graph flywheel.

---

## 2. THE 51 EXPERIMENTS — grouped by layer (proven = PASS/real; RUN = mechanism demo)

**L00-02 (envelope/provenance/marketplace):** validate-provenance (ceiling→PROV-K, real), eigenius-grades
(order-preserving), certification-weight (CW 36→1683 compounding), nano-stable-graph (deterministic GraphML).

**L03 (factory/staleness/what-if):** validate-layer03-05 (**PHYSICS retraction → FREE_WILL** + reducer gate,
REAL), rka-staleness (8 layers flagged), counterfactual-engine (THERMODYNAMICS most load-bearing, 11
downstream), salsa-incremental (O(1) memoized rebuild).

**L04 (argument/crux/enquiry):** crux-compiler (minimal divergence = INDETERMINISM necessity, REAL),
question-growth (question→theorem→boundary→frontier + PrimitiveRobustness), enquiry-discovery
(taxonomy+theorem+boundary+frontier from LOGICVID), gem-extraction (unseen gems from pushing),
essay-as-engine (mine Ratié→claim+argument+crux+evidence).

**L05/08 (review/scholar):** herdr-review (thesis stays CORRECTION), cross-review (4-phase adversarial),
review-bias (37.1% robust), rival-argument (justified claim wins), self-improve (weak proposal rejected),
validate-evolve (MAP-Elites 6 niches gen2 improves).

**L09 (education/organism/agent):** validate-education-organism, validate-pedagogy (7/7), validate-
organism-loop (8/8), validate-agent-delivery (10/10), bkt-mastery (pyBKT), evolving-memory (dream-cycle
consolidation), graphiti-temporal (valid_at/invalid_at replay), curiosity-patterns (from LOGICVID gold),
execution-replay (checkpoint/rollback/branch = gaps B+C).

**L10 (retrieval/executable):** pathrag (flow-pruned paths, REAL), hipporag (PPR, HUB-BIAS found),
kg2code (executable DSL, verified trace QM→FreeWill), validate-layer10 (PathRAG+KG2Code win), bounded-context,
context-coverage.

**L12/cross (self-proving):** signed-statement (cosign-style), signed-corpus (Merkle), reactive-essay
(source retraction→prose stale), causal-operational-graph (**the 5th graph**: Event→Run→Artifact→Finding→
Task→Event), claim-standardisation (structural claim vs tradition vocab, L06), koral-twograph (reality vs
literature, L06), unified-epistemic (kappa+herdr+RKA unified), verified-lifecycle (one claim through 8 laws),
**validate-stack (THE graduation/anti-theatre test, 9/9 REAL)**, validate-essay-ingest (9-stage on real
Ratié, 8/8), validate-products.

**Theatre truth:** 24 PROVEN on real data / 26 PROVEN-MECHANISM (synthetic) / 0 UNPROVEN. The
data-grounded tests are validate-stack, validate-layer03-05, validate-essay-ingest, pathrag, hipporag,
kg2code, crux-compiler. Several RUN scripts (essay-as-engine, enquiry-discovery, question-growth,
gem-extraction, claim-standardisation) encode the mechanism in hardcoded data + print a narrative — they
demonstrate the shape, not a source-verified pipeline. THE fix = the graduation test.

---

## 3. THE 32 ARXIV PAPERS + 7 ALGORITHMS

**Catalog statuses:** 11 graph-reasoning · 6 agent-rl · 4 agent-memory · 4 agent-eval · 3 agent-orchestration
· 2 agent-frameworks · 2 skills-datasets. Most are **GAP** (to adopt); few REFERENCE; PathRAG VALIDATES-ish;
**KG2Code = BET 2**, **HyperGraphRAG = BET 1**.

**The 7 algorithms (docs/ALGORITHMS.md):**
- **PathRAG** (2502.14902) — flow-based pruning; `S(vi)=Σ α·S(vj)/|N(vj)|, α=0.7`, path reliability,
  ascending-reliability prompting. ⭐ IMPLEMENTED (`lib/retrieval.py`).
- **HippoRAG** (2405.14831) — Personalized PageRank; ⭐ IMPLEMENTED; **hub-bias finding**.
- **KG2Code** (2607.22652) — KG→executable code; `resolve/neighbors/path/evidence` DSL. ⭐ IMPLEMENTED
  (**Bet 2**, promoted to `lib/query.py`).
- **ToG-2** (2407.10805) — alternating graph+context retrieval. GAP (adopt into trace/investigate).
- **SubgraphRAG** (2503.09287) — smallest useful subgraph. GAP (combine with bounded-context).
- **G-reasoner/GFM-RAG** (2509.24276) — graph foundation model. GAP (`export_gfm_graph()` interop).
- **HyperGraphRAG** (2505.07426) — n-ary/hypergraph structure. GAP (**Bet 1**: keep Argument non-flat).

**Only 3 of 7 are coded** (PathRAG/HippoRAG/KG2Code). ToG-2/SubgraphRAG/GFM-RAG/HyperGraphRAG are
read-only, pending adoption into Layers 04/06/07. KORAL is catalog-GAP but implemented
(`experiment-koral-twograph.py`, Layer 06).

---

## 4. THE ECOSYSTEM — 41 cloned repos (of 99 cataloged)

- **20 validated as experiments** (Tier 1 ✅): herdr-workflow, rka, knowledgeProvenance, nano-graphrag,
  PathRAG, HippoRAG, eigenius, self-improving-agent, evolving-memory, graphiti, pyBKT, cosign, openevolve,
  axplorer, salsa, agentstateprotocol, deterministic-memory-layer, adversarial-review, AgentReview, scifact.
- **21 reference-only** (Tier 2 📖): maestro, arcan, loom, loom-valkor, mcp-agent, mcp-spec, agent-kit,
  cmu-paper-reviewer, agent-review-panel, EverOS, dbos, graphrag, KAG, instagraph, sage-wiki,
  seventeen-centuries, kappa-graph, storm, literature-review-toolkit, paper-qa, nodedb.
- **~15 Tier 3 not cloned** (EleutherIA, DSPy, vouch, temporal, dapr, autogen, Microsoft GraphRAG,
  context-paging, inspect_ai, etc.).
- Note: only 4 cloned dirs retain `.git` (maestro, loom-valkor, kappa-graph, rka); rest are bare trees.
- **The 5 import adapters** (the generalization test): openalex, s2orc, scifact, xaif, eleutheria —
  only scifact done; others incomplete.

---

## 5. THE 10 VISIONS + 8 LAWS + 6 FRONTIERS

**The 8 laws (VISION-VERIFIED-EPISTEMIC-OS.md):** 1 epistemic honesty (eigenius+envelope) · 2 deterministic
promotion (herdr) · 3 self-maintaining staleness (RKA) · 4 temporal truth (graphiti+Merkle) · 5 publishable
provenance (PROV-K) · 6 executable retrieval (KG2Code+PathRAG+HippoRAG) · 7 reactive documents · 8 verified
self-knowledge (mutation testing + crux compiler).

**The 8 product visions + status:** Verified OS (VALIDATED) · Verified-Statement-Marketplace (CW+signing
validated, no marketplace) · Co-Evolving Organism (loop+pedagogy validated, human-gated) · What-If Machine
(counterfactual+crux+Research-Value validated) · Self-Proving System (signed corpus + causal-operational
validated) · General Engine (SciFact/EleutherIA proven, adapters incomplete) · Question-Growth Engine
(question tree + PrimitiveRobustness prototype) · Enquiry-Discovery Organism (questions reveal structure,
from LOGICVID gold). + THESIS-REVERSE-DELIVERY (the vcreate methodology).

**The 6 unconsidered frontiers:** A OS-dreams-in-public · B counterfactual-engine (whole-graph) · C
cross-organism-learning (learner error → source-repair) · D verifier-as-rival (hostile debater) · E temporal-
scholarship · F epistemic-provenance-of-the-system-itself.

---

## 6. THE 46 SPECS (grouped)

**Core spine:** SPEC-00 (INFRA-BUILD: compiler/factory) · SPEC-01 (canonical-dag) · SPEC-02 (epistemic-
envelope) · SPEC-03 (argument-graph AIF) · SPEC-13 (staleness toolbox) · SPEC-14 (frontier-layer-builds).
**Surveys (REF):** SPEC-07 ecosystem · SPEC-08 graph-reasoning · SPEC-09 agent-orchestration · SPEC-10
frontier-agent · SPEC-11 agent-memory · SPEC-12 agent-harness. **Pāṭala subsystems (REF):** SPEC-15
adversarial-scholar-workbench · SPEC-16 proof-carrying-translation · SPEC-17 githubs substrate · SPEC-18
complete-pipeline · SPEC-19 doyle-experiments (knowledge build system). **Education/organism (REF):**
SPEC-20 education-organism (wrong_answer_to_neighbor moat) · SPEC-21 consumer-organism · SPEC-22
consumer-organism-tech · SPEC-23 patala-organism · SPEC-24 organism-visions · SPEC-25 organism-meh (compose
BKT/FSRS) · SPEC-26 education-n · SPEC-27 education-2 · SPEC-28 education-global (education compiler) ·
SPEC-29 education-main (the motherlode). **Reviews (REF):** SPEC-30 hermes-peer-review · SPEC-31
patala-peer-review · SPEC-32 patala-mix-review (context paging). **Pushing (REF):** SPEC-33 pushing-guide ·
SPEC-34 autonomous-pushing · SPEC-35 comparative-pushing · SPEC-36 logicvid3 (PrimitiveRobustness).
**LOGICVID gold:** SPEC-40 logicdog · SPEC-41 logicframework (6 levels M→D→B→N→W→R) · SPEC-42 logicvidsmethod
· SPEC-43 logicvid-postmortem · SPEC-44 logicframework2 (internal self-determination) · SPEC-46 logic5
(presence≠manifestation≠consciousness≠experience) · SPEC-47 logic6 (self-present≠self-known≠self-validating
≠infallible≠liberating) · SPEC-48 logic7 (R/K/M; K=M unresolved = frontier) · SPEC-3x SESSION-Q1 +
SESSION-OBJECTIONS (Tantrāloka TĀ 1/52-55 reflexivity). *(SPEC-36 == SPEC-45, identical content.)*

---

## 7. THE LOGICVID GOLD — 5 findings (live human curiosity, the rarest data)

1. **Curiosity is not random** — repeatable structure: live-issue, distinction-forensics, tension,
   honest-boundary (the curiosity markers).
2. **Enquiry reveals topic structure** — presence enquiry DISCOVERED a taxonomy + theorem + boundary +
   frontier. Questioning = data about the topic.
3. **Agentic gem extraction** — pushing surfaces unseen gems (PENETRATION 1: asserts a collapse it doesn't
   prove).
4. **Cross-tradition standardisation** — same structural claim (determination requires self-reference)
   appears as vimarśa / svasaṃvedana / self-presence / metacognition; separable into claim+vocab+boundary.
5. **Convergence as epistemic signal** — same primitive rediscovered from many directions = fundamentality
   (basis of PrimitiveRobustness).

---

## 8. STATE BY LAYER (`STATE.yaml`) + THE HONEST DEBT

**Every layer VALIDATED except 07-surfaces (DISCOVERED).** "VALIDATED = prototype, not production." The
honest gaps (A-G, all DISCOVERED in STATE.yaml): A context-paging (NOT built) · B execution-branching
✅ BUILT · C deterministic-replay ✅ BUILT · D content-addressed run-traces (NOT) · E signed human
attestation (NOT — critical before marketplace; agent_delivery uses plain human_authorize) · F workspace
isolation (NOT) · G local-first workstation nodedb (cloned, NOT).

---

## 9. THE ROADMAP (DEV_PLAN/TODO/GAPS priorities)

- **P0 — the graduation test** (the biggest lever): ONE claim end-to-end on real evidence (two-stage
  free-will as IPVV stand-in), then MUTATE a premise and verify the whole organism reacts (staleness→
  reactive essay→pedagogy→signed re-release). `validate-stack.py` starts it. **THE next milestone.**
- **P1 — close gaps:** E signed attestation (before marketplace) · A context paging · 3 remaining adapters
  (openalex, s2orc, xaif).
- **P2 — deepen:** LOGICVID gold → enquiry graph (SPEC-40..48 → DiscoveryProgressions) · enquiry-discovery
  → pedagogy · MAP-Elites on real translation · essay-ingest on a FULL source.

---

## 10. HOW TO ORIENT FAST (the resolve chain)

```
Question → TRACEABILITY-MAP.md (vision+layer) → KERNELS-INDEX.md (kernel) → the validating
experiment (scripts/) → the source repo (ecosystem/ or arXiv) → the spec (specs/) → the doc (docs/)
```
The 5 most important things to know: (1) validate-stack.py is the only real end-to-end pipeline,
(2) epistemic ceiling invariant is the load-bearing law, (3) the human publication gate is everywhere,
(4) staleness blast-radius is the self-maintaining mechanism, (5) the graduation test is the #1 next step.
