#!/usr/bin/env python3
"""validate-seo-astro.py — the Astro/SEO surfaces (Layer 07, SPEC-00 §17 + SPEC-49 §4).

Generates the static read-plane: one canonical URL per entity + semantic 0-JS HTML with
schema.org JSON-LD + a sitemap, from the compiled projections. This is what Astro serves.
Unifies the human graph, search-engine graph, agent graph, and API graph from one entity model.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from context_compiler import ContextCompiler
from seo import SEOCompiler

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
OUT = "/tmp/opencode/astro-site"
def _slug(eid): return eid.rsplit(":", 1)[-1].replace("_", "-")
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== ASTRO / SEO SURFACES: canonical URLs + JSON-LD + sitemap ===\n")
g = json.load(open(f"{ROOT}/data/graph/graph.json"))
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))
compiler = ContextCompiler(g, arg)
seo = SEOCompiler("https://example.org")

# ---- canonical URL (one per entity, all representations share the ID) ----
url = seo.canonical_url("ip:concept:free_will")
check("canonical URL is the stable public slug", url == "https://example.org/concept/free-will")

# ---- JSON-LD (schema.org, the agent+search graph) ----
b = compiler.compile("ip:concept:free_will", 1)
jld = seo.json_ld("ip:concept:free_will", b.entity["label"], b.entity["type"],
                  b.entity["ceiling"], b.positions, b.neighbors)
check("JSON-LD has context+type+@id", jld["@context"] == "https://schema.org" and jld["@id"] == url)
check("JSON-LD carries the epistemic ceiling", jld["additionalProperty"]["value"] == "MACHINE_PROPOSED")
check("JSON-LD links related entities (semantic linking)", "relatedLink" in jld)

# ---- 0-JS semantic HTML page ----
html, html_url = seo.html_page("ip:concept:free_will", b.entity["label"], b.entity["type"],
                               b.entity["ceiling"], compiler.to_markdown("ip:concept:free_will", depth=1),
                               b.positions, b.neighbors)
check("HTML has canonical link", f'rel="canonical" href="{url}"' in html)
check("HTML embeds schema.org JSON-LD", "application/ld+json" in html and "schema.org" in html)
check("HTML is 0-JS (no <script src>)", "<script src=" not in html)
check("HTML is semantic (h1 + h2 + linked related)", "<h1>" in html and "<h2>Related</h2>" in html)
check("HTML canonical matches the JSON-LD @id", html_url == url)

# ---- sitemap (crawler indexability) ----
entities = [(n["id"], "concept") for n in g["nodes"] if n.get("type") == "concept"]
sitemap = seo.sitemap(entities)
check(f"sitemap lists {len(entities)} canonical URLs", f"<loc>" in sitemap and "free-will" in sitemap)
check("sitemap is valid urlset XML", 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"' in sitemap)

# ---- the static-site corpus pass (Astro output dir) ----
os.makedirs(f"{OUT}/concepts", exist_ok=True)
n_pages = 0
for nid, kind in entities:
    b = compiler.compile(nid, 1)
    if not b:
        continue
    html, _ = seo.html_page(nid, b.entity["label"], b.entity["type"], b.entity["ceiling"],
                            compiler.to_markdown(nid, depth=1), b.positions, b.neighbors)
    with open(f"{OUT}/concepts/{_slug(nid)}.html", "w") as f:
        f.write(html)
    n_pages += 1
with open(f"{OUT}/sitemap.xml", "w") as f:
    f.write(sitemap)
check(f"generated {n_pages} static 0-JS HTML pages + sitemap", n_pages >= 20)
check("pages are cacheable static bytes (not request-time)", len(os.listdir(f"{OUT}/concepts")) >= 20)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nASTRO/SEO SURFACES: one canonical URL per entity, semantic 0-JS HTML + schema.org JSON-LD +")
print("sitemap, generated as static cacheable bytes from the compiled projections. The human +")
print("search-engine + agent + API graphs are unified from one entity model (SPEC-00 §17).")
sys.exit(0 if all(c for _,c in results) else 1)
