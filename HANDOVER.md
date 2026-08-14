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

## 2. WHAT'S BUILT (the 16 reusable kernels)

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

## 3. THE THEATRE AUDIT (verifiable proofs)

**`scripts/theatre-check-all.py`** runs every experiment and stores a proof record (test exists +
passes + real-data + claim + hash) → `data/references/theatre-proofs-all.json`.

**Result (49/49 tests pass):**
```
22 experiments PROVEN on real data
26 PROVEN-MECHANISM (synthetic — mechanism works, not integrated)
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

## 5. THE VISIONS (where this is heading)

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

## 6. REVIEW CRITIQUES TO TRACK (the honest debt)

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

## 7. THE 7 AXIOMS (non-negotiable — from AGENTS.md)

1. One rule: nothing is real because a file exists — it's real when reproducible + verifiable.
2. Reuse don't rebuild (16 kernels in `lib/`).
3. Honest statuses — DONE is theatre.
4. Run `theatre-check` before claiming done; PROVEN-MECHANISM ≠ delivery.
5. Background long jobs with nohup; kill by PID never pkill.
6. External sources → R2; verify before deleting.
7. Every claim resolves to evidence + a real test.

---

## 8. EXACTLY WHAT TO DO NEXT (prioritized)

**P0 — the graduation test** (the biggest lever, patalamix #15):
Build ONE claim end-to-end on real evidence (use the two-stage free-will argument as the stand-in for
IPVV), then MUTATE a premise and verify the whole organism reacts (staleness→reactive essay→pedagogy
regeneration→signed re-release). This turns the lab into the kernel. `validate-stack.py` starts it.

**P1 — close the review gaps:**
1. **Signed human attestation** (gap E) — replace plain `human_authorize()` with a cosign-style signed
   HumanAttestation. Before any marketplace/public authority.
2. **Context paging** (gap A) — lossless context virtualization.
3. **Remaining import adapters** (OpenAlex, S2ORC, xAIF) — finish the generalization test.

**P2 — deepen the promising:**
- Parse the LOGICVID gold into a real enquiry graph (SPEC-40..48 → DiscoveryProgressions).
- Wire enquiry-discovery into pedagogy (learner reconstructs the discovered structure).
- MAP-Elites on a real translation task (patalamix EXP-43).

---

## 9. KEY COMMANDS

```bash
python3 scripts/run-tests.py              # full suite (49/49)
python3 scripts/theatre-check.py          # kernel theatre audit (verifiable proofs)
python3 scripts/theatre-check-all.py      # ALL-experiment theatre audit
python3 scripts/build-experiment-matrix.py # regenerate the matrix
python3 scripts/reverse-deliver.py --vision <Name>   # backward-delivery plan for a vision
rclone check <local> r2:atlas-sources/informationphilosopher  # R2 backup integrity
```

---

## 10. SESSION LOG (2026-08-14 — what was built this session)

1. Imported + saved 30+ R2 docs → SPEC-00..48 (reviews, education, organism, pushing, logicvid).
2. Built 16 kernels + 45 experiments across layers L00-L12 + 8 product visions.
3. Applied patalamix/v2 critiques: honest statuses, real MAP-Elites, causal-operational graph,
   execution branching/replay.
4. Cloned ~100 repos across categories; each high-value one → a validated experiment.
5. Built the theatre-check verifiable-proof skill; audited all experiments.
6. Discovered the LOGICVID gold (live human curiosity) → question-growth, enquiry-discovery,
   gem-extraction, claim-standardisation.
7. Current: **49/49 tests, 22 experiments PROVEN on real data, 16 kernels, 8 visions.**
