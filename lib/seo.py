"""lib/seo.py — the agent-SEO compiler (Layer 07, SPEC-00 §17 + SPEC-49 §4).

One canonical identifier unifies the human graph, search-engine graph, agent graph, and API graph.
For every entity we emit:
  - ONE canonical public URL            /concept/free-will
  - machine read                        /concept/free-will.json
  - agent/prose                         /concept/free-will.md
  - API                                 /api/v1/concepts/free-will
  - semantic HTML (0-JS) with <link rel="canonical"> + schema.org JSON-LD
  - a sitemap for crawlers

This is the SEO layer Astro serves as static pages (perf rule 4: 0 JS; JSON-LD for bots + agents).
"""
from __future__ import annotations
import json, os


def _slug(eid):
    # ip:concept:free_will -> free-will  (the canonical public slug)
    return eid.rsplit(":", 1)[-1].replace("_", "-")


class SEOCompiler:
    def __init__(self, base_url="https://example.org"):
        self.base_url = base_url.rstrip("/")

    def canonical_url(self, entity_id, kind="concept"):
        return f"{self.base_url}/{kind}/{_slug(entity_id)}"

    def json_ld(self, entity_id, label, entity_type, ceiling, positions=None, neighbors=None):
        """schema.org JSON-LD (the agent + search-engine graph). One entity model."""
        g = {
            "@context": "https://schema.org",
            "@type": "Thing",
            "@id": self.canonical_url(entity_id),
            "name": label,
            "identifier": entity_id,
            "additionalProperty": {"@type": "PropertyValue", "name": "epistemic_ceiling",
                                   "value": ceiling or "MACHINE_PROPOSED"},
        }
        if positions:
            g["mentions"] = [{"@type": "Claim", "name": p.get("claim", p.get("id"))} for p in positions[:10]]
        if neighbors:
            g["relatedLink"] = [{"@type": "Thing", "name": n.get("label", n.get("name", "?"))}
                                for n in neighbors[:10]]
        return g

    def html_page(self, entity_id, label, entity_type, ceiling, body_md=None,
                  positions=None, neighbors=None, view="context"):
        """A 0-JS semantic HTML page with canonical + JSON-LD (what Astro serves)."""
        url = self.canonical_url(entity_id)
        jld = self.json_ld(entity_id, label, entity_type, ceiling, positions, neighbors)
        # minimal semantic HTML (0-JS; the reading content)
        sections = []
        if positions:
            sections.append("<h2>Positions</h2><ul>" +
                            "".join(f"<li>{p.get('claim', p.get('id'))} <em>({p.get('ceiling')})</em></li>"
                                    for p in positions[:10]) + "</ul>")
        if neighbors:
            sections.append("<h2>Related</h2><ul>" +
                            "".join(f"<li><a href='{self.canonical_url(n['label'],'concept')}'>{n['label']}</a> "
                                    f"[{n.get('rel','')}]</li>" for n in neighbors[:10]) + "</ul>")
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{label}</title>
  <link rel="canonical" href="{url}">
  <meta name="description" content="{label} - canonical {entity_type} node ({ceiling})">
  <script type="application/ld+json">{json.dumps(jld)}</script>
</head>
<body>
  <h1>{label}</h1>
  <p><strong>Type:</strong> {entity_type} &middot; <strong>Ceiling:</strong> {ceiling}</p>
  <div class="content">
    <div class="entity">{_markdown(body_md)}</div>
    {"".join(sections)}
  </div>
  <nav><a href="/sitemap.xml">sitemap</a></nav>
</body>
</html>"""
        return html, url

    def sitemap(self, entities):
        """XML sitemap of all canonical URLs (crawler indexability)."""
        urls = "\n".join(
            f"  <url><loc>{self.canonical_url(eid, kind)}</loc></url>"
            for eid, kind in entities)
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""


def _markdown(body_md):
    if not body_md:
        return ""
    # crude md->html for the prose projection (0-JS reading)
    out = []
    for line in body_md.splitlines():
        if line.startswith("## "):
            out.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("- "):
            out.append(f"<li>{line[2:]}</li>")
        elif line.strip():
            out.append(f"<p>{line}</p>")
    return "".join(out)
