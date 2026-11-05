/* ══════════════════════════════════════════════════════════════════════════
   Gallery: nods to the homepage. The hero line's four phrases pick
   collections, a terracotta line tracks the scroll, and a title card names the
   collection on view. Everything is additive: without this file the gallery
   filters exactly as before.
   ══════════════════════════════════════════════════════════════════════════ */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* ── Title rises line by line ── */
  const title = document.querySelector('.gallery-title');
  if (title && !reduced) {
    title.innerHTML = '<span class="ln"><span class="ln-i">' + title.innerHTML + '</span></span>';
    title.classList.add('rise');
    requestAnimationFrame(() => requestAnimationFrame(() => title.classList.add('is-in')));
  }

  /* ── 1. The four phrases select collections ── */
  const lines = [...document.querySelectorAll('.line-link')];
  lines.forEach((b) => b.addEventListener('click', () => {
    if (window.oxGallery) window.oxGallery.select(b.dataset.line);
    const wrap = document.getElementById('gallery-wrap');
    if (wrap && wrap.getBoundingClientRect().top > innerHeight * 0.6) {
      setTimeout(() => wrap.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth' }), reduced ? 0 : 420);
    }
  }));

  /* ── 5. Title card for the collection on view ── */
  const card = document.getElementById('collection-card');
  const names = {
    ocean: 'Oceans', galapagos: 'Galápagos', abstracts: 'Salt and Stone', mountains: 'Mountains',
    forests: 'Forests', botanical: 'Botanical', urban: 'Urban', portraits: 'Portraits',
    events: 'Events', people: 'People',
  };
  document.addEventListener('gallery:filter', (e) => {
    const { cat, shown } = e.detail;
    lines.forEach((b) => b.classList.toggle('is-on', b.dataset.line === cat));
    if (!card) return;
    if (cat === 'all' || !names[cat]) { card.hidden = true; return; }
    card.querySelector('.cc-title').textContent = names[cat];
    card.querySelector('.cc-count').textContent = shown + (shown === 1 ? ' photograph' : ' photographs');
    card.hidden = false;
    card.classList.remove('is-in');
    void card.offsetWidth;
    card.classList.add('is-in');
  });

  // A deep link (/gallery#events) filtered before this file loaded: catch up.
  const pre = (location.hash || '').replace('#', '');
  if (names[pre]) {
    const shown = [...document.querySelectorAll('#gallery-grid .masonry-item')].filter((i) => !i.classList.contains('is-hidden')).length;
    document.dispatchEvent(new CustomEvent('gallery:filter', { detail: { cat: pre, shown } }));
  }

  /* ── 3. Terracotta line tracks the scroll ── */
  const bar = document.querySelector('.scroll-line span');
  if (bar) {
    let ticking = false;
    const paint = () => {
      ticking = false;
      const max = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? clamp(scrollY / max, 0, 1) : 0).toFixed(4) + ')';
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
    addEventListener('resize', paint);
    paint();
  }
})();
