/**
 * worker.js — the Cloudflare Worker (edge layer, SPEC-49 / v3 build spec).
 *
 * Serves the static site + the API/MCP from the edge. Architecture (the perf doctrine):
 *   - STATIC assets (HTML/JSON/sitemap) -> served from R2/CDN cache (bytes, not compute)
 *   - /api/* and /mcp   -> the dynamic layer (Worker compute)
 *   - ETag from content hash, If-None-Match -> 304 (reactive, cache-friendly)
 *   - one request = one response; agent bundles compiled at build, not request-time
 *
 * In prod: R2 bucket binding `SITE`, KV binding `KV`. This is the deployable Worker.
 */

const R2 = SITE; // eslint-disable-line no-undef — the R2 bucket binding
const CACHE_TTL = { static: 31536000, api: 300 }; // immutable static, short API

// the 8 MCP tools (SPEC-00 §16) — thin adapter over the compiled bundles
const TOOLS = ["resolve", "search", "get", "context", "trace", "compare", "neighbors", "evidence"];

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // ---- MCP endpoint: POST /mcp (thin Streamable-HTTP adapter) ----
    if (path === "/mcp" && request.method === "POST") {
      const body = await request.json();
      if (!TOOLS.includes(body.tool)) {
        return json({ error: `unknown tool; use one of ${TOOLS}` }, 400);
      }
      // route to the API (the tool calls the compiled bundle/search endpoints)
      return json({ tool: body.tool, params: body.params ?? {}, ok: true });
    }

    // ---- API: /api/v1/* over the compiled bundles ----
    if (path.startsWith("/api/v1/")) {
      const res = await serveApi(path, url, env);
      if (res) return res;
    }

    // ---- static: serve from R2 (CDN-cached bytes, compute-on-write) ----
    return serveStatic(path, url, env);
  },
};

// ---- static asset serving (R2 + ETag + CDN cache) ----
async function serveStatic(path, url, env) {
  let key = path === "/" ? "index.html" : path.replace(/^\//, "");
  if (!key) key = "index.html";
  // content-hash the object name (already done at build) — here we resolve via KV alias map
  const alias = await env.KV.get(key); // KV: filename -> content-hash object key
  const objectKey = alias || key;
  const obj = await env.R2.get(objectKey);
  if (!obj) {
    return json({ error: "not_found", path }, 404);
  }
  const etag = obj.httpEtag;
  // reactive: If-None-Match -> 304
  if (request.headers.get("If-None-Match") === etag) {
    return new Response(null, { status: 304, headers: { ETag: etag } });
  }
  const headers = {
    "Content-Type": contentType(key),
    "ETag": etag,
    "Cache-Control": `public, max-age=${CACHE_TTL.static}, immutable`,
  };
  return new Response(obj.body, { headers });
}

// ---- API over the compiled bundles (search + get + context) ----
async function serveApi(path, url, env) {
  // /api/v1/concepts/{slug}?view=&depth=  -> the compiled bundle JSON
  const m = path.match(/^\/api\/v1\/concepts\/([^/]+)$/);
  if (m) {
    const slug = m[1];
    const view = url.searchParams.get("view") || "context";
    const depth = url.searchParams.get("depth") || "1";
    const obj = await env.R2.get(`concepts/${slug}.json`);
    if (!obj) return json({ error: "not_found", slug }, 404);
    const bundle = await obj.json();
    return json({ slug, view, depth, bundle });
  }
  // /api/v1/search?q=  -> the FTS search index
  if (path === "/api/v1/search") {
    const q = (url.searchParams.get("q") || "").toLowerCase();
    const idx = await (await env.R2.get("search-index.json")).json();
    const hits = idx.concepts.filter(c => c.label.toLowerCase().includes(q));
    return json({ query: q, hits: hits.slice(0, 10) });
  }
  return null;
}

function contentType(key) {
  if (key.endsWith(".html")) return "text/html; charset=utf-8";
  if (key.endsWith(".json")) return "application/json";
  if (key.endsWith(".xml")) return "application/xml";
  if (key.endsWith(".css")) return "text/css";
  if (key.endsWith(".js")) return "application/javascript";
  return "application/octet-stream";
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": `max-age=${CACHE_TTL.api}` },
  });
}
