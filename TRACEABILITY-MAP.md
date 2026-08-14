# TRACEABILITY-MAP — everything resolves to vision + layer, rooted here

*2026-08-14. The ROOT of the traceability tree. Every artifact — root doc, docs/, vision, spec,
kernel, experiment, cloned repo — is assigned to a **VISION** + **LAYER** and resolves back to this map.
Nothing is orphaned. Machine-checkable: every entry has a path; every path exists.*

> **How to use:** start here. Find the artifact → its vision + layer → the experiment that proves it →
> the repo that informed it. Everything traces to root (this file) → NAVIGATION.md.

---

## 0. THE VISION MAP (every vision → its layer + docs)

| Vision | Layer(s) | Vision doc | Key kernels/experiments |
|--------|----------|-----------|------------------------|
| **Verified Epistemic OS** (the substrate) | ALL | `VISION-VERIFIED-EPISTEMIC-OS.md` | 8 laws, `validate-stack`, `theatre-check` |
| **Verified-Statement-Marketplace** | L02 | beyond-patala `VISION-VERIFIED-STATEMENT-MARKETPLACE.md` | `certificate.py`, signed-statement |
| **Co-Evolving Epistemic Organism** | L09 | beyond-patala `VISION-COEVOLVING-EPISTEMIC-ORGANISM.md` | organism-loop, pedagogy |
| **What-If Machine** | L03/L04 | beyond-patala `VISION-WHAT-IF-MACHINE.md` | `discovery.py`, counterfactual, crux |
| **Self-Proving System** | L12 | beyond-patala `VISION-SELF-PROVING-SYSTEM.md` | signed-corpus, causal-operational |
| **Question-Growth Engine** | L04 | beyond-patala `VISION-QUESTION-GROWTH-ENGINE.md` | question-growth |
| **Enquiry-Discovery Organism** | L04/L09 | beyond-patala `VISION-ENQUIRY-DISCOVERY-ORGANISM.md` | enquiry-discovery, gem-extraction |
| **General Engine** | L00/L01/L08 | `VISION.md` | import-scifact, eigenius |
| **Education+Organism** | L09 | `SPEC-20-EDUCATION-ORGANISM.md` | education, organism, pedagogy |
| **Unconsidered Frontiers** | — | `VISION-UNCONSIDERED-FRONTIERS.md` | the 6 novel directions |

---

## 1. THE LAYER MAP (every layer → its docs, kernels, experiments)

| Layer | Name | Docs | Kernels | Key experiments |
|-------|------|------|---------|-----------------|
| L00 | Core Engine | `layers/00`, `05-performance` | `epistemic.py`, `schema.py` | eigenius-grades, kernel-suite |
| L01 | Corpus/Provenance | `01-corpus` | (adapters) | import-scifact |
| L02 | Epistemic Graph | `03-graph`, `04-ontology` | `certificate.py` | communities, provenance, certification-weight |
| L03 | Factory | `03-factory` | `staleness.py`, `discovery.py` | rka, counterfactual, salsa |
| L04 | Argument Engine | `04-argument-engine` | — | crux-compiler, question-growth, gem-extraction |
| L05 | Research/Review | `05-review-gate` | `review.py` | herdr, self-improve |
| L06 | Retrieval Compiler | `06-retrieval-compiler` | `retrieval.py`, `query.py`, `context_compiler.py`, `fts_search.py`, `bundle_router.py` | context-compiler, fts-baseline, bundle-router |
| L07 | Surfaces (Astro/MCP/SEO) | `07-surfaces` | `seo.py`, `bundle_router.py` | seo-astro, bundle-router |
| L08 | Human Authority | `08-human-authority` | `scholar_review.py` | cross-review, review-bias |
| L09 | Organism/Education | `09-live-system` | `education.py`, `organism.py`, `pedagogy.py`, `agent_delivery.py`, `essay_ingest.py`, `patala_product.py` | organism-loop, pedagogy, execution-replay, essay-ingest, v3-product |
| L10 | Surfaces | `10-surfaces` | `query.py`, `retrieval.py` | kg2code, pathrag, hipporag |
| L12 | Live System | `12-live-system` | — | signed-corpus, reactive-essay, causal-operational |

---

## 2. THE ROOT DOC MAP (every root doc → its vision/layer + role)

| Root doc | Vision/Layer | Role |
|----------|-------------|------|
| `AGENTS.md` | Governance (L00) | axioms — the rules |
| `NAVIGATION.md` | ALL | the master index (root of all) |
| `LAB-REVIEW.md` | ALL | state of the lab (proven/exploratory) |
| `KERNELS-INDEX.md` | ALL | the reusable kernels |
| `MASTER-KNOWLEDGE-BASE.md` | ALL | the synthesized master reference (everything at a glance) |
| `HANDOVER.md` | ALL | session state + where to continue |
| `migration/v2/ESSAY-INGEST.md` | Enquiry-Discovery (L04/L09) | the 9-stage essay-as-derivation-input architecture |
| `migration/v2/INGESTION-ARCHITECTURE.md` | Enquiry-Discovery (L04/L09) | source-text vs essay-about-source vs standalone (KORAL) |
| `migration/v3/ULTIMATE-OPTIMIZED-PRODUCT.md` | Enquiry-Discovery (ALL) | the v3 organism on the real IPVV corpus |
| `TRACEABILITY-MAP.md` | ALL | **this file** — the traceability root |
| `BUILDNOTES.md` / `CHANGELOG.md` | ALL | history |
| `DEV_PLAN.md` | ALL | roadmap |
| `GAPS.md` / `TODO.md` | ALL | known holes / tasks |
| `VISION-CHUNK-LAYER-MAP.md` | ALL | vision→chunk→layer decomposition |

---

## 3. THE DOCS MAP (every docs/ file → vision/layer)

| Doc | Vision/Layer | Role |
|-----|-------------|------|
| `01-corpus.md` | General Engine (L01) | corpus ground truth |
| `02-extraction.md` | General Engine (L01) | text pipeline |
| `03-graph.md` | Verified OS (L02) | graph output |
| `04-ontology.md` | Verified OS (L02) | concept vocab |
| `05-performance.md` | Verified OS (L00) | perf doctrine |
| `ALGORITHMS.md` | Verified OS (L10) | the arXiv algorithms |
| `ARXIV-INDEX.md` | ALL | paper catalog |
| `ECOSYSTEM-INDEX.md` | ALL | repo/dataset/people index |
| `EXPERIMENT-MATRIX.md` | ALL | experiment↔layer↔vision |
| `EXPERIMENT-REPORT.md` | ALL | experiment results |
| `GITHUB-INDEX.md` | ALL | repo catalog |
| `GITHUB-TRACEABILITY.md` | ALL | repo→experiment link |
| `LOGICVID-GOLD-EXEMPLARS.md` | Enquiry-Discovery (L04/L09) | the human-curiosity gold |
| `TESTING-VALIDATION-REPORT.md` | ALL | test results |
---

## 4. VERIFY NOTHING IS ORPHANED (the machine check)

```bash
# every root doc resolves
for f in *.md; do echo "$f"; done
# every docs/ file has a vision+layer assignment (see table above)
# every spec traces to a vision
python3 -c "
import os,json
# check every experiment in the matrix has a script on disk
d=json.load(open('data/references/experiments.json'))
missing=[e['script'] for e in d['entries'] if not os.path.exists('scripts/'+e['script'])]
print('experiments with no script:', missing if missing else 'none')
"
# check every cloned repo is in the traceability
ls ecosystem/*/*/ | wc -l
```

---

## 5. THE RULE (add to axioms)

> **Every artifact must resolve.** A doc → a vision + layer. A kernel → a validating experiment. An
> experiment → a source repo/paper. A repo → a cloned dir + a link. If it can't resolve, it's either
> assigned to a vision/layer in this map or it's orphaned (flagged in GAPS). The root is this file +
> NAVIGATION.md.
