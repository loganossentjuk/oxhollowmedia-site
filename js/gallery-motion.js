/* ══════════════════════════════════════════════════════════════════════════
   Gallery: nods to the homepage. The hero line's four phrases pick
   collections, a shutter closes and opens over the page when the collection
   changes, a terracotta line tracks the scroll, and a title card names the
   collection on view. Everything is additive: without this file the gallery
   filters exactly as before, with no shutter.
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
    ocean: 'Ocean', galapagos: 'Galápagos', abstracts: 'Salt and Stone', mountains: 'Mountains',
    forests: 'Forests', botanical: 'Botanical', urban: 'Urban', portraits: 'Portraits',
    events: 'Events', people: 'The people in between',
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

  /* ── 2. Shutter: seven curved blades close over the page, the collection
     swaps while it's shut, and they open again (the homepage intro's iris,
     scaled up to the window). ── */
  if (reduced) {
    window.oxShutter = (swap) => {
      const grid = document.getElementById('gallery-grid');
      grid.style.transition = 'opacity .25s'; grid.style.opacity = 0;
      setTimeout(() => { swap(); grid.style.opacity = 1; }, 250);
    };
    return;
  }

  const NS = 'http://www.w3.org/2000/svg';
  const N = 7;
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('class', 'shutter');
  svg.setAttribute('aria-hidden', 'true');
  const defs = document.createElementNS(NS, 'defs');
  const lens = document.createElementNS(NS, 'clipPath');
  lens.id = 'gal-lens';
  const lensC = document.createElementNS(NS, 'circle');
  lens.appendChild(lensC); defs.appendChild(lens);
  const iris = document.createElementNS(NS, 'g');
  iris.setAttribute('clip-path', 'url(#gal-lens)');
  const masks = [], fills = [], edges = [];
  for (let i = 0; i < N; i++) {
    const m = document.createElementNS(NS, 'mask');
    m.id = 'gal-b' + i;
    m.setAttribute('maskUnits', 'userSpaceOnUse');
    const self = document.createElementNS(NS, 'circle'); self.setAttribute('fill', '#fff');
    const next = document.createElementNS(NS, 'circle'); next.setAttribute('fill', '#000');
    m.append(self, next); defs.appendChild(m); masks.push([m, self, next]);
    const g = document.createElementNS(NS, 'g'); g.setAttribute('mask', 'url(#gal-b' + i + ')');
    const f = document.createElementNS(NS, 'circle'); f.setAttribute('fill', i % 2 ? '#2B4535' : '#294132');
    const e = document.createElementNS(NS, 'circle'); e.setAttribute('fill', 'none');
    e.setAttribute('stroke', '#F4EEE2'); e.setAttribute('stroke-opacity', '.55'); e.setAttribute('stroke-width', '1.5');
    g.append(f, e); iris.appendChild(g); fills.push(f); edges.push(e);
  }
  svg.append(defs, iris);
  document.body.appendChild(svg);

  let W = 0, H = 0, R = 0;
  const size = () => {
    W = innerWidth; H = innerHeight; R = Math.hypot(W, H) / 2 + 4;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    lensC.setAttribute('cx', W / 2); lensC.setAttribute('cy', H / 2); lensC.setAttribute('r', R);
    masks.forEach(([m]) => { m.setAttribute('x', -3 * R); m.setAttribute('y', -3 * R); m.setAttribute('width', W + 6 * R); m.setAttribute('height', H + 6 * R); });
  };
  const draw = (gap, turn) => {
    // Each blade is a big disc set off to one side of the lens; its edge sweeps across as an arc.
    const RHO = R * 1.55, T = RHO * 0.62;
    const reach = Math.sqrt(Math.max(0, (RHO + gap) ** 2 - T * T));
    const C = Array.from({ length: N }, (_, i) => {
      const a = turn + i * 2 * Math.PI / N, ux = Math.cos(a), uy = Math.sin(a);
      return [W / 2 + reach * ux - T * uy, H / 2 + reach * uy + T * ux];
    });
    const put = (el, c) => { el.setAttribute('cx', c[0].toFixed(1)); el.setAttribute('cy', c[1].toFixed(1)); el.setAttribute('r', RHO.toFixed(1)); };
    for (let i = 0; i < N; i++) {
      put(masks[i][1], C[i]); put(masks[i][2], C[(i + 1) % N]);
      put(fills[i], C[i]); put(edges[i], C[(i + 1) % N]);
    }
  };
  const tween = (from, to, ms, ease, step) => new Promise((done) => {
    const t0 = performance.now();
    const f = (t) => {
      const k = clamp((t - t0) / ms, 0, 1);
      step(from + (to - from) * ease(k));
      if (k < 1) requestAnimationFrame(f); else done();
    };
    requestAnimationFrame(f);
  });
  const easeIn = (k) => k * k * k, easeOut = (k) => 1 - (1 - k) ** 3;

  let busy = false;
  window.oxShutter = async (swap) => {
    if (busy) { swap(); return; }
    busy = true;
    size();
    draw(R, 0);
    svg.classList.add('is-on');
    await tween(0, 1, 380, easeIn, (k) => draw(R * (1 - k), -0.9 * k));
    swap();
    await new Promise((r) => setTimeout(r, 120));
    await tween(0, 1, 520, easeOut, (k) => draw(R * k, -0.9 - 1.1 * k));
    svg.classList.remove('is-on');
    busy = false;
  };
})();
