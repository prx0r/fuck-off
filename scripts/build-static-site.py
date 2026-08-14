#!/usr/bin/env python3
"""build-static-site.py — the projection compiler → a real static site (SPEC-49 P0, the read plane).

Turns the canonical graph + argument into a fully static, deployable site (what Astro/Workers serve):
  site/
    index.html            the home page (0-JS, JSON-LD)
    concepts/{slug}.html  one 0-JS semantic HTML page per concept (JSON-LD + canonical + related)
    concepts/{slug}.json  the machine bundle per concept
    argument/             the argument graph pages
    sitemap.xml           all canonical URLs
    search-index.json     the FTS search index (for the Worker/API)
  All static bytes — compute on write, read from CDN (the perf doctrine).
"""
import os, sys, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from context_compiler import ContextCompiler
from seo import SEOCompiler

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
OUT = f"{ROOT}/site"
BASE_URL = "https://patala.org"
# real patala corpus data (read-only — agentpatala's production data, not modified)
PATALA_DATA = "/root/projects/patala/data"

def _slug(eid): return eid.rsplit(":", 1)[-1].replace("_", "-")

def sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


def compile_real_corpus(manifest):
    """Compile the REAL patala scholarship (bibliography + published IPVV passages + clusters)
    into the site's projections. Read-only on agentpatala's data — the organism's real content."""
    import glob
    os.makedirs(f"{OUT}/bibliography", exist_ok=True)
    os.makedirs(f"{OUT}/passages", exist_ok=True)
    os.makedirs(f"{OUT}/themes", exist_ok=True)

    # 1. bibliography (254 works)
    works = []
    bib_path = f"{PATALA_DATA}/corpus/atlas-bibliography.json"
    if os.path.exists(bib_path):
        bib = json.load(open(bib_path))
        for wid, rec in bib.get("records", {}).items():
            w = {"id": wid,
                 "title": rec.get("canonical_title") or rec.get("title") or wid,
                 "verified": str(rec.get("verified", "")).lower() == "true",
                 "translation_status": rec.get("translation_status") or "none",
                 "traditions": rec.get("traditions", [])}
            works.append(w)
            with open(f"{OUT}/bibliography/{_slug(wid)}.json", "w") as f:
                json.dump(w, f)
    manifest["bibliography"] = {"count": len(works), "works": works}

    # 2. published IPVV passages (49) — read the published index
    passages = []
    idx_path = f"{PATALA_DATA}/published/ipvv/index.json"
    if os.path.exists(idx_path):
        idx = json.load(open(idx_path))
        for p in idx.get("passages", []):
            pf = f"{PATALA_DATA}/published/ipvv/{p['file']}"
            d = {}
            if os.path.exists(pf):
                try: d = json.load(open(pf))
                except Exception: pass
            passages.append({"id": p.get("id"), "locator": p.get("locator"),
                             "reading": (d.get("l2_text") or d.get("l2") or "")[:400],
                             "has_c1": d.get("c1") is not None})
        manifest["passages"] = {"count": len(passages), "passages": passages}

    # 3. clusters (themes)
    clusters = []
    cl_path = f"{PATALA_DATA}/published/ipvv/clusters.json"
    if os.path.exists(cl_path):
        cl = json.load(open(cl_path))
        clusters = cl.get("clusters", cl) if isinstance(cl, dict) else cl
    manifest["clusters"] = {"count": len(clusters) if isinstance(clusters, list) else 0,
                            "clusters": clusters}

    with open(f"{OUT}/corpus.json", "w") as f:
        json.dump({"bibliography": len(works), "passages": len(passages),
                   "clusters": len(clusters) if isinstance(clusters, list) else 0}, f)
    print(f"  + real corpus: {len(works)} works, {len(passages)} passages, {len(clusters) if isinstance(clusters, list) else 0} clusters")
    return manifest

def main():
    g = json.load(open(f"{ROOT}/data/graph/graph.json"))
    a = json.load(open(f"{ROOT}/data/graph/argument.json"))
    cc = ContextCompiler(g, a)
    seo = SEOCompiler(BASE_URL)

    manifest = {"concepts": {}, "argument": {}, "generated": True, "counts": {}}
    # compile the REAL patala scholarship into the site (read-only on agentpatala's data)
    manifest = compile_real_corpus(manifest)

    os.makedirs(f"{OUT}/concepts", exist_ok=True)
    os.makedirs(f"{OUT}/argument", exist_ok=True)
    os.makedirs(f"{OUT}/assets", exist_ok=True)

    concepts = [n for n in g["nodes"] if n.get("type") == "concept"]
    n_pages = 0

    # ---- per-concept: HTML (JSON-LD + canonical) + JSON bundle ----
    for n in concepts:
        b = cc.compile(n["id"], depth=1)
        if not b:
            continue
        slug = _slug(n["id"])
        # JSON-LD
        jld = seo.json_ld(n["id"], b.entity["label"], b.entity["type"], b.entity["ceiling"],
                          b.positions, b.neighbors)
        # HTML page (0-JS semantic, canonical, JSON-LD)
        md = cc.to_markdown(n["id"], depth=1) or ""
        body_html = "".join(
            f"<p>{l[2:].strip()}</p>" if l.startswith("- ") else f"<h2>{l[3:].strip()}</h2>"
            if l.startswith("## ") else f"<p>{l}</p>" for l in md.splitlines() if l.strip())
        related = "".join(
            f'<li><a href="/concepts/{_slug(x["label"])}.html" data-rel="{x.get("rel","")}">{x["label"]}</a></li>'
            for x in b.neighbors[:12])
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{b.entity["label"]} — Pāṭala</title>
<meta name="description" content="{b.entity["label"]} — canonical {b.entity["type"]} node ({b.entity["ceiling"]})">
<link rel="canonical" href="{seo.canonical_url(n["id"])}">
<script type="application/ld+json">{json.dumps(jld)}</script>
<style>body{{font-family:system-ui,sans-serif;max-width:760px;margin:2rem auto;padding:0 1rem;line-height:1.6}}
a{{color:#0066cc;text-decoration:none}} .ceiling{{color:#666;font-size:.85rem}}
nav a{{margin-right:1rem}} ul{{margin:.5rem 0}}</style>
</head>
<body>
<nav><a href="/index.html">Home</a><a href="/sitemap.xml">Sitemap</a></nav>
<main>
<h1>{b.entity["label"]}</h1>
<p class="ceiling">Type: {b.entity["type"]} · Ceiling: {b.entity["ceiling"]} · <code>{b.bundle_hash}</code></p>
{body_html}
<h2>Related</h2><ul>{related}</ul>
</main>
</body>
</html>"""
        with open(f"{OUT}/concepts/{slug}.html", "w") as f:
            f.write(page)
        with open(f"{OUT}/concepts/{slug}.json", "w") as f:
            json.dump(b.to_dict("context", None, 1), f, indent=1)
        manifest["concepts"][slug] = {"id": n["id"], "label": b.entity["label"],
                                      "ceiling": b.entity["ceiling"],
                                      "url": seo.canonical_url(n["id"])}
        n_pages += 1

    # ---- argument pages ----
    for node in a.get("information_nodes", []):
        nid = node["id"]
        page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{node.get("label", nid)} — Argument</title>
<link rel="canonical" href="{BASE_URL}/argument/{nid}.html">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Claim","name":node.get("label", nid),"identifier":nid,"additionalProperty":{"@type":"PropertyValue","name":"epistemic_ceiling","value":node.get("epistemic_ceiling","MACHINE_PROPOSED")}})}</script>
</head><body><h1>{node.get("label", nid)}</h1><p class="ceiling">Ceiling: {node.get("epistemic_ceiling","MACHINE_PROPOSED")}</p>
</body></html>"""
        with open(f"{OUT}/argument/{nid}.html", "w") as f:
            f.write(page)
        manifest["argument"][nid] = {"label": node.get("label", nid),
                                     "ceiling": node.get("epistemic_ceiling", "MACHINE_PROPOSED")}

    # ---- sitemap ----
    urls = "\n".join(
        f"  <url><loc>{v['url']}</loc></url>" for v in manifest["concepts"].values())
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE_URL}/index.html</loc></url>
{urls}
</urlset>"""
    with open(f"{OUT}/sitemap.xml", "w") as f:
        f.write(sitemap)

    # ---- search index (for the Worker/API) ----
    search = []
    for slug, v in manifest["concepts"].items():
        search.append({"id": slug, "label": v["label"], "url": v["url"], "ceiling": v["ceiling"]})
    with open(f"{OUT}/search-index.json", "w") as f:
        json.dump({"concepts": search}, f)

    # ---- home page ----
    concept_rows = "".join(
        f'<li><a href="/concepts/{slug}.html">{v["label"]}</a> <span class="ceiling">({v["ceiling"]})</span></li>'
        for slug, v in sorted(manifest["concepts"].items(), key=lambda kv: kv[1]["label"]))
    home = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Pāṭala — the Verified Epistemic OS</title>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Pāṭala","description":"The Verified Epistemic OS"})}</script>
<style>body{{font-family:system-ui;max-width:900px;margin:2rem auto;padding:0 1rem;line-height:1.6}}
a{{color:#0066cc;text-decoration:none}}.ceiling{{color:#666;font-size:.85rem}}</style></head>
<body><h1>Pāṭala — the Verified Epistemic OS</h1>
<p>Canonical graph compiled to a static site. <strong>{n_pages}</strong> concept pages.</p>
<ul>{concept_rows}</ul>
</body></html>"""
    with open(f"{OUT}/index.html", "w") as f:
        f.write(home)

    manifest["counts"] = {"concepts": n_pages,
                          "argument_nodes": len(a.get("information_nodes", [])),
                          "bytes": sum(os.path.getsize(os.path.join(dp, fn))
                                       for dp, _, fns in os.walk(OUT) for fn in fns),
                          "root_hash": sha(json.dumps(manifest["concepts"], sort_keys=True))}
    with open(f"{OUT}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1)

    print(f"=== STATIC SITE BUILT → {OUT} ===")
    print(f"  {n_pages} concept pages (HTML + JSON)")
    print(f"  {len(a.get('information_nodes', []))} argument pages")
    print(f"  sitemap.xml + search-index.json + manifest.json")
    print(f"  total bytes: {manifest['counts']['bytes']}")
    print(f"  root hash: {manifest['counts']['root_hash']} (immutable, cacheable)")

if __name__ == "__main__":
    main()
