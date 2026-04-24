---
title: "From SaaS to self-hosted: a 30-day migration playbook"
description: "A week-by-week plan to move one service off SaaS and onto your own server without breaking your team's workflow."
date: 2026-04-24
category: Playbook
---

Moving a single service from SaaS to self-hosted is the kind of project most teams try to do over a weekend, then abandon three weeks in. The problem isn't the technology. It's that the weekend migration has no rollback plan, no clear success criteria, and no handle on the human side of the change.

This playbook is the opposite. It takes four weeks, not two days. It moves one service at a time. It's intentionally boring. If you run one service through this playbook successfully, you can run three. If you try to run three simultaneously, you'll probably run zero.

Pick one service. Nextcloud instead of Dropbox. Mattermost instead of Slack. Bitwarden/Vaultwarden instead of 1Password. Gitea/Forgejo instead of GitHub. One service. Run this playbook on it. Return here when it's been stable for 60 days.

## Week 0: the honest checklist before you start

Before any server gets touched, answer these questions *in writing*:

1. **Who is the point person?** Not "the team." One name. If that name isn't available to firefight for the next 30 days, wait until they are.
2. **What's the success metric?** Usually "all critical usage migrated, old service readable-only for 90 days, no data loss incidents, no workflow regressions lasting more than 24 hours."
3. **What's the rollback plan?** Specifically: if on day 14 things are worse than on day 0, can you switch back to the SaaS? For most services the answer is "yes, if we kept the subscription paid." For a few (email especially) it's "partially." Don't start if the answer is "no."
4. **Who approves the decision to continue vs. roll back?** One name.
5. **What's the budget?** Hosting costs are ~$10–30/month per service. Rollback costs are the SaaS seats you didn't cancel yet. Point: keep them running throughout the 30 days.

If you can't answer all five cleanly, you're not ready. Go do a project that isn't this.

## Week 1: infrastructure and install

### Day 1-2 — pick your host

- **VPS:** Hetzner ($5–15/month for a serious box), DigitalOcean, Linode, Vultr. EU jurisdiction if that matters to you.
- **Home server / NUC:** fine for services that don't need external access. Terrible for anything your team will reach on the go.
- **Managed Kubernetes:** don't, unless you already have this in your org. The ops cost is too high for one service.

One VPS, $15/month, fresh Debian 12 or Ubuntu 22.04. Set up SSH keys, a non-root user, UFW (only 22, 80, 443 open), unattended-upgrades, Fail2Ban. This is the foundation. Don't skip it.

### Day 3 — domain and DNS

Buy a subdomain if you don't have one. Point it to your VPS via an A record. While you're there, buy the main domain if you don't own it — it's $15/year and means you won't be dependent on your registrar's goodwill.

### Day 4 — reverse proxy and SSL

Caddy or Traefik. Caddy is the friendlier default for small setups: one service, one config line, automatic Let's Encrypt. The exact commands are in the docs for both. Don't try to learn Nginx just for this.

### Day 5-7 — install the service

Use the project's official docker-compose or install guide. Don't use third-party community AppImages unless you know what you're doing. Get it running on its subdomain. Log in. Click around. Make sure the basics work.

**Criteria for ending week 1:** you, the point person, can log into the self-hosted service at its new URL over HTTPS. Nothing else matters yet.

## Week 2: import and parallel run

### Day 8-9 — import data

Every serious open source project has an importer or migration script for the major SaaS they replace. Nextcloud imports Dropbox/Google Drive. Mattermost imports Slack. Vaultwarden accepts Bitwarden's standard export. Run the importer. Verify with spot checks — pick 10 random items from your SaaS and confirm they exist on the new system.

**Do not delete anything from the SaaS yet.** You are in parallel run. Both systems have the data. This is intentional.

### Day 10-12 — invite 2-3 early users

Not the whole team. Three people who are friendly to change and willing to tell you when things break. Give them both systems. Ask them to do their normal work.

Collect feedback. Some will be "this is fine." Some will be "I can't do X" — where X is usually some feature or integration you haven't enabled yet. Fix the fixable ones, document the gaps.

### Day 13-14 — rollout plan

Based on what you learned: can you onboard the rest of the team? If yes, proceed. If no, you've learned something valuable. Either fix the blockers or roll back cleanly. Communicate either decision to the team.

**Criteria for ending week 2:** 3 users have been on the new system for 3 days, you have a written list of fixes or deferred features, and you've made the go/no-go decision for the full team.

## Week 3: the rest of the team

### Day 15-17 — announce and onboard

Send the team a clear message. Example template:

> Starting this week, we're moving [service] from [SaaS] to our own hosted [alternative]. The old system stays active (read-only) for 90 days so you can still look things up. New work happens on the new system. Here's your login URL. Here's a 5-minute Loom walkthrough of the basics. Here's the Slack channel (or equivalent) for questions.

People will ask the same questions 10 times. That's fine. Answer them.

### Day 18-21 — bulk user provisioning

Bring the whole team onto the new system. SSO integration if you have one; manual accounts if you don't. Send the team a checklist:

- Log in
- Set your password (or link SSO)
- Verify your critical data is there
- Bookmark the new URL

Watch the support requests. Most will be "I forgot how to do X" where X is something they did daily. These aren't bugs; they're retraining. Allocate some of the point person's time to answer.

**Criteria for ending week 3:** every active team member has logged into the new system at least once and verified their data.

## Week 4: stabilization and SaaS wind-down

### Day 22-25 — watch for edge cases

The edge cases emerge now. Users who didn't log in during week 3 show up and find problems. Workflows that weren't exercised during your test phase turn out to have gaps. Fix or defer each one with a clear communication to the team.

### Day 26-28 — cancel / downgrade the SaaS

Do not cancel entirely. **Downgrade** to the minimum tier that lets your team still read the old data. For most SaaS this is a free or $5-10/month read-only mode. Keep it around for 90 days.

If the SaaS requires a full paid seat to read data, pay for one admin seat for 90 days. You'll use it to answer "hey, what was in that one channel from March" questions that come up randomly. That's just part of the migration cost.

### Day 29-30 — decision freeze

Formal review with your stakeholder (from week 0 question 4). Are we committed to the migration? Document the commitment in writing. Update your internal wiki, runbooks, onboarding docs.

**Criteria for ending week 4:** SaaS usage has dropped to near-zero for new work, the old data is still retrievable, the team has stopped asking "how do I..." questions more than once a day.

## Post-migration: 30 to 90 days

You're not done yet. Keep:

- **Daily check** on the self-hosted service's logs (automate alerts).
- **Weekly backup verification** (actually restore one item, don't just watch the green check).
- **Monthly review** with the point person: what's broken, what's degraded, what's better.

Somewhere between day 60 and day 90, you'll know. The migration either stuck or it didn't. If it didn't, roll back cleanly to the SaaS (you kept it paid — thank you past self). If it did, proceed to decommission the SaaS permanently at day 90+. Export any historical data you want, archive it, cancel the subscription.

## What goes wrong most often

**The point person burns out.** They're doing their day job + running the migration support. Reduce their regular workload during the 30 days. This isn't a nice-to-have.

**Nobody planned for the integrations gap.** You didn't inventory what the SaaS was integrated with before you started. Ten services broke, one at a time, over two weeks. This is why week 2 has a parallel run phase.

**The backup plan wasn't tested.** Day 42, something goes wrong, you go to restore, the backup was never working. Test before day 42, not on it.

**The rollback wasn't actually possible.** You canceled the SaaS too early. Don't.

## Which services to run this playbook on first

In rough order of "easiest to migrate successfully":

1. **Password manager** (Bitwarden / Vaultwarden): very few integrations, clean export/import, instant reward.
2. **File storage** (Nextcloud / Seafile): clean migration path, but slow — your users will need to re-sync a lot.
3. **RSS reader** (FreshRSS / Miniflux): nearly stakes-free, per-user. Good practice run.
4. **Kanban boards** (Planka / Focalboard): usually done by one team at a time, low blast radius.
5. **Team chat** (Mattermost / Rocket.Chat): this is the big one. Only do this after you've run the playbook successfully twice on easier services.

Don't start with email. Email deserves its own series of articles. Self-hosting email in 2026 is a deliverability project, not a migration project.

---

If you've read this far, you probably have a specific migration in mind. Pick it. Write down your answers to the Week 0 questions. Book 30 days on your calendar. Don't start before you've finished the pre-work.

And if you want to see what open source alternatives are worth running this playbook for, browse [our full category list](/categories/). There's a reasonable chance we already have a profile for the one you're eyeing.
