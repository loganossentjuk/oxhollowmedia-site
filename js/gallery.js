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

  filterBar.addEventListener('click', (e) => {
    const chip = e.target.closest('.filter-chip');
    if (!chip) return;
    filterBar.querySelectorAll('.filter-chip').forEach((c) => c.classList.remove('active'));
    chip.classList.add('active');
    applyFilter(chip.dataset.filter);
  });
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
