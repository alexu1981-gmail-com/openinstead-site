# OpenInstead — Open Source Alternatives Directory

Programmatic SEO directory site: **44 popular SaaS products** mapped to **68 open source alternatives**, generating **257 SEO-optimized pages** from structured YAML data.

- Categories index: 20 categories
- `/alternatives-to/{saas}/` : one page per SaaS product (44)
- `/open-source/{oss}/` : one page per OSS project (68)
- `/category/{slug}/` : one page per category (20)
- `/vs/{saas}-vs-{oss}/` : 121 direct comparison pages
- Plus: home, about, privacy, 404, sitemap.xml, robots.txt

---

## What Alexandru needs to do (one-time, ~30 min)

### Step 1 — Pick and buy a domain (~10€/year)

Suggested domain ideas (verify availability when you read this):

| Domain | Vibe | Note |
|--------|------|------|
| **openinstead.dev** | Clean, developer-friendly | Used in code as default, easy to change |
| **openinstead.com** | Classic | If available |
| **ditchsaas.com** | Punchy | Memorable for social shares |
| **unSaaS.dev** | Short | Dev-community friendly |
| **selfhosted.directory** | Descriptive | Appeals to self-host audience |
| **oss-alt.com** | Abbreviated | Cheap and specific |
| **theopensource.fyi** | Fun | If you want personality |

Where to buy: **Namecheap**, **Porkbun** (cheapest TLDs), or **Cloudflare Registrar** (at cost, no markup — recommended if you'll use Cloudflare Pages anyway).

### Step 2 — Create a free GitHub repo

1. Go to github.com, new repo (public or private, both work).
2. Name suggestion: `openinstead-site`.
3. Upload the whole `pSEO-oss-alternatives/` folder. Easiest: install GitHub Desktop, drag-drop, commit, push.

### Step 3 — Deploy on Cloudflare Pages (FREE, unlimited bandwidth)

1. Go to `dash.cloudflare.com` → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**.
2. Authorize the GitHub repo.
3. **Build settings:**
   - Build command: `pip install pyyaml jinja2 && python build.py`
   - Build output directory: `dist`
   - Environment variable: `SITE_URL=https://yourdomain.com` (use your chosen domain)
   - Python version: set env var `PYTHON_VERSION=3.10` (Cloudflare Pages supports this)
4. Click Deploy. First build takes ~2 minutes.
5. You'll get a `.pages.dev` subdomain immediately (site is live).

### Step 4 — Point your domain

1. In Cloudflare Pages → your project → Custom domains → add `yourdomain.com` and `www.yourdomain.com`.
2. If domain is on Cloudflare Registrar: zero config.
3. If domain is elsewhere: Cloudflare will show DNS records to add.

### Step 5 — Google Search Console (FREE, essential)

1. `search.google.com/search-console` → add property → your domain.
2. Verify ownership (Cloudflare DNS = one-click).
3. Submit sitemap: `https://yourdomain.com/sitemap.xml`.
4. Google starts indexing within 1-7 days.

### Step 6 — Google AdSense (once you have ~20 days of traffic + 15-30 posts)

AdSense is stricter now — apply **after** the site has been live for ~3-4 weeks with organic traffic. We already reserved ad slots in the templates (`<div class="ad-slot">`). When approved:

1. Get your `ca-pub-XXXXXXXX` ID.
2. Uncomment the `<script async src="...">` line in `templates/base.html`.
3. Replace the placeholder `<div class="ad-slot">` blocks with real AdSense `<ins>` tags (AdSense Auto Ads can handle placement automatically — easier for start).
4. Rebuild and push.

AdSense pays out via **wire transfer** directly to your Romanian bank account once you pass **$100** (threshold can be US $100 or equivalent).

### Step 7 — (Optional) Backup analytics

- Install **Cloudflare Web Analytics** (free, privacy-friendly, comes with Pages): dash.cloudflare.com → Analytics → Web Analytics.
- Or add **Plausible** self-hosted for more detail (gratis if you spin up on your VPS; $9/month if you use Plausible Cloud).

---

## How to regenerate the site

After editing any `data/*.yaml` (adding more SaaS/OSS):

```bash
pip install pyyaml jinja2 --break-system-packages
python3 build.py
```

Output goes in `dist/`. Commit + push and Cloudflare Pages rebuilds automatically.

---

## Adding new content (for Claude to do in future sessions)

To scale past the initial 44 SaaS / 121 comparisons, next sessions will:

1. Add 30-50 more SaaS products (especially high-intent ones: Adobe CC, Salesforce, SAP, Workday, Asana upsells, etc.).
2. Expand each mapping with 4-6 alternatives instead of 2-4.
3. Add "roundup" pages (e.g. "Best open source alternatives in 2026").
4. Add individual feature-comparison essays for top products (manual effort, high SEO value).
5. Submit to directories: ProductHunt, HackerNews Show HN, Reddit r/selfhosted.

Each sprint of this kind adds ~50-150 more pages.

---

## SEO targets (realistic)

- **Month 1-2:** Google indexes ~50-80% of pages. 0-20 vis/day.
- **Month 3-4:** Long-tail queries start ranking. 30-150 vis/day.
- **Month 6-9:** Mature — 300-1500 vis/day depending on niche depth and backlinks.
- **Revenue estimate at maturity:** 30k vis/month × $4-8 RPM = $120-400/month *on this one site*.

The "big unlock" is external links: HN Show HN, Reddit r/selfhosted + r/degoogle, a mention in a self-hosting YouTuber's video. One or two of these can accelerate the timeline by 3-6 months.

---

## File structure

```
pSEO-oss-alternatives/
├── README.md                    (this file)
├── build.py                     (site generator)
├── status_log.md                (session-by-session progress)
├── data/
│   ├── categories.yaml          (20 categories)
│   ├── saas_products.yaml       (44 SaaS products)
│   ├── oss_alternatives.yaml    (68 OSS projects)
│   └── mappings.yaml            (SaaS → [OSS, OSS, ...])
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── categories_index.html
│   ├── category.html
│   ├── saas_page.html
│   ├── oss_page.html
│   ├── comparison.html
│   └── static_page.html
├── static/
│   └── css/style.css
└── dist/                        (generated, deploy this)
    ├── index.html
    ├── sitemap.xml
    ├── robots.txt
    └── ... (257 pages in various subdirs)
```

---

## Revenue collection — how you get paid

| Source | Payout method | Minimum |
|--------|---------------|---------|
| Google AdSense | Wire transfer to bank (EUR/USD) or SEPA | $100 |
| Direct affiliates (if we add them later) | PayPal / Stripe / Wise | Varies |
| Sponsored posts (if site grows) | Invoice + bank transfer | — |

**Pre-requisites on your side:** RO bank account that accepts USD/EUR wire (ING, BT, Revolut all fine), EU VAT check-in if annual revenue ever exceeds threshold (not a concern until ~€10,000).
