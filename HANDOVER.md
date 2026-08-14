# HANDOVER — session state & where to continue

*2026-08-14. The complete handover for the next agent/session. Everything built, the honest state, the
proven core, the theatre risks, and exactly what to do next. Read `AGENTS.md` (axioms) + `NAVIGATION.md`
(index) + `LAB-REVIEW.md` (state) first — this file is the session narrative + continuation guide.*

---

## 1. WHAT THIS PROJECT IS NOW

The `ip-graph` lab (`fuck-off`) has evolved from a **knowledge graph** into the **Verified Epistemic OS**
— a domain-agnostic engine where machines propose, reducers gate, humans adjudicate, staleness
propagates, truth is signed + replayable, agents navigate via executable queries, learners drive
pedagogy, and questions grow new knowledge. It is patala's second-generation kernel, proving mechanisms
on the Doyle corpus before the IPVV graduation test.

**Core philosophy (from patalamix/v2 reviews):** honest statuses, no theatre, one derivation graph =
correctness + staleness + scheduler + retrieval, and the graduation test (real data through the whole
stack) is what makes a mechanism real.

---

## 2. WHAT'S BUILT (the 37 reusable kernels)

| Kernel | What it does | Theatre verdict |
|--------|-------------|-----------------|
| `epistemic.py` | envelope + 4-axis authority + invariant | PROVEN (real data) |
| `review.py` | herdr reducer (promotion gate) | PROVEN |
| `staleness.py` | RKA blast-radius + rebuild order | PROVEN |
| `query.py` | KG2Code executable graph queries | PROVEN |
| `retrieval.py` | PathRAG + HippoRAG | PROVEN |
| `schema.py` | single-source schema compiler | PROVEN |
| `scholar_review.py` | adversarial panel + cross-review + citecheck | PROVEN |
| `translation.py` | TranslationProof (non-aggregate vector) | PROVEN |
| `certificate.py` | Certification Weight (compounding) | PROVEN |
| `discovery.py` | Research Value Score | PROVEN |
| `education.py` | LearningClaim + interaction compiler | PROVEN-MECHANISM |
| `organism.py` | UserKnowledgeState + MisconceptionGraph | PROVEN-MECHANISM |
| `organism_loop.py` | consumer→research machine | PROVEN-MECHANISM |
| `pedagogy.py` | live adaptive pedagogy | PROVEN-MECHANISM |
| `evolve.py` | MAP-Elites evolution loop | PROVEN-MECHANISM |
| `agent_delivery.py` | task contract + context routing + budget + human gate | PROVEN-MECHANISM |
| `essay_ingest.py` | essay-as-derivation-input: 9-stage pipeline (structure→claims→evidence→argument→crux→review→pedagogy→reactive) | PROVEN (real Ratié data) |

## 3. THE THEATRE AUDIT (verifiable proofs)

**`scripts/theatre-check-all.py`** runs every experiment and stores a proof record (test exists +
passes + real-data + claim + hash) → `data/references/theatre-proofs-all.json`.

**Result (52 experiments, self excluded):**
```
25 experiments PROVEN on real data
27 PROVEN-MECHANISM (synthetic — mechanism works, not integrated)
 0 UNPROVEN
```

**The honest gap:** 26 experiments prove the mechanism on synthetic/stand-in data but aren't yet wired
into a real patala pipeline. Many DO use real exemplar data (the LOGICVID gold — live human curiosity),
which is valuable but not the graph integration test. The fix = the graduation test.

---

## 4. THE GOLD EXEMPLARS (live human curiosity — the rarest data)

The LOGICVID files (SPEC-40..48) are **live human scholarly questioning** — not synthetic. This is gold
training data for what a curious human finds interesting. Findings from analyzing them:
- **Curiosity is not random** — it has repeatable structure: live-issue (does X explain or rename?),
  distinction-forensics (are terms equivalent?), tension, honest-boundary.
- **Enquiry reveals topic structure** — the presence enquiry DISCOVERED a taxonomy (prakāśa≠presence≠
  experience≠consciousness), a theorem, a boundary, and a frontier. Questioning = data about the topic.
- **Agentic gem extraction** — pushing a text surfaces UNSEEN gems (e.g. PENETRATION 1: the text
  asserts a collapse it doesn't prove).
- **Cross-tradition standardisation** — the same structural claim (determination requires
  self-reference) appears as vimarśa / svasaṃvedana / self-presence / metacognition; separable into
  structural-claim + tradition-vocab + boundary.

These are the **prima materia** for the Question-Growth Engine, the What-If Machine, and the
Co-Evolving Organism.

---

## 5. THE ESSAY-INGEST ARCHITECTURE (essays as derivation input)

A scholarly essay (Ratié, Torella, Dyczkowski) is a **dense bundle of machine-derivable objects** —
thesis-moves, source-cited claims, argument moves, scholar disagreements (cruxes), verbatim quotes.
We ingest it through our **existing epistemic pipeline**, NOT a separate "essay reader." The 9 stages:

| Stage | Kernel | Why |
|-------|--------|-----|
| Structure | `schema.py` | anatomy (book→chapters→sections→IPK→move) is a contract, not free text |
| Mine claims | `epistemic.py` | honest ceilings: SOURCE-SAYS ≠ SCHOLAR-RECONSTRUCTS ≠ PĀṬALA-INFERS |
| Evidence | `translation.py`/signing | grounded + signed verbatim quotes, no phantoms |
| Argument | `review.py` | AIF graph, real reducer gates |
| Crux | `crux-compiler` | minimal divergence, master tension preserved |
| Review | `scholar_review.py` | adversarial panel + citecheck (anti-theatre) |
| Organism | `organism.py` | readers probe the essay-derived graph, improve it |
| Pedagogy | `pedagogy.py` | the mined structure IS the curriculum |
| Reactive | `staleness.py` | the essay is a projection — source change marks its sections stale |

**Source text vs essay-about-source vs standalone essay** (the three ingest types, KORAL two-graph):
- **Source text** (IPVV, Tantrāloka) ingests VERTICALLY as ground truth (raw→translation→proof), each
  passage a node. Reality graph.
- **Essay-about-source** (Ratié on IPVV) ingests at the COMMENTARIAL layer; its claims are
  `derived_from` + reviewed AGAINST the source passages. Interpretation lives in the literature graph.
- **Standalone essay** ingests at the ARGUMENT layer; references whatever it cites as evidence.
- **KORAL rule (already proven):** interpretation NEVER corrupts the primary source. Re-reading Ratié
  flags HER claims, not the source passage.

**The unifying insight:** essay ingest is the pipeline applied to a structured document — no new
machinery, just wiring proven kernels. The essay becomes derivation input feeding review, comparison,
research, education, and the organism. "One graph" made literal for the scholarly essay corpus.

Proofs: `validate-essay-ingest.py` (8/8 on real Ratié), `experiment-essay-as-engine.py`,
`experiment-koral-twograph.py`. Docs: `migration/v2/ESSAY-INGEST.md`, `migration/v2/INGESTION-ARCHITECTURE.md`.

---

## 6. THE VISIONS (where this is heading)

| Vision | Status |
|--------|--------|
| Verified Epistemic OS (8 laws) | substrate exists, VALIDATED |
| Verified-Statement-Marketplace | Certification Weight + signing validated; no marketplace |
| Co-Evolving Epistemic Organism | organism loop + pedagogy validated (human-gated) |
| What-If Machine | counterfactual + crux + Research-Value validated |
| Self-Proving System | signed corpus + causal-operational graph validated |
| General Engine | SciFact + EleutherIA generalization proven; adapters incomplete |
| Question-Growth Engine | question tree + PrimitiveRobustness prototype (from pushing method) |
| Enquiry-Discovery Organism | questions reveal topic structure (from LOGICVID gold) |

All in `docs/vision/` — see `docs/vision/beyond-patala/` for the product visions.

---

## 7. REVIEW CRITIQUES TO TRACK (the honest debt)

From **patalamix (SPEC-32)** + the v2 migration:
- ✅ Honest status ladder (DISCOVERED→PRODUCTION) — adopted.
- ✅ Real MAP-Elites (behavioral niches + cost/latency) — adopted.
- ✅ Execution branching + deterministic replay (gaps B+C) — built.
- ✅ 5th graph (causal-operational) — built.
- ⬜ **Gap A**: context-paging (lossless context virtualization) — not built.
- ⬜ **Gap D**: content-addressed run-traces (RunManifest/ArtifactReference) — not built.
- ⬜ **Gap E**: signed human attestation (replace plain `human_authorize()`) — not built (critical
  before any marketplace/public authority).
- ⬜ **Gap F**: workspace isolation — not built.
- ⬜ **Gap G**: local-first scholar workstation (nodedb) — cloned, not built.
- ⬜ **The graduation test**: ONE IPVV claim through the whole stack — the real milestone, not yet done.

---

## 8. THE 7 AXIOMS (non-negotiable — from AGENTS.md)

1. One rule: nothing is real because a file exists — it's real when reproducible + verifiable.
2. Reuse don't rebuild (17 kernels in `lib/`).
3. Honest statuses — DONE is theatre.
4. Run `theatre-check` before claiming done; PROVEN-MECHANISM ≠ delivery.
5. Background long jobs with nohup; kill by PID never pkill.
6. External sources → R2; verify before deleting.
7. Every claim resolves to evidence + a real test.

---

## 9. EXACTLY WHAT TO DO NEXT (prioritized)

**✅ DONE — P0, the graduation test** (`validate-graduation.py`, **14/14 on real data**):
One claim (I5, two-stage free-will) now runs through the WHOLE organism: ingest → envelope → review →
**MUTATE premise I1** → staleness blast-radius → reactive essay (prose stale) → pedagogy (learner
re-examined) → organism (misconception = signal) → signed re-release → invariant still 0 violations.
This is the anti-theatre proof that turns the lab into the kernel. See `migration/v2/GRADUATION.md`.

**✅ DONE — the IPVV graduation** (`validate-graduation-ipvv.py`, **18/18 on real IPK**):
The graduation on the ACTUAL corpus: IPK 1.5.19 (vimarśa/adhyavasāya, the felt→ground step) through
the whole organism, with the real Ratié commentary (Ch7 camatkāra) feeding the essay stage and a real
premise mutation (1.5.11). Honest ceilings (corroborated text vs machine-proposed addition) +
adversarial review + mutation → staleness → reactive Ratié essay → pedagogy → organism → signed
re-release. **18/18.** See `migration/v3/ULTIMATE-OPTIMIZED-PRODUCT.md`.

**✅ DONE — the ultimate product** (`lib/patala_product.py` + `validate-product-stack.py`, **13/13**):
The full v3 product stack assembled from ALL 18 kernels for one real IPK claim — 18 products across the
4 families (TEXTS/ARGUMENTS/SCHOLAR/LEARN). TranslationProof moat (non-aggregate), Certification
Weight, Research Value, LearningClaim — all projections of the proven kernels, honest statuses.

**P0 — widen + deepen the real corpus run:**
- Run the product stack + graduation over MANY IPK claims (a real IPVV corpus pass), feeding produced
  essays/lessons through the real organism loop.
- Build the 3 v3 needs-build products (Essay projection, Commentary, Tokenization).
- Signed human attestation (gap E).

**P1 — close the review gaps:**
1. **Signed human attestation** (gap E) — replace plain `human_authorize()` with a cosign-style signed
   HumanAttestation. Before any marketplace/public authority.
2. **Context paging** (gap A) — lossless context virtualization.
3. **Remaining import adapters** (OpenAlex, S2ORC, xAIF) — finish the generalization test.

**P2 — deepen the promising:**
- Parse the LOGICVID gold into a real enquiry graph (SPEC-40..48 → DiscoveryProgressions).
- Wire enquiry-discovery into pedagogy (learner reconstructs the discovered structure).
- MAP-Elites on a real translation task (patalamix EXP-43).
- **Run the essay-ingest on a FULL source** (not just the Ratié breakdown excerpts): feed a whole
  chapter text through all 9 stages → graduation-style proof that a real essay becomes real derivation
  input, cross-linked to the source passages it cites (KORAL two-graph respected).

---

## 10. KEY COMMANDS

```bash
python3 scripts/run-tests.py              # full suite (53/53, incl traceability + graduation gates)
python3 scripts/audit-traceability.py     # every .md resolves to an index doc (agent-org gate)
python3 scripts/validate-graduation.py    # THE full organism graduation test (14/14 on real data)
python3 scripts/validate-graduation-ipvv.py  # IPVV graduation (18/18 on real IPK text)
python3 scripts/validate-product-stack.py    # the v3 product stack (13/13, 18 products/4 families)
python3 scripts/validate-essay-ingest.py  # essay-ingest pipeline (8/8 on real Ratié)
python3 scripts/theatre-check.py          # kernel theatre audit (verifiable proofs)
python3 scripts/theatre-check-all.py      # ALL-experiment theatre audit (51: 24/27/0)
python3 scripts/build-experiment-matrix.py # regenerate the matrix
python3 scripts/reverse-deliver.py --vision <Name>   # backward-delivery plan for a vision
rclone check <local> r2:atlas-sources/informationphilosopher  # R2 backup integrity
```

---

## 11. SESSION LOG (2026-08-14 — what was built this session)

1. Imported + saved 30+ R2 docs → SPEC-00..48 (reviews, education, organism, pushing, logicvid).
2. Built 17 kernels + 51 experiments across layers L00-L12 + 8 product visions.
3. Applied patalamix/v2 critiques: honest statuses, real MAP-Elites, causal-operational graph,
   execution branching/replay.
4. Cloned ~100 repos across categories; each high-value one → a validated experiment.
5. Built the theatre-check verifiable-proof skill; audited all experiments.
6. Discovered the LOGICVID gold (live human curiosity) → question-growth, enquiry-discovery,
   gem-extraction, claim-standardisation.
7. Final alignment: **full traceability** (TRACEABILITY-MAP + GITHUB-TRACEABILITY — every doc/
   experiment/repo resolves to vision + layer), **theatre-check-all**, clean AGENTS navigation,
   all 46 specs indexed.
8. **ESSAY-INGEST (this session):** surfaced logicvid/pushing + organism/consumers + essays in the
   migration (`migration/v2/PUSHING-ORGANISM-ESSAYS.md`). Built `experiment-essay-as-engine.py` (mine
   a scholar essay into claim+argument+crux+evidence objects). Built the **17th kernel**
   `lib/essay_ingest.py` — the 9-stage essay-as-derivation-input pipeline — + `validate-essay-ingest.py`
   (8/8 on real Ratié data, all through proven kernels). Wrote the deep architecture docs:
   `migration/v2/ESSAY-INGEST.md` (9 stages × kernel × why) and `migration/v2/INGESTION-ARCHITECTURE.md`
   (source-text vs essay-about-source vs standalone essay, KORAL two-graph). Fixed the theatre audit
   self-recursion bug (audit no longer audits itself).
9. **GRADUATION (this session):** the P0 milestone is DONE. Built `validate-graduation.py` — the full
   organism test (**14/14 on real data**): one real claim (I5) through ingest→envelope→review→
   **MUTATE premise I1**→staleness→reactive essay→pedagogy→organism→signed re-release→invariant
   (0 violations). Wrote `migration/v2/GRADUATION.md`. Also: `audit-traceability.py` gate (every .md
   resolves) + fixed 13 doc-traceability gaps + AGENTS axiom 22 (docs resolve, agent-optimized).
10. **IPVV + PRODUCT (this session):** the IPVV graduation is DONE (`validate-graduation-ipvv.py`,
    **18/18 on real IPK text**): IPK 1.5.19 (felt→ground, vimarśa/adhyavasāya) through the whole
    organism with the real Ratié commentary + a real premise mutation. Built the **18th kernel**
    `lib/patala_product.py` — the ULTIMATE product: assembles all 17 kernels into v3's 4-family product
    stack for one claim (`validate-product-stack.py`, **13/13**, 18 products). Wrote
    `migration/v3/ULTIMATE-OPTIMIZED-PRODUCT.md` (the v3 organism on the real IPVV corpus).
11. **READ-PLANE (this session):** the full read plane is BUILT (SPEC-49 P0/P1), inspired by the
    graphrag `LocalSearchMixedContext` frontier pattern. Added 4 kernels: `context_compiler.py`
    (projection compiler, 12/12), `fts_search.py` (Postgres-FTS-equivalent + benchmark, 9/9, p50<10ms
    → no Tantivy needed), `bundle_router.py` (compiled agent bundles + MCP 8-tool, 16/16),
    `seo.py` (canonical URLs + JSON-LD + sitemap + 31 static 0-JS HTML pages, 13/13). L06+L07 now BUILT.
 13. **INTEGRATION (this session):** refreshed MASTER-KNOWLEDGE-BASE to the full integrated state
      (25 kernels / 63 experiments / 43 clones / 47 specs) + added the frontier compares (LightRAG,
      cognee) to the ecosystem. Cloned + tested LightRAG (⭐38k, graph-RAG, 10/10) and cognee (⭐30k,
      AI-memory, 11/11) — both confirm our architecture (PathRAG still wins on our graph; our bundles
      match Cognee's recall). Extended theatre-check to all 25 kernels.
 14. **GEMS (this session):** mined the patala v2/v3 GEMs + external sources (fojin, EleutherIA, vidyut).
      Built 8 infra kernels, all real-data: `source_registry` (fojin, 10/10), `evidence_ledger` (typed+
      confidence_kind, 9/9), `alignment_flywheel` (cross-source, 10/10), `integrity_gate` (EleutherIA,
      8/8), `next_action` (deterministic scheduler, 7/7), `vidyut_l0` (Sanskrit L0, 9/9),
      `verification_ensemble` (RefChecker+GraphCheck+RARR, 8/8), `translation_variant` (three-version,
      8/8). + `ORGANISM-OPERATING-MODEL.md` (the zoom-out of how the organism lives).
 15. **EVOLUTION (this session):** mined the arXiv GAP/BET papers for stealable architectures. Cloned
      dgm (Darwin Godel ⭐2.2k) + awesome-self-evolving survey. Built 4 steals: `open_ended_evolve`
      (Darwin, 6/6), `self_healing` (typed repair cascade, 8/8), `skill_graph` (kernels-as-skills,
      verifiable-reward, 8/8), `structure_recall` (SAGE, 9/9). + `COHERENCE-AUDIT.md` (the proof that
      every kernel → patala layer + every frontier build → patala product).
 16. **FINAL STATE: 75/75 tests, 35 experiments PROVEN on real data / 39 mechanism / 0 unproven (74
       audited), 37 kernels, 8 product visions, 75-experiment matrix, 48 cloned repos, fully traceable,
       graduation done (Doyle 14/14 + IPK 18/18), ultimate v3 product (13/13), read plane built,
       VISION F (self-provenance) built, 8 infra gems + 4 evolution steals integrated, coherent by
       layer (COHERENCE-AUDIT).**
 17. **INTEGRATION BUILD (later session):** per the master devplan, integrated with patala's mature
       factory. Added: `ingest-ipvv-gold.py` (5/5, validates the 49 REAL patala IPVV gold passages with my
       TranslationProof + integrity gate), `translation-audit-compiler.py` (SPEC-16 §30 CLI),
       `projection_dag.py` (6/6, the SPEC-00 §22 per-artifact incremental — new doc ≠ whole corpus rebuild),
       `factory_pool.py` (parallel DAG-gated workers), `hermes_exec.py` (agentic generation), `commentary_lift.py`,
       `pushing_miner.py`. The other agent completed OpenAlex-for-Sanskrit v1 (47k SOURCE, /resolve crosswalk,
       release, work pages). Created `devplans/` (4 canonical plans: master-integration, translation-production,
       read-plane-organism, tantraloka-production) + copied to shared.
 18. **FINAL STATE (current): 47 kernels, 97 experiments, fully traceable. The integration
       is REAL: patala produces the gold/factory; my read plane + organism + validation kernels validate
       and serve it. The canonical devplan set is locked in `devplans/`.**
 19. **INTEGRATION BUILD LOG (later, this session — the full build record):**
     - **Iteration 4**: `ingest-ipvv-gold.py` (5/5) validates the 49 REAL patala IPVV gold passages with my
       TranslationProof + integrity gate; `translation-audit-compiler.py` (SPEC-16 §30 CLI). State 44/90.
     - **Iteration 5**: `lib/proof_generators.py` (9/9) — the real Sanskrit proof-generator lattice (Vidyut
       SLP1 + token floor + negation) → real TranslationProof analysis, not hand-filled (closes the
       audit's "hand-fills morphology from bool()" theatre). `lib/projection_dag.py` (6/6, SPEC-00 §22
       per-artifact incremental). State 46/92.
     - **Iteration 6**: the **Tantrāloka corpus X1-X3** — `run-tantraloka-corpus.py` (7/7, 30 real Āhnika-1
       kārikās → real corpus TranslationProofs), `run-tantraloka-commentary.py` (5/5, B3→B4 commentary-lift
       across the corpus, 30/30 reach the gold frame), `run-tantraloka-validate.py` (4/4, corpus vs
       Dyczkowski, 30/30 corroborate the core). The 30-kārikā corpus is real: proofs + commentaries +
       validation. State 47/97.
     - **The organism→factory loop**: `lib/organism_factory_bridge.py` (6/6) — my next_action ranks WHAT +
       patala's corpus_state FSM returns the legal action.
 20. **FINAL STATE (current): 47 kernels, 97 experiments, fully traceable. The Tantrāloka 30-kārikā corpus
       has real proofs + commentaries + validation vs Dyczkowski. The integration is REAL.**

---

## 12. READ-ME-FIRST CHECKLIST (for the new agent)

**Fastest orientation (3 reads):** `devplans/MASTER-INTEGRATION-DEVPLAN.md` (the canonical integration
build) → `COHERENCE-AUDIT.md` (what the whole thing is, by layer) → `KERNELS-INDEX.md` (the 47 kernels to
reuse, don't rebuild).

1. Read `AGENTS.md` — the axioms (esp. axiom 4/5: reuse don't rebuild, never ignore mature infra; axiom
   12: every artifact must resolve; axiom 22: every doc).
2. Read `NAVIGATION.md` → `TRACEABILITY-MAP.md` → `HANDOVER.md` (this file).
3. Read `devplans/` — the canonical build plans (master-integration, translation-production,
   read-plane-organism, tantraloka-production). **This is where we're going.**
4. Read `COHERENCE-AUDIT.md` — the zoom-out: every kernel → patala layer, every frontier build → patala product.
5. Read `ORGANISM-OPERATING-MODEL.md` — how the organism ingests/translates/teaches/publishes + stays
   durable/secure.
6. Read `MASTER-KNOWLEDGE-BASE.md` + `KERNELS-INDEX.md` — reuse the 47 kernels, don't rebuild.
7. Read §5 essay-ingest architecture — the source-text vs essay-about-source vs standalone design.
8. Read `tantraloka/` (run-all.py harness + PROGRESS-STATUS) — the live 7-stage Tantrāloka suite.
9. Check `TODO.md` + `GAPS.md` + `STATE.yaml` + `state.json` — the live state.
10. Run `scripts/run-tests.py` (97/97, incl all gates) + `scripts/theatre-check-all.py` + `audit-state.py`
    before claiming anything done.
11. **The integration is REAL:** patala produces the gold/factory; my read plane + organism + validation
    kernels validate and serve it. The next build phases are in `devplans/`.

**The single most important next step (context-engineered start for the next agent):**
The Tantrāloka 30-kārikā corpus is DONE (real proofs + commentaries + validated vs Dyczkowski). Continue
the devplan sequence:
1. **X4 (in progress):** build the education/essay products from the validated corpus — take
   `tantraloka/corpus/ahnika-1-commentaries.json` → `compile_interactions` → LearningClaims → the read
   plane (education product). This turns the validated corpus into touchable products.
2. **Read-plane incremental:** wire `lib/projection_dag.py` into `build-static-site.py` so the site
   rebuilds per-artifact (a new kārikā rebuilds only its page, not the whole corpus — SPEC-00 §22).
3. **Real proof auditors:** wire xCOMET/MQM as smoke-detector wrappers where available (SPEC-16).
4. **Shared coordination:** agentpatala is assigned the harvest→factory-runnable work (extract verse text
   → `<work>.jsonl`). Once they make the SOURCE runnable, my proof generators validate the output.

**Start with X4** — it's the natural continuation (corpus → products) and uses only proven kernels.
The shared folder (`migration/shared/AGENTGRAPH-PROGRESS-ASSIGNMENT.md`) records my progress + the
agentpatala assignment so you don't collide.
