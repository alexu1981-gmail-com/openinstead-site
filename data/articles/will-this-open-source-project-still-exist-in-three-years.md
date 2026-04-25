---
title: "Will the open source project you depend on still exist in three years?"
description: "Bus factor, maintainer burnout, funding models, and the signals that separate OSS projects that survive from those that quietly decay."
date: 2026-04-25
category: Opinion
---

You're evaluating an open source alternative to some SaaS tool. It looks great. The demo is polished, the features are there, the license is permissive, the community on GitHub feels alive. You migrate over.

Two years later, you hit a bug that nobody is fixing. The last commit on main was four months ago. The single maintainer's social accounts have gone quiet. The two pull requests you opened are sitting there, unreviewed. Your data is locked inside a thing that isn't really going anywhere anymore.

This is not a rare story. It's the single biggest risk of adopting open source software, and we almost never talk about it until it's too late.

This piece is a framework for asking, before you adopt something, whether it's going to be there when you need it to be.

## Why "open" doesn't mean "forever"

People assume open source is automatically durable. The logic runs: the code is public, so if the original maintainer disappears, someone can fork it. This is true in principle and often false in practice.

Forks happen when three things line up: the project is valuable enough to fork, there are qualified engineers willing to maintain the fork, and those engineers can coordinate. Plenty of beloved projects have died not because the code became useless, but because no fork cohered around them. The maintainers drifted, the fork attempts never reached critical mass, and the codebase rotted.

"It's open source, someone will keep it going" is a hope, not a plan. If you're choosing software to depend on, you need to do better than hope.

## The signals that actually matter

We've watched enough projects grow, plateau, and decline to have opinions. Here are the signals that predict durability — ordered roughly by how much they matter.

### How many humans pay attention to this repo every week

Open up the repo and look at the last four weeks of activity. Count distinct human authors across commits, PR reviews, and substantive issue comments. If the answer is one person, that's a bus factor of one. If it's three or four, better. If it's ten or more, you're in a different category of durability entirely.

This is easier to assess than it looks. GitHub's "Insights → Contributors" graph shows you recent activity. The pattern you want is: steady, distributed contributions, not a spiky graph that's all one person.

### Whether someone is being paid to work on it

Unpaid volunteer maintainers burn out. Not every one of them, not always, but often enough that you should weight paid contribution heavily when you're picking a dependency.

Look for: a sponsoring company (Sentry for Symfony, Percona for MySQL forks, Grafana Labs for Grafana); a foundation (Apache Software Foundation, CNCF, Linux Foundation); a commercial entity behind the open source version (Metabase, Mattermost, Chatwoot); a healthy GitHub Sponsors or Open Collective balance that actually funds someone's hours.

A project with zero paid contribution isn't doomed, but it's running on pure volunteer energy, and volunteer energy is finite.

### Release cadence over the last twelve months

A healthy project ships releases. Not necessarily major versions — point releases, bug fixes, security patches. Open the releases page and look at the last year. A handful of thoughtful releases is better than a flurry of unstable ones or a silent stretch.

Watch out for the "big rewrite in progress" pattern, where the maintainer has announced that v2 is coming and v1 is in maintenance-only mode. Sometimes v2 ships and is great. More often v2 takes three years and demoralizes the v1 community in the meantime. Ask yourself whether you're willing to be the user who sits on v1 while the big rewrite happens elsewhere.

### Issue-closure behaviour

This one is subtle. Open the issue tracker and sort by "recently updated." Are maintainers responding to issues within days? Triaging, labeling, asking clarifying questions? Or are issues piling up unanswered, sorted into stale buckets?

The pattern you want isn't "every issue gets solved" (that's unrealistic) — it's "issues get acknowledged." A project where maintainers respond to users is a project that respects the users. A project where issues go into a silent pit is a project that's lost its connection to the people depending on it.

### The license and its drift risk

Open source licenses are not neutral. They shape what the project can become later.

Genuinely open licenses (MIT, Apache-2.0, BSD, GPL family) protect users over time — even if the original project gets acquired or the maintainers pivot, the last open release stays available and forkable.

Source-available licenses (BSL, SSPL, Elastic License, Commons Clause) do not offer that guarantee. They allow the company behind them to restrict use in ways a classic OSS license wouldn't. We've watched several beloved tools (Redis, Elastic, HashiCorp's stack) relicense under source-available terms, forcing downstream users and cloud providers to fork or migrate.

If the license isn't an OSI-approved one, factor in: what happens when this project gets acquired or pivots? Usually the answer is "we relicense, and your use case might not survive the change."

### Whether the core maintainers talk about burnout

Read the maintainers' public writing. Their blog posts, their social-media accounts, their conference talks, their commit messages. Are they excited about the project? Frustrated? Tired?

Burnout is the single largest killer of one-person and two-person OSS projects. A maintainer who is publicly exhausted is a maintainer who may not be maintaining the project in eighteen months. This isn't a judgment — burnout is deeply human and often justified. It's a data point for you, the user, about the durability of the thing you're about to depend on.

## The checklist we use

Before adopting anything for real work, we run through this quickly:

1. **Recent activity.** At least three distinct human contributors in the last thirty days.
2. **Paid contribution.** Someone's full or partial salary depends on this project continuing. Ideally, more than one someone.
3. **Releases.** At least one release in the last three months, with release notes that aren't just "bug fixes."
4. **Issue hygiene.** Maintainers respond to new issues within a week on average, even if just to triage.
5. **License.** OSI-approved. If it's source-available, treat it as a commercial dependency with extra steps.
6. **Bus factor.** If the top committer left tomorrow, could the project continue? At what velocity?
7. **Roadmap honesty.** Is the roadmap public, up to date, and realistic? Or is it aspirational wishlist that hasn't been touched since launch?

A project that hits five of seven is probably safe to depend on. A project that hits three or fewer is one you should adopt only if you're comfortable being the one who might have to fork it someday.

## What to do when you spot risk but love the tool anyway

Sometimes the answer is "yes, the bus factor is one, and yes, I'm going to use it anyway." That's fine. Just do it with eyes open.

Two habits help:

**Keep your data portable.** If the project dies tomorrow, you shouldn't be trapped. Pick tools whose data formats are open (SQLite, plain markdown, standard protocols) over tools that lock your data into a custom binary format only the vendor's software reads. Export regularly. Store exports somewhere the project itself can't write over.

**Contribute defensively.** If you're depending on a small project, contribute to it proportionally. Not because you owe the maintainer — though if they're solo and unpaid, you kind of do — but because being part of the contributor pool means you have a say if the project needs a fork or a handoff later.

## The landscape we actually live in

Most open source projects in this directory, most projects anywhere, are maintained by small teams with narrow budgets. That's not a problem; it's the model. But it means the thing you're adopting today may not be the thing running in 2029.

The projects that *do* make it that long share patterns. They have more than one maintainer. Someone gets paid. Releases ship. Issues get answered. The license protects users, not just the vendor. And the maintainers sound, in their writing, like people who still like working on the project after several years.

We weight our recommendations by these signals. We don't always get it right, but we try not to recommend anything we wouldn't be comfortable depending on for three years. If you spot a project in our directory that's showing the warning signs above — stale commits, unanswered issues, pivoting license — tell us. We update entries when the reality changes.

The goal isn't to be cynical about open source. It's to be honest about it. Open source, when it works, is the most durable software in existence. When it doesn't work, it fails quietly, over years, and the users who depended on it are the last to know.

Choose like you'll still be running the choice three years from now. Because often, you will be.
