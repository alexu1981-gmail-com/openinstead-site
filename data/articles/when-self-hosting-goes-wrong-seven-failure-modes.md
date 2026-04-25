---
title: "When self-hosting goes wrong: seven failure modes and how to avoid them"
description: "An honest retrospective on the ways self-hosted setups break — not in theory, but in practice — and the small habits that prevent most of them."
date: 2026-04-25
category: Opinion
---

Most self-hosting guides are written from the high of a fresh install. You `docker compose up`, the dashboard loads, and the post writes itself. This one is written from the other side of that experience — six months or two years later, when the fresh install is running your family's photos, your side project's auth, or your small team's wiki, and something goes sideways.

We've been doing this long enough, and talking to enough people who do, that the failure modes rhyme. Almost none of them are exotic. They're not "the filesystem melted" or "a zero-day took me out." They're small, human, and preventable if you know they exist.

Here are the seven that come up most often. If you're in year zero of self-hosting, read this before the failures find you.

## 1. "It worked, so I stopped thinking about it"

This is the deepest one, and the hardest to see coming.

You set up Nextcloud on a Sunday. It works. You copy some files over. It keeps working. A month goes by, then three, then a year. You have not logged into the server in eleven months. The box is on a VPS you forgot the root password for. The SSH key is on a laptop you replaced.

Then something breaks — a disk fills up, a package fails to upgrade, TLS certificate expires silently because certbot's cron was wiped by an OS update. And now you're locked out of a machine that holds the only copy of some of your data.

**How to avoid it:** Two habits. First, schedule *you* into the loop on a cadence: once a month, log in, look at disk usage, tail the logs, confirm backups ran. Second, keep a `README.md` in the repo that runs the server (you do have one, right?) with the three things you will forget: where SSH keys live, where backups are restored from, and who to call if the server is a shared responsibility. Treat future-you like a new hire who knows nothing.

## 2. Backups that aren't tested are not backups

Everyone reading this knows you need backups. Fewer people know that a backup you haven't restored from is not a backup, it's a hope.

The pattern: you install restic or duplicati or borg. You point it at your data directory. It runs nightly. The dashboards are green. Two years in, the main disk fails, you pull the backup down, and `restic restore` tells you the snapshot is corrupt, or the encryption key is on the machine that just died, or the backup volume was actually mounted read-only for the last fourteen months and nothing was being written.

**How to avoid it:** The restore drill is non-negotiable. Once a quarter, spin up a throwaway VPS, pull your most recent backup, and restore it end to end. Not "verify the archive" — actually restore and see the files. Also: backups that live on the same host as the thing you're backing up are not backups; make sure at least one copy is on a different provider, different credentials, different physical place.

## 3. Upgrades you put off because they're scary

Self-hosted software evolves. Releases ship. The further behind you fall, the scarier the next upgrade feels, which makes you fall further behind.

We've seen this with GitLab (jumping over three major versions is an expedition), Nextcloud (apps break between minor versions and you discover it only after the migration), and Jellyfin (upgrades themselves are fine but the ffmpeg transcoder config changes). The longer you wait, the more the delta accumulates, and the higher the stakes when you finally attempt it.

**How to avoid it:** Upgrade on a schedule, not when you feel like it. Monthly or bi-monthly is enough for most things. Read the release notes — not all of them, just the ones between your version and the next. Snapshot the volume before the upgrade if your provider supports it. If a bad upgrade is going to cost you four hours, spend twenty minutes preparing so the rollback path is real.

## 4. Running on a single cheap VPS and nothing else

The classic starter setup: a $5 VPS, Docker Compose, a dozen services stacked on top. This is fine for a year. It becomes a single point of failure on the day the provider has an incident, or the instance ID gets terminated by a billing error, or an overzealous abuse-report bot flags your traffic.

There are three things worth separating early: **storage** (your data doesn't belong on the same VPS as the services), **DNS** (don't tie yourself to a provider whose dashboard is down at the moment you need to change records), and **email** (if you're sending it at all, treat deliverability as a separate problem from hosting).

**How to avoid it:** You don't need Kubernetes to be resilient. You need to answer the question "what happens if this VPS disappears tonight?" without the answer being "I lose everything." A second region's backup, DNS at a separate registrar, data-only volumes that can be moved — those three alone eliminate most catastrophic failure modes.

## 5. Exposing things to the public internet before you understand what you exposed

The day you port-forward a service, your box is on the internet. Bots find it within hours. Mature projects defend against the obvious — brute-force logins, common CVEs — but "mature" is doing a lot of work in that sentence.

The failure mode isn't "I got hacked." It's "I got hacked, and then I found out six months later that my server was part of a botnet, because I wasn't watching logs, and my VPS provider emailed me a nastygram before I noticed myself."

**How to avoid it:** Default to private. If a service doesn't need to be public, put it behind a VPN (WireGuard is excellent here) or a reverse-proxy with SSO (Authelia, Authentik). Enable fail2ban. Turn on 2FA on anything that offers it. Read the logs *at least* once a week during the first few months — you learn what normal looks like, and anomalies become obvious.

## 6. Forgetting that your instance is a legal entity too

This one surprises people. The moment you host a service that other humans use — even friends, even just family members — you've taken on some operational responsibilities you didn't have when you were a paying customer of a SaaS.

Your photos of other people? GDPR-adjacent. Your friend's calendar on your CalDAV? You're a data controller. Your family's Bitwarden vault? If you lose it, you've lost their passwords.

This doesn't mean you can't self-host. It means you should think about it the way a SaaS vendor thinks: retention, export, delete-on-request, incident response. Not as a legal exercise, but because the people trusting you with their data deserve the same minimum guarantees a paid SaaS would offer.

**How to avoid it:** Write a one-page "if this service dies, here's what happens" for anyone who isn't you using your infrastructure. Include how they export their data, how they get it recovered, and what your realistic response time is when they email you at 11pm. Being honest about "I'm not on-call for this" is a feature, not an apology.

## 7. Picking software on hype, not on maintainership

This one maps directly onto the work that informs this site. Not all open source projects are equally likely to still exist in three years. Some are maintained by one person; some by a small handful; some by a foundation; some by a company that could pivot or fold.

The failure mode: you pick the flashy new Notion clone, migrate your notes, and two years later the maintainer burns out, the fork languishes, and you're migrating out on a deadline. Meanwhile the boring project with three commits a week and seven active maintainers would have been there for a decade.

**How to avoid it:** Before you adopt something, look at the last twelve months of commits, the number of distinct contributors, the response time on issues, whether releases ship regularly, and who pays for the maintainers' time if anyone. We wrote a whole checklist for this in [Open source alternatives: the comparison criteria that actually matter](/article/evaluating-open-source-alternatives-framework/) — the short version is: prefer the project that's boring but reliably maintained over the one that's exciting but fragile.

## The meta-failure: believing self-hosting means never paying

This is the stubborn one. Self-hosting can be cheaper than SaaS, and often is, but "cheaper" isn't "free," and the cost is rarely just money.

The cost is: your time to install and maintain, your attention to upgrades and incidents, the opportunity cost of what you could be doing instead. For a weekend hobbyist, that's a feature — you want to tinker. For someone running a team tool, it's a budget line item that usually gets under-counted.

We have a piece called [Self-hosting in 2026: the honest survey](/article/self-hosting-in-2026-honest-survey/) that goes deeper into this. The short version: budget at least an hour a week for anything you care about keeping running, and be honest when that budget is too expensive.

## The throughline

None of these failure modes are exotic. They're what happens when motivated, smart people set up something real and then drift away from it, assuming the system will keep running because it's been running. Almost always it does keep running — until one day it doesn't, and the recovery bill has been quietly accumulating interest.

The mitigation isn't heroism or automation. It's a small ritual — once a month, maybe, twenty minutes — where you log in, look at the machine, run the restore drill when it's time, and decide whether the thing you're hosting still deserves the attention it takes.

Self-hosting done well is sustainable. Self-hosting done by default, or by momentum, isn't. Knowing the difference is the whole game.
