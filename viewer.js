/* Home page: copy the workshop hashtag to the clipboard. */
(function () {
  var btn = document.querySelector('.tag-copy');
  if (!btn) return;
  var timer = null;
  function flash() {
    btn.classList.add('is-copied');
    clearTimeout(timer);
    timer = setTimeout(function () { btn.classList.remove('is-copied'); }, 1800);
  }
  btn.addEventListener('click', function () {
    var tag = btn.getAttribute('data-tag');
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(tag).then(flash, function () {});
      return;
    }
    var t = document.createElement('textarea');
    t.value = tag;
    t.setAttribute('readonly', '');
    t.style.position = 'fixed';
    t.style.opacity = '0';
    document.body.appendChild(t);
    t.select();
    try { document.execCommand('copy'); flash(); } catch (e) {}
    document.body.removeChild(t);
  });
})();

/* Home page structure viewer. Loads 3Dmol only when the reader asks for it. */
(function () {
  var root = document.querySelector('.viewer');
  if (!root) return;
  var stage = root.querySelector('.viewer-stage');
  var bar = root.querySelector('.viewer-bar');
  var startBtn = root.querySelector('.viewer-load');
  var viewer = null, model = null, chains = [], style = 'cartoon', spinning = true;
  var PALETTE = ['#5f468d', '#ca6560', '#7c4b83', '#a85674', '#2a5396', '#403855'];

  function chainColor(i) { return PALETTE[i % PALETTE.length]; }

  function fail(msg) {
    stage.innerHTML = '<div class="viewer-start"><span>' + msg + '</span></div>';
  }

  function script(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = src; s.onload = res; s.onerror = rej;
      document.head.appendChild(s);
    });
  }

  function data() {
    if (window.__AIG_CIF__) return Promise.resolve(window.__AIG_CIF__);
    return fetch(root.getAttribute('data-cif')).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    });
  }

  function apply() {
    viewer.setStyle({}, {});
    if (viewer.removeAllSurfaces) viewer.removeAllSurfaces();
    chains.forEach(function (c, i) {
      var col = chainColor(i);
      var sel = { chain: c };
      if (style === 'sticks') {
        viewer.setStyle(sel, { stick: { radius: 0.15, color: col } });
      } else {
        viewer.setStyle(sel, { cartoon: { color: col } });
      }
    });
    if (!chains.length) viewer.setStyle({}, { cartoon: { color: 'spectrum' } });
    if (style === 'surface') {
      chains.forEach(function (c, i) {
        viewer.addSurface($3Dmol.SurfaceType.VDW,
          { opacity: 0.7, color: chainColor(i) }, { chain: c });
      });
    }
    viewer.render();
  }

  startBtn.addEventListener('click', function () {
    startBtn.disabled = true;
    startBtn.textContent = 'Loading…';
    Promise.all([
      script('https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.5.5/3Dmol-min.js'),
      data()
    ]).then(function (out) {
      stage.innerHTML = '';
      viewer = $3Dmol.createViewer(stage, { backgroundAlpha: 0 });
      model = viewer.addModel(out[1], 'cif');
      var seen = {};
      model.selectedAtoms({}).forEach(function (a) {
        if (a.chain && !seen[a.chain]) { seen[a.chain] = 1; chains.push(a.chain); }
      });
      apply();
      viewer.zoomTo();
      viewer.spin('y', 0.4);
      viewer.render();
      bar.hidden = false;
    }).catch(function () {
      fail('The structure could not be loaded. It is in the repository at ' +
           'data/practical-02_interpret/exercise-2.1/7B1I.cif');
    });
  });

  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b || !viewer) return;
    if (b.hasAttribute('data-reset')) { viewer.zoomTo(); viewer.render(); return; }
    if (b.hasAttribute('data-spin')) {
      spinning = !spinning;
      viewer.spin(spinning ? 'y' : false, 0.4);
      b.classList.toggle('on', spinning);
      return;
    }
    style = b.getAttribute('data-style');
    bar.querySelectorAll('[data-style]').forEach(function (o) {
      o.classList.toggle('on', o === b);
    });
    apply();
  });
})();
