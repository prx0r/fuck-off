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
