---
title: "Self-hosting in 2026: the honest survey"
description: "An honest look at what self-hosting actually costs in 2026 — time, money, attention — and who should and shouldn't do it."
date: 2026-04-24
category: Opinion
---

For the past few years, "self-host everything" has been having a moment. Meta's TOS scares, the LastPass breach, Notion pricing climbs, the 1Password ownership change in 2023. Every incident nudges another cohort into a weekend of Docker Compose files and subdomain juggling. If you're reading this, you're probably somewhere on that gradient yourself.

I'm going to try to be useful in a different way from the usual self-hosting post. No promises about freedom. We'll count hours instead.

## The two mental models

People self-host for two different reasons, and they lead to different setups. Confusing them is the most common mistake I see.

**Model A: "I want the bill to stop."** You looked at the Notion plus Slack plus Dropbox plus 1Password plus ChatGPT Plus line on your card and did the math: $240/year here, $420 there, $1,200 there. Twelve services later you're at $3,000+ a year on subscriptions for things that, physically, could all run on a $15/month Hetzner box.

**Model B: "I want my data out of there."** Healthcare, law, journalism, jurisdictions where data residency matters. The question isn't cost. It's custody.

These produce different decisions. The Model A person should self-host their *consumer-facing* personal data (photos, files, notes, RSS) and *keep paying* for the team productivity suite — running Mattermost for a five-person team takes more hours per month than Slack Pro costs them. The Model B person should do the opposite: self-host the crown jewels (docs, email, chat) and not sweat the photo library.

Most people try to do both at once. Pick one model first. Pick the stack second.

## The real costs nobody talks about

**Hosting hardware.** A 4 GB / 2 vCPU VPS runs you $5–10/month at Hetzner, $12–25 at DigitalOcean or Linode. That's enough for Nextcloud and one or two light services. Add Immich with ML tagging, a Plausible instance, and a Matrix server, and you're at $20–40 for a bigger box. Plus 2 TB of object storage for backups (another $5–10). Call it **$25–50/month all in** for a serious personal setup. Real money. Probably less than you're paying SaaS now, but not free.

**Domains.** $10–15/year. Most people end up with two or three.

**Backups.** This is where 90% of self-hosters silently fail. The cost isn't the tool — Restic, Borg, Kopia are all free. The cost is *testing*. You need to actually restore from a backup at least twice a year or you don't have backups. You have a feelings file. Budget four hours a year here. One of those hours will involve cursing.

**Time.** This is the big one. Initial install of a mature project (Nextcloud, Jellyfin) on a fresh VPS: 1–3 hours if things go well, 5–10 if you hit a wall. Monthly maintenance — updates, alerts, fixing what broke — runs 1–3 hours per service. Backup rehearsal: 1–2 hours a year. Catastrophic recovery (VPS dies, disk corrupts, an upgrade destroys config): 4–8 hours, once every 18–36 months.

For a personal stack of four or five services, a realistic time budget is **10–20 hours a year on top of initial setup**. That's one Saturday every 3–6 months. For some people this is cheaper than the subscriptions. For others, it's five Saturdays they can't spare.

## Who self-hosting is genuinely great for

Four groups, in rough order of how often I see them succeed:

- **You already have a homelab.** The marginal cost of one more container is near zero. You have the skills.
- **You run a small agency or studio and bill for your time.** Self-hosting internal tooling saves real money at 5–15 seats, where per-user SaaS pricing stings worst.
- **You're in a data-sensitive profession.** Legal, medical, journalism. Self-hosting isn't a preference, it's compliance, and the budget reflects that.
- **You enjoy running services.** This is the honest one. If the weekend of tinkering *is the point*, go.

## Who self-hosting is a trap for

- **Solo professionals whose time is scarce.** Twenty hours a year is half a workweek. Very few SaaS bills justify half a workweek of sysadmin, even at consultant rates.
- **Teams that need uptime SLAs.** Self-hosted means you're oncall, and most people quietly burn out on that within a year.
- **People who want to "replace Gmail."** Self-hosting email is its own category of suffering in 2026. Deliverability to Gmail and Outlook from a fresh VPS IP is awful. Use Proton or Fastmail. Spend the energy elsewhere.

## The sane hybrid most people land on

After watching friends do this for years, here's the pattern that tends to work:

**Self-host:** files (Nextcloud or Seafile), photos (Immich or PhotoPrism), media (Jellyfin), RSS (Miniflux), bookmarks (Wallabag or LinkAce), password manager (Vaultwarden, because the Bitwarden clients are polished and Vaultwarden is tiny).

**Pay for:** email (Proton or Fastmail), team chat (Slack or Discord for a small team unless compliance demands otherwise), video meetings (a paid option, because Jitsi is fine but not rock-solid at scale), source code hosting (GitHub for small public projects, plus Forgejo or Gitea only if your team is big enough that the seat cost matters).

The logic: self-host the things that are *one-person, stateful, private, and infrequently trafficked.* Pay for things that are *team-facing, real-time, and where an outage means someone is blocked.*

I think this hybrid is right for maybe 70% of the people who ask me about self-hosting. The other 30% know who they are.

## Before you go hunting for alternatives

A gentle nudge. Look at our [open source alternatives by category](/categories/), but before you pick any, ask three questions of the SaaS you're leaving:

1. Is the thing bothering me about this service actually going to be solved by switching? Or am I trading one set of problems for another?
2. How much will I actually save in a year, *net of hosting, net of time*?
3. Is there a middle-ground plan (self-host the personal slice, keep the team slice) that captures 80% of the benefit with 20% of the work?

If the answers are honest yes / meaningful savings / no middle ground, go. Otherwise, keep reading before you pull the plug.

---

Self-hosting is more accessible than it's ever been. Docker Compose files you can copy-paste. Installation scripts that work on the first try about half the time. Documentation that's actually good. But "easier to install" is not "easier to own." Ownership is a subscription paid in your own time. Pick your services the way you pick any subscription: based on what it buys you, not what it costs someone else.
