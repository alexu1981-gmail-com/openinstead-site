# Reddit + HN launch drafts — for review

**Status:** drafts. Read at your own pace, mark up anything that doesn't sound like you, and we iterate before posting.

**Submit-week target:** Tuesday of Sprint 4 Week 3 (~2026-05-12), 9–12 EST window.

---

## Account preparation (do BEFORE posting)

Reddit will silently filter posts from accounts that look suspicious. Don't lose this launch to a moderation filter.

1. **Use an existing Reddit account** if you have one with any history. New accounts with 0 karma posting links to a domain in r/selfhosted are auto-filtered or removed by mods within minutes.
2. **If your account is new (<30 days, <50 karma):** spend 15 minutes a day this week commenting genuinely in r/selfhosted, r/opensource, r/sysadmin. Helpful comments on other people's posts. Build 50–100 karma minimum. Don't rush this — it's the difference between "post live" and "post auto-removed before anyone sees it."
3. **Verify the account email** if not already done.
4. **Check the subreddit rules pages** the morning of the post — rules change. Both r/selfhosted and r/opensource have specific self-promotion clauses you must respect. r/selfhosted: "self-promotion welcomed if it's open source and you've engaged with the community first." We meet that bar (the directory is free, no signup, no upsell), but the engagement part is on you.

---

## Post 1 — r/selfhosted (anchor: failure modes article)

**Subreddit:** https://www.reddit.com/r/selfhosted/
**Audience:** ~550k subscribers, technical, allergic to marketing, generous to genuine contribution.
**Best window:** Tuesday or Wednesday, 9–11 AM EST (= 16–18 ora României).

### Title (pick one)

A. **The seven self-hosting failure modes I keep seeing — and the boring habits that prevent most of them**

B. **After two years of running self-hosted infra, the real failure modes are not the ones the guides warn you about**

C. **What goes wrong with self-hosting six months after the install (a retrospective)**

→ My pick: **A**. Title promises a list (Reddit clicks lists), uses "boring" as a credibility signal, and the framing is *insight* not *announcement*.

### Body

```
I've been running a stack of self-hosted services for a few years (Nextcloud,
Vaultwarden, Jellyfin, the usual), helping friends and family migrate to a few of
them, and lately I've been writing down the failure modes I keep seeing — both in
my own setups and in conversations with other self-hosters.

None of them are exotic. They're not "the filesystem melted" or "I got hacked."
They're small, human, preventable, and almost always invisible until something
breaks.

Top of the list, in rough order of how often they show up:

1. **"It worked, so I stopped thinking about it."** You set up Nextcloud on a
   Sunday, it worked, and eleven months later you can't remember the SSH key
   location for the VPS.

2. **Backups that nobody has tested.** Restic snapshots green for two years, then
   the first real restore reveals a corrupt encryption key that lived on the
   machine that just died.

3. **Upgrades you put off because they're scary.** GitLab three majors behind is
   no longer an upgrade, it's an expedition.

4. **A single $5 VPS as your single point of failure.** The provider has an
   incident, the instance gets terminated by a billing mistake, and your data
   wasn't on a separate volume.

5. **Exposing things to the public internet before understanding what was
   exposed.** Bots find your port-forward in hours.

6. **Forgetting your instance is a legal entity now.** Hosting data for friends
   and family makes you a data controller, whether you signed up for that role
   or not.

7. **Picking software on hype, not maintainership.** The flashy new Notion clone
   migrates beautifully and dies with its single maintainer eighteen months
   later.

I wrote up each of these with the small habits that actually mitigate them —
none of which involve heroism or full automation, mostly a 20-minute monthly
ritual where you log in and check things. Full piece is here if anyone wants the
long version: https://openinstead.dev/article/when-self-hosting-goes-wrong-seven-failure-modes/

What's missing from this list? I have a strong suspicion #8 should be "running
your service on the same machine as your reverse proxy and forgetting one of
them needs a separate restart strategy" but I haven't found a clean way to
phrase it.

(Disclosure: I run openinstead.dev, a small editorial directory of open source
alternatives to SaaS. This piece lives there. The site is free, no signup, no
affiliate links.)
```

### Why this works

- **Lead is insight, not announcement.** The first 4 paragraphs give value before any link.
- **List format earns clicks** even from people who scroll past long Reddit posts.
- **The disclosure is at the bottom and honest.** r/selfhosted mods explicitly tolerate this format. Hiding the connection to the site is what gets posts removed.
- **The closing question invites discussion.** Comments boost ranking; a discussion thread helps the post survive the first two hours.

### What NOT to do

- Don't link the homepage. Anchor on the article. The site itself is the bonus, not the headline.
- Don't reply to the first 5 comments with link drops to other articles. Reddit notices, mods notice, your own karma takes a hit.
- Don't argue if someone says "this could just be an awesome list" — that comment is correct and you can address it gracefully (see reply templates below).

---

## Post 2 — r/opensource (anchor: OSS sustainability article)

**Subreddit:** https://www.reddit.com/r/opensource/
**Audience:** ~250k subscribers, more philosophical, license-aware, enjoys evaluation frameworks.
**Best window:** Same day, ~3-5 PM EST or the day after (avoid stacking both posts within 12h).

### Title

**Will the open source project you depend on still exist in three years? A bus-factor checklist**

### Body

```
This started as a private rule of thumb for myself: before I migrate any real
work onto an open source project, run a quick check on whether it'll still be
maintained when I need it to be.

I wrote it up because I've watched enough beloved projects fade — not because
the code became useless, but because the single maintainer burned out and no
fork ever cohered. "It's open source, someone will keep it going" is a hope,
not a plan.

The signals I weight, ordered by predictive power:

1. **Distinct human contributors in the last 30 days.** One person = bus
   factor 1. Three or four = different category. Ten+ = durable.

2. **Whether someone is paid to work on it.** Sponsoring company, foundation,
   funded GitHub Sponsors. Volunteer-only is fine for a side project; risky for
   anything you'll depend on for years.

3. **Release cadence.** Steady minor releases beat a year of silence followed
   by "v2 rewrite is coming soon."

4. **Issue-closure behaviour.** Maintainers respond within days, even if just to
   triage? That's a project that respects users. Issues piling up unanswered is
   a slow-motion abandonment signal.

5. **License.** OSI-approved licenses (MIT, Apache, GPL family) protect users
   when the company pivots. BSL/SSPL/Elastic License don't. Treat
   source-available the way you'd treat a paid SaaS dependency.

6. **Burnout signals from the maintainers.** Read their commit messages, blog
   posts, social accounts. A maintainer who is publicly exhausted is a
   maintainer who may not be there in 18 months. Not a judgement — a data point.

A project that hits 5/6 is safe to depend on. 3/6 or fewer means you should
plan for the day you might fork it, or pick something else.

Full version with the checklist and examples here:
https://openinstead.dev/article/will-this-open-source-project-still-exist-in-three-years/

I'm curious what others on this sub have added to their own version of this
list — what signals do you weight that I'm missing?

(Disclosure: link is to a piece on a directory I maintain, openinstead.dev. No
ads yet, no affiliate, free to read.)
```

### Why this works

- **Frames as a private heuristic shared publicly** — feels useful, not promotional.
- **Numbered list with concrete signals** — Reddit-friendly, scannable.
- **Closing question** invites the audience to add to the list rather than judge it. Great for engagement.

---

## Post 3 — Show HN (Hacker News)

**Submit at:** https://news.ycombinator.com/submit
**Audience:** ~5M monthly readers, technical, pricing-aware, builder-mode.
**Best window:** Sunday evening or Monday early morning EST. HN front page churn is fast — early hours of low-traffic days have the best landing odds.

### Title

```
Show HN: OpenInstead – curated open source alternatives to popular SaaS
```

(Note: HN strips trailing punctuation and rewrites titles aggressively. Keep it short, lead with "Show HN:" exactly, no emoji, no clickbait.)

### Text body (optional but recommended for Show HN)

```
Hi HN,

I built openinstead.dev because every time I went looking for "open source
alternative to X" I ended up with one of three problems: AlternativeTo's
upvote-driven lists buried the actually-good options under abandonware,
awesome-selfhosted is comprehensive but unopinionated, and one-off blog posts
were either ad-driven or stale.

So I'm trying a fourth option: editorial directory. Hand-curated, written like a
human read each project before adding it, and explicit about strengths and
weaknesses (not just "Notion alternative — features").

Current state: 88 SaaS products, 122 OSS alternatives, 245 side-by-side
comparisons, 8 long-form essays. Static site, no JS framework, no signup, no
affiliate links. Hosted free on Cloudflare Pages.

Three things I'd appreciate honest feedback on:

1. The "best for" pairing on each comparison page — is the framing helpful or
   does it feel forced?
2. The article on evaluating OSS sustainability
   (https://openinstead.dev/article/will-this-open-source-project-still-exist-in-three-years/) —
   anything I'm missing from the bus-factor checklist?
3. What categories I should add next? I currently skipped self-hosted email
   servers (Mailcow, Mail-in-a-Box) deliberately because the deliverability
   story isn't a fair fight. Curious whether that's the right call.

Source data is YAML, the build is Python + Jinja2, total ~1k lines. Repo is
private for now (it has my draft article ideas in it) but happy to open if
there's interest.

— Alex
```

### Why this works

- **Show HN posts that work all share this pattern:** brief context, what's different, what feedback you want, signal that you're a real person.
- **The "what feedback you want" framing** turns the post from "look at my thing" into "help me improve my thing." HN responds to that.
- **Honest about what's static and what's missing.** HN is brutal about overclaiming.

---

## Pre-written reply templates

These are the comments you'll get. Have answers ready. Don't paste verbatim — adapt to the specific commenter, but the core message stays.

### "Why not just use AlternativeTo / awesome-selfhosted?"

```
Both are great, and I use them too. The difference I'm trying to draw is:

- AlternativeTo is upvote-driven, which means popularity beats quality. Notion's
  top alternatives there include several abandoned projects with last commits
  in 2022.
- awesome-selfhosted is comprehensive but lists everything. It tells you what
  exists, not what to pick.
- I'm trying to be opinionated. Each pairing on my site has a 'best for' line
  that says when this specific OSS makes sense and when it doesn't.

Whether opinionated curation actually scales editorially is the open question.
We'll see.
```

### "How do you make money / what's the catch?"

```
Currently nothing — the site has zero ads. I plan to apply for AdSense in a few
weeks once it has more traffic history. Long-term goal is display ads only, no
affiliate kickbacks, no paid placements (which is why every entry says "no paid
placements" on the contact page).

If that ever changes, I'll add a disclosure on the relevant pages. The whole
point of the site is to be the source you trust when the rest of the
"alternatives to X" results are SEO spam.
```

### "What about [specific tool X]?"

```
Good catch — adding it to the queue. If you have a paragraph on what it's good
at and where it falls short, drop it here or email contact@openinstead.dev and
I'll credit you in the entry. (I don't do user-submitted content as a feature
yet, but I do happily incorporate suggestions when they're better than what I'd
write myself.)
```

### "This looks AI-generated"

```
Some of the build tooling was written with AI help (the static site generator,
the OG image generator). The editorial content — the strengths/weaknesses, the
'best for' lines, the articles — is mine, written by a human, and that's the
part that matters for trust. Easy way to verify: read three OSS profiles and
ask whether the weaknesses sound like things a human noticed or like generic
bullet points. Genuine question — if any feel hollow, tell me which and I'll
rewrite them.
```

### "Why is X / Y / Z missing?"

```
Two reasons usually:

1. I want each entry to mean something — adding entries faster than I can
   verify them would dilute the directory's value. So I'm gating on quality of
   research, not coverage.
2. Some categories I've deliberately skipped because the comparison isn't fair
   yet (self-hosted email is the canonical example — running your own MX is
   not a like-for-like swap with Mailgun/SendGrid).

If there's a specific tool you'd like to see, the queue is real and I'd rather
know what people actually want than guess.
```

---

## After-post checklist

The first 60 minutes of a Reddit post matter more than the next 23 hours combined. Plan to be at your computer.

- [ ] Post goes live → reload after 5 min, confirm it didn't get auto-removed (look for "[removed]" tag). If removed, check modmail.
- [ ] Reply to the first 5 comments within 15 minutes. Generously. Even to skeptics — *especially* to skeptics.
- [ ] Don't post the second piece (r/opensource) until the first has stabilized. If r/selfhosted goes flat, the second post can repurpose the energy. If it's blowing up, give it room.
- [ ] Track Cloudflare Web Analytics every 30 min for the first 4 hours. The shape of the traffic curve tells you whether the post landed.
- [ ] Save the post URL — you'll want it for the post-mortem in a week.

---

## Schedule recommendation

| When | What |
|------|------|
| **Sat-Sun** (now) | You read these drafts, mark up anything off-voice |
| **Mon** | We iterate based on your feedback — final versions ready by EOD |
| **Tue 16:00 RO** | r/selfhosted post goes live |
| **Tue 21:00 RO** | r/opensource post goes live (only if Tuesday's first post landed cleanly) |
| **Sun (week 3)** | Show HN goes live (different audience, different week) |
| **Fri end of week 3** | AdSense apply (after ≥3 weeks of analytics history) |

Optional but worth considering: cross-post to **DEV.to** and **Hashnode** with canonical URL pointing to openinstead.dev. Free dofollow backlinks, takes 10 min total. We can do this in Bucket 5 prep.
