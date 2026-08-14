# KERNELS-INDEX — the reusable kernels (what's in lib/, what it does, how it's validated)

*2026-08-14. The agent-facing map of every reusable kernel (now 22). Reuse these — never rebuild. Each
maps to: what it is · layer · vision · the experiment(s) that validate it · honest status.*

| Kernel | What it does | Layer | Vision | Validated by | Status |
|--------|-------------|-------|--------|--------------|--------|
| `epistemic.py` | envelope + 4-axis authority + invariant | L00 | Verified OS | kernel-suite, eigenius | VALIDATED |
| `schema.py` | single-source schema compiler | L00 | Complete Pipeline | kernel-suite | VALIDATED |
| `review.py` | herdr reducer (promotion gate) | L05 | Self-Maintaining | layer03-05 | VALIDATED |
| `scholar_review.py` | adversarial panel + cross-review + citecheck | L08 | Complete Pipeline | kernel-suite | VALIDATED |
| `staleness.py` | RKA blast-radius + rebuild order | L03 | Self-Maintaining | layer03-05 | VALIDATED |
| `query.py` | KG2Code executable graph queries | L10 | Executable Knowledge | kernel-suite | VALIDATED |
| `retrieval.py` | PathRAG + HippoRAG | L10 | Argument Map | kernel-suite, layer10 | VALIDATED |
| `translation.py` | TranslationProof (non-aggregate vector) | L03 | Complete Pipeline | products | VALIDATED |
| `education.py` | LearningClaim + interaction compiler | L09 | Education+Organism | education-organism | VALIDATED |
| `organism.py` | UserKnowledgeState + MisconceptionGraph | L09 | Education+Organism | education-organism | VALIDATED |
| `organism_loop.py` | consumer→research machine | L09 | Co-Evolving Organism | organism-loop | VALIDATED |
| `pedagogy.py` | live adaptive pedagogy | L09 | Education+Organism | pedagogy | VALIDATED |
| `agent_delivery.py` | task contract + context routing + budget + human gate | L09 | Autonomous Institute | agent-delivery | PROTOTYPED (needs signed auth) |
| `evolve.py` | MAP-Elites evolution loop | ALL | Autonomous Institute | evolve | VALIDATED |
| `certificate.py` | Certification Weight (compounding) | L02 | Verified-Statement-Marketplace | kernel-suite | VALIDATED |
| `discovery.py` | Research Value Score | L03 | What-If Machine | kernel-suite | VALIDATED |
| `essay_ingest.py` | 9-stage essay-as-derivation-input pipeline (structure→claims→evidence→argument→crux→review→pedagogy→reactive) | L04-L09 | Enquiry-Discovery Organism | validate-essay-ingest | VALIDATED (real Ratié data, 8/8) |
| `patala_product.py` | the ULTIMATE product: assembles ALL 17 kernels into the v3 4-family/16-product stack for one claim | ALL | Enquiry-Discovery Organism | validate-product-stack | VALIDATED (real IPK, 13/13) |
| `context_compiler.py` | the projection compiler: canonical graph → immutable per-entity context bundles | L06 | Verified OS | validate-context-compiler | VALIDATED (real graph, 12/12) |
| `fts_search.py` | Postgres-FTS-equivalent inverted index + benchmark (SPEC-49 Tantivy decision point) | L06 | Verified OS | validate-fts-baseline | VALIDATED (real corpus, 9/9) |
| `bundle_router.py` | compiled agent bundles + MCP 8-tool adapter + R2-style immutable emission | L06/L07 | Verified OS | validate-bundle-router | VALIDATED (real data, 16/16) |
| `seo.py` | agent-SEO: canonical URLs + JSON-LD + sitemap + static 0-JS HTML | L07 | Verified OS | validate-seo-astro | VALIDATED (real graph, 13/13) |

## Rules for agents
1. **Reuse, don't rebuild** (axiom): a task that maps to a kernel → call the kernel.
2. **A kernel is VALIDATED** only if its `validate-*.py` passes in `scripts/run-tests.py`.
3. **Nothing is PRODUCTION** until it's INTEGRATED into a real pipeline and passes on real evidence.
4. To add a kernel: `lib/<name>.py` + a `validate-<name>.py` + matrix entry + this index.
