/* ── Campaign tag on Shopify cart links ──
   A visit that lands with ?utm_campaign=... keeps it for the session
   (sessionStorage) and adds it to every Shopify cart permalink as ref=<campaign>,
   so the order shows where the buyer came from. No UTM, no change.
   https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks */
(() => {
  const KEY = 'ohm_ref';
  const clean = (v) => (v || '').replace(/[^A-Za-z0-9_-]/g, '').slice(0, 50);
  let ref = '';
  try { ref = clean(new URLSearchParams(location.search).get('utm_campaign')); } catch {}
  try {
    if (ref) sessionStorage.setItem(KEY, ref);
    else ref = clean(sessionStorage.getItem(KEY));
  } catch {}
  if (!ref) return;
  const CART = /^https:\/\/[^/]+\.myshopify\.com\/cart\//;
  const tag = (a) => {
    if (!a || !CART.test(a.href)) return;
    const u = new URL(a.href);
    if (u.searchParams.get('ref') === ref) return;
    u.searchParams.set('ref', ref);
    a.href = u.toString();
  };
  const tagAll = () => document.querySelectorAll('a[href*=".myshopify.com/cart/"]').forEach(tag);
  tagAll();
  // Links built later (gallery viewer) are tagged as they are clicked.
  ['click', 'auxclick', 'contextmenu'].forEach((t) =>
    document.addEventListener(t, (e) => tag(e.target.closest && e.target.closest('a')), true));
})();

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
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && drawer.classList.contains('open')) { closeDrawer(); toggle.focus(); } });
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
      status.textContent = 'Form not configured yet. Email oxhollowmedia@gmail.com.';
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
        status.textContent = 'Message sent. We\'ll be in touch soon.';
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
