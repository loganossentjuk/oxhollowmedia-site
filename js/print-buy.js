/* ── Print buy buttons ──
   Each .buy-btn starts as an enquiry link. Once scripts/make_stripe_links.py
   has written a checkout URL for "<slug>|<size>" into /stripe-links.json, the
   button points straight at Stripe checkout instead. A missing file or entry
   leaves the enquiry link in place, so a button is never dead. */
(() => {
  const buttons = document.querySelectorAll('.buy-btn[data-slug][data-size]');
  if (!buttons.length) return;
  fetch('/stripe-links.json', { cache: 'no-cache' })
    .then((r) => (r.ok ? r.json() : {}))
    .then((links) => {
      buttons.forEach((b) => {
        const url = (links || {})[`${b.dataset.slug}|${b.dataset.size}`];
        if (url) { b.href = url; b.classList.remove('is-pending'); }
      });
    })
    .catch(() => {});
})();
