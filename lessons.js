/* Resources page: the Fold on Tight thread.
   The posts are off by default; one button turns them on for the whole
   thread, and each is rendered by X's widget only as it scrolls into view.
   If X never loads, the lesson headings are still the content. */
(function () {
  var root = document.querySelector('.lessons');
  if (!root) return;
  var toggle = root.querySelector('.lessons-toggle');
  var items = root.querySelectorAll('.lessons-track > li[data-tweet]');
  if (!toggle || !items.length) return;

  var shown = false;
  var widgets = null;
  var io = null;

  function loadWidgets() {
    if (widgets) return widgets;
    widgets = new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.async = true;
      s.charset = 'utf-8';
      s.src = 'https://platform.twitter.com/widgets.js';
      s.onload = res;
      s.onerror = rej;
      document.head.appendChild(s);
    });
    return widgets;
  }

  function render(li) {
    if (li.dataset.built) return;
    li.dataset.built = '1';
    var url = li.getAttribute('data-tweet');
    var holder = document.createElement('div');
    holder.className = 'lesson-tweet';
    holder.innerHTML = '<blockquote class="twitter-tweet" data-dnt="true" ' +
      'data-conversation="none" data-width="420"><a href="' + url + '">' +
      'Opening the post on X\u2026</a></blockquote>';
    li.querySelector('.lesson-body').appendChild(holder);
    loadWidgets().then(function () {
      if (window.twttr && window.twttr.widgets) window.twttr.widgets.load(holder);
    }, function () {
      holder.innerHTML = '<p class="lesson-fallback">X could not be reached. ' +
        '<a href="' + url + '" target="_blank" rel="noopener">Open the post</a></p>';
    });
  }

  function showAll() {
    if (window.IntersectionObserver) {
      io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { render(e.target); io.unobserve(e.target); }
        });
      }, {rootMargin: '600px 0px'});
      Array.prototype.forEach.call(items, function (li) { io.observe(li); });
    } else {
      Array.prototype.forEach.call(items, render);
    }
  }

  function hideAll() {
    if (io) { io.disconnect(); io = null; }
    Array.prototype.forEach.call(items, function (li) {
      var h = li.querySelector('.lesson-tweet');
      if (h) h.remove();
      delete li.dataset.built;
    });
  }

  toggle.addEventListener('click', function () {
    shown = !shown;
    toggle.textContent = shown ? 'Hide the posts' : 'Show the posts';
    if (shown) showAll(); else hideAll();
  });
})();
