// astro.config.mjs — the Astro static site (SPEC-49, 0-JS reading)
import { defineConfig } from 'astro/config';

// The site is precompiled by build-static-site.py (0-JS HTML + JSON-LD + canonical URLs).
// Astro reads the compiled projections (site/concepts/*.json) and renders semantic pages.
// Output static, server-output to dist/ (deployed to Cloudflare Pages/Workers static assets).
export default defineConfig({
  output: 'static',
  site: 'https://patala.org',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto',
  },
  // islands only where needed; reading pages are 0-JS
  // integrations: [preact()]  // add only for interactive islands
});
