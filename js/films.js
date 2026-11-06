/* Films: a poster (the film's opening frame) stands in for each player.
   Clicking it swaps in the Vimeo player and starts the film. Without JS the
   poster is a plain link to Vimeo. */
document.querySelectorAll('.film-poster[data-vimeo]').forEach((a) => {
  a.addEventListener('click', (e) => {
    e.preventDefault();
    const f = document.createElement('iframe');
    f.src = 'https://player.vimeo.com/video/' + a.dataset.vimeo + '?autoplay=1&title=0&portrait=0&byline=0&badge=0&controls=1';
    f.title = a.getAttribute('aria-label').replace(/^Play /, '');
    f.allow = 'autoplay; fullscreen; picture-in-picture';
    f.allowFullscreen = true;
    a.replaceWith(f);
  });
});
