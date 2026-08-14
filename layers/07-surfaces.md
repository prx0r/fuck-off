# LAYER 07 — SURFACES
*Spine (Chunk 8). Astro site + API + MCP.*

## 1. What it is
The read surfaces: an Astro static site (0-JS reading), a Cloudflare Worker API, and an MCP server —
all serving compiled projections, not reconstructing at request time.

## 2. Purpose
Expose the argument objects as living pages (`/free-will`, `/consciousness`, ...) + agent endpoints.

## 3. Data
- Compiled projections from Layer 06

## 4. Processes
```
Astro over projections → Workers on /api /search /mcp → edge cache
```

## 5. Implementations
- Spec: `specs/SPEC-00-INFRA-BUILD.md` (§9-16 Astro/Workers/MCP) + `specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md`
- Perf: `docs/05-performance.md`

## 6. Docs
- `specs/SPEC-00-INFRA-BUILD.md` (§9-16 Astro/Workers/MCP)

## 7. Current state
`BUILT — the SEO/Astro surfaces are live (SPEC-49 P1)`: `lib/seo.py` (13/13). One canonical URL per
entity + semantic 0-JS HTML + schema.org JSON-LD + sitemap, generated as static cacheable bytes from
the compiled projections. Unifies the human/search-engine/agent/API graphs.
