# OpenInstead — Session Status Log

Persistent log, updated by Claude every session. Read from top-down.

---

## 2026-04-24 — Session 1b: Deploy-prep (added)

Alexandru wants to preview the site before buying a domain. Added:
- [x] `openinstead-preview.zip` (541 KB, 524 files) — drag into [app.netlify.com/drop](https://app.netlify.com/drop) for 2-min preview at an `xxx.netlify.app` URL.
- [x] `init-repo.sh` — one-command git init + push, parameterized by GitHub username + repo name.
- [x] `DEPLOY_NOW.md` — step-by-step guide with options A (Netlify Drop, 2 min) + B (GitHub + Cloudflare Pages, 10 min).
- [x] `.gitignore` — keeps `dist/` in repo (so Cloudflare/Netlify can serve it without a build step).

**NOT DONE (needs Alexandru's action):**
- GitHub repo creation — no MCP connector available for GitHub; Alexandru creates empty repo manually (1 min), then runs `init-repo.sh` or manual 5-cmd flow.
- GitHub auth — he'll use a Personal Access Token on first push.

**Known benign quirk:** Google Drive sync locks `.git/objects/*` when I try to init from the sandbox, so `init-repo.sh` starts with `rm -rf .git` to clean any partial state. On his local Mac this works fine.

---

## 2026-04-24 — Session 1: Initial build (COMPLETE)

**Duration:** single session.
**Owner this sprint:** Claude (autonomous build).
**Result:** 257 SEO pages generated, deploy-ready.

### What was built

- [x] Analysis document: `analiza_venit_pasiv_2026-04-24.md` (in parent folder)
- [x] Project decision: pSEO directory on "Open Source Alternatives to SaaS"
- [x] Full project scaffold in `pSEO-oss-alternatives/`
- [x] Data: 20 categories, 44 SaaS products, 68 OSS alternatives, 44 mappings
- [x] Templates: 8 Jinja2 templates (base, home, categories, category, saas, oss, comparison, static)
- [x] Build script: `build.py` (Python + Jinja2 + PyYAML)
- [x] Static CSS: dark modern theme, fully responsive
- [x] Generated output in `dist/`: 258 HTML files (257 in sitemap + 404)
  - 1 homepage
  - 1 categories index
  - 20 category pages
  - 44 SaaS "Alternatives to X" pages
  - 68 OSS profile pages
  - 121 side-by-side comparison pages (`/vs/{saas}-vs-{oss}/`)
  - About, Privacy, 404
- [x] SEO: unique titles + meta descriptions per page, canonical URLs, OpenGraph tags, JSON-LD ItemList on SaaS pages, sitemap.xml, robots.txt
- [x] AdSense: ad slots reserved (placeholder divs), ready to replace with real ad code post-approval

### What's blocked on Alexandru (see README.md for exact steps)

- [ ] Buy domain (~10€/year — Cloudflare Registrar cheapest for Cloudflare Pages deploy)
- [ ] Create GitHub repo, push the project
- [ ] Connect Cloudflare Pages → auto-deploy
- [ ] Verify Google Search Console + submit sitemap
- [ ] Wait ~3 weeks → apply for Google AdSense
- [ ] Configure RO bank account for USD/EUR wire transfer (for AdSense payout)

### Decisions taken (rationale)

- **Niche choice:** pSEO directory > utility tools first, because one property covers 257 pages vs 5 properties × 10 pages. Better compounding, single AdSense approval, single domain.
- **Sub-niche:** "Open Source Alternatives to SaaS" chosen over visa-requirements and cost-of-living because (a) incumbent awesome-selfhosted has poor SEO presence and (b) developer/tech audience = higher AdSense RPM ($5-10 vs $2-6 for travel).
- **Stack:** Python + Jinja2 + YAML (no JS framework). Output is pure static HTML → Cloudflare Pages gives unlimited bandwidth free. No build-time JS means Googlebot indexes everything on first crawl.
- **Data approach:** Editorial YAML (hand-curated), not scraped. Google Helpful Content penalizes AI-spun content; curated editorial survives.
- **Ad strategy:** Reserved 3 ad slot positions per long page (above-fold, mid-content, below-body). Placeholder divs until AdSense approves. Auto Ads strategy recommended for start.

### Verified facts at time of build

- Cloudflare Pages free tier: unlimited bandwidth, up to 20k files per site (we are at ~260).
- Chrome Web Store developer fee: $5 one-time (cited in README for future extension project).
- AdSense RPM for tech/dev audience: $5-15 typical.
- Gumroad: 10% flat fee (for when we diversify).
- Etsy: ~10-12% total fees (for when we diversify).

### Known limitations

- Only 4 alternatives per popular SaaS (some SaaS only have 2). Future sprint should expand to 5-6 per product.
- No screenshots yet — all-text content. Adding tool screenshots (even as SVG placeholders) would improve dwell time.
- No search functionality on-site. Could add client-side Fuse.js index in a future sprint.
- Comparison pages are "thin" (single alternative). Could expand each with a feature-by-feature deep dive.
- No blog / editorial layer yet. Google rewards sites with a mix of pSEO pages AND original essays/guides. Next sprint: add 5-10 long-form articles.

### Next session's priority list (Claude's TODO for session 2)

If Alexandru has completed deploy: confirm analytics → then:

1. Add 20 more SaaS products (focus: Adobe Creative Cloud, Microsoft Office 365, Salesforce Enterprise, Asana Enterprise, QuickBooks, Xero, Dropbox Business, Box, Sketch, InVision, HelpScout, Freshdesk, Notion AI, ClickUp, Airtable Enterprise, Webflow, Wix, Squarespace, Shopify, MailerLite).
2. Add 30 more OSS projects they map to.
3. Write 5 long-form articles (e.g., "Self-hosting in 2026: the honest survey", "Why your team can't ditch Slack yet", "The real cost of a Notion workspace at scale").
4. Add a search box (Fuse.js, client-side, no backend).
5. Add simple SVG/emoji icons per category for visual variety.
6. Submit to HN Show HN / Reddit r/selfhosted once site has real domain + ~3 polished articles.

---

## Template for future entries

```
## YYYY-MM-DD — Session N: <one-line summary>

### What was built
- [x] ...

### Blocks on Alexandru
- [ ] ...

### Decisions / notable
- ...

### Metrics at time of session (if deploy is live)
- Index coverage: X / 257 pages
- Google Search Console impressions (last 28 days): ...
- Clicks: ...
- AdSense eligibility status: ...
- Revenue to date: $...
```
