# KERNELS-INDEX — the reusable kernels (what's in lib/, what it does, how it's validated)

*2026-08-14. The agent-facing map of every reusable kernel. Reuse these — never rebuild. Each maps to:
what it is · layer · vision · the experiment(s) that validate it · honest status.*

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

## Rules for agents
1. **Reuse, don't rebuild** (axiom): a task that maps to a kernel → call the kernel.
2. **A kernel is VALIDATED** only if its `validate-*.py` passes in `scripts/run-tests.py`.
3. **Nothing is PRODUCTION** until it's INTEGRATED into a real pipeline and passes on real evidence.
4. To add a kernel: `lib/<name>.py` + a `validate-<name>.py` + matrix entry + this index.
