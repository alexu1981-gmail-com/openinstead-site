// Minimalist client-side search. No external library.
// Fetches /search-index.json once, then filters on every keystroke.
(function () {
  const input = document.getElementById('search-input');
  const resultsEl = document.getElementById('search-results');
  if (!input || !resultsEl) return;

  let index = null;
  let loading = false;

  async function ensureIndex() {
    if (index || loading) return;
    loading = true;
    try {
      const res = await fetch('/search-index.json', { cache: 'force-cache' });
      index = await res.json();
    } catch (e) {
      console.error('search index load failed', e);
    } finally {
      loading = false;
    }
  }

  function tokenize(s) {
    return s.toLowerCase().split(/\s+/).filter(Boolean);
  }

  function score(entry, tokens) {
    // Higher = better match. Simple substring scoring on title and tags.
    const hay = (entry.title + ' ' + (entry.tags || '')).toLowerCase();
    let s = 0;
    for (const t of tokens) {
      if (!hay.includes(t)) return 0;
      if (entry.title.toLowerCase().startsWith(t)) s += 5;
      if (entry.title.toLowerCase().includes(t)) s += 3;
      if ((entry.tags || '').toLowerCase().includes(t)) s += 1;
    }
    // Prefer SaaS/OSS pages over comparison pages.
    if (entry.type === 'saas' || entry.type === 'oss') s += 2;
    return s;
  }

  function render(results) {
    if (!results.length) {
      resultsEl.innerHTML = '<div class="search-empty">No matches</div>';
      resultsEl.hidden = false;
      return;
    }
    const html = results.slice(0, 10).map(r =>
      '<a class="search-item" href="' + r.url + '">' +
        '<div class="search-item-title">' + escapeHtml(r.title) + '</div>' +
        '<div class="search-item-type">' + escapeHtml(r.typeLabel || r.type) + '</div>' +
      '</a>'
    ).join('');
    resultsEl.innerHTML = html;
    resultsEl.hidden = false;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]
    );
  }

  function runSearch() {
    const q = input.value.trim();
    if (!q) {
      resultsEl.hidden = true;
      return;
    }
    if (!index) return;
    const tokens = tokenize(q);
    const scored = index.map(e => ({ e, s: score(e, tokens) })).filter(x => x.s > 0);
    scored.sort((a, b) => b.s - a.s);
    render(scored.map(x => x.e));
  }

  input.addEventListener('focus', ensureIndex);
  input.addEventListener('input', function () {
    if (!index) { ensureIndex().then(runSearch); return; }
    runSearch();
  });

  // Close results on outside click
  document.addEventListener('click', (e) => {
    if (!resultsEl.contains(e.target) && e.target !== input) {
      resultsEl.hidden = true;
    }
  });
  input.addEventListener('focus', () => {
    if (input.value.trim()) resultsEl.hidden = false;
  });

  // Keyboard navigation
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      input.value = '';
      resultsEl.hidden = true;
    } else if (e.key === 'Enter') {
      const first = resultsEl.querySelector('.search-item');
      if (first) {
        e.preventDefault();
        window.location.href = first.getAttribute('href');
      }
    }
  });
})();
