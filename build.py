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
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_OK = True
except Exception:
    PIL_OK = False

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SITE_NAME = "OpenInstead"
SITE_URL = os.environ.get("SITE_URL", "https://openinstead.dev")  # production domain, live since 2026-04-25
ROOT = Path(__file__).parent
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

# OG image generation (sprint 4 — social share surface)
OG_DIR_NAME = "og"
OG_BG = (14, 17, 22)          # #0e1116 — matches site dark theme
OG_TITLE_COLOR = (240, 246, 252)
OG_SUB_COLOR = (139, 148, 158)
OG_ACCENT = (63, 185, 80)     # #3fb950 — green accent used across site
OG_BADGE_BG = (22, 27, 34)    # subtly lighter dark for badge chip
OG_CARD_BORDER = (48, 54, 61)
OG_W, OG_H = 1200, 630

# Try common font paths that exist across Linux/macOS — all graceful fallback
FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
]
FONT_CANDIDATES_REG = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
]


def _font(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def _wrap_text(draw, text, font, max_width):
    """Greedy word-wrap against max pixel width."""
    words = text.split()
    lines = []
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def generate_og_image(title: str, kicker: str, out_path: Path):
    """Render a 1200x630 OG card: dark bg, green accent bar, kicker chip, big title,
    OpenInstead wordmark bottom-right. Safe no-op if PIL isn't available."""
    if not PIL_OK:
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (OG_W, OG_H), OG_BG)
    draw = ImageDraw.Draw(img)

    # Green accent bar on the left — signature brand mark
    draw.rectangle([0, 0, 14, OG_H], fill=OG_ACCENT)

    # Card border (subtle) — echoes site cards
    draw.rectangle([60, 60, OG_W - 60, OG_H - 60], outline=OG_CARD_BORDER, width=2)

    pad_x = 100
    y = 120

    # Kicker / category chip
    if kicker:
        kicker_text = kicker.upper()
        kf = _font(FONT_CANDIDATES_BOLD, 22)
        kb = draw.textbbox((0, 0), kicker_text, font=kf)
        kw = kb[2] - kb[0]
        kh = kb[3] - kb[1]
        chip_pad = 18
        chip_h = kh + chip_pad
        draw.rounded_rectangle(
            [pad_x, y, pad_x + kw + chip_pad * 2, y + chip_h],
            radius=int(chip_h / 2),
            fill=OG_BADGE_BG,
            outline=OG_ACCENT,
            width=2,
        )
        draw.text((pad_x + chip_pad, y + chip_pad / 2 - 2), kicker_text, font=kf, fill=OG_ACCENT)
        y += chip_h + 46

    # Title — greedy wrap, pick largest size that fits in 3 lines
    title_max_w = OG_W - pad_x * 2
    title_font = None
    lines = []
    for size in (84, 76, 68, 60, 52, 46):
        f = _font(FONT_CANDIDATES_BOLD, size)
        ls = _wrap_text(draw, title, f, title_max_w)
        if len(ls) <= 3:
            title_font = f
            lines = ls
            break
    if title_font is None:
        title_font = _font(FONT_CANDIDATES_BOLD, 46)
        lines = _wrap_text(draw, title, title_font, title_max_w)[:3]

    line_gap = 14
    bbox_h = draw.textbbox((0, 0), "Ay", font=title_font)
    line_h = bbox_h[3] - bbox_h[1] + line_gap
    for line in lines:
        draw.text((pad_x, y), line, font=title_font, fill=OG_TITLE_COLOR)
        y += line_h

    # Bottom wordmark: OpenInstead (right-aligned) + tagline (left)
    wm_font = _font(FONT_CANDIDATES_BOLD, 34)
    tag_font = _font(FONT_CANDIDATES_REG, 24)
    wm_y = OG_H - 110
    # Left tagline
    draw.text(
        (pad_x, wm_y + 6),
        "Open source alternatives to popular SaaS",
        font=tag_font,
        fill=OG_SUB_COLOR,
    )
    # Right wordmark
    wm_text_open = "Open"
    wm_text_inst = "Instead"
    bo = draw.textbbox((0, 0), wm_text_open, font=wm_font)
    bi = draw.textbbox((0, 0), wm_text_inst, font=wm_font)
    total_w = (bo[2] - bo[0]) + (bi[2] - bi[0])
    wm_x = OG_W - pad_x - total_w
    draw.text((wm_x, wm_y), wm_text_open, font=wm_font, fill=OG_TITLE_COLOR)
    draw.text((wm_x + (bo[2] - bo[0]), wm_y), wm_text_inst, font=wm_font, fill=OG_ACCENT)

    img.save(out_path, format="PNG", optimize=True)
    return True

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


def load_articles():
    """Read all markdown files in data/articles/ and parse frontmatter."""
    art_dir = DATA / "articles"
    if not art_dir.exists():
        return []
    articles = []
    for md in sorted(art_dir.glob("*.md")):
        raw = md.read_text(encoding="utf-8")
        fm = {}
        body = raw
        if raw.startswith("---"):
            _, fm_block, body = raw.split("---", 2)
            for line in fm_block.strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
        articles.append({
            "slug": md.stem,
            "title": fm.get("title", md.stem),
            "description": fm.get("description", ""),
            "date": fm.get("date", ""),
            "category": fm.get("category", ""),
            "body_md": body.strip(),
        })
    # Most recent first by ISO date
    articles.sort(key=lambda a: a.get("date", ""), reverse=True)
    return articles


def md_to_html(md: str) -> str:
    """Minimal Markdown → HTML converter. Handles headings, paragraphs,
    ordered/unordered lists, links, inline code, bold and italic, hr and blockquotes."""
    lines = md.split("\n")
    out = []
    in_list = None  # 'ul' or 'ol'
    in_para = False
    in_bq = False
    in_code = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    def close_para():
        nonlocal in_para
        if in_para:
            out.append("</p>")
            in_para = False

    def close_bq():
        nonlocal in_bq
        if in_bq:
            out.append("</blockquote>")
            in_bq = False

    def inline(s: str) -> str:
        # Code spans
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        # Bold
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        # Italic (underscore avoids clashing with **bold**)
        s = re.sub(r"(?<!\*)\*(?!\*)([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        # Links  [text](url)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for raw in lines:
        line = raw.rstrip()

        # fenced code (```)
        if line.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                close_para(); close_list(); close_bq()
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(line)
            continue

        stripped = line.strip()

        if not stripped:
            close_para(); close_list(); close_bq()
            continue

        # Headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            close_para(); close_list(); close_bq()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue

        # HR
        if re.match(r"^-{3,}$", stripped) or re.match(r"^\*{3,}$", stripped):
            close_para(); close_list(); close_bq()
            out.append("<hr>")
            continue

        # Blockquote
        if stripped.startswith("> "):
            close_para(); close_list()
            if not in_bq:
                out.append("<blockquote>")
                in_bq = True
            out.append(f"<p>{inline(stripped[2:])}</p>")
            continue
        else:
            close_bq()

        # Ordered list
        om = re.match(r"^\d+\.\s+(.*)$", stripped)
        if om:
            close_para()
            if in_list != "ol":
                close_list()
                out.append("<ol>")
                in_list = "ol"
            out.append(f"<li>{inline(om.group(1))}</li>")
            continue

        # Unordered list
        if stripped.startswith(("- ", "* ")):
            close_para()
            if in_list != "ul":
                close_list()
                out.append("<ul>")
                in_list = "ul"
            out.append(f"<li>{inline(stripped[2:])}</li>")
            continue

        # Paragraph
        close_list()
        if not in_para:
            out.append("<p>")
            in_para = True
        else:
            out.append(" ")
        out.append(inline(stripped))

    close_para(); close_list(); close_bq()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# JSON-LD schema helpers
# ---------------------------------------------------------------------------
def jsonld(obj) -> str:
    """Serialize a dict to a compact JSON-LD string."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def schema_organization() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE_NAME,
        "url": SITE_URL,
        "logo": f"{SITE_URL}/static/favicon.svg",
        "description": "Open source alternatives to popular SaaS — curated and editorial.",
        "sameAs": [],
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "customer support",
            "email": "contact@openinstead.dev",
        }],
    }


def schema_website() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": SITE_URL,
        "potentialAction": {
            "@type": "SearchAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": f"{SITE_URL}/?q={{search_term_string}}",
            },
            "query-input": "required name=search_term_string",
        },
    }


def schema_breadcrumb(items) -> dict:
    """items = [(name, path), ...]   path '' or '/' allowed for home."""
    elements = []
    for i, (name, path) in enumerate(items, start=1):
        elements.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": f"{SITE_URL}{path or '/'}",
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def to_iso_datetime(date_str: str) -> str:
    """Convert YYYY-MM-DD (or full ISO) to ISO 8601 with timezone, as required
    by schema.org Article spec. Existing full ISO strings pass through."""
    if not date_str:
        return ""
    s = date_str.strip()
    # Already has time component?
    if "T" in s:
        # Add UTC suffix if missing both Z and offset.
        if "+" not in s and "Z" not in s and not s.endswith("+00:00"):
            return s + "+00:00"
        return s
    # Plain date — assume 08:00 UTC publication time.
    return f"{s}T08:00:00+00:00"


def schema_article(art, og_image_url, body_text) -> dict:
    """Build an Article schema from an article dict + computed OG image + body text."""
    word_count = len(body_text.split())
    obj = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art["title"],
        "description": art.get("description", ""),
        "image": [og_image_url] if og_image_url else [],
        "url": f"{SITE_URL}/article/{art['slug']}/",
        "wordCount": word_count,
        "author": {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE_URL,
        },
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE_URL,
            "logo": {
                "@type": "ImageObject",
                "url": f"{SITE_URL}/static/favicon.svg",
            },
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{SITE_URL}/article/{art['slug']}/",
        },
    }
    if art.get("date"):
        iso_dt = to_iso_datetime(art["date"])
        obj["datePublished"] = iso_dt
        obj["dateModified"] = iso_dt
    return obj


def schema_software_application(oss, category_name) -> dict:
    obj = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": oss["name"],
        "description": oss.get("tagline", ""),
        "applicationCategory": category_name,
        "url": oss.get("website", ""),
        "operatingSystem": ", ".join(oss.get("desktop_apps", []) or ["Web"]),
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD",
        },
    }
    if oss.get("license"):
        obj["license"] = oss["license"]
    return obj


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
    shutil.copytree(STATIC, DIST / "static", dirs_exist_ok=True)

    # OG image output dir
    og_dir = DIST / OG_DIR_NAME
    og_dir.mkdir(parents=True, exist_ok=True)
    og_generated = 0

    def og_url(slug: str) -> str:
        return f"{SITE_URL}/{OG_DIR_NAME}/{slug}.png"

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

    # Pre-load articles so we can build "related articles" rails on hub pages.
    # Articles are loaded again later for actual rendering — this is a cheap pre-pass.
    pre_articles = load_articles()

    # Crude topical map from article slug → keywords used to match SaaS/OSS/category pages.
    # Editorial rather than ML — simple keyword set per article.
    article_topics = {
        "self-hosting-in-2026-honest-survey": {
            "selfhost", "self-hosting", "general",
        },
        "why-your-team-cant-ditch-slack-yet": {"team-communication", "slack", "selfhost"},
        "real-monthly-cost-of-notion-workspace-at-scale": {"note-taking", "notion", "selfhost"},
        "evaluating-open-source-alternatives-framework": {"general", "selfhost", "evaluation"},
        "30-day-saas-to-self-hosted-migration-playbook": {"general", "selfhost", "migration"},
        "avoiding-mega-incumbents-oss-alternatives": {"general", "selfhost"},
        "when-self-hosting-goes-wrong-seven-failure-modes": {"general", "selfhost", "ops"},
        "will-this-open-source-project-still-exist-in-three-years": {
            "general", "evaluation", "sustainability",
        },
    }

    def related_articles_for(category_slug: str, limit: int = 3) -> list:
        """Return up to N article dicts whose topics match the given category, with
        'general' articles as fallback."""
        scored = []
        for a in pre_articles:
            topics = article_topics.get(a["slug"], {"general"})
            score = 0
            if category_slug in topics:
                score += 3
            if "general" in topics:
                score += 1
            if score:
                scored.append((score, a))
        scored.sort(key=lambda x: -x[0])
        return [a for _, a in scored[:limit]]

    # -------------------------------------------------------------------
    # Home page
    # -------------------------------------------------------------------
    print("[build] home page")
    featured_saas = sorted(saas_products, key=lambda s: -s["alternative_count"])[:18]
    total_comparisons = sum(len(v) for v in mappings_by_saas.values())
    if generate_og_image(
        "Open source alternatives to popular SaaS",
        "",
        og_dir / "home.png",
    ):
        og_generated += 1
    home_jsonld = [
        jsonld(schema_organization()),
        jsonld(schema_website()),
    ]
    html = render(
        "home.html",
        page_title=f"Open source alternatives to popular SaaS · {SITE_NAME}",
        meta_description=(
            f"{len(saas_products)} popular cloud tools mapped to {len(oss_alternatives)} "
            f"open source alternatives. Honest pros, cons and self-host notes."
        ),
        canonical_path="/",
        og_image=og_url("home"),
        structured_data=home_jsonld,
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
    cat_index_breadcrumb = jsonld(schema_breadcrumb([
        ("Home", "/"),
        ("Categories", "/categories/"),
    ]))
    html = render(
        "categories_index.html",
        page_title=f"All categories · {SITE_NAME}",
        meta_description="Browse every category of SaaS tools and the open source alternatives we track.",
        canonical_path="/categories/",
        structured_data=[cat_index_breadcrumb],
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
        og_slug = f"category-{cat['slug']}"
        if generate_og_image(
            f"{cat['name']} — open source alternatives",
            "Category",
            og_dir / f"{og_slug}.png",
        ):
            og_generated += 1
        cat_breadcrumb = jsonld(schema_breadcrumb([
            ("Home", "/"),
            ("Categories", "/categories/"),
            (cat["name"], f"/category/{cat['slug']}/"),
        ]))
        # 3 sibling categories (same alphabetic order, wrap-around) for "related" rail
        cat_idx = next((i for i, c in enumerate(categories) if c["slug"] == cat["slug"]), 0)
        siblings = [categories[(cat_idx + offset) % len(categories)]
                    for offset in (1, 2, 3) if categories[(cat_idx + offset) % len(categories)]["slug"] != cat["slug"]]
        html = render(
            "category.html",
            page_title=f"{cat['name']} — open source alternatives · {SITE_NAME}",
            meta_description=cat["description"],
            canonical_path=f"/category/{cat['slug']}/",
            og_image=og_url(og_slug),
            structured_data=[cat_breadcrumb],
            category=cat,
            saas_in_category=saas_in_cat,
            oss_in_category=oss_in_cat,
            siblings=siblings,
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
        item_list_sd = {
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
        breadcrumb_sd = schema_breadcrumb([
            ("Home", "/"),
            ("Categories", "/categories/"),
            (saas["category_name"], f"/category/{saas['category']}/"),
            (f"Alternatives to {saas['name']}", f"/alternatives-to/{saas['slug']}/"),
        ])

        og_slug = f"saas-{saas['slug']}"
        if generate_og_image(
            f"{len(alternatives)} open source alternatives to {saas['name']}",
            saas["category_name"],
            og_dir / f"{og_slug}.png",
        ):
            og_generated += 1
        # Sibling SaaS in the same category for an internal-link rail.
        related_saas = [s for s in saas_products
                        if s["category"] == saas["category"] and s["slug"] != saas["slug"]][:3]
        related_arts = related_articles_for(saas["category"])
        html = render(
            "saas_page.html",
            page_title=f"{len(alternatives)} open source alternatives to {saas['name']} ({datetime.now().year}) · {SITE_NAME}",
            meta_description=(
                f"The best open source alternatives to {saas['name']}: "
                + ", ".join(a["oss"]["name"] for a in alternatives[:3])
                + ". Honest pros, cons, licenses and self-host difficulty."
            ),
            canonical_path=f"/alternatives-to/{saas['slug']}/",
            og_image=og_url(og_slug),
            saas=saas,
            category=categories_by_slug[saas["category"]],
            alternatives=alternatives,
            related_saas=related_saas,
            related_articles=related_arts,
            og_type="article",
            structured_data=[jsonld(item_list_sd), jsonld(breadcrumb_sd)],
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
        oss_cat = categories_by_slug[oss["category"]]
        oss_breadcrumb = schema_breadcrumb([
            ("Home", "/"),
            ("Categories", "/categories/"),
            (oss_cat["name"], f"/category/{oss['category']}/"),
            (oss["name"], f"/open-source/{oss['slug']}/"),
        ])
        oss_sw = schema_software_application(oss, oss_cat["name"])
        related_oss_list = [o for o in oss_alternatives
                            if o["category"] == oss["category"] and o["slug"] != oss["slug"]][:3]
        related_arts = related_articles_for(oss["category"])
        html = render(
            "oss_page.html",
            page_title=f"{oss['name']} — {oss['tagline']} · {SITE_NAME}",
            meta_description=oss["tagline"],
            canonical_path=f"/open-source/{oss['slug']}/",
            structured_data=[jsonld(oss_breadcrumb), jsonld(oss_sw)],
            oss=oss,
            category=oss_cat,
            replaces=oss_replaces[oss["slug"]],
            related_oss=related_oss_list,
            related_articles=related_arts,
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
            comp_breadcrumb = schema_breadcrumb([
                ("Home", "/"),
                ("Categories", "/categories/"),
                (saas["category_name"], f"/category/{saas['category']}/"),
                (f"{saas['name']} vs {oss['name']}", f"/vs/{saas['slug']}-vs-{oss['slug']}/"),
            ])
            # Up to 3 other comparisons for the same SaaS (other OSS pairings).
            sibling_alts = [x for x in alts if x["slug"] != oss["slug"]][:3]
            related_comparisons = []
            for s_alt in sibling_alts:
                s_oss = oss_by_slug.get(s_alt["slug"])
                if not s_oss:
                    continue
                related_comparisons.append({
                    "saas_slug": saas["slug"],
                    "saas_name": saas["name"],
                    "oss_slug": s_oss["slug"],
                    "oss_name": s_oss["name"],
                    "subline": s_alt["best_for"],
                })
            related_arts = related_articles_for(saas["category"])
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
                structured_data=[jsonld(comp_breadcrumb)],
                related_comparisons=related_comparisons,
                related_articles=related_arts,
            )
            write_page(DIST / "vs" / f"{saas['slug']}-vs-{oss['slug']}" / "index.html", html)
            add_url(f"/vs/{saas['slug']}-vs-{oss['slug']}/", 0.6, "monthly")
            comparison_count += 1
    print(f"         {comparison_count} comparison pages")

    # -------------------------------------------------------------------
    # Articles (long-form essays)
    # -------------------------------------------------------------------
    articles = load_articles()
    print(f"[build] {len(articles)} articles")
    for art in articles:
        body_html = md_to_html(art["body_md"])
        og_slug = f"article-{art['slug']}"
        og_image_url = og_url(og_slug)
        if generate_og_image(
            art["title"],
            art.get("category") or "Article",
            og_dir / f"{og_slug}.png",
        ):
            og_generated += 1
        article_breadcrumb = schema_breadcrumb([
            ("Home", "/"),
            ("Articles", "/articles/"),
            (art["title"], f"/article/{art['slug']}/"),
        ])
        article_sd = schema_article(art, og_image_url, art["body_md"])
        html = render(
            "article.html",
            page_title=f"{art['title']} · {SITE_NAME}",
            meta_description=art["description"],
            canonical_path=f"/article/{art['slug']}/",
            og_image=og_image_url,
            article=art,
            body=body_html,
            og_type="article",
            structured_data=[jsonld(article_sd), jsonld(article_breadcrumb)],
        )
        write_page(DIST / "article" / art["slug"] / "index.html", html)
        add_url(f"/article/{art['slug']}/", 0.7, "monthly")

    # Articles index
    art_idx_breadcrumb = schema_breadcrumb([
        ("Home", "/"),
        ("Articles", "/articles/"),
    ])
    html = render(
        "articles_index.html",
        page_title=f"Articles · {SITE_NAME}",
        meta_description="Long-form essays on self-hosting, open source evaluation and SaaS migration.",
        canonical_path="/articles/",
        structured_data=[jsonld(art_idx_breadcrumb)],
        articles=articles,
    )
    write_page(DIST / "articles" / "index.html", html)
    add_url("/articles/", 0.7, "monthly")

    # -------------------------------------------------------------------
    # Search index (for client-side search)
    # -------------------------------------------------------------------
    print("[build] search-index.json")
    search_index = []

    for s in saas_products:
        search_index.append({
            "title": f"Alternatives to {s['name']}",
            "url": f"/alternatives-to/{s['slug']}/",
            "type": "saas",
            "typeLabel": f"SaaS · {s['category_name']}",
            "tags": f"{s['name']} {s['tagline']} {s['category_name']}",
        })

    for o in oss_alternatives:
        search_index.append({
            "title": o["name"],
            "url": f"/open-source/{o['slug']}/",
            "type": "oss",
            "typeLabel": f"Open source · {categories_by_slug[o['category']]['name']}",
            "tags": f"{o['name']} {o['tagline']} {o['license']}",
        })

    for cat in categories:
        search_index.append({
            "title": cat["name"],
            "url": f"/category/{cat['slug']}/",
            "type": "category",
            "typeLabel": "Category",
            "tags": f"{cat['name']} {cat['description']}",
        })

    for saas_slug, alts in mappings_by_saas.items():
        saas = saas_by_slug[saas_slug]
        for a in alts:
            oss = oss_by_slug.get(a["slug"])
            if not oss:
                continue
            search_index.append({
                "title": f"{saas['name']} vs {oss['name']}",
                "url": f"/vs/{saas['slug']}-vs-{oss['slug']}/",
                "type": "comparison",
                "typeLabel": "Comparison",
                "tags": f"{saas['name']} {oss['name']}",
            })

    for art in articles:
        search_index.append({
            "title": art["title"],
            "url": f"/article/{art['slug']}/",
            "type": "article",
            "typeLabel": f"Article · {art.get('category', '')}",
            "tags": f"{art['title']} {art['description']}",
        })

    with open(DIST / "search-index.json", "w", encoding="utf-8") as f:
        json.dump(search_index, f, separators=(",", ":"))
    print(f"         {len(search_index)} entries")

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

    contact_body = """
    <p>Have a correction? Notice a dead project or a missed alternative? Want to suggest a new SaaS to track?</p>
    <p>Email us at <a href="mailto:contact@openinstead.dev">contact@openinstead.dev</a> and we'll update the directory.
    We read every message and usually reply within 72 hours.</p>
    <p>We do not accept paid placements. Every entry in this directory is editorial; we say so publicly because it
    affects how much you should trust our recommendations.</p>
    <p>For press, partnerships or larger conversations, same address.</p>
    """
    html = render(
        "static_page.html",
        page_title=f"Contact · {SITE_NAME}",
        meta_description=f"Contact {SITE_NAME} — corrections, suggestions and press enquiries.",
        canonical_path="/contact/",
        page_heading="Contact",
        lead="How to reach us about the directory.",
        body=contact_body,
    )
    write_page(DIST / "contact" / "index.html", html)
    add_url("/contact/", 0.3, "yearly")

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
    # RSS feed for articles
    # -------------------------------------------------------------------
    print("[build] rss feed for articles")
    rss_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>\n',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n',
        '<channel>\n',
        f'  <title>{SITE_NAME} Articles</title>\n',
        f'  <link>{SITE_URL}/articles/</link>\n',
        f'  <atom:link href="{SITE_URL}/articles/rss.xml" rel="self" type="application/rss+xml" />\n',
        '  <description>Long-form essays on self-hosting, open source evaluation and SaaS migration.</description>\n',
        '  <language>en-us</language>\n',
    ]
    for art in articles:
        rss_parts.append('  <item>\n')
        rss_parts.append(f'    <title>{art["title"]}</title>\n')
        rss_parts.append(f'    <link>{SITE_URL}/article/{art["slug"]}/</link>\n')
        rss_parts.append(f'    <guid>{SITE_URL}/article/{art["slug"]}/</guid>\n')
        rss_parts.append(f'    <description><![CDATA[{art["description"]}]]></description>\n')
        if art.get("date"):
            try:
                d = datetime.fromisoformat(art["date"])
                rss_parts.append(f'    <pubDate>{d.strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>\n')
            except Exception:
                pass
        rss_parts.append('  </item>\n')
    rss_parts.append('</channel>\n</rss>\n')
    write_page(DIST / "articles" / "rss.xml", "".join(rss_parts))

    # -------------------------------------------------------------------
    # robots.txt + sitemap.xml + _headers (Cloudflare Pages cache hints)
    # -------------------------------------------------------------------
    print("[build] robots.txt + sitemap.xml + _headers")
    robots = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    write_page(DIST / "robots.txt", robots)

    # _headers — Cloudflare Pages reads this from the build output root.
    # 1-year cache for assets that never change content (versioned by name);
    # short cache for HTML so updates ship quickly.
    headers = """\
/static/*
  Cache-Control: public, max-age=31536000, immutable
  X-Content-Type-Options: nosniff

/og/*
  Cache-Control: public, max-age=31536000, immutable
  X-Content-Type-Options: nosniff

/*.png
  Cache-Control: public, max-age=31536000, immutable

/*.svg
  Cache-Control: public, max-age=2592000

/sitemap.xml
  Cache-Control: public, max-age=3600

/articles/rss.xml
  Cache-Control: public, max-age=3600

/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
"""
    write_page(DIST / "_headers", headers)

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
    print(f"        OG images generated: {og_generated} (in {og_dir})")


if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print(f"[build] ERROR: {e}", file=sys.stderr)
        raise
