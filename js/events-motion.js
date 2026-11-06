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

  /* ── 3. What I photograph: the four cards rise in one after another ── */
  const cards = document.querySelector('.aud-cards');
  if (cards && !reduced && hasIO) {
    cards.classList.add('will-rise');
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { cards.classList.add('is-in'); cio.disconnect(); } });
    }, { threshold: 0.15 });
    cio.observe(cards);
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

  /* ── 6. Recent events filmstrip ──
     With motion on, the section pins and scrolling down slides the strip
     sideways (like the homepage flight lines). With reduced motion it stays a
     normal sideways-scrolling row. */
  const strip = document.getElementById('event-grid');
  const sec = document.getElementById('highlights');
  if (strip && sec && strip.classList.contains('filmstrip')) {
    const bar = document.querySelector('.strip-bar span');
    const pin = sec.querySelector('.container');
    const btns = document.querySelectorAll('.strip-btn');
    const filters = document.getElementById('event-filters');

    if (!reduced) {
      sec.classList.add('pinned');
      const SPEED = innerWidth <= 600 ? 2.5 : 3.5;   // px of sideways travel per px scrolled
      let travel = 0, start = 0, len = 1, target = 0, drawn = 0, running = false;

      const visible = () => [...strip.children].filter((c) => c.offsetParent !== null);
      const layout = () => {
        sec.style.height = '';
        const items = visible();
        const last = items[items.length - 1];
        const left = strip.getBoundingClientRect().left;
        const end = last ? last.offsetLeft + last.offsetWidth : 0;
        const pad = innerWidth <= 600 ? 20 : 40;
        travel = Math.max(0, end - (innerWidth - left) + pad);
        const top = Math.max(parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-h')) || 72,
                             (innerHeight - pin.offsetHeight) / 2);
        pin.style.top = top + 'px';
        const base = sec.offsetHeight;
        len = Math.max(1, travel / SPEED);
        sec.style.height = (base + len) + 'px';
        start = sec.getBoundingClientRect().top + scrollY + parseFloat(getComputedStyle(sec).paddingTop) - top;
        if (bar) bar.style.setProperty('--w', (100 * (innerWidth - left) / (innerWidth - left + travel)).toFixed(2) + '%');
        update();
      };
      const progress = () => clamp((scrollY - start) / len, 0, 1);
      const draw = () => {
        strip.style.transform = 'translate3d(' + (-drawn * travel).toFixed(1) + 'px,0,0)';
        if (bar) {
          const w = parseFloat(bar.style.getPropertyValue('--w')) || 20;
          bar.style.setProperty('--l', (drawn * (100 - w)).toFixed(2) + '%');
        }
      };
      const tick = () => {
        drawn += (target - drawn) * 0.12;
        if (Math.abs(target - drawn) < 0.0005) { drawn = target; running = false; draw(); return; }
        draw();
        requestAnimationFrame(tick);
      };
      const update = () => { target = progress(); if (!running) { running = true; requestAnimationFrame(tick); } };

      addEventListener('scroll', update, { passive: true });
      addEventListener('resize', layout);
      addEventListener('load', layout);
      layout();

      // Arrows move the page, so the strip follows.
      btns.forEach((b) => b.addEventListener('click', () => {
        const step = (innerWidth * 0.6) / Math.max(1, travel) * len;
        scrollTo({ top: clamp(scrollY + Number(b.dataset.dir) * step, start, start + len), behavior: 'smooth' });
      }));
      // Keyboard: arrow keys on the focused strip do the same.
      strip.addEventListener('keydown', (e) => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        e.preventDefault();
        btns[e.key === 'ArrowRight' ? 1 : 0].click();
      });
      // A filter changes the strip's length: re-measure and go back to its start.
      if (filters) filters.addEventListener('click', () => requestAnimationFrame(() => {
        layout();
        if (scrollY > start) scrollTo({ top: start, behavior: 'auto' });
        drawn = target = progress(); draw();
      }));
      return;
    }

    // Reduced motion: plain sideways scrolling with arrows and a progress bar.
    const paint = () => {
      const max = strip.scrollWidth;
      if (bar && max) {
        bar.style.setProperty('--w', (strip.clientWidth / max * 100).toFixed(2) + '%');
        bar.style.setProperty('--l', (strip.scrollLeft / max * 100).toFixed(2) + '%');
      }
    };
    strip.addEventListener('scroll', paint, { passive: true });
    addEventListener('resize', paint);
    paint();
    btns.forEach((b) => b.addEventListener('click', () => {
      strip.scrollBy({ left: Number(b.dataset.dir) * strip.clientWidth * 0.75 });
    }));
    if (filters) filters.addEventListener('click', () => { strip.scrollLeft = 0; paint(); });
  }
})();
