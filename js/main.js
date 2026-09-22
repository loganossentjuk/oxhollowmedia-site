/* ── Nav: add scrolled class ── */
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

/* ── Mobile drawer ── */
const toggle  = document.querySelector('.nav-toggle');
const drawer  = document.getElementById('drawer');
const overlay = document.getElementById('overlay');
const close   = document.querySelector('.drawer-close');

const openDrawer  = () => { drawer.classList.add('open'); overlay.classList.add('active'); toggle.setAttribute('aria-expanded', 'true'); };
const closeDrawer = () => { drawer.classList.remove('open'); overlay.classList.remove('active'); toggle.setAttribute('aria-expanded', 'false'); };

toggle.setAttribute('aria-expanded', 'false');
toggle.setAttribute('aria-controls', 'drawer');
toggle.addEventListener('click', openDrawer);
close.addEventListener('click', closeDrawer);
overlay.addEventListener('click', closeDrawer);
drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', closeDrawer));

/* ── Footer year ── */
document.getElementById('year').textContent = new Date().getFullYear();

/* ── Conversion event tracking (analytics-agnostic) ──
   Fires to Plausible and/or GA4 if either is installed; no-ops otherwise.
   Works the moment an analytics tag is added — no further code needed. */
function track(name, props) {
  if (window.plausible) window.plausible(name, { props: props || {} });
  if (window.gtag) window.gtag('event', name, props || {});
}
document.addEventListener('click', (e) => {
  const a = e.target.closest('a, button');
  if (!a) return;
  const href = a.getAttribute('href') || '';
  if (href.startsWith('mailto:')) {
    const isOrder = /subject=Print%20order/i.test(href);
    track(isOrder ? 'Print Order Click' : 'Email Click', { product: a.dataset.product || undefined });
  } else if (href.startsWith('tel:')) {
    track('Phone Click');
  } else if (a.dataset.product) {
    track('Buy Button Click', { product: a.dataset.product, size: a.dataset.size || undefined });
  } else if (a.dataset.cta) {
    track('CTA Click', { cta: a.dataset.cta });
  }
});

/* ── Contact form via Formspree ── */
const form   = document.querySelector('.contact-form');
const status = document.getElementById('form-status');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (form.action.includes('YOUR_FORM_ID')) {
      status.textContent = 'Form not configured yet — email oxhollowmedia@gmail.com.';
      return;
    }
    status.textContent = 'Sending…';
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
      });
      if (res.ok) {
        status.textContent = 'Message sent — we\'ll be in touch soon.';
        track('Contact Form Submit');
        form.reset();
      } else {
        status.textContent = 'Something went wrong. Please email us directly.';
      }
    } catch {
      status.textContent = 'Network error. Please try again.';
    }
  });
}

/* Reveal-on-scroll lives in motion.js. */
