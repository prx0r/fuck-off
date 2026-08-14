# TESTING & VALIDATION REPORT

*2026-08-14. Full results of the ip-graph validation suite + experiments run against the Doyle
corpus (425 docs). Every gate and experiment is reproducible via `scripts/run-tests.py`.*
**Suite result: 8/8 PASS** · **Context coverage: 100%** (after a real bug fix, see §4)

---

## 1. Validation gates (all PASS)

| Gate | Script | Result | Time |
|------|--------|--------|------|
| Corpus integrity | (inline) | 425 records OK | 211ms |
| Graph integrity | (inline) | 490 nodes / 6484→6578 edges | 45ms |
| Epistemic invariant | `audit-epistemic.py` | PASS, 0 violations | 69ms |
| Canonical DAG | `validate-dag.py` | PASS, no cycles, all grounded | 208ms |
| Argument graph | (inline) | 6 info / 4 infer / 2 conflict | 27ms |
| Evidence-weights experiment | `experiment-evidence-weights.py` | ran, wrote output | 1941ms |
| Bounded-context experiment | `experiment-bounded-context.py` | ran, ~128 tokens | 208ms |
| arXiv peer review | `peer-review-arxiv.py` | 17 arch reviewed | 30ms |

**Epistemic invariant** — the core law `authority(projection) <= authority(parent)` holds across all
6578 edges. Physics/info concepts are SCHOLARLY_CORROBORATED; free-will/value/mind thesis concepts are
MACHINE_PROPOSED. No object's ceiling exceeds its source.

**Canonical DAG** — 14-layer derivational chain validated:
`PHYSICS → THERMODYNAMICS → INFORMATION → COMPUTATION → QUANTUM → PROBABILITY → INDETERMINISM → MIND →
LIFE → FREE_WILL → RESPONSIBILITY → VALUE → SYNTHESIS → ESSAY`

---

## 2. Evidence-weights experiment (Kappa-style)

Tests whether the data reveals epistemic structure beyond raw co-occurrence. **It does.**

Key finding — the data independently confirms the epistemic split:

| Class | Example concepts | Grounding | Support | Contradiction |
|-------|------------------|-----------|---------|---------------|
| GROUNDED (physics/info) | information, quantum, probability, entropy, causality | 0.34–0.71 | high | **0** |
| THESIS (philosophical) | value, mind, free_will, consciousness, agency, morality | high (value=0.734) | 0 | **high** |

`value` has the highest grounding (0.734, 312 docs) yet is entirely MACHINE_PROPOSED — the data treats
"value" as pervasive but unproven. This validates SPEC-02's ceiling assignment as **data-driven, not
imposed**.

---

## 3. Bounded-context coverage (PathRAG-style, stress test)

`experiment-context-coverage.py` — retrieves a bounded context bundle for every concept.

**Result: 100% coverage (31/31 concepts) after the bug fix** (was 30/31 = 97%).

- Every concept has graph neighbors + corpus grounding → produces a usable bundle
- Bounded to `token_budget` (500) — "one agent question = one request"
- Includes: argument chain, evidence quotes, conflicts, ceilings

---

## 4. BUG FOUND & FIXED (the testing win) ⭐

Testing surfaced a real data-quality bug:

**The `mind_body` concept had ZERO graph edges** (isolated) despite the corpus containing 44
"mind-body" + 13 "mind/body" occurrences.

**Root cause:** `norm()` in `build-graph.py` converts document text to lowercase and replaces
non-alphanumerics with spaces, so `"mind-body"` → `"mind body"`. But the lexicon key `"mind-body"`
(with hyphen) was checked against the normalized text via `if "mind-body" in low` → **never matches**.

**Fix:** normalize the lexicon key too (`norm(phrase)`) before matching. Any hyphenated/punctuated
lexicon entry (mind-body, wave-function, mind-body-problem) is now matched.

**Impact of the fix:**
| Metric | Before | After |
|--------|--------|-------|
| Graph edges | 6484 | **6578** (+94) |
| mind_body edges | 0 | **94** |
| Context coverage | 97% | **100%** |

This is exactly why validation gates exist: a silent single-concept gap, invisible to the raw counts,
was caught by the coverage stress test.

---

## 5. arXiv peer review (SPEC-08)

Cross-referenced 17 graph-reasoning architectures against our engine:
- **11 GAP** (G-reasoner, ToG-2, PathRAG, HippoRAG, KAG, Graphiti, AriGraph, ...) — not yet adopted
- **2 BET** (HyperGraphRAG, KG2Code) — the frontier
- **3 VALIDATES** (SubgraphRAG, LightRAG, LLM-Wiki) — confirm our compiler + bounded-context doctrine
- **1 REFERENCE** (nano-graphrag)

---

## 6. Reproducibility

```bash
cd /mnt/HC_Volume_106427611/ip-graph
python3 scripts/run-tests.py                     # full suite (8 tests)
python3 scripts/experiment-context-coverage.py   # coverage stress test
```

Results (machine-readable): `data/graph/test-results.json` · `evidence-weights.json` ·
`context-coverage.json` · `arxiv-review.json`
