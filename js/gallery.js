/* ── Gallery category filter ── */
const filterBar = document.getElementById('filters');
const grid      = document.getElementById('gallery-grid');
const emptyMsg  = document.getElementById('gallery-empty');

if (filterBar && grid) {
  const items = Array.from(grid.querySelectorAll('.masonry-item'));

  const applyFilter = (cat) => {
    let shown = 0;
    items.forEach((item) => {
      const match = cat === 'all' || item.dataset.cat === cat;
      item.classList.toggle('is-hidden', !match);
      if (match) shown++;
    });
    emptyMsg.style.display = shown === 0 ? 'block' : 'none';
  };

  const selectChip = (chip) => {
    filterBar.querySelectorAll('.filter-chip').forEach((c) => {
      c.classList.toggle('active', c === chip);
      c.setAttribute('aria-pressed', c === chip ? 'true' : 'false');
    });
    applyFilter(chip.dataset.filter);
  };

  filterBar.addEventListener('click', (e) => {
    const chip = e.target.closest('.filter-chip');
    if (!chip) return;
    selectChip(chip);
  });

  /* Deep-linkable filters: /gallery#events preselects the Events chip
     (linked from the corporate landing page and Work With Me). */
  const hash = (location.hash || '').replace('#', '');
  if (hash && hash !== 'films') {
    const chip = filterBar.querySelector(`.filter-chip[data-filter="${hash}"]`);
    if (chip) selectChip(chip);
  }
}

/* ── Visible frame titles (buyer feedback: titles were hover-only) ── */
document.querySelectorAll('#gallery-grid .masonry-item').forEach((item) => {
  const t = item.querySelector('.cap-title');
  const c = item.querySelector('.cap-cat');
  if (!t) return;
  const line = document.createElement('span');
  line.className = 'frame-title';
  line.textContent = t.textContent;
  if (c) {
    const cat = document.createElement('span');
    cat.className = 'frame-cat';
    cat.textContent = c.textContent;
    line.appendChild(cat);
  }
  item.appendChild(line);
});
