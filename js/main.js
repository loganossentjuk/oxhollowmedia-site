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

/* ── GA4 events (gtag is loaded in each page's <head>) ──
   Never send names, emails or messages: only print, size, price and the
   form's dropdown answers. https://support.google.com/analytics/answer/6366371 */
const ga = (...args) => { if (typeof gtag === 'function') gtag(...args); };
const SHOP_CART = /^https:\/\/[^/]+\.myshopify\.com\/cart\//;

/* Cart permalinks skip the Shopify storefront and open checkout, so a click
   is GA4's begin_checkout. Beacon transport survives the navigation.
   https://developers.google.com/analytics/devguides/collection/ga4/reference/events#begin_checkout */
document.addEventListener('click', (e) => {
  const a = e.target.closest && e.target.closest('a');
  if (!a || !SHOP_CART.test(a.href)) return;
  const text = (sel) => (a.querySelector(sel)?.textContent || '').trim();
  const price = parseFloat(text('.price, strong').replace(/[^0-9.]/g, ''));
  const size = a.dataset.size?.replace('x', '×') || text('.size, span').replace(/^Buy\s+/, '').replace(/″$/, '');
  const mat = a.closest('[data-mat]')?.dataset.mat;
  const frame = a.closest('[data-frame]')?.dataset.frame;
  const item = {
    item_id: a.href.match(/\/cart\/(\d+)/)?.[1],
    item_name: (document.querySelector('.detail-title, .lb-title')?.textContent || '').trim() || a.dataset.product,
    item_variant: [size, mat, frame].filter(Boolean).join(' / '),
    quantity: 1,
  };
  const params = { currency: 'USD', items: [item], transport_type: 'beacon' };
  if (price > 0) { params.value = price; item.price = price; }
  ga('event', 'begin_checkout', params);
});

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
  // GA4 event names allow only letters, digits and underscores.
  // https://support.google.com/analytics/answer/13316687
  ga('event', name.toLowerCase().replace(/\s+/g, '_'), props || {});
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
  } else if (a.dataset.product && !SHOP_CART.test(a.href)) { // Shopify: begin_checkout above
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
        // Dropdown answers only; never the name, email or message.
        // https://developers.google.com/analytics/devguides/collection/ga4/reference/events#generate_lead
        ga('event', 'generate_lead', {
          lead_source: form.elements.heard_about?.value || '(not set)',
          budget: form.elements.budget?.value,
          project: form.elements.project?.value,
        });
        if (window.plausible) window.plausible('Contact Form Submit');
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
