/* ── Gallery category filter ── */
const filterBar = document.getElementById('filters');
const grid      = document.getElementById('gallery-grid');
const emptyMsg  = document.getElementById('gallery-empty');

if (filterBar && grid) {
  const items = Array.from(grid.querySelectorAll('.masonry-item'));

  // Candids / Portraits / Atmosphere row, shown only under the Events filter.
  const subBar = document.getElementById('event-filters');
  let currentCat = 'all';
  let sub = 'all';

  const applyFilter = (cat) => {
    currentCat = cat;
    let shown = 0;
    items.forEach((item) => {
      // Event coverage is client work, not part of the print collection, so it
      // stays out of the default view and only appears under its own filter.
      const match = cat === 'all'
        ? item.dataset.cat !== 'events'
        : item.dataset.cat === cat
          && (cat !== 'events' || sub === 'all' || item.dataset.sub === sub);
      item.classList.toggle('is-hidden', !match);
      if (match) shown++;
    });
    emptyMsg.style.display = shown === 0 ? 'block' : 'none';
    if (subBar) subBar.hidden = cat !== 'events';
  };

  if (subBar) {
    subBar.addEventListener('click', (e) => {
      const chip = e.target.closest('.filter-chip[data-sub]');
      if (!chip) return;
      sub = chip.dataset.sub;
      subBar.querySelectorAll('.filter-chip').forEach((c) => {
        c.classList.toggle('active', c === chip);
        c.setAttribute('aria-pressed', c === chip ? 'true' : 'false');
      });
      applyFilter(currentCat);
    });
  }

  const selectChip = (chip) => {
    filterBar.querySelectorAll('.filter-chip').forEach((c) => {
      c.classList.toggle('active', c === chip);
      c.setAttribute('aria-pressed', c === chip ? 'true' : 'false');
    });
    applyFilter(chip.dataset.filter);
  };

  filterBar.addEventListener('click', (e) => {
    // .chip-films links out to /films, not a category — it has no data-filter and
    // must not fall through to applyFilter(undefined), which would hide the grid.
    const chip = e.target.closest('.filter-chip[data-filter]');
    if (!chip) return;
    selectChip(chip);
  });

  /* Deep-linkable filters: /gallery#events preselects the Events chip
     (linked from the corporate landing page and Work With Me). */
  const hash = (location.hash || '').replace('#', '');
  const deepLinked = hash
    ? filterBar.querySelector(`.filter-chip[data-filter="${hash}"]`)
    : null;
  if (deepLinked) selectChip(deepLinked);
  else applyFilter('all');   // run once on load so events start hidden
}

/* ── Visible frame titles (buyer feedback: titles were hover-only) ── */
document.querySelectorAll('#gallery-grid .masonry-item').forEach((item) => {
  const t = item.querySelector('.cap-title');
  const c = item.querySelector('.cap-cat');
  if (!t) return;
  const line = document.createElement('span');
  line.className = 'frame-title';
  line.textContent = t.textContent;
  if (c) {
    const cat = document.createElement('span');
    cat.className = 'frame-cat';
    cat.textContent = c.textContent;
    line.appendChild(cat);
  }
  item.appendChild(line);
});

/* ── Frame size (S / M / L) ────────────────────────────────────────────────
   Changes the masonry column count. The choice sticks across pages and
   visits, since it's a browsing preference rather than a filter. */
(() => {
  const grid = document.getElementById('gallery-grid');
  const bar  = document.querySelector('.size-toggle');
  if (!grid || !bar) return;

  const SIZES = ['s', 'm', 'l'];
  const KEY = 'oxh-frame-size';

  const apply = (size) => {
    if (!SIZES.includes(size)) size = 'm';
    SIZES.forEach((s) => grid.classList.toggle('size-' + s, s === size));
    bar.querySelectorAll('.size-btn').forEach((b) => {
      b.setAttribute('aria-pressed', b.dataset.size === size ? 'true' : 'false');
    });
    try { localStorage.setItem(KEY, size); } catch { /* private mode */ }
  };

  bar.addEventListener('click', (e) => {
    const btn = e.target.closest('.size-btn');
    if (btn) apply(btn.dataset.size);
  });

  let saved = 'm';
  try { saved = localStorage.getItem(KEY) || 'm'; } catch { /* private mode */ }
  apply(saved);
})();

/* ── Lightbox: click a frame to view it large, step through with ‹ › ──────
   Steps through the frames the current filter shows, in grid order. Nature
   and urban frames carry size buttons that go straight to Stripe checkout
   (links from /stripe-links.json, made by scripts/make_stripe_links.py);
   until a link exists, a button falls back to the enquiry form with the
   print and size filled in. Events and portraits are client work: no buy. */
(() => {
  const grid = document.getElementById('gallery-grid');
  if (!grid) return;

  const SIZES = [
    { key: '8x12',  label: '8×12″',  price: 35 },
    { key: '12x18', label: '12×18″', price: 50 },
    { key: '16x24', label: '16×24″', price: 55 },
    { key: '24x36', label: '24×36″', price: 70 },
  ];
  const NOT_FOR_SALE = ['events', 'portraits'];
  const slugify = (t) => t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

  let links = {};
  fetch('/stripe-links.json', { cache: 'no-cache' })
    .then((r) => (r.ok ? r.json() : {}))
    .then((j) => { links = j || {}; })
    .catch(() => {});

  // Prints in the shop get a link to their page (/prints/<slug>) and the
  // shop's sizes; anything else falls back to SIZES above.
  let shopSizes = new Map();
  fetch('/prints/catalog.json', { cache: 'no-cache' })
    .then((r) => (r.ok ? r.json() : { prints: [] }))
    .then((c) => {
      // Only the sizes the print's file supports (long side x 150 ppi), as on its page.
      const fits = (p) => (z) => Math.max(...z.key.split('x').map(Number)) * 150 <= (p.source_px || 0);
      shopSizes = new Map((c.prints || []).map((p) => [p.slug, (c.sizes || SIZES).filter(fits(p))]));
    })
    .catch(() => {});

  const box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Photo viewer');
  box.hidden = true;
  box.innerHTML = `
    <button class="lb-close" aria-label="Close">✕</button>
    <button class="lb-nav lb-prev" aria-label="Previous photo">‹</button>
    <figure class="lb-stage">
      <picture><source type="image/webp"><img alt=""></picture>
    </figure>
    <button class="lb-nav lb-next" aria-label="Next photo">›</button>
    <div class="lb-info">
      <div class="lb-head">
        <h2 class="lb-title"></h2>
        <span class="lb-count"></span>
      </div>
      <div class="lb-buy">
        <p class="lb-spec">Archival matte paper · made to order · free US shipping</p>
        <div class="lb-sizes"></div>
        <a class="lb-page" hidden>Print details &amp; story →</a>
      </div>
    </div>`;
  document.body.appendChild(box);

  const $ = (s) => box.querySelector(s);
  const img = $('.lb-stage img'), src = $('.lb-stage source');
  let list = [], i = 0, lastFocus = null;

  const visible = () => Array.from(grid.querySelectorAll('.masonry-item:not(.is-hidden)'));

  const render = () => {
    const item = list[i];
    const pic = item.querySelector('img');
    const webp = item.querySelector('source');
    const cat = item.dataset.cat;
    // Event frames go untitled for visitors; we track them by data-ref (E01…).
    const title = cat === 'events'
      ? ''
      : (item.querySelector('.cap-title') || {}).textContent || pic.alt;

    src.srcset = webp ? webp.srcset : '';
    img.src = pic.currentSrc || pic.src;
    img.alt = pic.alt;
    $('.lb-title').textContent = title;
    $('.lb-count').textContent = `${i + 1} / ${list.length}`;

    const forSale = !NOT_FOR_SALE.includes(cat);
    $('.lb-buy').hidden = !forSale;
    const page = $('.lb-page');
    page.hidden = true;
    if (forSale) {
      const slug = slugify(title);
      if (shopSizes.has(slug)) { page.href = `/prints/${slug}`; page.hidden = false; }
      $('.lb-sizes').innerHTML = (shopSizes.get(slug) || SIZES).map((s) => {
        const url = links[`${slug}|${s.key}`];
        const href = url || `/contact?print=${encodeURIComponent(`${title} (${s.label})`)}`;
        return `<a class="lb-size" href="${href}" data-size="${s.key}" data-product="${slug}"${url ? ' data-checkout="stripe"' : ''}>`
             + `<span>${s.label}</span><strong>$${s.price}</strong></a>`;
      }).join('');
    }

    // Warm the neighbours so ‹ › feel instant.
    [list[i - 1], list[i + 1]].forEach((n) => {
      if (!n) return;
      const im = n.querySelector('img');
      if (im) { const p = new Image(); p.src = im.currentSrc || im.src; }
    });
    $('.lb-prev').disabled = list.length < 2;
    $('.lb-next').disabled = list.length < 2;
  };

  const open = (item) => {
    list = visible();
    i = Math.max(0, list.indexOf(item));
    lastFocus = document.activeElement;
    box.hidden = false;
    document.documentElement.classList.add('lb-open');
    render();
    $('.lb-close').focus();
  };
  const close = () => {
    box.hidden = true;
    document.documentElement.classList.remove('lb-open');
    if (lastFocus) lastFocus.focus();
  };
  const step = (d) => { i = (i + d + list.length) % list.length; render(); };

  grid.addEventListener('click', (e) => {
    const item = e.target.closest('.masonry-item');
    if (!item || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    e.preventDefault();
    open(item);
  });

  $('.lb-close').addEventListener('click', close);
  $('.lb-prev').addEventListener('click', () => step(-1));
  $('.lb-next').addEventListener('click', () => step(1));
  box.addEventListener('click', (e) => { if (e.target === box || e.target.classList.contains('lb-stage')) close(); });

  document.addEventListener('keydown', (e) => {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
    else if (e.key === 'Tab') {             // keep focus inside the viewer
      const f = Array.from(box.querySelectorAll('button:not([disabled]), a[href]')).filter((n) => n.offsetParent);
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  // Swipe on touch screens.
  let x0 = null;
  box.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) step(dx < 0 ? 1 : -1);
    x0 = null;
  });
})();
