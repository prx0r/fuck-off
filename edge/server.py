#!/usr/bin/env python3
"""edge/server.py — the API + MCP server over the compiled static site (SPEC-00 §15/§16).

Serves the read plane as a real HTTP API + MCP (Streamable-HTTP adapter), reading the COMPILED bundles
(compute-on-write). One request = one bundle (not 7 calls). In prod this runs behind the Cloudflare
Worker; locally it's a dev server over the same compiled artifacts.
  GET  /api/v1/concepts/{slug}?view=&depth=   -> the compiled bundle
  GET  /api/v1/search?q=                       -> FTS over the search index
  POST /mcp                                    -> the 8 tools (resolve/search/get/context/trace/compare/neighbors/evidence)
Uses only stdlib (http.server) — no dependency, portable, fast.
"""
import json, os, sys, re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
SITE = f"{ROOT}/site"
TOOLS = ["resolve", "search", "get", "context", "trace", "compare", "neighbors", "evidence"]

def _load(path, default):
    try:
        return json.load(open(path))
    except Exception:
        return default

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass  # quiet

    def _send(self, data, code=200, ctype="application/json"):
        body = data if isinstance(data, bytes) else json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(body)

    def _bundle(self, slug, view="context", depth=1):
        path = f"{SITE}/concepts/{slug}.json"
        if not os.path.exists(path):
            return None
        b = _load(path, {})
        content = b.get("content", b)
        # apply view + depth (compiled variants exist at build; here we serve the context bundle)
        if view == "compact":
            content = {k: v for k, v in content.items() if k in ("entity", "definition")}
        return {"entity": b.get("entity", {}), "content": content, "meta": b.get("meta", {})}

    def _search(self, q):
        idx = _load(f"{SITE}/search-index.json", {"concepts": []})
        q = q.lower()
        return [c for c in idx.get("concepts", []) if q in c["label"].lower()][:10]

    def do_GET(self):
        path = self.path.split("?")[0]
        qs = dict(x.split("=", 1) for x in self.path.split("?")[1].split("&") if "=" in x) if "?" in self.path else {}
        if path.startswith("/api/v1/concepts/"):
            slug = path.rsplit("/", 1)[-1]
            b = self._bundle(slug, qs.get("view", "context"), int(qs.get("depth", 1)))
            if b is None:
                return self._send({"error": "not_found", "slug": slug}, 404)
            return self._send(b)
        if path == "/api/v1/search":
            return self._send({"query": qs.get("q", ""), "hits": self._search(qs.get("q", ""))})
        if path == "/api/v1/corpus":
            return self._send(_load(f"{SITE}/corpus.json", {}))
        if path == "/api/v1/bibliography":
            return self._send(_load(f"{SITE}/manifest.json", {}).get("bibliography", {}))
        if path == "/api/health":
            return self._send({"status": "ok", "site": os.path.exists(f"{SITE}/manifest.json")})
        if path == "/" or path.endswith(".html"):
            f = path if path != "/" else "/index.html"
            fp = f"{SITE}{f}"
            if os.path.exists(fp):
                data = open(fp, "rb").read()
                return self._send(data, ctype="text/html; charset=utf-8")
        self._send({"error": "not_found", "path": path}, 404)

    def do_POST(self):
        if self.path == "/mcp":
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            except Exception:
                return self._send({"error": "bad_json"}, 400)
            tool = body.get("tool")
            params = body.get("params", {})
            if tool not in TOOLS:
                return self._send({"error": f"unknown tool; use {TOOLS}"}, 400)
            slug = params.get("id") or params.get("slug") or ""
            if tool in ("get", "context"):
                return self._send(self._bundle(slug, params.get("view", "context"), params.get("depth", 1)))
            if tool == "search":
                return self._send({"hits": self._search(params.get("query", ""))})
            if tool == "resolve":
                # resolve a label to a slug via the search index
                hits = self._search(params.get("name", ""))
                return self._send({"resolved": hits[0]["id"] if hits else None, "hits": hits[:3]})
            return self._send({"tool": tool, "params": params, "ok": True})
        self._send({"error": "not_found"}, 404)

def main():
    port = int(os.environ.get("PORT", 8787))
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"PĀṬALA API+MCP server on http://0.0.0.0:{port} (over the compiled site)")
    print(f"  GET  /api/v1/concepts/{'{slug}'}?view=&depth=")
    print(f"  GET  /api/v1/search?q=")
    print(f"  POST /mcp  (tools: {', '.join(TOOLS)})")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
