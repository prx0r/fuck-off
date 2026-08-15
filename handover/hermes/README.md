# handover/hermes — Hermes execution kernel notes (imported from patala, adapted for ip-graph)

*2026-08-15. Imported from patala's `handover/hermes/` + `docs/global/HERMES-CALLING.md` so ip-graph
holds the correct Hermes thesis + calling convention in its own repo. agentgraph's hard-won lesson:
**Hermes is the execution kernel — call it as an AGENT (`hermes chat`), never blind `-z`, and never
fake generation with regex.***

## THE ONE RULE (read this first — the mistake I keep making)

> **`hermes -z "<prompt>"` is BLIND** — one-shot text completion, no file access / tools / skills
> (~3.8% yield on translation). **Use `hermes chat` (agentic)** so Hermes can read the repo + skills +
> reference maps itself. The architecture rule: **HERMES for GENERATION, .py for REDUCTION.**
> (Full reference: `HERMES-CALLING.md`.)

## The docs (in this folder)

| File | What |
|---|---|
| **`HERMES-CALLING.md`** | THE calling convention — agentic `hermes chat`, profile+project, the anti-patterns (blind `-z`, ARG_MAX overflow). READ FIRST. |
| **`CANONICAL.md`** | THE integration thesis: Hermes = replaceable execution kernel; Pāṭala = durable epistemic state. |
| **`hermespatala-architecture-review.md`** | The DAG/Hermes architecture review — why orchestration is deterministic Python, Hermes is the execution fabric (TWO DAGs, not interchangeable). |
| **`AUTOTRANSLATE-NORTHSTAR.md`** | The engineering objective: RAW-L0 (MODE_B) — the one gap blocking autonomous translation. |
| **`TRANSLATION-APPROACH-AND-VALIDATION.md`** | The production doctrine (validation-first, Dyczkowski gold, term-context packets). |
| `DEV-PLAN.md` · `PATALA-SETUP.md` · `PEER-REVIEW.md` | patala's Hermes build plan, profile setup, and the peer-review/scholar-surface spec. |
| `README-PATALA.md` | patala's original index (context). |

## Hermes has FULL filebase access (read AND edit every file)

**Crucial capability (do not waste it):** when Hermes runs as an agent through the `patala` profile
(`hermes chat -p patala --yolo`), it has read/write access to the **entire filebase** — it can open,
read, and **edit any file** across both repos (ip-graph AND patala) and run tools, not just answer
prompts. So the agentic pattern is not limited to "return JSON":

- **Passing file paths in the prompt = Hermes reads them itself** — you do NOT need to hand-stuff file
  contents into the prompt (that is exactly the blind-`-z` mistake; it blows ARG_MAX and hides context).
- **You can delegate real WORK to Hermes** — e.g. "read `specs/SPEC-46...md`, derive the enquiry
  structure, and WRITE it to `data/logicvid/enquiry-gold.json`." Hermes can do the file I/O + the
  generation, and `.py` reduces/validates afterwards.
- **It can edit its own outputs / other files** — great for autonomous overnight work where Hermes does
  the generation + file writes and a Python gate verifies.
- **Constraint (single-writer):** because it can write, coordinate so two agents don't both edit the
  same registry/file — the `schema.py` separate-process rule + one-heavy-job rule still hold.

## How ip-graph calls Hermes (the wrapper)

Use `lib/hermes_exec.py` — it already shells to the CORRECT agentic call and, since 2026-08-15, runs
through the **`patala` profile** (`hermes -p patala chat ...`, env `HERMES_PROFILE`, default `patala`)
so the Pāṭala skills + MCP load.

```python
from hermes_exec import agentic
out = agentic(system, user, cwd="<repo>", max_turns=8)   # returns model text
```

- GENERATION (translation, commentary, cruxes, essays, enquiry-discovery, new pushing) → `agentic`.
- REDUCTION (review, staleness, evidence, gates, epistemic, aggregation) → deterministic `.py` kernels.
- Correct model invocation (fixed): **always use `deepseek-v4-flash` with provider `opencode-go`**
  (`-m deepseek-v4-flash --provider opencode-go`). This is pinned in `lib/hermes_exec.py` (defaults
  `PATALA_MODEL`/`PATALA_PROVIDER`) AND in the patala profile `~/.hermes/profiles/patala/config.yaml`.
  Never rely on `HERMES_MODEL` alone, and never use a different model.

## The LOGICVID gold rule (anti-theatre)

The LOGICVID gold is **meant to be Hermes-driven**: the model reads each real gold transcript and
derives the enquiry structure (taxonomy → theorem → boundary → frontier) + curiosity markers — that is
GENERATION. `.py` only REDUCES (validates + aggregates). `scripts/ingest-logicvid-gold-enquiry.py` does
exactly this: Hermes derives per file, .py aggregates, regex is only an honest fallback.
