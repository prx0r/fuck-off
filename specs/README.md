# SPECS — the design/draft area

This is where the ip-graph product is **specified before it's built**. Specs here are proposals;
they become **live docs** (`docs/01-*.md`) only when approved and implemented.

## Workflow (how a spec becomes real)

```
specs/SPEC-XX-*.md      (draft / proposed)
   │  reviewed + approved
   ▼
docs/0N-*.md            (live — implemented, reconciled to ground truth)
```

1. **Write a SPEC** in `specs/` with a clear scope + concrete design.
2. **Mark its status** in the header: `DRAFT` → `PROPOSED` → `APPROVED` → `IMPLEMENTED`.
3. **When implemented,** fold its decisions into the matching `docs/0N-*.md` and mark the spec
   `SUPERSEDED` (patala discipline: old docs become redirects, never left stale).
4. **Track progress** in `../DEV_PLAN.md`; note gaps in `../GAPS.md`.

## Naming convention

- `SPEC-01-<topic>.md` — numbered, one concern per spec (mirrors patala's SPEC discipline)
- Status in the first line, e.g. `**Status:** PROPOSED`
- Keep each spec self-contained: What / Why / Design / Data model / Build steps / Acceptance

## Current specs

| Spec | Topic | Status |
|------|-------|--------|
| `SPEC-00-INFRA-BUILD.md` | **CANONICAL** master infra build (compiler/factory → R2 → edge) | CANONICAL |
| `SPEC-01-canonical-dag.md` | the layer dependency DAG (physics→…→value) | DRAFT (impl: data/graph/canonical-dag.yaml) |
| `SPEC-02-epistemic-envelope.md` | epistemic status ladder + 4-axis authority | DRAFT (impl: lib/epistemic.py) |
| `SPEC-03-argument-graph.md` | AIF-style Info/Inference/Conflict graph | DRAFT (impl: data/graph/argument.json) |
| `SPEC-07-ECOSYSTEM-SURVEY.md` | repos/datasets/benchmarks | CANONICAL |
| `SPEC-08-GRAPH-REASONING-SURVEY.md` | arXiv GraphRAG architectures | CANONICAL |
| `SPEC-09-AGENT-ORCHESTRATION-SURVEY.md` | runtimes/protocols/universal schema | CANONICAL |
| `SPEC-10-FRONTIER-AGENT-SURVEY.md` | people/labs to track + the convergence | CANONICAL |
| `SPEC-11-AGENT-MEMORY-SURVEY.md` | agent memory / self-evolving systems | CANONICAL |
| `SPEC-12-AGENT-HARNESS-SURVEY.md` | agent-harness repos (maestro/arcan/herdr/looms) | CANONICAL |
| `SPEC-13-STALENESS-PERFORMANCE.md` | staleness + performance for all 7 futures | CANONICAL |
| `SPEC-14-FRONTIER-LAYER-BUILDS.md` | frontier-optimized build for all 13 patala layers | CANONICAL |
| `SPEC-15-PATALA-REVIEW.md` | scholar review survey | CANONICAL |
| `SPEC-16-PATALA-TRANSLATE.md` | translation subsystem survey | CANONICAL |
| `SPEC-17-PATALA-GITHUBS.md` | textual/identity/provenance survey | CANONICAL |
| `SPEC-18-COMPLETE-PIPELINE.md` | complete product pipeline | CANONICAL |
| `SPEC-19-DOYLE-EXPERIMENTS.md` | the 16 Doyle experiments | CANONICAL |
| `SPEC-20-EDUCATION-ORGANISM.md` | education + organism (learner + sensor) | CANONICAL |
| `SPEC-21-CONSUMER-ORGANISM.md` | consumer organism (R2) | CANONICAL |
| `SPEC-22-CONSUMER-ORGANISM-TECH.md` | consumer organism tech (R2) | CANONICAL |
| `SPEC-23-PATALA-ORGANISM.md` | patala organism (R2) | CANONICAL |
| `SPEC-24-ORGANISM-VISIONS.md` | organism visions (R2) | CANONICAL |
| `SPEC-25-ORGANISM-MEH.md` | organism critiques (R2) | CANONICAL |
| `SPEC-26-EDUCATION-N.md` | education (R2) | CANONICAL |
| `SPEC-27-EDUCATION-2.md` | education 2 (R2) | CANONICAL |
| `SPEC-28-EDUCATION-GLOBAL.md` | education global (R2) | CANONICAL |
| `SPEC-29-EDUCATION-MAIN.md` | education main (R2) — the motherlode | CANONICAL |
| `SPEC-30-HERMES-PEER-REVIEW.md` | hermes peer review (R2) | CANONICAL |
| `SPEC-31-PATALA-PEER-REVIEW.md` | patala peer review (R2) | CANONICAL |

### Planned specs (not yet written — content lives in SPEC-00/02/03/08/09)
| Spec | Topic |
|------|-------|
| `SPEC-04-verification.md` | verify the two-stage claim against evidence (covered by SPEC-02/08) |
| `SPEC-05-surfaces.md` | Astro site + agent API + MCP (covered by SPEC-00/09) |
| `SPEC-06-live-system.md` | the 12-layer structure + staleness tracking (covered by SPEC-09) |

## How this relates to the rest of the project

- **Live docs** (`docs/0N-*.md`) = what's built. **Specs** (`specs/`) = what's next.
- `AGENTS.md` = rules. `NAVIGATION.md` = index. `BUILDNOTES.md` = history. `TODO.md` = tasks.
- `DEV_PLAN.md` = the roadmap. `GAPS.md` = known holes. `CHANGELOG.md` = change log.

### Imported reviews, pushing method, and LOGICVID gold (SPEC-32..48)
| Spec | Vision/Layer | Source |
|------|-------------|--------|
| `SPEC-32-PATALA-MIX-REVIEW.md` | Verified OS (audit) | R2 patalamix |
| `SPEC-33-PUSHING-GUIDE.md` | Enquiry-Discovery (L04) | research-library/pushing |
| `SPEC-34-AUTONOMOUS-PUSHING.md` | Enquiry-Discovery (L04) | research-library/pushing |
| `SPEC-35-COMPARATIVE-PUSHING.md` | Comparative Philosophy (L06) | research-library/pushing |
| `SPEC-36-LOGICVID3.md` | Enquiry-Discovery (L04) | research-library |
| `SPEC-3x-SESSION-Q1.md` | Enquiry-Discovery (L04) | Tantrāloka session (TĀ 1/52-55 reflexivity) |
| `SPEC-3x-SESSION-OBJECTIONS.md` | Enquiry-Discovery (L04) | hardest objections faced |
| `SPEC-40-LOGICVID-logicdog.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-41-LOGICVID-logicframework.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-42-LOGICVID-logicvidsmethod.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-43-LOGICVID-logicvid-postmortem.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-44-LOGICVID-logicframework2.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-45-LOGICVID-logicvid3.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-46-LOGICVID-logic5.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-47-LOGICVID-logic6.md` | Enquiry-Discovery (L04) | LOGICVID gold |
| `SPEC-48-LOGICVID-logic7.md` | Enquiry-Discovery (L04) | LOGICVID gold |
