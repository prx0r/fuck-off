# epistemic/ — epistemic-state reference clones

Repos that model knowledge with epistemic state (claims, evidence, review, supersession). See
`../../docs/ECOSYSTEM-INDEX.md` §1.

| Repo | Why we cloned |
|------|---------------|
| RKA (infinitywings/rka) | research-workflow-as-state; supersession/staleness propagation (the killer idea) |
| Kappa Graph (aaronsb/knowledge-graph-system) | supporting vs contradicting evidence, grounding+diversity |
| Vouch (vouchdev/vouch) | git-native write/review gate (don't rebuild) |
| Eigenius (eigenius/eigenius) | typed knowledge classes (Declared/Observed/Derived/Verified) |
| DocGraph (Detective-XH/DocGraph) | SQLite KG + drift audits (staleness) |

| infinitywings/rka | **CLONED local-only** (30M) — review_queue w/ stale_dependency flag, blast-radius propagation, openalex/arxiv/crossref backends |
| aaronsb/knowledge-graph-system | **CLONED local-only** (49M) — Kappa grounding/contradiction, FUSE over graph |
