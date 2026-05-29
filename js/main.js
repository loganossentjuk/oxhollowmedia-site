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

const openDrawer  = () => { drawer.classList.add('open'); overlay.classList.add('active'); };
const closeDrawer = () => { drawer.classList.remove('open'); overlay.classList.remove('active'); };

toggle.addEventListener('click', openDrawer);
close.addEventListener('click', closeDrawer);
overlay.addEventListener('click', closeDrawer);
drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', closeDrawer));

/* ── Footer year ── */
document.getElementById('year').textContent = new Date().getFullYear();

/* ── Contact form via Formspree ── */
const form   = document.querySelector('.contact-form');
const status = document.getElementById('form-status');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    status.textContent = 'Sending…';
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
      });
      if (res.ok) {
        status.textContent = 'Message sent — we\'ll be in touch soon.';
        form.reset();
      } else {
        status.textContent = 'Something went wrong. Please email us directly.';
      }
    } catch {
      status.textContent = 'Network error. Please try again.';
    }
  });
}

/* ── Fade-in on scroll ── */
const fadeEls = document.querySelectorAll('.service-card, .work-card, .about-grid, .contact-grid');
const io = new IntersectionObserver(
  (entries) => entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } }),
  { threshold: 0.1 }
);
fadeEls.forEach(el => { el.classList.add('fade-in'); io.observe(el); });
