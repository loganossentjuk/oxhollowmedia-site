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

/* ── Frame preview ──
   A frame swatch with data-preview (Gelato's mockup of this print in that
   frame, from prints/catalog.json "previews") swaps the page photo to it;
   "No frame" swaps back to the photo itself. */
(() => {
  const img = document.querySelector('.detail-frame img');
  const source = document.querySelector('.detail-frame source');
  if (!img) return;
  const original = { src: img.getAttribute('src'), srcset: source ? source.srcset : '' };
  const show = (url) => {
    const back = !url || url === original.src;
    if (source) source.srcset = back ? original.srcset : '';
    img.src = back ? original.src : url;
  };
  if (!document.querySelector('.frame-radio[data-preview]')) return;
  // A frame with no mockup yet shows the photo itself.
  document.querySelectorAll('.frame-radio').forEach((r) => {
    r.addEventListener('change', () => { if (r.checked) show(r.dataset.preview); });
  });
  // Switching material shows that material's checked frame (or the photo).
  document.querySelectorAll('.mat-radio').forEach((r) => {
    r.addEventListener('change', () => {
      const panel = document.querySelectorAll('.mat-panel')[[...document.querySelectorAll('.mat-radio')].indexOf(r)];
      const picked = panel && panel.querySelector('.frame-radio:checked');
      show(picked ? picked.dataset.preview : '');
    });
  });
  const first = document.querySelector('.mat-radio:checked');
  if (first) first.dispatchEvent(new Event('change'));
})();
