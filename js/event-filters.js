/* ── Event photo categories on /events: Candids / Portraits / Atmosphere ──
   Each frame carries data-sub; the chip row shows one category at a time. */
(() => {
  const bar  = document.getElementById('event-filters');
  const grid = document.getElementById('event-grid');
  if (!bar || !grid) return;

  const items = Array.from(grid.querySelectorAll('.masonry-item'));

  bar.addEventListener('click', (e) => {
    const chip = e.target.closest('.filter-chip[data-sub]');
    if (!chip) return;
    const sub = chip.dataset.sub;
    bar.querySelectorAll('.filter-chip').forEach((c) => {
      c.classList.toggle('active', c === chip);
      c.setAttribute('aria-pressed', c === chip ? 'true' : 'false');
    });
    items.forEach((item) => {
      item.classList.toggle('is-hidden', sub !== 'all' && item.dataset.sub !== sub);
    });
  });
})();
