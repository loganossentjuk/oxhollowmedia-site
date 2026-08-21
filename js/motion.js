/* ══════════════════════════════════════════════════════════════════════════
   Motion — hand-rolled, no dependencies.

   Four effects: weighted scroll, hero slideshow, nav label swap, and reveal
   on scroll. Each one is additive: if this file fails to load or throws, the
   site falls back to its pre-motion behaviour rather than breaking.
   ══════════════════════════════════════════════════════════════════════════ */

const REDUCED = matchMedia('(prefers-reduced-motion: reduce)');

/* ── Weighted scroll ───────────────────────────────────────────────────────
   Lerps the window toward a wheel-driven target so momentum carries past the
   gesture. Desktop pointers only: touch already has native momentum, and
   hijacking it there costs more than it gives. */
(() => {
  if (REDUCED.matches || !matchMedia('(pointer: fine)').matches) return;

  const EASE = 0.085;          // lower = heavier
  let target = window.scrollY;
  let current = target;
  let frame = null;
  let driving = false;         // true while we own the scroll position

  const limit = () => document.documentElement.scrollHeight - window.innerHeight;

  // Wheel deltas arrive in pixels, lines, or pages depending on the device.
  const toPixels = (e) => {
    if (e.deltaMode === 1) return e.deltaY * 16;
    if (e.deltaMode === 2) return e.deltaY * window.innerHeight;
    return e.deltaY;
  };

  const tick = () => {
    const gap = target - current;
    if (Math.abs(gap) < 0.5) {
      current = target;
      window.scrollTo(0, current);
      frame = null;
      driving = false;
      return;
    }
    current += gap * EASE;
    window.scrollTo(0, current);
    frame = requestAnimationFrame(tick);
  };

  window.addEventListener('wheel', (e) => {
    if (e.ctrlKey) return;                                  // pinch-zoom
    // e.target is not always an Element (document, or a text node), and calling
    // closest() on those throws — which would kill scrolling outright.
    const el = e.target instanceof Element ? e.target : null;
    if (el && el.closest('.nav-drawer, [data-native-scroll]')) return;
    e.preventDefault();
    target = Math.min(Math.max(target + toPixels(e), 0), limit());
    driving = true;
    if (!frame) frame = requestAnimationFrame(tick);
  }, { passive: false });

  /* Anything that scrolls by other means — keyboard, anchor jumps, find-in-page,
     focus — moves the window directly. Resync so the next wheel event starts
     from where the page actually is instead of snapping back. */
  window.addEventListener('scroll', () => {
    if (driving) return;
    target = current = window.scrollY;
  }, { passive: true });

  window.addEventListener('resize', () => {
    target = current = window.scrollY;
  }, { passive: true });
})();

/* ── Hero slideshow ───────────────────────────────────────────────────────*/
(() => {
  const media = document.querySelector('#hero .hero-media');
  if (!media) return;

  const slides = [...media.querySelectorAll('.hero-slide')];
  if (slides.length < 2) return;

  const dots = [...document.querySelectorAll('.hero-dot')];
  const DWELL = 6000;
  let index = 0;
  let timer = null;

  // The base layer's own background would show through the cross-fade.
  media.classList.add('has-slides');

  const show = (next) => {
    index = (next + slides.length) % slides.length;
    slides.forEach((s, i) => s.classList.toggle('is-active', i === index));
    dots.forEach((d, i) => {
      d.classList.toggle('is-active', i === index);
      d.setAttribute('aria-pressed', i === index ? 'true' : 'false');
    });
  };

  const start = () => {
    if (REDUCED.matches) return;
    stop();
    timer = setInterval(() => show(index + 1), DWELL);
  };
  const stop = () => { if (timer) { clearInterval(timer); timer = null; } };

  show(0);
  document.documentElement.style.setProperty('--hero-dwell', DWELL + 'ms');

  dots.forEach((dot, i) => dot.addEventListener('click', () => { show(i); start(); }));

  // Don't burn frames cross-fading a hero nobody is looking at.
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));
  REDUCED.addEventListener('change', () => (REDUCED.matches ? stop() : start()));

  start();
})();

/* ── Nav label swap ───────────────────────────────────────────────────────
   Built at runtime so the HTML stays a single clean label per link — no
   duplicated text for screen readers to read twice, and no effect at all if
   this script never runs. */
(() => {
  const links = document.querySelectorAll('.nav-links a, .footer-social a');
  links.forEach((a) => {
    if (a.querySelector('.swap-in') || a.children.length) return;   // leave icon links alone
    const label = a.textContent.trim();
    if (!label) return;
    a.dataset.label = label;
    a.innerHTML = '<span class="swap-in">' + label + '</span>';
    a.classList.add('swap');
  });
})();

/* ── Reveal on scroll ─────────────────────────────────────────────────────
   Staggered by position within the item's own group, so a row of tiles
   cascades instead of arriving as one block. */
(() => {
  const SELECTOR = [
    '.statement-block', '.offer-card', '.masonry-item', '.about-grid',
    '.contact-grid', '.highlights-head', '.film-row', '.follow-links',
    '.newsletter-inner', '#films-cta .container',
  ].join(', ');

  const els = [...document.querySelectorAll(SELECTOR)];
  if (!els.length) return;

  /* .reveal starts at opacity 0, so it must only ever be applied when something
     is guaranteed to clear it. No observer, or reduced motion, means no hiding. */
  if (REDUCED.matches || !('IntersectionObserver' in window)) {
    els.forEach((el) => el.classList.add('reveal', 'is-in'));
    return;
  }

  const seen = new WeakMap();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      el.style.transitionDelay = (seen.get(el) || 0) + 'ms';
      el.classList.add('is-in');
      io.unobserve(el);
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -6% 0px' });

  els.forEach((el) => {
    el.classList.add('reveal');
    // Index within the parent caps the cascade so long grids don't crawl.
    const peers = [...el.parentElement.children].filter((c) => c.matches(SELECTOR));
    seen.set(el, Math.min(peers.indexOf(el), 5) * 70);
    io.observe(el);
  });
})();
