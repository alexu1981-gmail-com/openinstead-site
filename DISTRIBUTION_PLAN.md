# OpenInstead — Plan distribuție, domeniu și AdSense

**Creat:** 2026-04-25
**Status site:** live pe `openinstead-site.alexu1981.workers.dev`, 394 pagini indexabile, 0 vizite organice
**Obiectiv acest plan:** de la "site live pe subdomeniu" la "primul payout AdSense" în 12 săptămâni.

---

## 1. Domeniu — alegerea

### Candidații (verifică disponibilitatea la momentul când cumperi)

| # | Domeniu | TLD cost/an | Pro | Contra |
|---|---------|------------|-----|--------|
| 1 | **openinstead.dev** | ~$12 | Match cu brand-ul existent (pages: "OpenInstead"), audiența tech e relevantă pentru .dev, rezistent la imitatori. Chrome forțează HTTPS pe .dev = trust signal. | .dev e mai necunoscut pentru publicul non-tech. |
| 2 | **openinstead.com** | ~$12 | TLD universal, credibil pentru orice audiență, AdSense îl tratează identic cu .dev. | Poate fi deja luat sau parcat (verifică). |
| 3 | **ditchsaas.com** | ~$10 | Punchy, memorabil, shareable pe social. "Ditch SaaS" e un mesaj clar. | Mesaj prea activist; unii vizitatori pot fi puși pe gardă. Brandul existent din pagini e "OpenInstead" — ar trebui rebranded. |
| 4 | **selfhosted.directory** | ~$25 | TLD .directory e keyword-rich, Google îl tratează bine pentru pSEO de tip directory. | TLD nou, mai scump decât .dev/.com. |
| 5 | **ossalternatives.com** | ~$10 | Keyword-dense, ajută la SEO pe query-uri generice ("oss alternatives"). | Mai lung, mai greu de amintit. |

### Recomandare

**Pasul 1:** verifică disponibilitatea lui `openinstead.dev` și `openinstead.com` pe:
- [Porkbun](https://porkbun.com) (cele mai mici prețuri pentru .dev — ~$12/an)
- [Cloudflare Registrar](https://dash.cloudflare.com/?to=/:account/registrar) (at-cost, fără markup, integrare nativă cu Pages)

**Pasul 2:** dacă ambele libere → cumpără **openinstead.dev** (mai scurt, HTTPS forțat, audiență tech directă) ȘI `openinstead.com` (parkez-l pe un redirect 301 către .dev — costă $10, îl are cineva rău intenționat nu-l are; investiție defensivă).

**Pasul 3:** dacă .dev e luat, treci pe **openinstead.com**.

**Pasul 4:** dacă amândouă sunt luate, `ossalternatives.com` e plan B. Rebrand minimal în header-ul site-ului.

### De unde cumperi — comparație rapidă

- **Cloudflare Registrar:** la cost, fără markup (e.g. .dev ~$10.18/an). Domeniile cumpărate aici sunt deja în Cloudflare = zero config DNS. **Recomandat.**
- **Porkbun:** al doilea cel mai ieftin, promoții frecvente pentru primul an. Trebuie să migrezi NS-urile manual în Cloudflare.
- **Namecheap:** clasic, fiabil, mai scump cu ~$2-3.
- **GoDaddy:** evită — prețul crește la reînnoire și promoțiile sunt înșelătoare.

---

## 2. Timeline 12 săptămâni — de la launch la prima plată

### Săptămâna 1 — Fundament tehnic

- [ ] Cumpără domeniul (10 min).
- [ ] Conectează-l la Cloudflare Pages → Workers & Pages → OpenInstead → Custom domains → Add (5 min).
- [ ] Forțează HTTPS (default pe Cloudflare — verifică că e on).
- [ ] Setează redirect de la `www.openinstead.dev` către `openinstead.dev` (sau invers — pick one, stick with it).
- [ ] Schimbă `SITE_URL` în `build.py` la noul domeniu; Claude face push-ul cu fix-ul.
- [ ] Google Search Console: add property, verify via DNS (1 click pe Cloudflare), submit sitemap.xml.
- [ ] Bing Webmaster Tools: add site (face parte din ~10% trafic vestic, gratis 5 min).
- [ ] Cloudflare Web Analytics (gratis, privacy-friendly) — enable, add script în template.

**Deliverable săpt 1:** site live pe domeniu propriu, indexarea Google începută, analytics pornite.

### Săptămâna 2 — Content polish & AdSense pre-requirements

AdSense vrea să vadă că site-ul e "serios". Check-list înainte să aplici:

- [x] **15+ pagini de conținut unic** — avem 394, covered.
- [x] **Despre** (have `/about/`).
- [x] **Privacy policy** (have `/privacy/`).
- [ ] **Contact page** — AdSense cere contact info vizibil. Claude adaugă `/contact/` cu email.
- [x] **Conținut original** — editorial, nu AI-spun generic.
- [x] **Design profesional** — dark theme, responsive, rapid.
- [ ] **Domeniu propriu** — nu subdomeniu. Asta e prereq #1 al AdSense.
- [x] **Site mobile-friendly** — CSS e responsive.
- [x] **Navigare ușoară** — categorii + articole + search.

Plus nice-to-have:
- [ ] RSS feed pentru articles (Claude adaugă `/articles/rss.xml`) — ajută share-urile și creează backlink-uri naturale când oameni se aboneaează.
- [ ] Open Graph images per articol (Claude poate genera SVG-uri customizate per slug).

### Săptămâna 3 — Primul test de distribuție (soft)

Post în 2-3 comunități prietenoase, nu pe HN direct. Ca reconnaissance:

- **Reddit r/selfhosted** (~500k membri). Post text, nu link stuff. Format care merge:
  > *Title:* "Made a directory of open source alternatives to 68 popular SaaS tools — feedback welcome"
  > *Body:* ce ai construit, de ce, link la câteva pagini (nu doar homepage), invitație la feedback.
  > *Important:* răspunde la fiecare comment în 24h. Comunitatea simte efortul.
- **Reddit r/opensource** (~160k membri). Similar.
- **Mastodon / Bluesky / Twitter / LinkedIn personal.** Cu screenshots. Scriu eu post-urile în sesiunea următoare dacă vrei.
- **Hacker News Show HN:** ÎNCĂ NU. HN e pentru v1.1, nu v1.0. Primul post HN trebuie să fie cu domeniu propriu, polish complet, tot setup-ul AdSense gata. Dacă ratezi Show HN, nu mai ai al doilea chance.

**Deliverable săpt 3:** 200-500 vizite din Reddit, 5-15 backlinks naturale (cineva îl menționează pe propriul blog sau feed), primele semnale pentru Google.

### Săptămâna 4 — Aplicare AdSense

Requirement-urile sunt îndeplinite? Check. Aplică.

1. **https://www.google.com/adsense/start** → Sign up.
2. Add site: `openinstead.dev`.
3. Alege țara de payout (România dacă ai cont bancar RO).
4. Google verifică site-ul → adaugi un snippet HTML în `<head>` (Claude îl pune în template la push-ul următor, sau îl pui tu manual în Cloudflare Pages ca header injection).
5. Aștepți aprobare: **1-4 săptămâni**.

**Ce te poate face să fii respins:**
- Trafic prea mic (Google caută ≥100 vizite/zi pentru o aplicație serioasă; sub 20/zi e risk).
- Copiere de conținut → nu-i cazul, totul e original.
- Ads.txt problems → nu-i cazul, nu ai alte rețele.
- Policy violations → site-ul nostru e safe pentru brand.

Dacă primul apply e respins: nu-i catastrofă. Re-aplici în 2-4 săptămâni după ce ai mai mult trafic / mai multe articole. Cel mai comun motiv de respingere în 2026 e "insufficient content" + "low traffic" — ambele se rezolvă așteptând.

### Săptămâna 5-6 — Second wave distribution

După ce AdSense e aprobat (sau în paralel, dacă durează):

- **Hacker News Show HN**. Post în dimineață US/est (~9-11am EST). Format:
  > *Title:* "Show HN: OpenInstead – directory of open source alternatives to popular SaaS"
  > *Body:* paragraf scurt despre ce e, de ce l-ai făcut, ce te-a surprins construindu-l (transparență e cheia pe HN).
- **Product Hunt** lansare. Planificat dimineața SFO (00:01 PST) într-o zi de marți/miercuri. Get 5-10 prieteni pregătiți să upvote-uie în prima oră.
- **Indie Hackers** — share story-ul în Community / Growth.

**Realistic expectation de la HN Show:** 1-3k vizite în 24h dacă postul ajunge pe frontpage. 100-300 backlinks rezultate (tweets, reblogs, mentions în newslettere indie). Aceste backlinks sunt cel mai valoros asset SEO pe care îl poți câștiga.

### Săptămâna 7-8 — Add first paid ads

Odată AdSense aprobat:
- Activează Auto Ads din AdSense dashboard (plasament automat optim — start simplu).
- Monitorizează RPM (revenue per mille) și Page views în AdSense + Search Console.
- Dacă Auto Ads plasează ads în locuri proaste (UX ruinat), trecem manual la ad slots defined în template.

### Săptămâna 9-12 — Steady growth + content additions

- Claude mai face 1-2 sprint-uri de content (ex. +20 SaaS, +3 articole).
- Tu răspunzi la cerințele AdSense (uneori cer optimizări).
- Monitorizezi ce pagini iau cel mai mult trafic → le extinzi.
- Începi să primești primele $ (de obicei la luna 3-4 ajungi la ~$30-100/lună dacă SEO-ul merge bine).

---

## 3. Projections realiste (nu promisiuni)

Aceste cifre sunt bazate pe benchmark-uri pSEO 2025-2026 pentru nișe tech similare:

| Săptămâna | Vizitatori/zi | Revenue/lună | Status |
|-----------|--------------|--------------|---------|
| 1-2 | 0-10 | $0 | Indexare Google încă nu e efectivă |
| 3-4 | 20-100 | $0-2 | Primii vizitatori din Reddit + Google |
| 5-8 | 50-300 | $3-30 | HN Show HN + AdSense aprobat |
| 9-12 | 100-500 | $15-80 | Compound de backlinks + content adițional |
| Luna 4-6 | 300-1500 | $50-300 | SEO matur pe query-uri long-tail |
| Luna 6-12 | 500-3000 | $150-600 | Plateau sau creștere funcție de content velocity |
| Luna 12-18 | 1000-5000 | $300-1500 | Cu sprint-uri regulate de content |

**Primul payout AdSense:** de obicei la luna 4-6 (threshold $100).

### Ce poate accelera

- **Un HN frontpage spike (>1k vizite)** — +2-3 luni avans.
- **Un backlink de la awesome-selfhosted / privacytools.io / un YouTuber de self-hosting** — +1-2 luni.
- **Un spike pe Reddit r/selfhosted cu 500+ upvotes** — +1 lună.

### Ce poate întârzia

- **Google Helpful Content updates** lovesc pSEO. Ne protejăm prin conținut editorial (articolele!) și unghi genuin util (filtre, comparații side-by-side care nu există pe awesome-selfhosted).
- **AdSense respingere inițială** → 2-4 săpt întârziere.
- **Lansarea fără domeniu propriu** → Google nu indexează subdomeniul serios, AdSense nu aprobă. Ne-cumpărarea domeniului e single biggest risk.

---

## 4. Cheltuieli estimate primele 3 luni

| Item | Cost | Note |
|------|------|------|
| Domeniu .dev | $12 | 1 an, Cloudflare Registrar |
| Domeniu .com (defensiv) | $10 | Optional |
| Cloudflare Pages | $0 | Bandwidth nelimitat, unlimited builds |
| Cloudflare Web Analytics | $0 | Privacy-friendly |
| Google Search Console | $0 | |
| Bing Webmaster Tools | $0 | |
| AdSense | $0 | Payment processing încorporat |
| Timpul tău | 2-3h/săpt | Răspuns la comment-uri Reddit, monitoring |
| Timpul Claude | ~8h (cumulat) | 4-5 sesiuni următoare pentru content + fixes |
| **Total cash** | **~$12-22** | |

Toate celelalte sunt gratis. Threshold-ul de breakeven: la prima plată AdSense (~$100), cost real rambursat de ~10x.

---

## 5. Next actions — ce fac eu vs ce faci tu

### Eu (Claude, sprint-ul următor, fără necesar input de la tine)

- Adaug `/contact/` page cu email-ul tău (care? `alexu1981@gmail.com` or creezi unul dedicat?).
- Adaug RSS feed la `/articles/rss.xml` pentru conținut indexable.
- Adaug JSON-LD Organization + BreadcrumbList markup pentru Rich Results.
- Adaug OG image generator (SVG) per articol și per SaaS page.
- Corectez `SITE_URL` în build.py odată ce știu domeniul.

### Tu (acțiuni manual, spread peste 2-3 zile)

- [ ] **Verifică disponibilitatea și cumpără domeniul** (5 min).
- [ ] **Conectează-l la Cloudflare Pages** prin Custom Domains (5 min, ghidat în README.md).
- [ ] **Google Search Console** → add property + verify + submit sitemap (10 min).
- [ ] **Bing Webmaster Tools** → add + verify (5 min).
- [ ] **Enable Cloudflare Web Analytics** (2 min).
- [ ] **AdSense** apply la săpt 4 (10 min + aștept aprobare).
- [ ] **Reddit post** la săpt 3 (30 min de scriere + monitoring comments).
- [ ] **Bank account pregătit pentru payout USD** (dacă n-ai: Revolut / ING / BT).

**Timp total tu:** ~4-6 ore spread peste 4-6 săptămâni. Plus timpul de răspuns la comment-uri (opțional dar merită).

---

## 6. Decizii pending — ce te rog să-mi confirmi înainte de next sprint

1. **Ce email pentru contact page?** `alexu1981@gmail.com` direct, sau creezi `contact@openinstead.dev` odată ce ai domeniul?
2. **Ce domeniu ai ales?** (Când ajungi la pasul de cumpărare.)
3. **AdSense cont pe numele tău personal (CF Alexandru Drăghici) sau PFA/SRL?** Afectează cum declari fiscal veniturile. Dacă targetezi $500-1000/lună susținut, PFA e mai fluent la ANAF decât PF simplu.

---

## 7. Risk log (transparent)

- **Google Helpful Content update care lovește pSEO.** Mitigare: articolele editoriale + conținut unic vs. awesome-list reposts.
- **AlternativeTo.net se trezește și face SEO serios.** Mitigare: noi avem UX mai bun + articole + comparison pages, dar vom fi eclipsați pe brand authority. Ne diferențiem prin editorial.
- **Cloudflare Workers platform schimbă terms pentru site-uri monetizate.** Mitigare: static site = portabil. Mutăm pe Netlify/Vercel în 1 zi dacă e cazul.
- **Tu decizi să nu continui proiectul.** Mitigare: site-ul e al tău, repo e al tău, plata merge în contul tău. Nimic nu depinde de mine. Dacă dispar pentru 6 luni, site-ul continuă să genereze trafic și AdSense.

---

*Acesta e un document viu. Claude îl updatează la fiecare sesiune strategică. Next review: după ce cumperi domeniul.*
