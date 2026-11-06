/* About, Contact and Films pages: headings rise line by line and the name equation steps in. */
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { threshold: 0.2 });
  document.querySelectorAll(':is(.abt, .cnt, .flm) h1, :is(.abt, .cnt, .flm) section h2').forEach((h) => {
    const lines = h.innerHTML.split(/<br\s*\/?>/i);
    h.innerHTML = lines.map((l) => '<span class="ln"><span class="ln-i">' + l.trim() + '</span></span>').join('');
    h.classList.add('rise');
    io.observe(h);
  });
  document.querySelectorAll('.craft-grid, .contact-form, .flm .film-row').forEach((g) => { g.classList.add('will-rise'); io.observe(g); });
  const eq = document.querySelector('.name-eq');
  if (eq) { eq.classList.add('will-rise'); io.observe(eq); }
})();
