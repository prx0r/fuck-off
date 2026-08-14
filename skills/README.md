# SKILLS — reusable agent capabilities

*2026-08-14. Skills are reusable agent BEHAVIORS (distinct from processes/docs — a skill is something
an agent *does*, triggered by intent; a process is a workflow). This directory follows the skill format
used by our cloned agent repos (YAML frontmatter: name/version/author/description/triggers).*

## Convention
Each skill lives in `skills/<name>/SKILL.md` with YAML frontmatter:
```yaml
---
name: <skill-name>
version: <x.y.z>
author: <owner>
description: >-        # what it does + trigger phrases
  ...
---
```

## Skills
| Skill | What it does | Mechanism |
|-------|--------------|-----------|
| `vcreate/` | backward-delivery planning (goal-regression): walk from a vision to current implementations, output reuse/to_build/ungrounded | `scripts/reverse-deliver.py` |
| `theatre-check/` | the verifiable-proof auditor (anti-theatre): for each kernel/docs claim, produce a VERIFIABLE PROOF it is implemented (test exists + passes + REAL data) with a hash; verdicts PROVEN / PROVEN-MECHANISM / UNPROVEN | `scripts/theatre-check.py` → `data/references/theatre-proofs.json` |

## The theatre-check rule (anti-theatre)
> Before declaring a claim "done"/"validated", run `python3 scripts/theatre-check.py` and confirm the
> kernel is **PROVEN** (real data). **PROVEN-MECHANISM** is an honest "mechanism works, not integrated"
> — not a claim of delivery. The kernel audit now covers all **22 kernels** (16 PROVEN / 6 mechanism /
> 0 unproven).

## To add a skill
1. `mkdir skills/<name>` + `skills/<name>/SKILL.md` (with frontmatter).
2. Code the mechanism as a `scripts/` script.
3. Reference it in `AGENTS.md` (the behavior is then required/available to agents) + `NAVIGATION.md`.
4. If it's an *agent behavior* an agent should adopt, add it to the relevant AGENTS.md section.
