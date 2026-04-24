#!/usr/bin/env python3
"""
OpenInstead — static site generator.

Reads YAML data + Jinja2 templates and produces a static site under dist/.
Designed for Cloudflare Pages (or any static host).

Usage:
    python build.py
"""

import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SITE_NAME = "OpenInstead"
SITE_URL = os.environ.get("SITE_URL", "https://openinstead.dev")  # change after you pick a domain
ROOT = Path(__file__).parent
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_yaml(name):
    with open(DATA / name, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def write_page(out_path: Path, html: str):
    ensure_dir(out_path.parent)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def render(template_name: str, **ctx) -> str:
    tmpl = env.get_template(template_name)
    defaults = {
        "site_name": SITE_NAME,
        "site_url": SITE_URL,
        "static_prefix": "/static",
        "root_prefix": "",
        "updated": datetime.now(timezone.utc).strftime("%B %Y"),
        "og_type": "website",
        "structured_data": None,
    }
    defaults.update(ctx)
    return tmpl.render(**defaults)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build():
    print(f"[build] cleaning {DIST}")
    if DIST.exists():
        # On mounted drives we may not be able to rmdir the top folder itself.
        # Clean its contents instead.
        for child in DIST.iterdir():
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                try:
                    child.unlink()
                except Exception:
                    pass
    else:
        DIST.mkdir()

    # Copy static assets.
    print("[build] copying static assets")
    shutil.copytree(STATIC, DIST / "static")

    # Load data.
    print("[build] loading YAML data")
    categories = load_yaml("categories.yaml")
    saas_products = load_yaml("saas_products.yaml")
    oss_alternatives = load_yaml("oss_alternatives.yaml")
    mappings = load_yaml("mappings.yaml")

    categories_by_slug = {c["slug"]: c for c in categories}
    saas_by_slug = {s["slug"]: s for s in saas_products}
    oss_by_slug = {o["slug"]: o for o in oss_alternatives}
    mappings_by_saas = {m["saas"]: m["alternatives"] for m in mappings}

    # Precompute category counts.
    for cat in categories:
        cat["saas_count"] = sum(1 for s in saas_products if s["category"] == cat["slug"])
        cat["oss_count"] = sum(1 for o in oss_alternatives if o["category"] == cat["slug"])

    # Precompute alternative counts per SaaS.
    for s in saas_products:
        alts = mappings_by_saas.get(s["slug"], [])
        s["alternative_count"] = len(alts)
        s["category_name"] = categories_by_slug[s["category"]]["name"]

    sitemap_urls = []

    def add_url(path: str, priority: float = 0.5, changefreq: str = "monthly"):
        sitemap_urls.append((path, priority, changefreq))

    # -------------------------------------------------------------------
    # Home page
    # -------------------------------------------------------------------
    print("[build] home page")
    featured_saas = sorted(saas_products, key=lambda s: -s["alternative_count"])[:18]
    total_comparisons = sum(len(v) for v in mappings_by_saas.values())
    html = render(
        "home.html",
        page_title=f"Open source alternatives to popular SaaS · {SITE_NAME}",
        meta_description=(
            f"{len(saas_products)} popular cloud tools mapped to {len(oss_alternatives)} "
            f"open source alternatives. Honest pros, cons and self-host notes."
        ),
        canonical_path="/",
        categories=categories,
        featured_saas=featured_saas,
        total_saas=len(saas_products),
        total_oss=len(oss_alternatives),
        total_comparisons=total_comparisons,
    )
    write_page(DIST / "index.html", html)
    add_url("/", 1.0, "weekly")

    # -------------------------------------------------------------------
    # Categories index
    # -------------------------------------------------------------------
    print("[build] categories index")
    html = render(
        "categories_index.html",
        page_title=f"All categories · {SITE_NAME}",
        meta_description="Browse every category of SaaS tools and the open source alternatives we track.",
        canonical_path="/categories/",
        categories=categories,
    )
    write_page(DIST / "categories" / "index.html", html)
    add_url("/categories/", 0.8, "monthly")

    # -------------------------------------------------------------------
    # Category pages
    # -------------------------------------------------------------------
    print(f"[build] {len(categories)} category pages")
    for cat in categories:
        saas_in_cat = [s for s in saas_products if s["category"] == cat["slug"]]
        oss_in_cat = [o for o in oss_alternatives if o["category"] == cat["slug"]]
        html = render(
            "category.html",
            page_title=f"{cat['name']} — open source alternatives · {SITE_NAME}",
            meta_description=cat["description"],
            canonical_path=f"/category/{cat['slug']}/",
            category=cat,
            saas_in_category=saas_in_cat,
            oss_in_category=oss_in_cat,
        )
        write_page(DIST / "category" / cat["slug"] / "index.html", html)
        add_url(f"/category/{cat['slug']}/", 0.7, "monthly")

    # -------------------------------------------------------------------
    # SaaS "Alternatives to X" pages
    # -------------------------------------------------------------------
    print(f"[build] {len(saas_products)} SaaS alternative pages")
    for saas in saas_products:
        alt_list_raw = mappings_by_saas.get(saas["slug"], [])
        alternatives = []
        for alt in alt_list_raw:
            oss = oss_by_slug.get(alt["slug"])
            if not oss:
                print(f"  WARN: unknown oss slug {alt['slug']} for saas {saas['slug']}")
                continue
            alternatives.append({"oss": oss, "best_for": alt["best_for"]})

        # Structured data for ItemList.
        sd = {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": f"Open source alternatives to {saas['name']}",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": a["oss"]["name"],
                    "url": f"{SITE_URL}/open-source/{a['oss']['slug']}/",
                }
                for i, a in enumerate(alternatives)
            ],
        }

        html = render(
            "saas_page.html",
            page_title=f"{len(alternatives)} open source alternatives to {saas['name']} ({datetime.now().year}) · {SITE_NAME}",
            meta_description=(
                f"The best open source alternatives to {saas['name']}: "
                + ", ".join(a["oss"]["name"] for a in alternatives[:3])
                + ". Honest pros, cons, licenses and self-host difficulty."
            ),
            canonical_path=f"/alternatives-to/{saas['slug']}/",
            saas=saas,
            category=categories_by_slug[saas["category"]],
            alternatives=alternatives,
            og_type="article",
            structured_data=json.dumps(sd),
        )
        write_page(DIST / "alternatives-to" / saas["slug"] / "index.html", html)
        add_url(f"/alternatives-to/{saas['slug']}/", 0.9, "monthly")

    # -------------------------------------------------------------------
    # OSS profile pages
    # -------------------------------------------------------------------
    print(f"[build] {len(oss_alternatives)} OSS profile pages")
    # Index: which SaaS products does each OSS replace?
    oss_replaces = {o["slug"]: [] for o in oss_alternatives}
    for saas_slug, alts in mappings_by_saas.items():
        for a in alts:
            if a["slug"] in oss_replaces:
                oss_replaces[a["slug"]].append(saas_by_slug[saas_slug])

    for oss in oss_alternatives:
        html = render(
            "oss_page.html",
            page_title=f"{oss['name']} — {oss['tagline']} · {SITE_NAME}",
            meta_description=oss["tagline"],
            canonical_path=f"/open-source/{oss['slug']}/",
            oss=oss,
            category=categories_by_slug[oss["category"]],
            replaces=oss_replaces[oss["slug"]],
        )
        write_page(DIST / "open-source" / oss["slug"] / "index.html", html)
        add_url(f"/open-source/{oss['slug']}/", 0.8, "monthly")

    # -------------------------------------------------------------------
    # Comparison pages: SaaS vs OSS
    # -------------------------------------------------------------------
    print("[build] comparison pages")
    comparison_count = 0
    for saas_slug, alts in mappings_by_saas.items():
        saas = saas_by_slug[saas_slug]
        for alt in alts:
            oss = oss_by_slug.get(alt["slug"])
            if not oss:
                continue
            html = render(
                "comparison.html",
                page_title=f"{saas['name']} vs {oss['name']} — honest comparison · {SITE_NAME}",
                meta_description=(
                    f"Side-by-side: {saas['name']} (paid SaaS) vs {oss['name']} "
                    f"(open source). Pricing, license, self-host difficulty."
                ),
                canonical_path=f"/vs/{saas['slug']}-vs-{oss['slug']}/",
                saas=saas,
                oss=oss,
                best_for=alt["best_for"],
                og_type="article",
            )
            write_page(DIST / "vs" / f"{saas['slug']}-vs-{oss['slug']}" / "index.html", html)
            add_url(f"/vs/{saas['slug']}-vs-{oss['slug']}/", 0.6, "monthly")
            comparison_count += 1
    print(f"         {comparison_count} comparison pages")

    # -------------------------------------------------------------------
    # Static content pages (About, Privacy)
    # -------------------------------------------------------------------
    print("[build] about / privacy")
    about_body = """
    <p><strong>OpenInstead</strong> is a curated directory of open source alternatives to the SaaS tools most
    teams and individuals use every day. Every page is editorial, not affiliate-driven: we list strengths,
    weaknesses, licenses and self-host difficulty without picking winners for money.</p>
    <p>We maintain this directory because every SaaS subscription is three things: a monthly bill,
    a data-sharing decision, and a lock-in risk. Open source gives you the option to step out.</p>
    <p>Spot something wrong? Projects evolve, licenses change, features ship. Reach out and we'll update the entry.</p>
    """
    html = render(
        "static_page.html",
        page_title=f"About · {SITE_NAME}",
        meta_description=f"About {SITE_NAME} — why we track open source alternatives.",
        canonical_path="/about/",
        page_heading="About",
        lead="Curated open source alternatives to popular SaaS, without the affiliate spam.",
        body=about_body,
    )
    write_page(DIST / "about" / "index.html", html)
    add_url("/about/", 0.3, "yearly")

    privacy_body = """
    <p>This site uses privacy-friendly analytics to understand which pages are helpful. No personal data is
    collected or sold. We may show display advertising from Google AdSense; advertisers receive only the
    information AdSense itself collects, per their privacy policy at
    <a href="https://policies.google.com/privacy" target="_blank" rel="noopener nofollow">policies.google.com/privacy</a>.</p>
    <p>If you prefer to opt out of personalised ads, see
    <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener nofollow">aboutads.info/choices</a>.</p>
    <p>Outbound links to project websites and GitHub repos use <code>rel="nofollow"</code> so we pass no editorial
    endorsement by default.</p>
    """
    html = render(
        "static_page.html",
        page_title=f"Privacy · {SITE_NAME}",
        meta_description=f"Privacy policy for {SITE_NAME}.",
        canonical_path="/privacy/",
        page_heading="Privacy",
        lead="How we handle data on this site.",
        body=privacy_body,
    )
    write_page(DIST / "privacy" / "index.html", html)
    add_url("/privacy/", 0.2, "yearly")

    # -------------------------------------------------------------------
    # robots.txt + sitemap.xml
    # -------------------------------------------------------------------
    print("[build] robots.txt + sitemap.xml")
    robots = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    write_page(DIST / "robots.txt", robots)

    sitemap_parts = ['<?xml version="1.0" encoding="UTF-8"?>\n',
                     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n']
    for path, priority, changefreq in sitemap_urls:
        sitemap_parts.append("  <url>\n")
        sitemap_parts.append(f"    <loc>{SITE_URL}{path}</loc>\n")
        sitemap_parts.append(f"    <changefreq>{changefreq}</changefreq>\n")
        sitemap_parts.append(f"    <priority>{priority:.1f}</priority>\n")
        sitemap_parts.append("  </url>\n")
    sitemap_parts.append("</urlset>\n")
    write_page(DIST / "sitemap.xml", "".join(sitemap_parts))

    # 404
    html404 = render(
        "static_page.html",
        page_title=f"Page not found · {SITE_NAME}",
        meta_description="Page not found.",
        canonical_path="/404.html",
        page_heading="Page not found",
        lead="This page does not exist or was moved.",
        body="<p>Try the <a href='/'>home page</a> or browse <a href='/categories/'>all categories</a>.</p>",
    )
    write_page(DIST / "404.html", html404)

    # -------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------
    total_pages = len(sitemap_urls) + 1  # +404
    print(f"[build] DONE — {total_pages} pages in {DIST}")
    print(f"        home 1 · categories {len(categories) + 1} · saas {len(saas_products)} · "
          f"oss {len(oss_alternatives)} · vs {comparison_count} · static 2")


if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print(f"[build] ERROR: {e}", file=sys.stderr)
        raise
