---
title: "The real monthly cost of a Notion workspace at scale"
description: "Add-ons, seats, AI credits, storage. What a mid-sized team actually pays for Notion once you count everything — and what switching saves."
date: 2026-04-24
category: Analysis
---

Notion's pricing page reads clean: **$10 per user per month** for the Plus plan, billed annually. Easy mental math. Thirty people? Three hundred a month. Three hundred sixty a year per seat.

Except that's not what most teams actually pay. By the time a 30-person team has been on Notion for 18 months, the real line item looks more like $550–700/month. This piece walks through where the extra $250+ comes from, and what switching would and wouldn't save.

## Where the real cost hides

### The base tier is almost never enough

The $10/month Plus tier gets you unlimited blocks, 30-day page history, and basic workflow features. What it doesn't get you: SAML SSO, workspace-level permissions, audit logs, a 90-day version history, private teamspaces, security controls, or the admin API.

For companies under 20 employees who haven't had a compliance conversation, Plus is fine. For anyone above that, or with a legal or IT function paying attention, the gravitational pull toward **Business** ($20/user/month) or **Enterprise** ($25+/user/month, quoted) is strong. Often one person at the company reads through the SAML and audit requirements from IT and forwards the upgrade request.

Notional sticker price: $10 × 30 = $300/month. Actual tier most 30-person companies settle on: Business, so $20 × 30 = **$600/month**.

### AI add-on

Notion AI launched as a separate add-on and has stayed one. It's **$10/user/month** on top of the base tier, and it's a per-seat add-on for the whole workspace — you can't pay for AI for just 5 of the 30 seats. All-or-nothing.

The feature is genuinely good for note-summarization and block-level writing help. Once a few people on the team start using it, the rest of the team starts asking "wait, why don't we all have this?" And the admin quietly upgrades the whole workspace.

That's another $300/month on our 30-person example. Cumulative: **$900/month**.

### Storage

Notion is generous with file uploads (5 MB on Free, unlimited on paid), but when your team starts using it as a file store — meeting notes with PDF attachments, design assets, recordings — performance can drag and the experience gets clunky. Many teams end up paying for adjacent services: Dropbox or Google Drive for real file hosting. That cost already existed, but Notion quietly didn't displace it.

This one doesn't show up on the Notion line item, but it shows up somewhere — usually another **$15–30/month** for the team's shared Dropbox or Google Drive seats that got added "just to handle the big files."

### The orphan seats

A 30-person team this year is a 32- or 34-seat bill. Contractors get added, interns get seats, somebody creates a "readonly" account for a vendor. Most teams don't prune these regularly. Over 18 months, a team of 30 quietly becomes a license count of 34–36.

At $20/user/month, that's another **$80–120/month** over what you "should" be paying.

### The running total

For a well-established 30-person team on Notion:
- Base tier (Business): $600/month
- Notion AI: $300/month
- Orphan seats: $100/month
- *Hidden:* supplementary file hosting: $25/month

**Total Notion line item: ~$1,000/month. $12,000/year.** The difference between this and the sticker price ($300/month, $3,600/year) is 3.3×. Most teams have no idea.

## Where a self-hosted alternative saves money

Let's run the same math for [AppFlowy](/open-source/appflowy/) and [AFFiNE](/open-source/affine/) — the two most credible open source Notion replacements in 2026.

### AppFlowy self-hosted

- VPS: $20/month for a 4 GB / 2 vCPU instance that comfortably handles 30 users.
- Object storage for attachments: $5–10/month.
- Domain + SSL: $15/year.
- AI: free if you self-host with a local model (slow), or bring your own OpenAI/Anthropic API key at roughly $0.50–2/user/month depending on usage.

**All in: $45–85/month.** Annual: **$540–1,020**. Savings vs Notion: **~$11,000/year**.

### AFFiNE self-hosted

Similar math. AFFiNE's self-host story has improved rapidly, though real-time collaboration is still maturing.

**All in: $40–80/month.** Similar savings.

## Where the math breaks down

Before you start planning the migration, the uncomfortable half of the ledger.

**Migration time.** Moving an 18-month-old Notion workspace to AppFlowy is a month of project work. Structure has to be reconciled (Notion databases behave differently from AppFlowy grids). Internal links break. Permissions have to be rewritten. For a 30-person team, call it **80–120 person-hours** of work, plus the productivity dip during handover.

At a fully-loaded cost of $80/hour, that's $6,400–9,600 of labor. Your first year's savings are roughly break-even. Year two is where you start actually winning.

**Support overhead.** Notion has a support team. AppFlowy has GitHub issues and a Discord. When something breaks for a non-technical user, a technical person on your team owns the fix. Budget **2–5 hours/month** for this at scale. At consultant rates, that's another $200–500/month — which you should price in against the savings.

**Feature gaps.** AppFlowy has shipped most of Notion's primitives, but some are missing or different. If your team uses Notion's AI auto-fill, button automations, or the API heavily, map those to AppFlowy's equivalents (some exist, some are on the roadmap, some will never exist in the form you want). Missing features have costs: workarounds are time, or external tools are money.

Realistically: **year-one savings: $1,000–4,000. Year-two and beyond: $8,000–10,000/year.**

## When switching makes sense

- You're over 25 seats and growing (per-seat savings compound).
- You have at least one technical person who can own the self-hosted stack.
- Your Notion workspace is less than two years old (migration cost scales brutally with content age).
- Notion AI hasn't become load-bearing for your team's workflows.

## When to stay

- Small teams under 15 seats (savings don't justify the 80+ hours of migration).
- Teams where 5+ people rely on Notion API integrations.
- Teams on Notion Enterprise for SAML/compliance — those features exist in AppFlowy's Enterprise tier too, but "one vendor for compliance" is a hard thing to walk away from.
- Workspaces with 100+ interconnected databases and automations.

## The middle path

Self-host a new Notion replacement **for new projects** starting now. Let the Notion workspace wind down naturally. Over 12–18 months, the mass center of your knowledge base shifts to the new tool. You never do a hard migration. You just do a soft one, every time a new project starts. Your Notion bill shrinks as you remove seats.

This approach loses ~20% of the savings relative to a clean break, but it also costs ~80% less time and disruption. For most teams, it's the right trade.

---

If you want to explore the open source alternatives to Notion we cover in this directory: [see the full list →](/alternatives-to/notion/). The numbers in this article are based on public pricing and our analysis; your mileage will vary with team size and usage intensity.
