/* Print shop: headings rise, each wall of frames steps in, and the pinned
   subject bar marks the section on screen. All additive. */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasIO = 'IntersectionObserver' in window;
  if (!reduced && hasIO) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll('.pshop h1, .pshop .print-section h2, .pshop #print-info h2').forEach((h) => {
      h.innerHTML = h.innerHTML.split(/<br\s*\/?>/i).map((l) => '<span class="ln"><span class="ln-i">' + l.trim() + '</span></span>').join('');
      h.classList.add('rise');
      io.observe(h);
    });
    document.querySelectorAll('.pshop .print-grid').forEach((g) => {
      [...g.children].forEach((c, i) => c.style.setProperty('--i', Math.min(i, 8)));
      g.classList.add('will-rise');
      io.observe(g);
    });
  }
  // Subject bar: light the chip for the section in view.
  const chips = [...document.querySelectorAll('.print-jump-bar .filter-chip')];
  const secs = chips.map((c) => document.querySelector(c.getAttribute('href'))).filter(Boolean);
  if (!chips.length || !secs.length) return;
  let ticking = false;
  const spy = () => {
    ticking = false;
    const line = innerHeight * 0.35;
    let on = null;
    secs.forEach((s) => { if (s.getBoundingClientRect().top <= line) on = s.id; });
    chips.forEach((c) => {
      const hit = c.getAttribute('href') === '#' + on;
      c.classList.toggle('is-on', hit);
      if (hit && c.scrollIntoView && c.parentElement.scrollWidth > c.parentElement.clientWidth) {
        c.parentElement.scrollTo({ left: c.offsetLeft - 20, behavior: reduced ? 'auto' : 'smooth' });
      }
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(spy); } }, { passive: true });
  spy();
})();

/* Gallery-walk version: arrows to move along each wall. */
(() => {
  if (!document.body.classList.contains('pgal')) return;
  document.querySelectorAll('.pgal .print-grid').forEach((g) => {
    const nav = document.createElement('div');
    nav.className = 'wall-nav';
    nav.innerHTML = '<button type="button" class="wall-btn" data-dir="-1" aria-label="Previous prints">&larr;</button><button type="button" class="wall-btn" data-dir="1" aria-label="Next prints">&rarr;</button>';
    g.after(nav);
    const sync = () => {
      nav.querySelector('[data-dir="-1"]').disabled = g.scrollLeft < 8;
      nav.querySelector('[data-dir="1"]').disabled = g.scrollLeft > g.scrollWidth - g.clientWidth - 8;
    };
    nav.addEventListener('click', (e) => {
      const b = e.target.closest('.wall-btn'); if (!b) return;
      g.scrollBy({ left: Number(b.dataset.dir) * g.clientWidth * 0.8, behavior: 'smooth' });
    });
    g.addEventListener('scroll', sync, { passive: true });
    addEventListener('resize', sync); sync();
  });
})();
