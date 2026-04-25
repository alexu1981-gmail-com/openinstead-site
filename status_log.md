# OpenInstead — Session Status Log

Persistent log, updated by Claude every session. Read from top-down.

---

## 2026-04-25 — Session 4: Reddit-ready maturity sprint ✅

**Goal:** mature site înainte de Reddit launch (r/selfhosted + r/opensource).

**Total pages now: 508** (up from 394 — +114 pages, +29%).
**OG share images: 135** (homepage + 38 categorii + 88 SaaS + 8 articole), 1200×630 PNG.

Added:
- [x] **Pillow-based OG image generator** în build.py (`generate_og_image()`): dark `#0e1116`, accent verde `#3fb950`, kicker chip pentru categorie, titlu mare cu greedy-wrap, OpenInstead wordmark bottom-right. ~135 PNG generate la fiecare build.
- [x] **base.html upgrade:** `og:image` + `og:image:width/height` + `twitter:card=summary_large_image` + `twitter:image`. Previous era doar `summary` text card.
- [x] **+8 categorii noi:** identity-sso, vpn, transactional-email, wiki-docs, time-tracking, status-pages, business-intelligence, newsletters.
- [x] **+20 SaaS produse:** Okta, NordVPN, ExpressVPN, SendGrid, Mailgun, Netlify, Render, Railway, Pipedrive, Freshdesk, Box, Confluence, GitBook, Toggl, Harvest, Statuspage, Tableau, Power BI, Dashlane, Substack.
- [x] **+23 OSS profiles noi:** Keycloak, Authentik, Authelia, Zitadel, WireGuard, OpenVPN, Postal, Haraka, Twenty CRM, osTicket, BookStack, Wiki.js, Outline, Docusaurus, MkDocs, Kimai, Cachet, Gatus, Apache Superset, Metabase, Redash, Passbolt, WriteFreely.
- [x] **+20 mappings** (toate cele 20 SaaS noi → OSS alternatives, best-fit ordered).
- [x] **+2 long-form articles:**
  - "When self-hosting goes wrong: seven failure modes and how to avoid them" (~2400 words, Reddit-bait honest retrospective)
  - "Will the open source project you depend on still exist in three years?" (~2400 words, bus-factor checklist)
- [x] **+60 comparison pages** (185 → 245).
- [x] Build re-run clean: 0 warnings, 0 errors, 501 search-index entries.

Sanity check după rebuild:
- HTML pages: 508 ✓
- OG PNGs: 135 ✓ (1+38+88+8)
- Sitemap URLs: 507 ✓
- Toate paginile au `og:image` absolute URL în meta + `twitter:card=summary_large_image`.

**Next steps (ale tale, după push):**
- [ ] Așteaptă ~2 min Cloudflare Pages rebuild → verifică https://openinstead.dev (homepage + un articol nou + un SaaS nou).
- [ ] **Test OG card pe Twitter/X:** [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator) cu URL `https://openinstead.dev/article/when-self-hosting-goes-wrong-seven-failure-modes/`.
- [ ] **Test OG card pe LinkedIn:** [linkedin.com/post-inspector](https://www.linkedin.com/post-inspector/).
- [ ] **Test pe Facebook:** [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug/) — forțează refresh dacă a fost cached.
- [ ] **Reddit pre-launch:** alege un articol-anchor pentru r/selfhosted (probabil failure-modes), vezi DISTRIBUTION_PLAN.md pentru timing.

---

## 2026-04-25 — Session 3: Domain live ✅🌐

**Pushed:** commit `7e29712` pe main. Cloudflare Pages rebuild automat în ~2 min.

**Site live pe domeniu propriu:** https://openinstead.dev

Added:
- [x] `SITE_URL = https://openinstead.dev` în build.py (confirmat, era deja default — bine că l-am pus așa din sprint 1).
- [x] Favicon SVG (monogram "OI" pe fond dark cu accent verde) — elimina 404 pentru /favicon.ico.
- [x] `<link rel="icon">` în base template.
- [x] Toate 395 pagini rebuilded cu canonical URL corect către openinstead.dev.
- [x] Sitemap.xml actualizat cu noul domeniu.

Pending Alexandru (acum e timpul):
- [ ] **Google Search Console** — add property `openinstead.dev`, verify via DNS (1 click pe Cloudflare), submit sitemap `https://openinstead.dev/sitemap.xml`. Link: https://search.google.com/search-console
- [ ] **Bing Webmaster Tools** — https://www.bing.com/webmasters
- [ ] **Cloudflare Web Analytics** — dash.cloudflare.com → Analytics → Web Analytics → Add site.
- [ ] **Redirect `www.openinstead.dev` → `openinstead.dev`** (sau invers, pick one) — în Cloudflare Pages → Custom domains, sau via Page Rule.

---

## 2026-04-25 — Session 2.1: Distribution strategy + AdSense prep ✅

**Pushed:** commit `13ae462` pe main.

**Added:**
- [x] [DISTRIBUTION_PLAN.md](DISTRIBUTION_PLAN.md) — 12-week roadmap: domeniu, Search Console, Reddit launch, AdSense application timing, projections realiste, cheltuieli estimate.
- [x] Contact page (`/contact/`) — prerequirement pentru AdSense (email: `hello@openinstead.dev`).
- [x] RSS feed la `/articles/rss.xml` — pentru subscribe/backlink-uri naturale.
- [x] Footer nav extins cu Contact + RSS links.

**Decizii pending (de la Alexandru):**
1. Domeniu — recomandat `openinstead.dev` pe Cloudflare Registrar (~$12/an).
2. Email pentru contact page — `alexu1981@gmail.com` direct sau `contact@openinstead.dev` după domain setup?
3. Cont AdSense — PF (Alexandru Drăghici) sau PFA/SRL? Depinde de target revenue.

**Next concrete steps (ale tale, în ordine):**
- [ ] Verifică și cumpără domeniul (5-10 min).
- [ ] Conectează-l la Cloudflare Pages (Custom Domains) — 5 min.
- [ ] Google Search Console: add property + submit sitemap (10 min).
- [ ] Bing Webmaster Tools (5 min).
- [ ] Cloudflare Web Analytics enable (2 min).
- [ ] La săpt 3: Reddit r/selfhosted + r/opensource post.
- [ ] La săpt 4: AdSense apply.

**Planning review:** după ce cumperi domeniul, open new Claude session — voi reciti memory + status_log și continuăm cu sprint 3 (OG images, JSON-LD Org markup, +20 SaaS al doilea val).

---

## 2026-04-24 — Session 2: Expansion sprint ✅

**Pushed:** commit `3766bfe` pe main. Cloudflare Pages face rebuild automat în ~2 min.

**Total pages now: 394** (up from 257 — +137 pages, +53%).

Added:
- [x] +10 categorii noi: whiteboards, screen-recording, writing-tools, rss-readers, social-media, website-builders, ecommerce, paas-hosting, accounting, ai-coding.
- [x] +24 SaaS products: Microsoft Teams, Webex, ClickUp, Linear, Basecamp, Miro, InVision, Sketch, Loom, Grammarly, Pocket, Feedly, Buffer, Hootsuite, Airtable, Webflow, Wix, Shopify, HelloSign, Heroku, Vercel, Xero, QuickBooks, GitHub Copilot.
- [x] +31 OSS profiles: Kanboard, Redmine, OpenBoard, Drawpile, OBS Studio, ShareX, LanguageTool, Wallabag, LinkAce, FreshRSS, Miniflux, Mixpost, Postiz, Teable, Silex, GrapesJS, WordPress, Hugo, Ghost, WooCommerce, Saleor, Medusa, ERPNext, Akaunting, InvoicePlane, Dokku, Coolify, CapRover, Continue, Aider, Tabby.
- [x] +64 comparison pages (185 total).
- [x] **6 long-form articles** at `/article/{slug}/`:
  - Self-hosting in 2026: the honest survey
  - Why your team can't ditch Slack yet
  - The real monthly cost of a Notion workspace at scale
  - Open source alternatives: the comparison criteria that actually matter
  - From SaaS to self-hosted: a 30-day migration playbook
  - Why the best open source alternative is sometimes a smaller one
- [x] Articles index la `/articles/`.
- [x] **Client-side search** în header — no JS framework, minimal scorer; index la `/search-index.json` (388 entries).
- [x] Mobile-responsive CSS pentru header + search.
- [x] Build script: markdown parser inline (fără dependencies noi), `dirs_exist_ok` pentru re-copy static.

Fixed:
- YAML parse error în saas_products (tagline ClickUp cu ghilimele neescape-uite).
- `shutil.copytree` fail pe re-build (folderele din Drive nu pot fi șterse în sandbox — `dirs_exist_ok=True`).

**Next sprint (session 3) — decision pending:**
- Opțiune A: a doua proprietate (utility tool — concrete calculator, RPM $6-15).
- Opțiune B: planificare distribuție (Show HN, Reddit r/selfhosted, domeniu propriu + AdSense roadmap).
- Opțiune C: mai multe articole + un al doilea round de expansion (GraphQL categories, marketing automation, CDN alternatives).

**Site live după auto-deploy:** https://openinstead-site.alexu1981.workers.dev (va reflecta sprint 2 în ~2 min după push).

---

## 2026-04-24 — Session 1d: SITE LIVE ✅✅

- [x] Cloudflare Pages/Workers deploy succeeded.
- [x] **Live URL:** https://openinstead-site.alexu1981.workers.dev
- [x] Visual verification by Alexandru: homepage OK, category cards OK, SaaS pages + comparison tables render correctly.
- [x] Auto-deploy pipeline active: any future `git push` to main → rebuild in ~2 min.

**Site is now LIVE.** Sprint 1 complete. Total cost so far: **0€**.

**What's next (decisions pending for sprint 2):**
- Expansion: +20 SaaS, +30 OSS, 5 long-form articles, search box.
- OR: kick off a second property (utility tool #1 — concrete calculator has highest RPM in xlsx).
- OR: domain + AdSense application planning (works.dev subdomain is NOT AdSense-eligible).

**Security housekeeping:** PAT `github_pat_11BFD...` still active. If no updates needed in next 48h, Alexandru should revoke it at https://github.com/settings/tokens.

---

## 2026-04-24 — Session 1c: GitHub repo live ✅

- [x] Repo created: **https://github.com/alexu1981-gmail-com/openinstead-site** (public).
- [x] 280 files pushed on `main` branch, commit `b2b0ab0`.
- [x] 258 HTML pages in `dist/` pushed and visible on GitHub.
- [x] Verified clone pulls everything back correctly.

**How push was done (so future sessions can repeat):**
- User provided a Fine-grained PAT.
- Note: `api.github.com` is blocked in Claude's sandbox egress list, so I cannot create repos via REST API from here — user had to create the empty repo via web UI (github.com/new).
- `git push` to `github.com` WORKS (github.com is allowed). Push flow: copy project to `/tmp` (avoid Drive permission issues with `.git/`), `git init`, commit, `git remote add origin https://x-access-token:TOKEN@github.com/USER/REPO.git`, `git push -u origin main`. Done.

**Security note:** PAT lives only in conversation context, not in memory or any file. When Alexandru finishes with this project, he should revoke the token at https://github.com/settings/tokens.

**Next step for Alexandru (5 min):** connect the repo to Cloudflare Pages via [dash.cloudflare.com](https://dash.cloudflare.com) → Workers & Pages → Create → Pages → Connect to Git → select `openinstead-site` → Build output: `dist`. Site live at `openinstead-site.pages.dev` in ~2 min.

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
