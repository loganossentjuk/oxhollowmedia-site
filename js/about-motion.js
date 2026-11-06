/* About page: headings rise line by line and the name equation steps in. */
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { threshold: 0.2 });
  document.querySelectorAll('.abt h1, .abt main h2, .abt section h2').forEach((h) => {
    const lines = h.innerHTML.split(/<br\s*\/?>/i);
    h.innerHTML = lines.map((l) => '<span class="ln"><span class="ln-i">' + l.trim() + '</span></span>').join('');
    h.classList.add('rise');
    io.observe(h);
  });
  const eq = document.querySelector('.name-eq');
  if (eq) { eq.classList.add('will-rise'); io.observe(eq); }
})();
