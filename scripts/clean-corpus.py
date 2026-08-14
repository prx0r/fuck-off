#!/usr/bin/env python3
"""Clean + organize the informationphilosopher corpus into a modular structure.

Source: /mnt/HC_Volume_106427611/CX-Train/informationphilosopher/www.informationphilosopher.com
Target: /mnt/HC_Volume_106427611/ip-graph/data/raw/

Layout (modular, mirrors patala's layering):
  01_raw/
    html_articles/    real content HTML, one flat dir with per-source subdirs
    pdfs/             the 437 PDFs (books/papers), organized by section
    images/           supporting images
    errors/           the error pages (quarantined, not deleted — safe to inspect)
    MANIFEST.json     full inventory with quality classification
"""
import os, re, json, shutil, html as htmllib

SRC = "/mnt/HC_Volume_106427611/CX-Train/informationphilosopher/www.informationphilosopher.com"
DST = "/mnt/HC_Volume_106427611/ip-graph/data/raw"

ERROR_MARKERS = ["Bad Request", "skybuilders", "Apache/2.4", "afrispa", "server could not understand",
                 "Your browser sent a request"]

HTML_DST = os.path.join(DST, "html_articles")
PDF_DST = os.path.join(DST, "pdfs")
IMG_DST = os.path.join(DST, "images")
ERR_DST = os.path.join(DST, "errors")
for d in (HTML_DST, PDF_DST, IMG_DST, ERR_DST):
    os.makedirs(d, exist_ok=True)

def is_error_html(text):
    return sum(1 for m in ERROR_MARKERS if m.lower() in text.lower()) >= 1

def real_h1(text):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if not m: return None
    t = htmllib.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    return t if len(t) >= 5 and "Bad Request" not in t else None

def safe(seg):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", seg).strip("_")

manifest = {"html_real": [], "pdfs": [], "images": [], "errors": [], "other": []}

for dirpath, dirnames, filenames in os.walk(SRC):
    for fn in filenames:
        fp = os.path.join(dirpath, fn)
        rel = os.path.relpath(fp, SRC)
        ext = os.path.splitext(fn)[1].lower()
        relparts = rel.split("/")
        section = relparts[0] if len(relparts) > 1 else "root"

        if ext == ".html":
            try:
                text = open(fp, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            if is_error_html(text):
                dest = os.path.join(ERR_DST, section)
                os.makedirs(dest, exist_ok=True)
                shutil.copy2(fp, os.path.join(dest, fn))
                manifest["errors"].append(rel)
            else:
                title = real_h1(text)
                m = re.search(r'<div class="bodycontent"[^>]*>(.*?)</div>', text, re.S)
                body = m.group(1) if m else text
                blen = len(re.sub(r"<[^>]+>", "", body))
                dest = os.path.join(HTML_DST, safe(section))
                os.makedirs(dest, exist_ok=True)
                shutil.copy2(fp, os.path.join(dest, fn))
                manifest["html_real"].append({"path": rel, "title": title, "body_len": blen})
        elif ext == ".pdf":
            dest = os.path.join(PDF_DST, safe(section))
            os.makedirs(dest, exist_ok=True)
            shutil.copy2(fp, os.path.join(dest, fn))
            manifest["pdfs"].append({"path": rel, "size": os.path.getsize(fp)})
        elif ext in (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"):
            dest = os.path.join(IMG_DST, safe(section))
            os.makedirs(dest, exist_ok=True)
            shutil.copy2(fp, os.path.join(dest, fn))
            manifest["images"].append(rel)
        else:
            manifest["other"].append(rel)

with open(os.path.join(DST, "MANIFEST.json"), "w") as f:
    json.dump(manifest, f, indent=1)

print("=== CLEAN ORGANIZATION DONE ===")
print(f"  real HTML: {len(manifest['html_real'])}")
print(f"  PDFs:      {len(manifest['pdfs'])} ({sum(p['size'] for p in manifest['pdfs'])/1048576:.1f}MB)")
print(f"  images:    {len(manifest['images'])}")
print(f"  errors:    {len(manifest['errors'])}")
print(f"  other:     {len(manifest['other'])}")
print("\n  HTML by section:")
from collections import Counter
c = Counter(p["path"].split("/")[0] for p in manifest["html_real"])
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(f"    {k:20s} {v}")
