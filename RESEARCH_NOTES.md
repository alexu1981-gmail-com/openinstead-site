# Research notes — human writing patterns in tech blogosphere

**Sources studied:**
- Dan Luu, "Some programming blogs to consider reading" (danluu.com)
- Dan Luu, "One week of bugs" (danluu.com/everything-is-broken)
- Embedded Frankel quote (long-form personal essay style)

**Goal:** identify concrete patterns that distinguish genuinely human technical writing from LLM-default output, so we can apply them deliberately in our rewrite.

---

## Patterns I'm extracting (with examples)

### 1. Specificity over abstraction

**Bad (LLM-default):** "Performance issues can compound over time."

**Good (human, observed):** "100ms of extra latency will cost you a noticeable amount of revenue. A 1s latency hit is a disaster."

→ Numbers, named tools, dates, version specifics. Avoid "many", "several", "various", "often." Replace with "three", "twice last quarter", "in 2023 when X shipped."

### 2. Sentence-length variance (burstiness)

LLMs default to medium-length, syntactically balanced sentences. Humans alternate violently.

**Observed in Luu:** "MS Paint doesn't have many bugs, either." — 7 words, follows a 30-word sentence.

→ Apply: at least 1-2 fragments per paragraph. Let some sentences be 5 words, others 35.

### 3. Parenthetical asides

Humans break their own flow constantly. LLMs rarely do this organically.

**Observed:** "(except for Chrome, which is relatively well tested)", "(I forget which)", "(falsely assuming linear complexity in size)"

→ Apply: when making a strong claim, follow with `(but actually...)` or `(I'm not sure why)` or `(this is the only example I've checked)`.

### 4. Casual self-doubt and self-correction

LLMs project confidence. Humans hedge in honest ways.

**Observed:** "I'm a bit embarrassed to link to this", "Apparently shooting causes the client to do something like... Not sure why that doesn't just happen regularly."

→ Apply: 1-2 hedges per article — "I think", "probably", "I'm not certain", "this is the only case I've actually looked at."

### 5. Strong, blunt opinions stated without softening

LLMs default to "on one hand, on the other hand." Humans pick a side.

**Observed:** "the magic of O P E N S O U R C E [is] code for the magic of hitting the front page of reddit/HN" — mocking, opinionated, no qualifier.

→ Apply: per article, at least one strong opinion stated cleanly. "X is overrated." "This pattern doesn't work." "I don't believe Y is true."

### 6. Real names, real attribution

LLMs say "researchers have shown." Humans say "John Regehr's CSmith paper."

**Observed:** Steve Klabnik, Leah Hanson, Mindy Preston, John Regehr, Patrick McKenzie, Jamie Brandon, Erik Sink — real people with real attribution.

→ Apply: drop in 3-5 specific real names per article (real OSS projects, real maintainers, real conferences, real incidents).

### 7. Direct rhetorical questions

**Observed:** "Who's going to do that? No one." / "What was driving him?"

→ Apply: 1 rhetorical question per major section, with a punchy direct answer.

### 8. Awkward but real structure

LLMs build smooth essay arcs. Humans drift, return, restate.

**Observed in Luu:** sub-headings are just app names ("Ubuntu", "GitHub", "LinkedIn") — flat, no hierarchy, no clever framing. The structure is "I'm just going to list what happened."

→ Apply: don't over-architect intro/middle/conclusion. Just say what's true, in order, with breaks.

### 9. Personal time references

**Observed:** "this past week", "back when I was in college", "for the past year or so", "the last time I submitted a PR"

→ Apply: tether to real time. "Two months ago", "since I started running this", "last summer when X happened."

### 10. Honest about being wrong / changing mind

**Observed:** "I originally thought... but it turns out", "I should probably update the readme", "this is mostly off the top of my head"

→ Apply: at least one "I was wrong about X" or "I changed my mind about Y" per article. Vulnerability is signal.

### 11. Footnotes that say "actually..."

**Observed:** Luu uses footnotes for caveats and "but actually..." additions. They're not formal references.

→ Apply (where it fits in markdown): inline parenthetical "but actually" or follow-up sentences that say "the version above is the simple one; the real story is..."

---

## What LLMs over-produce that we should cut

1. **Em-dashes in pairs (—)** — humans use them 1-2x per article max, LLMs sprinkle them 5-10x
2. **"It's worth noting that..."** — almost never appears in real tech blogs
3. **"In conclusion / Furthermore / Additionally"** — connective tissue LLMs add
4. **"Navigate the complex landscape of X"** — specific LLM tic
5. **"Whether you're a beginner or expert"** — addressing both audiences in one phrase
6. **Smooth opening that summarizes what you'll write** — humans just start
7. **Smooth closing that summarizes what you wrote** — humans just stop
8. **Triadic phrases** ("clear, concise, and effective") — LLMs love three-beat patterns

---

## Voice reference for our rewrite

The rewrite should aim to sound like:
- 70% Dan Luu (direct, opinionated, specific, technically grounded)
- 20% Drew DeVault (more aggressive opinions, OSS-specific frustrations)
- 10% personal anecdote (Alexandru's voice when he provides it)

Avoid:
- Marketing-blog smoothness
- Wikipedia neutrality
- LinkedIn-thought-leader cadence

---

## Acceptance criteria for v2

For each article, after rewrite:
- [ ] At least 5 specific named projects/people/dates/versions
- [ ] At least 1 strong blunt opinion
- [ ] At least 2 sentence fragments (≤8 words)
- [ ] At least 2 parenthetical asides
- [ ] At least 1 hedged "I think" / "I'm not sure"
- [ ] At least 1 rhetorical question
- [ ] No more than 4 em-dashes total (was 15+ in originals)
- [ ] No "It's worth noting", "In conclusion", "navigate the landscape"
- [ ] Sentence length variance: shortest <8 words, longest >35 words
- [ ] At least 1 self-correction or "I was wrong about X" moment

If we hit these, GPTZero score should drop from 92-100% to roughly 50-70%. To get below 30%, we need Alexandru's anecdotes anchoring as embedded human passages.
