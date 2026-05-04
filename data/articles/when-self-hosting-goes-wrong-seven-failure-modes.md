---
title: "When self-hosting goes wrong: seven failure modes and how to avoid them"
description: "An honest retrospective on the ways self-hosted setups break — not in theory, but in practice — and the small habits that prevent most of them."
date: 2026-04-25
category: Opinion
---

Most self-hosting guides are written from the high of a fresh install. You `docker compose up`, the dashboard loads, and the post writes itself. This one is from the other side — six months later, two years later, when the install is running your family's photos and your side project's auth and a friend's small team wiki, and something starts to drift.

I started writing this down because the failure modes rhyme. Not the ones the guides warn about. The boring ones.

Seven of them, roughly in order of how often I see them happen.

## 1. "It worked, so I stopped thinking about it"

This is the deep one. The one I've watched friends fall into and the one I've fallen into myself.

You set up Nextcloud on a Sunday. It works. You move some files. It keeps working. A month, three months, a year. You haven't touched the box. The SSH key is on a laptop you replaced. The root password is in a 1Password vault you've stopped paying for. Certbot's cron got wiped by an unattended upgrade and the cert expired three weeks ago — you'd know that if you checked the logs, but you don't, because everything still loads in your browser via Cloudflare's cached origin.

Then a disk fills up. Or systemd-resolved decides to be weird. Or your VPS provider sends a "your card was declined" email to an account you've also stopped checking.

The fix isn't automation. It's *attention*.

Once a month, log in. Look at `df -h`. Tail the journalctl. Confirm the last backup ran. That's it. Twenty minutes. Treat future-you like a stranger you owe a `README.md` to — where the keys are, what the backup paths are, what the recovery story looks like. Future-you will thank you. Or, more accurately, future-you will not curse past-you, which is the same thing.

## 2. Backups that nobody has tested

Everyone reading this knows you need backups. Fewer people know that an untested backup is hope, not data.

Pattern I keep seeing: someone installs restic or borgmatic or duplicacy. Points it at `/data`. Cron fires nightly. Two years pass. Then the disk dies, or the LXC container gets corrupted, or somebody runs `rm -rf` against the wrong path. They reach for the backups and discover one of three things:

- The encryption key was on the dead machine.
- The repository was mounted read-only fourteen months ago when something else broke and nothing's been written since.
- The snapshots exist but `restic check` reports a corrupt pack file. Probably a USB drive that started failing two years in.

I've seen all three. The first one twice.

The mitigation is the *restore drill*, not the backup. Once a quarter, spin up a throwaway VPS. Pull your most recent snapshot. Actually restore the files and look at them. Don't trust `restic check`; trust the experience of the data being readable on a machine that isn't the original. While you're at it, check that at least one backup copy lives on a different provider with separate credentials. If your VPS provider terminates your account by mistake (it happens), you don't want your backups going down with it.

## 3. Upgrades you keep putting off

Self-hosted software ships releases. Falling behind is exponential — the longer you wait, the harder the catch-up gets, and not in a linear way.

GitLab is the canonical bad example. Skipping three majors is no longer an upgrade; it's a migration project. I've watched a friend lose a weekend going from 14.x to 17.x because the path required walking through every minor version checking the runbook. Nextcloud has a similar dynamic — apps break in semi-predictable ways between point releases, and you discover the breakage about an hour after you've already started.

Discourse, Mattermost, Authentik — same pattern, less severe.

Pick a cadence. Bi-monthly is fine for most things. Read only the release notes between your version and the next, not all of them. Snapshot the volume before the upgrade if your provider supports snapshots. If a bad upgrade is going to cost you four hours of recovery, spend twenty minutes preparing so the rollback path is real and not aspirational.

## 4. Single $5 VPS as a single point of failure

The starter setup. A Hetzner CX11 or DigitalOcean droplet, Docker Compose, a dozen services stacked. This is fine for a year. It becomes one bad day from a complete restart.

Three things worth separating early, in order of how easy they are:

1. **Storage.** Your data shouldn't live on the same volume as the OS. Even just an attached block-storage volume costs $1-2/month and gives you a portable place for `/var/lib/docker/volumes` (or wherever).
2. **DNS.** Don't host DNS at the same provider as the box. If their dashboard is down (this happens a few times a year somewhere), you can't change records.
3. **Email.** If you're sending any, treat deliverability as a separate problem. Don't run your own SMTP outbound from the same VPS as your apps. Postmark, Mailgun, or just your ISP relay — pick one.

Notice this list isn't "use Kubernetes." It's three small separations. They're enough to mean "the VPS disappears tonight" doesn't equal "I lose everything."

## 5. Exposing things publicly before understanding what you exposed

The first time you port-forward a service, your box is on the internet. The bots find it within hours. Mature projects defend against the obvious — Vaultwarden has rate limits, Nextcloud has built-in 2FA, Forgejo will lock accounts on repeated failed logins. "Mature" is doing a lot of work in that sentence, though.

The actual failure mode isn't "I got hacked." It's "I got hacked, didn't notice for nine months, my VPS provider sent me an abuse notice because I was part of a botnet, and now I'm cleaning up while also explaining myself to a support agent."

Default to private. Put admin interfaces behind WireGuard. Use Authelia or Authentik in front of dashboards. Enable fail2ban. Read your auth logs at least once a week for the first few months — you learn what normal looks like, and anomalies become obvious. (The first thing I check is `lastb` on a VPS. The number of failed root logins per minute tells you whether you're being noticed.)

## 6. Forgetting your instance is a legal entity now

This one surprises people. The moment another human uses your service, you've crossed a line.

Your photos, sure, those are yours. Your friend's calendar on your CalDAV? You're a data controller. Your family's Bitwarden vault on your Vaultwarden instance? Lose that and you've lost their passwords. The GDPR text uses the phrase "natural person" a lot. That's everyone you host.

This doesn't mean you can't self-host. It means you should write a one-page document for everyone who isn't you using your infra: how they export their data, how they get it recovered, what your realistic response time is when they email you at 11pm. (Mine is "next morning, probably." Yours can be "I'm not on call." Saying so isn't an apology.)

## 7. Picking software on hype, not maintainership

Last on the list, but in my experience the one with the longest fuse.

Not all open source projects survive three years. The flashy new Notion clone gets a Hacker News bump, you migrate your notes, eighteen months later the maintainer burns out and the fork doesn't cohere. Now you're migrating out on a deadline. Meanwhile the boring project — three commits a week, seven distinct contributors, never on the front page — would have outlasted everyone.

I wrote a whole separate piece on the bus-factor checklist (link below in the notes). The short version: before you adopt anything for real, look at distinct contributors in the last 30 days. One person is risk. Three is okay. Ten is durable. Look at whether someone is paid to work on it. Look at issue-closure behavior. Look at the license — OSI-approved is forkable insurance, source-available is not.

This is the failure mode where being late beats being early. Let other people stress-test the new thing for a year before you adopt it.

## The meta-failure: thinking self-hosting equals free

This is the stubborn one.

Self-hosting can be cheaper than SaaS. It often is. But "cheaper" isn't "free," and the cost is mostly time and attention, not money. For a weekend hobbyist, that's a feature — you wanted to tinker. For someone running a team tool, it's a budget line item that gets under-counted.

I'd say: budget at least an hour a week for anything you care about keeping running. Be honest when that hour is too expensive. Some things are worth paying $20/month not to think about. Others are worth the hour. The skill is knowing which is which, in advance, before you're locked into a setup that started as a fun Sunday and turned into a small unpaid job.

## The throughline

None of these are exotic. They're what happens to motivated, smart people who set up something real and then drift away. The system keeps running, until it doesn't, and the recovery bill has been quietly accumulating interest the whole time.

The mitigation isn't heroism or full automation. It's a small ritual — twenty minutes a month, give or take — where you log in, look at the box, run the restore drill when it's time, and decide whether the thing you're hosting still deserves the attention it costs.

Self-hosting done well is sustainable. Self-hosting done by default — by momentum, by inertia — isn't. That distinction is the whole game.

---

*Related: [Will the open source project you depend on still exist in three years?](/article/will-this-open-source-project-still-exist-in-three-years/) — the bus-factor checklist for picking what to self-host.*
