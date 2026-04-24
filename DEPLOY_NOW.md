# Deploy rapid — ghid instant

Două căi. Alege A pentru preview instant (2 minute), apoi B pentru deploy permanent.

---

## OPȚIUNEA A — Preview instant pe Netlify Drop (2 min, fără GitHub, fără cont)

Vrei să vezi site-ul live în 2 minute? Asta e calea.

### Pași

1. Deschide în browser: **[app.netlify.com/drop](https://app.netlify.com/drop)**
2. În folder-ul `pSEO-oss-alternatives/` ai fișierul **`openinstead-preview.zip`** (541 KB).
3. Tragi zip-ul peste zona mare din pagina Netlify Drop (drag-and-drop).
4. În ~20 de secunde primești un URL de forma `https://AMAZING-WORD-123.netlify.app`.

### Note despre această cale

- Deploy-ul e **public** (oricine cu URL-ul îl vede).
- Fără cont Netlify: URL-ul expiră după 24h. **Cu cont gratuit Netlify** (creat cu email/Google, 1 min), URL-ul e permanent + poți adăuga domeniu personal mai târziu.
- Este **doar pentru preview**. AdSense nu funcționează pe subdomenii `.netlify.app` (Google nu aprobă monetizarea pe subdomenii). Pentru monetizare reală, treci la Opțiunea B.

---

## OPȚIUNEA B — Deploy permanent (GitHub + Cloudflare Pages, ~10 min)

Asta e setup-ul real, monetizabil, gratis permanent. Alege fie B1 (manual, 5 comenzi) fie B2 (scriptul `init-repo.sh`, și mai rapid).

### B1 — Manual

#### Pasul 1: creează repo gol pe GitHub (1 minut)

1. Deschide **[github.com/new](https://github.com/new)** (dacă nu ai cont, îți iei unul gratuit acum cu email-ul `alexu1981@gmail.com` — 1 min).
2. **Repository name:** `openinstead-site`
3. **Public** (necesar ca să funcționeze cu Cloudflare Pages Free).
4. **IMPORTANT:** NU bifa "Add a README", "Add .gitignore", "Add license". Trebuie să fie complet gol.
5. Click "Create repository".
6. Pagina care apare îți arată URL-ul repo-ului: `https://github.com/USER/openinstead-site.git`. Copiază-l.

#### Pasul 2: deschide Terminal pe Mac și rulează

```bash
cd "/Users/alexandrudraghici/Library/CloudStorage/GoogleDrive-alexu1981@gmail.com/My Drive/AI Software Projects/Passive-Income-Ideas-Exploring/Explore Passive Income Ideas/pSEO-oss-alternatives"

# Curăț orice .git parțial (din build-ul meu)
rm -rf .git

# Init + commit
git init -b main
git config user.email "alexu1981@gmail.com"
git config user.name "Alexandru"
git add -A
git commit -m "Initial commit: OpenInstead pSEO site"

# Conectez la GitHub (înlocuiește USER cu username-ul tău GitHub)
git remote add origin https://github.com/USER/openinstead-site.git
git push -u origin main
```

La primul `git push`, Mac-ul îți va cere să te autentifici la GitHub (popup sau terminal). Folosește username-ul + un **Personal Access Token** ca parolă (nu parola contului):
- Generează PAT la [github.com/settings/tokens](https://github.com/settings/tokens) → "Generate new token (classic)" → bifează `repo` scope → Generate → copiază.
- La prompt, la username scrii `alexu1981`, la password lipești PAT-ul.
- Sau, mai simplu pe Mac: instalezi [GitHub Desktop](https://desktop.github.com/) care se ocupă de auth vizual.

### B2 — Automat cu init-repo.sh (și mai rapid)

1. Fă ce scrie la Pasul 1 de mai sus (crează repo gol pe GitHub).
2. Deschide Terminal pe Mac:

```bash
cd "/Users/alexandrudraghici/Library/CloudStorage/GoogleDrive-alexu1981@gmail.com/My Drive/AI Software Projects/Passive-Income-Ideas-Exploring/Explore Passive Income Ideas/pSEO-oss-alternatives"
chmod +x init-repo.sh
./init-repo.sh USERNAME_GITHUB openinstead-site
```

Înlocuiește `USERNAME_GITHUB` cu username-ul tău real. Scriptul face tot restul.

#### Pasul 3: conectează Cloudflare Pages (~5 min)

1. Du-te la **[dash.cloudflare.com](https://dash.cloudflare.com)** (cont gratuit cu email dacă n-ai încă).
2. Bara stânga: **Workers & Pages** → **Create** → tab **Pages** → **Connect to Git**.
3. Autorizează GitHub → selectează repo-ul `openinstead-site`.
4. Build settings:
   - **Framework preset:** None
   - **Build command:** lasă gol (deja avem `dist/` in repo)
   - **Build output directory:** `dist`
   - Environment variable (opțional): `SITE_URL=https://your-subdomain.pages.dev` (poți schimba mai târziu)
5. Click **Save and Deploy**.
6. În ~1-2 minute site-ul e live la `https://openinstead-site.pages.dev` (sau un nume pe care îl alegi).

**Important:** Cloudflare Pages are deploy automat — de fiecare dată când faci `git push` cu modificări, site-ul se re-publică automat în ~2 min.

#### Pasul 4 (opțional, mai târziu): conectează domeniul

După ce cumperi `openinstead.dev` (sau orice alt domeniu):
1. Cloudflare Pages → proiectul tău → **Custom domains** → Add → introduci domeniul.
2. Dacă ai cumpărat domeniul pe Cloudflare Registrar: zero config, e gata imediat.
3. Dacă e pe Namecheap/GoDaddy: Cloudflare îți arată 2 name-servere. Le pui în panoul DNS al registratorului tău. Propagare 5 min - 24h.

---

## Care e diferența între A și B?

| | Netlify Drop (A) | GitHub + Cloudflare (B) |
|---|---|---|
| Timp setup | 2 min | 10 min |
| Cost | 0€ | 0€ |
| Suport AdSense | ❌ Nu (subdomeniu) | ✅ Da, când adaugi domeniu propriu |
| Update = rebuild automat | ❌ Manual drag-drop | ✅ `git push` → 2 min |
| Bandwidth | Generos | **Nelimitat** |
| Persistență | 24h fără cont | Permanent |

**Recomandare:** începe cu A **acum** ca să vezi site-ul funcționând, apoi **în următoarea oră** treci la B ca să fie setup-ul final.
