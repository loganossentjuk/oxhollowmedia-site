/* ══════════════════════════════════════════════════════════════════════════
   Events page motion: headings that rise line by line, the "What I
   photograph" word list that swaps its photo, the terracotta line under
   "How it works", and the Recent events filmstrip. Everything here is
   additive: without this file the page reads the same, just still.
   ══════════════════════════════════════════════════════════════════════════ */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasIO = 'IntersectionObserver' in window;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* ── 2. Headings rise line by line ── */
  if (!reduced && hasIO) {
    const heads = document.querySelectorAll('.ev .page-hero h1, .ev main section h2, .ev section h2');
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.2 });
    heads.forEach((h) => {
      if (h.classList.contains('rise')) return;
      const lines = h.innerHTML.split(/<br\s*\/?>/i);
      h.innerHTML = lines.map((l) => '<span class="ln"><span class="ln-i">' + l.trim() + '</span></span>').join('');
      h.classList.add('rise');
      io.observe(h);
    });
  }

  /* ── 3. What I photograph: the active word picks the photo ── */
  const aud = document.querySelector('.aud');
  if (aud) {
    const rows = [...aud.querySelectorAll('.aud-row')];
    const photos = [...aud.querySelectorAll('.aud-photo')];
    const frame = aud.querySelector('.aud-frame');
    let current = 0;
    let hovering = false;
    const set = (i) => {
      if (i === current) return;
      current = i;
      rows.forEach((r, k) => r.classList.toggle('is-active', k === i));
      photos.forEach((p, k) => p.classList.toggle('is-active', k === i));
    };
    rows.forEach((r, i) => {
      r.addEventListener('mouseenter', () => { hovering = true; set(i); });
      r.addEventListener('mouseleave', () => { hovering = false; });
      r.addEventListener('focusin', () => set(i));
      r.addEventListener('click', () => set(i));
    });
    // Scrolling also walks the list: the row nearest the reading line is active.
    const onScroll = () => {
      if (hovering) return;
      const stacked = getComputedStyle(aud).gridTemplateColumns.split(' ').length === 1;
      const line = stacked ? frame.getBoundingClientRect().bottom + 90 : innerHeight * 0.5;
      let best = current, dist = Infinity;
      rows.forEach((r, i) => {
        const b = r.getBoundingClientRect();
        const d = Math.abs((b.top + Math.min(b.height, 120) / 2) - line);
        if (d < dist) { dist = d; best = i; }
      });
      set(best);
    };
    addEventListener('scroll', onScroll, { passive: true });
  }

  /* ── 4. Rates count up the first time they come into view ── */
  if (!reduced && hasIO) {
    const fmt = (n) => '$' + Math.round(n).toLocaleString('en-US');
    const io2 = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        io2.unobserve(e.target);
        const el = e.target, to = Number(el.dataset.to), t0 = performance.now(), dur = 1100;
        const step = (t) => {
          const k = Math.min(1, (t - t0) / dur);
          el.textContent = fmt(to * (1 - Math.pow(1 - k, 3)));
          if (k < 1) requestAnimationFrame(step); else el.textContent = fmt(to);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('.pkg-num[data-to]').forEach((el) => io2.observe(el));
  }

  /* ── 5. How it works: the line draws as you scroll ── */
  const proc = document.getElementById('process');
  const line = proc && proc.querySelector('.step-line');
  if (proc && line && !reduced) {
    const cards = [...proc.querySelectorAll('.offer-card')];
    const update = () => {
      const r = proc.getBoundingClientRect();
      const p = clamp((innerHeight * 0.8 - r.top) / (r.height * 0.75), 0, 1);
      line.style.setProperty('--p', p.toFixed(3));
      cards.forEach((c, i) => c.classList.toggle('lit', p >= (i + 0.5) / cards.length - 0.06));
    };
    addEventListener('scroll', update, { passive: true });
    addEventListener('resize', update);
    update();
  }

  /* ── 6. Recent events filmstrip ── */
  const strip = document.getElementById('event-grid');
  if (strip && strip.classList.contains('filmstrip')) {
    const bar = document.querySelector('.strip-bar span');
    let ticking = false;

    const paint = () => {
      ticking = false;
      const max = strip.scrollWidth;
      if (bar && max) {
        bar.style.setProperty('--w', (strip.clientWidth / max * 100).toFixed(2) + '%');
        bar.style.setProperty('--l', (strip.scrollLeft / max * 100).toFixed(2) + '%');
      }
    };
    const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
    strip.addEventListener('scroll', req, { passive: true });
    addEventListener('resize', req);
    addEventListener('load', req);
    req();

    document.querySelectorAll('.strip-btn').forEach((b) => {
      b.addEventListener('click', () => {
        strip.scrollBy({ left: Number(b.dataset.dir) * strip.clientWidth * 0.75, behavior: reduced ? 'auto' : 'smooth' });
      });
    });

    // Filters reset the strip to the start.
    const filters = document.getElementById('event-filters');
    if (filters) filters.addEventListener('click', () => { strip.scrollLeft = 0; req(); });

    // Mouse drag (touch and trackpads scroll natively).
    let down = false, startX = 0, startLeft = 0, moved = false;
    strip.addEventListener('pointerdown', (e) => {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      down = true; moved = false; startX = e.clientX; startLeft = strip.scrollLeft;
    });
    addEventListener('pointermove', (e) => {
      if (!down) return;
      const dx = e.clientX - startX;
      if (!moved && Math.abs(dx) > 5) { moved = true; strip.classList.add('dragging'); }
      if (moved) strip.scrollLeft = startLeft - dx;
    });
    addEventListener('pointerup', () => {
      if (!down) return;
      down = false;
      strip.classList.remove('dragging');
    });
    // A drag shouldn't also open the photo it ended on.
    strip.addEventListener('click', (e) => { if (moved) { e.preventDefault(); moved = false; } }, true);
    strip.addEventListener('dragstart', (e) => e.preventDefault());
  }
})();
