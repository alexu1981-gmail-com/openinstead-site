---
title: "Self-hosting in 2026: the honest survey"
description: "An honest look at what self-hosting actually costs in 2026 — time, money, attention — and who should and shouldn't do it."
date: 2026-04-24
category: Opinion
---

For the past few years, "self-host everything" has been having a moment. Meta's TOS scares, LastPass breaches, Notion pricing climbs — every incident nudges another cohort into a weekend of Docker Compose files and subdomain juggling. If you're reading this, you're probably somewhere on that gradient yourself.

This piece tries to be useful in a different way from the usual self-hosting content. We won't promise freedom. We'll count hours. The goal is to help you decide, clear-eyed, whether self-hosting any given service is the right move for you in 2026 — or whether you should keep paying.

## The two mental models of self-hosting

People self-host for two different reasons, and they lead to different setups.

**Model A: "I want the bill to stop."** You looked at the Notion/Slack/Dropbox line on your credit card and did the math: $240 a year, $420 a year, $1,200 a year. Twelve services later, you're burning through $3,000+ annually on subscriptions for things that, physically, could all run on a $15/month VPS.

**Model B: "I want my data out of there."** You work in healthcare, law, journalism, or you live in a jurisdiction where data residency matters. The question isn't cost — it's custody.

These two models produce different decisions. The Model A person should probably self-host for their **consumer-facing personal data** (photos, files, notes, RSS) and **keep paying** for their team's productivity suite, because the hours per month to run a self-hosted Slack for a five-person team exceed what Slack Pro costs them. The Model B person should do the opposite: self-host the crown jewels (docs, email, chat) and not sweat the photo library.

Most people try to do both simultaneously, and end up overwhelmed. Pick a model before you pick a stack.

## The real costs nobody talks about

**Hosting hardware.** A 4 GB / 2 vCPU VPS runs you $5–10/month at Hetzner, $12–25/month at DigitalOcean or Linode. That's enough to run Nextcloud + one or two light services. If you want to run Immich with ML tagging, a Plausible instance, and a Matrix server, you're now at $20–40/month for a bigger box. Plus 2 TB of object storage for backups (another $5–10). Call it **$25–50/month all in** for a serious personal setup.

**Domains.** If you self-host, you want your own domain so nothing feels like an ad URL. $10–15/year per domain. Most people end up with two or three.

**Backups.** This is where 90% of self-hosters silently fail. The cost isn't the tool (Restic, Borg, Duplicati are all free) — it's the testing. You need to actually restore from a backup at least twice a year or you don't have backups, you have a feelings file. Budget four hours a year here. One of those hours will involve crying.

**Time.** This is the big one. Initial install of a mature project (Nextcloud, Jellyfin) on a fresh VPS: 1–3 hours if things go well, 5–10 if you hit a wall. Monthly maintenance (updates, monitoring alerts, fixing what broke): 1–3 hours per service. Backup rehearsal: 1–2 hours a year. A catastrophic recovery (VPS dies, disk corrupts, upgrade destroys config): 4–8 hours, once every 18–36 months.

For a personal stack of four or five services, a realistic time budget is **10–20 hours a year** on top of initial setup. That's one Saturday every 3–6 months. For many people this is cheaper than the subscriptions. For others, it's five Saturdays they can't spare.

## Who self-hosting is genuinely great for

- **You already have a home server or homelab.** The marginal cost of adding one more container is near zero. You have the skills.
- **You own a small agency or studio and bill for your time.** Self-hosting internal tooling saves real money at the scale of 5–15 seats, where per-user SaaS pricing stings worst.
- **You're in a data-sensitive profession.** Legal, medical, journalism. Self-hosting isn't a preference, it's a compliance requirement — and the budget reflects that.
- **You enjoy running services.** This is the honest one. If the weekend of tinkering is the point, go.

## Who self-hosting is a trap for

- **Solo professionals whose time is scarce.** Twenty hours a year is half a workweek. Very few SaaS bills justify half a workweek of sysadmin, even at consultant rates.
- **Teams that need uptime SLAs.** Self-hosted means you're the oncall, and most people quietly burn out on that within a year.
- **People who want to "replace Gmail."** Self-hosting email is its own category of suffering in 2026. Deliverability to Gmail and Outlook from a fresh VPS IP is awful. Use Proton or Fastmail instead; put your energy elsewhere.

## The sane hybrid most people land on

After watching friends do this for years, here's the pattern that tends to work:

**Self-host:** files and sync (Nextcloud or Seafile), photos (Immich or PhotoPrism), media (Jellyfin), RSS (Miniflux), bookmarks (Wallabag or LinkAce), password manager (Vaultwarden — because Bitwarden clients are polished and Vaultwarden is tiny).

**Pay for:** email (Proton or Fastmail), team chat (Slack or Discord for the small team, unless compliance demands otherwise), video meetings (a pay-per-minute option, because Jitsi is fine but not rock-solid at scale), source code hosting (GitHub for small public projects, plus Forgejo or Gitea only if your team is big enough).

**The logic:** self-host the things that are one-person, stateful, private, and infrequently trafficked. Pay for things that are team-facing, real-time, and where an outage means someone is blocked.

## Before you go hunting for alternatives

A gentle nudge. Look at our directory of [open source alternatives by category](/categories/), but before you pick any of them, ask three questions of the SaaS you're leaving:

1. Is the thing that's bothering me about this service actually going to be solved by switching? Or am I trading one set of problems for another?
2. How much will I actually save — in a year, net of hosting, net of time?
3. Is there a middle-ground plan (self-host the personal slice, keep the team slice) that captures 80% of the benefit with 20% of the work?

If the answers are honest yes / meaningful savings / no middle ground, go. Otherwise, keep reading before you pull the plug.

---

Self-hosting is more accessible than it's ever been — Docker Compose files you can copy-paste, installation scripts that work, documentation that's actually good. But "easier to install" is not the same as "easier to own." Ownership is a subscription paid in your own time. Pick your services the way you pick any subscription: based on what it buys you, not what it costs someone else.
