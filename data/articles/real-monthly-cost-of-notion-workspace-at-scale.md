---
title: "The real monthly cost of a Notion workspace at scale"
description: "Add-ons, seats, AI credits, storage. What a mid-sized team actually pays for Notion once you count everything — and what switching saves."
date: 2026-04-24
category: Analysis
---

Notion's pricing page reads clean: **$10 per user per month** for the Plus plan, billed annually. Easy mental math. Thirty people? Three hundred a month. Three sixty a year per seat.

That's not what most teams actually pay.

By the time a 30-person team has been on Notion for 18 months, the real line item is more like $550–700/month. Sometimes higher. This piece walks through where the extra $250+ comes from, and what switching would and wouldn't save.

I'm using a 30-person team as the running example because that's roughly the size where the gap between sticker and actual gets most painful.

## Where the real cost hides

### The base tier is almost never enough

The $10/month Plus tier gets you unlimited blocks, 30-day page history, and basic workflow features. What it doesn't get you: SAML SSO, workspace-level permissions, audit logs, 90-day version history, private teamspaces, security controls, the admin API.

For companies under 20 people who haven't had a compliance conversation, Plus is fine. For anyone above that, or with a legal or IT function paying attention, the gravitational pull toward **Business** ($20/user/month) or **Enterprise** ($25+/user/month, quoted) is strong. Usually one person at the company reads through the SAML and audit requirements from IT and forwards the upgrade request. Two weeks later, the workspace is on Business. I've seen this happen at three companies I've worked with — same script, slightly different month.

Sticker price: $10 × 30 = $300/month. Actual tier most 30-person companies settle on: Business, so $20 × 30 = **$600/month**.

### AI add-on

Notion AI launched as a separate add-on and stayed one. It's **$10/user/month** on top of the base tier, and it's all-or-nothing for the workspace. You can't pay for AI for just five of the thirty seats.

The feature is genuinely useful for note summarization and block-level writing help. Once a few people on the team start using it, the rest start asking "wait, why don't we all have this?" Admin quietly upgrades the whole workspace.

Another $300/month on the 30-person example. Cumulative: **$900/month**.

### Storage you don't see

Notion is generous with file uploads (5 MB on Free, unlimited on paid). But when teams start using it as a file store — meeting notes with PDF attachments, design assets, recordings — performance drags. Search starts feeling slow. Many teams end up paying for adjacent services: Dropbox or Google Drive for actual file hosting. The cost was already there, but Notion quietly didn't displace it.

This doesn't show up on the Notion line. It shows up somewhere though. Usually another **$15–30/month** for the team's shared Dropbox seats that got added "just to handle the big files."

### Orphan seats

A 30-person team this year is a 32- or 34-seat bill. Contractors get added. Interns get seats. Someone creates a "readonly" account for a vendor and forgets it exists. Over 18 months, a team of 30 quietly becomes a license count of 34–36.

At $20/user/month, that's another **$80–120/month** over what you "should" be paying. (Notion doesn't make orphan seat detection particularly easy — there's an admin export, but you have to go looking for it. I won't speculate on whether that's deliberate.)

### Running total

For an established 30-person team on Notion:
- Base tier (Business): $600/month
- Notion AI: $300/month
- Orphan seats: $100/month
- Hidden: supplementary file hosting: $25/month

**Total: ~$1,000/month. $12,000/year.** The gap between this and the sticker price ($300/month, $3,600/year) is 3.3×.

Most teams have no idea. The CFO sees the line item and asks "wait, when did this triple?" Answer: it didn't, exactly. It accreted.

## What a self-hosted alternative actually saves

Let's run the same math for [AppFlowy](/open-source/appflowy/) and [AFFiNE](/open-source/affine/), the two most credible open source Notion replacements in 2026.

### AppFlowy self-hosted

- VPS: $20/month for a 4 GB / 2 vCPU instance that comfortably handles 30 users.
- Object storage for attachments: $5–10/month.
- Domain plus SSL: $15/year.
- AI: free if you self-host with a local model (slow), or bring your own OpenAI/Anthropic API key at roughly $0.50–2/user/month depending on usage.

**All in: $45–85/month.** Annual: **$540–1,020**. Savings vs Notion: **~$11,000/year**.

### AFFiNE self-hosted

Similar math. AFFiNE's self-host story improved rapidly through 2024–2025, though real-time collab is still maturing in places.

**All in: $40–80/month.** Similar savings.

## Where the math breaks down

Before you start planning the migration, the uncomfortable half of the ledger.

**Migration time.** Moving an 18-month-old Notion workspace is a month of project work. Structure has to be reconciled (Notion databases behave differently from AppFlowy grids). Internal links break. Permissions get rewritten. For a 30-person team, call it **80–120 person-hours** of work, plus the productivity dip during handover.

At a fully-loaded cost of $80/hour, that's $6,400–9,600 of labor. Your first year's savings are roughly break-even. Year two is where you start actually winning.

**Support overhead.** Notion has a support team. AppFlowy has GitHub issues and a Discord. When something breaks for a non-technical user, a technical person on your team owns the fix. Budget **2–5 hours/month** at scale. At consultant rates, that's another $200–500/month, which you should price in against the savings.

**Feature gaps.** AppFlowy has shipped most of Notion's primitives. Some are missing or different. If your team uses Notion's AI auto-fill, button automations, or the API heavily, map those to AppFlowy's equivalents. Some exist, some are on the roadmap, some will probably never exist in the form you want. Missing features have costs: workarounds are time, or external tools are money.

Realistically: **year-one savings: $1,000–4,000. Year-two onward: $8,000–10,000/year.**

## When switching makes sense

- You're over 25 seats and growing. Per-seat savings compound.
- You have at least one technical person who can own the self-hosted stack.
- Your Notion workspace is less than two years old. Migration cost scales brutally with content age.
- Notion AI hasn't become load-bearing for your team's workflows.

## When to stay

- Small teams under 15 seats. Savings don't justify 80+ hours of migration.
- Teams where five or more people rely on Notion API integrations.
- Teams on Notion Enterprise for SAML/compliance — those features exist in AppFlowy's Enterprise tier too, but "one vendor for compliance" is a hard thing to walk away from for risk-averse legal departments.
- Workspaces with 100+ interconnected databases and automations.

## The middle path

Self-host a new Notion replacement **for new projects** starting now. Let the existing Notion workspace wind down naturally. Over 12–18 months, the center of mass of your knowledge base shifts to the new tool. You never do a hard migration. You do a soft one, every time a new project starts. Notion bill shrinks as you prune seats.

This loses about 20% of the maximum savings versus a clean break, but it costs about 80% less time and disruption. For most teams that's the right trade.

---

If you want to explore the open source alternatives to Notion we cover here: [see the full list →](/alternatives-to/notion/). The numbers in this article are based on public pricing as of April 2026 and our own analysis. Your mileage will vary with team size and usage intensity.
