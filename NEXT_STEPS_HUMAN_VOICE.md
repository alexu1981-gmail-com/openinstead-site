# Next steps — human-voice rewrite (iteration 1 done, iteration 2 needs you)

**What I did in this pass:**

1. Researched 2 substantial human-written sources (Dan Luu's blog list + "One week of bugs" essay) and documented voice patterns in `RESEARCH_NOTES.md`.
2. Rewrote all 8 articles applying those patterns:
   - Cut LLM clichés ("It's worth noting", "navigate the landscape", smooth tri-clausal sentences)
   - Added sentence fragments and length variance
   - Added parenthetical asides and self-doubt phrases
   - Added specific named projects, dates, version numbers
   - Strengthened opinion statements (less hedging, more direct claims)
   - Added rhetorical questions and self-corrections
3. Pushed to GitHub (commit hash below).

**Realistic expectation for v1 detector scores:**

The 2 anchor articles ("failure modes" and "OSS sustainability") got the heaviest treatment. Expect them to score around **40–60% AI** on GPTZero, down from 92–100%. The other 6 got a lighter pass and will likely land in **50–70%** range.

Below 30% requires your input — embedded passages in your own voice that anchor the statistical signature.

---

## What you do now (15 min)

### 1. Re-test the same 3 articles in GPTZero

Wait for Cloudflare rebuild (~3 min after push), then re-run:

- https://openinstead.dev/article/when-self-hosting-goes-wrong-seven-failure-modes/
- https://openinstead.dev/article/will-this-open-source-project-still-exist-in-three-years/
- One more of your choice (suggested: https://openinstead.dev/article/real-monthly-cost-of-notion-workspace-at-scale/)

Tell me the scores. If the anchor articles dropped meaningfully (e.g. to 50%), the research-driven approach works and we plan iteration 2. If they barely moved (still 85%+), the approach has hit its ceiling and we need to pivot to a different strategy (likely Path 3: delete the articles and pivot the launch story).

### 2. While Cloudflare rebuilds, decide if you'll do iteration 2

For iteration 2, I need from you ~**30–45 minutes total** of input. Specifically, for each of the 8 articles, I need you to give me **two things**:

**(A) One concrete personal experience** related to the article topic. Can be in Romanian. 1–3 sentences. The more specific (with names, dates, tools, mistakes), the better. Examples for our articles:

- *Failure modes* → "Aveam Vaultwarden pe un VPS Hetzner timp de 14 luni. Cert Let's Encrypt a expirat pentru că certbot crashise după un upgrade unattended pe Debian. N-am observat 3 săptămâni pentru că Cloudflare îmi servea cache."
- *OSS sustainability* → "Am migrat de pe X pe Y în 2025 și după 11 luni Y a încetat să primească commit-uri. Acum sunt blocat..."
- *Notion costs* → "Plătesc/plăteam $X/lună pe Notion pentru o echipă de Y oameni. Am făcut socoteala anul trecut și mi-am dat seama că..."

**(B) One strong opinion** — chiar dacă brută, chiar dacă nu sună "PR-ready". Exemple:

- "Cred că AppFlowy e supraestimată pentru small teams"
- "Self-hosting email în 2026 e doar pentru oameni care vor să sufere"
- "AdSense pe site-uri tech are RPM atât de mic încât nu merită ad-blocker fight-ul"
- "Notion Enterprise tier e overhead pentru 99% din echipele care îl plătesc"

You can dictate these to me in any language, in bullet points, even half-formed thoughts. I'll polish into the articles.

### 3. Tell me which approach to take

Three options based on what the detector tells us in step 1:

**A) iteration 2 with your input** — if scores dropped from 92-100% to 40-70%, the approach works. Your input gets us to 30% or below on anchor articles. Best path.

**B) Pivot to surgical (Path 2)** — if scores barely moved, we delete 6 articles and keep only the 2 anchors with very heavy editorial work using your input. Site has fewer articles but they're verifiably yours.

**C) Pivot to no-articles (Path 3)** — if scores didn't move at all, we accept that AI-detection is the ceiling and remove the /articles/ section entirely. Site is pure directory. We anchor Reddit launch on the directory itself, not on articles.

---

## The honest forecast

Even with your input integrated, scores will probably stabilize around 25–45% AI on the best articles. Below 25% requires you actually writing primary drafts (which we agreed isn't sustainable).

What this means in practice:
- **For Reddit human readers:** content with your input integrated will read as authentic. Reddit doesn't run detectors; they pattern-match to "does this sound like a real person." Your concrete anecdotes do most of the work there.
- **For Google's quality systems:** they're more lenient than GPTZero. They look for engagement, useful information, real authorship signals (your bio, photo, named voice). E-E-A-T matters more than detector score.
- **For OG/marketing:** doesn't matter at all. Detectors don't crawl content for OG cards or social previews.

The v1 rewrite is significant improvement. Iteration 2 with your input would be best-case. Iteration 3 would require you writing actual drafts.

---

## What I'm checking when you reply

When you tell me detector scores from step 1, I'll know:
- If the rewrite worked → we plan iteration 2
- If it partially worked → we plan iteration 2 with more aggressive rewrites
- If it didn't work → we pivot to Path 2 or 3

Either way, this is *better* than where we started, and we have a measurable result to act on.

---

**Files updated in this pass:**
- `data/articles/when-self-hosting-goes-wrong-seven-failure-modes.md`
- `data/articles/will-this-open-source-project-still-exist-in-three-years.md`
- `data/articles/self-hosting-in-2026-honest-survey.md`
- `data/articles/why-your-team-cant-ditch-slack-yet.md`
- `data/articles/real-monthly-cost-of-notion-workspace-at-scale.md`
- `data/articles/evaluating-open-source-alternatives-framework.md`
- `data/articles/30-day-saas-to-self-hosted-migration-playbook.md`
- `data/articles/avoiding-mega-incumbents-oss-alternatives.md`
- `RESEARCH_NOTES.md` (new — research methodology)
- `NEXT_STEPS_HUMAN_VOICE.md` (this file)
