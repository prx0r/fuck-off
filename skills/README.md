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

## To add a skill
1. `mkdir skills/<name>` + `skills/<name>/SKILL.md` (with frontmatter).
2. Code the mechanism as a `scripts/` script.
3. Reference it in `AGENTS.md` (the behavior is then required/available to agents) + `NAVIGATION.md`.
4. If it's an *agent behavior* an agent should adopt, add it to the relevant AGENTS.md section.
