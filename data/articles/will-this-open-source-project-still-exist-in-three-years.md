---
title: "Will the open source project you depend on still exist in three years?"
description: "Bus factor, maintainer burnout, funding models, and the signals that separate OSS projects that survive from those that quietly decay."
date: 2026-04-25
category: Opinion
---

You're evaluating an open source alternative to some SaaS. The demo loads, the features are there, the license is permissive, the GitHub looks alive. You migrate.

Two years later, you hit a bug nobody is fixing. Last commit on `main` was five months ago. The single maintainer's Mastodon went quiet in October. Your two PRs are sitting there, marked "needs review" since February. Your data is now hostage to a project that isn't going anywhere.

Not a rare story. The single biggest risk of adopting open source software, and we almost never talk about it until it's too late.

This piece is the rule of thumb I use before adopting anything for real work.

## Why "open" doesn't mean "forever"

The standard reassurance: the code is public, so if the maintainer disappears, someone forks it. True in principle. False often in practice.

Forks happen when three things line up: the project is *valuable enough* to fork, qualified engineers are *willing* to maintain it, and those engineers can *coordinate*. Plenty of beloved projects have died not because the code became useless, but because the fork attempt never reached critical mass.

The pattern I've watched: maintainer announces "I need a break, I'll be back in a few weeks." Two months pass, no commits. A well-meaning forker shows up, pushes a few PRs, gets discouraged when nobody reviews them. Six months later the original repo is archived, the fork has 12 stars, and nobody's running either in production.

"It's open source, someone will keep it going" is hope, not a plan. If you're choosing software to depend on for actual work, you need better than hope.

## The signals that actually matter

Roughly ordered by predictive power, based on the projects I've watched succeed and fail.

### Distinct human contributors in the last 30 days

Open the repo, click Insights → Contributors. Look at the last four weeks. Count distinct human authors across commits, PR reviews, and substantive issue triage.

One person? Bus factor 1. That's not necessarily bad — a lot of fantastic tools are one-person projects — but it's *risk*, and you should price it in.

Three or four? Different category.

Ten or more? Durably alive in a way that survives any single contributor walking away.

The shape you want is steady, distributed, and recent. A spiky graph that's all one person, or a flat graph for the last six months, are both warning signs.

### Whether someone is being paid

Volunteer maintainers burn out. Not all of them, not always, but more often than the OSS romantic story admits.

What you're looking for, in rough order of robustness:

- A foundation backing it. Apache, CNCF, Linux Foundation, OWASP. These projects survive individual maintainers leaving.
- A commercial company whose business is the project. Mattermost, Metabase, Chatwoot, Ghost — open core or open source with a paid hosted version.
- A sponsoring corporate user. Cloudflare paying for OctoMozilla bandwidth, Stripe paying for someone's Symfony hours, Sentry's open source program.
- GitHub Sponsors that actually fund a part-time effort. (Most don't. Check the sponsorship page.)
- Patreon or Open Collective with enough monthly to fund a few hours weekly.

A project with zero paid contribution isn't doomed. But it's running on volunteer energy, and volunteer energy is finite. You should know which side of that line your dependency sits on.

### Release cadence over the last twelve months

Healthy projects ship. Not necessarily major versions — point releases, security patches, bug fixes count.

Open the releases page. Last year. What does the rhythm look like?

Watch out for the "big rewrite in progress" pattern, where the maintainer announced v2 is coming and v1 is in maintenance-only mode. Sometimes v2 ships and is great. More often v2 takes three years. The v1 community demoralizes in the meantime. Are you willing to be the user who sits on v1 while the rewrite eats the maintainer's energy for two years? Sometimes the answer is yes, but you should answer it consciously.

### Issue closure behaviour

Open the issue tracker. Sort by "recently updated." Are maintainers responding within days, even just to triage and label? Or are issues piling up unanswered, getting stale-bot closed automatically with no human in the loop?

You don't want "every issue gets fixed" — that's unrealistic. You want "issues get acknowledged."

A project that responds to users is a project that respects users. A project where issues vanish into a silent pit has lost its connection to the people depending on it. That's usually a precursor to maintainer burnout, not a separate phenomenon.

### License (the slow-fuse risk)

Open source licenses aren't neutral. They shape what the project can become later.

Genuinely open licenses — MIT, Apache-2.0, BSD, GPL family — protect users over time. Even if the project gets acquired or pivots, the last open release stays available and forkable. Vaultwarden exists because Bitwarden's server is GPL.

Source-available licenses don't. BSL, SSPL, Elastic License, Commons Clause — these allow the company behind them to restrict use later. We've watched Redis, Elastic, and HashiCorp's stack relicense in the last few years, forcing downstream users and cloud providers to fork (Valkey, OpenSearch, OpenTofu).

If the license isn't OSI-approved, treat it as a paid SaaS dependency, not as open source. The economics are different and the long-term protections are weaker.

### Maintainer burnout signals

Read the maintainers' public writing. Their commit messages. Their blog. Their social accounts. Their conference talks if there are any.

Are they excited? Frustrated? Tired?

This isn't about judging anyone. Burnout is human and often justified. It's a *data point* — about the durability of the thing you're about to depend on for years.

A maintainer who is publicly exhausted is a maintainer who may not be there in eighteen months. Plan accordingly.

## The checklist I actually use

Before adopting anything for real work:

1. **Recent activity.** At least three distinct human contributors in the last 30 days, not just the bot account.
2. **Paid contribution.** Someone's full or partial salary depends on this project continuing. Ideally more than one someone.
3. **Releases.** At least one release in the last three months, with release notes that aren't just "bug fixes."
4. **Issue hygiene.** Maintainers respond to new issues within a week on average, even if just to triage.
5. **License.** OSI-approved. Source-available means commercial dependency with extra steps.
6. **Bus factor.** If the top committer left tomorrow, could the project continue at any reasonable velocity?
7. **Roadmap honesty.** Is the public roadmap up to date and realistic, or is it an aspirational wishlist nobody's touched since launch?

A project that hits five of seven is probably safe to depend on. Three or fewer means you should adopt only with eyes open about possibly forking it yourself someday.

## What to do when you spot risk but love the tool anyway

Sometimes the answer is "yes, the bus factor is one, and yes, I'm using it anyway." That's fine. Just go in honestly.

Two habits help:

**Keep your data portable.** If the project dies tomorrow, you shouldn't be trapped. Pick tools whose data formats are open — SQLite, plain markdown, mbox, standard protocols — over tools that lock data into a custom binary only the vendor's software reads. Export regularly. Store exports somewhere the project itself can't write over.

**Contribute defensively.** If you're depending on a small project, contribute proportionally. Not because you owe the maintainer (though if they're solo and unpaid, you kind of do). Because being part of the contributor pool means you have *standing* if the project needs a fork or a handoff later. Maintainers hand projects to people they recognize.

## What I get wrong

I've been using this checklist informally for a few years and I get it wrong regularly. A few examples I can remember:

- I undervalued Plausible early because the contributor graph looked thin. The two-person team turned out to be much more reliable than the metric implied.
- I overvalued a federated search project (which I won't name) because activity was high. Turns out activity was high *because* of internal disagreement, and the project effectively forked itself a year later.
- I dismissed Forgejo when it forked from Gitea because forks usually fail. This one didn't. Sometimes the right people coordinate.

The checklist is a heuristic. It's wrong about ~20% of the projects I run it against. That's still better than no checklist, which was my baseline before.

## The landscape we live in

Most OSS projects are maintained by small teams with narrow budgets. That isn't a problem; it's the model. But it means the thing you're adopting today may not be the thing running in 2029.

Projects that *do* make it that long share patterns. More than one maintainer. Someone gets paid. Releases ship. Issues get answered. The license protects users, not just the vendor. And the maintainers, when you read their writing, sound like people who still find the project interesting.

Choose like you'll still be running the choice three years from now. Because often, you will be — and the cost of being wrong is paid in migrations you didn't plan for.
