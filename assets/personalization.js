/**
 * Personalization panel for the Building Access Guide Toolkit.
 *
 * Provides visitor-controlled display preferences:
 *   - Color theme: Light / System / Dark
 *   - Text size:   Smaller / Default / Large / Larger
 *   - Reduce motion: toggle
 *
 * Preferences are persisted in localStorage and announced to screen readers.
 * This widget does NOT claim to "fix" accessibility – it complements proper
 * accessible design.  Users' own assistive technology always takes precedence.
 *
 * Implements patterns from:
 *   https://github.com/mgifford/ACCESSIBILITY.md/blob/main/examples/USER_PERSONALIZATION_ACCESSIBILITY_BEST_PRACTICES.md
 *   https://github.com/mgifford/ACCESSIBILITY.md/blob/main/examples/LIGHT_DARK_MODE_ACCESSIBILITY_BEST_PRACTICES.md
 */
(function () {
  'use strict';

  // ── Storage keys ────────────────────────────────────────────────────────────
  var KEYS = {
    theme: 'theme',
    fontSize: 'preferredFontSize',
    reducedMotion: 'preferredReducedMotion'
  };

  function getPref(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }
  function setPref(key, value) {
    try { localStorage.setItem(key, value); } catch (e) {}
  }
  function removePref(key) {
    try { localStorage.removeItem(key); } catch (e) {}
  }

  // ── Announce changes to screen readers ──────────────────────────────────────
  function announce(msg) {
    var el = document.getElementById('pref-announcement');
    if (!el) { return; }
    el.textContent = '';
    // 100ms delay ensures repeated messages are reliably picked up across screen readers
    setTimeout(function () { el.textContent = msg; }, 100);
  }

  // ── Theme management ─────────────────────────────────────────────────────────
  var darkMQ = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;

  /**
   * Apply CSS: set or remove data-theme attribute on <html>.
   * 'system' removes the attribute so the CSS media query takes effect.
   */
  function applyThemeCss(choice) {
    if (choice === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    } else if (choice === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      // 'system' – let the CSS prefers-color-scheme media query decide
      document.documentElement.removeAttribute('data-theme');
    }
  }

  /** Sync aria-pressed state on the three theme buttons. */
  function updateThemeUI(choice) {
    document.querySelectorAll('.pref-theme-btn').forEach(function (btn) {
      btn.setAttribute('aria-pressed', btn.dataset.theme === choice ? 'true' : 'false');
    });
  }

  function applyTheme(choice) {
    applyThemeCss(choice);
    updateThemeUI(choice);
  }

  function setTheme(choice) {
    setPref(KEYS.theme, choice);
    applyTheme(choice);
    var labels = { light: 'light mode', dark: 'dark mode', system: 'system preference' };
    announce('Color theme set to ' + (labels[choice] || choice));
  }

  function initTheme() {
    var stored = getPref(KEYS.theme) || 'system';
    applyTheme(stored);
  }

  // Re-apply if the OS colour scheme changes while "System" is chosen
  if (darkMQ) {
    darkMQ.addEventListener('change', function () {
      if (!getPref(KEYS.theme) || getPref(KEYS.theme) === 'system') {
        applyTheme('system');
      }
    });
  }

  // ── Font-size management ─────────────────────────────────────────────────────
  var FONT_LEVELS = [
    { pct: '87.5%',  label: 'Smaller' },
    { pct: null,     label: 'Default' },  // null = remove inline style
    { pct: '112.5%', label: 'Large'   },
    { pct: '125%',   label: 'Larger'  }
  ];
  var DEFAULT_FONT = 1;
  var MIN_FONT = 0;
  var MAX_FONT = FONT_LEVELS.length - 1;

  function applyFontSizeCss(level) {
    var pct = FONT_LEVELS[level].pct;
    if (pct) {
      document.documentElement.style.fontSize = pct;
    } else {
      document.documentElement.style.removeProperty('font-size');
    }
  }

  function updateFontSizeUI(level) {
    var display = document.getElementById('font-size-display');
    if (display) { display.textContent = FONT_LEVELS[level].label; }

    var dec = document.getElementById('font-decrease');
    var inc = document.getElementById('font-increase');
    if (dec) { dec.disabled = level <= MIN_FONT; }
    if (inc) { inc.disabled = level >= MAX_FONT; }
  }

  function currentFontLevel() {
    var n = parseInt(getPref(KEYS.fontSize), 10);
    return (isNaN(n) || n < MIN_FONT || n > MAX_FONT) ? DEFAULT_FONT : n;
  }

  function applyFontSize(level) {
    applyFontSizeCss(level);
    updateFontSizeUI(level);
  }

  function changeFontSize(delta) {
    var next = Math.max(MIN_FONT, Math.min(MAX_FONT, currentFontLevel() + delta));
    if (next === currentFontLevel()) { return; }
    setPref(KEYS.fontSize, next);
    applyFontSize(next);
    announce('Text size changed to ' + FONT_LEVELS[next].label);
  }

  function initFontSize() {
    applyFontSize(currentFontLevel());
  }

  // ── Reduced-motion management ────────────────────────────────────────────────
  var reducedMQ = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;

  function applyReducedMotionCss(enabled) {
    if (enabled) {
      document.documentElement.setAttribute('data-reduced-motion', 'true');
    } else {
      document.documentElement.removeAttribute('data-reduced-motion');
    }
  }

  function updateReducedMotionUI(enabled) {
    var toggle = document.getElementById('reduce-motion-toggle');
    if (toggle) { toggle.checked = enabled; }
  }

  function applyReducedMotion(enabled) {
    applyReducedMotionCss(enabled);
    updateReducedMotionUI(enabled);
  }

  function setReducedMotion(enabled) {
    setPref(KEYS.reducedMotion, enabled ? 'true' : 'false');
    applyReducedMotion(enabled);
    announce(enabled ? 'Reduced motion enabled' : 'Reduced motion disabled');
  }

  function initReducedMotion() {
    var stored = getPref(KEYS.reducedMotion);
    var enabled;
    if (stored !== null) {
      enabled = stored === 'true';
    } else {
      // Default to the OS preference
      enabled = !!(reducedMQ && reducedMQ.matches);
    }
    applyReducedMotion(enabled);
  }

  // ── Panel open / close ───────────────────────────────────────────────────────
  var panelOpen = false;

  function getPanel()  { return document.getElementById('personalization-panel'); }
  function getTrigger(){ return document.getElementById('personalization-btn');   }

  function openPanel() {
    var panel   = getPanel();
    var trigger = getTrigger();
    if (!panel || !trigger) { return; }
    panel.removeAttribute('hidden');
    trigger.setAttribute('aria-expanded', 'true');
    panelOpen = true;
    // Move focus to the first interactive element inside the panel
    var first = panel.querySelector('button:not([disabled]), input');
    if (first) { first.focus(); }
  }

  function closePanel(returnFocus) {
    var panel   = getPanel();
    var trigger = getTrigger();
    if (!panel || !trigger) { return; }
    panel.setAttribute('hidden', '');
    trigger.setAttribute('aria-expanded', 'false');
    panelOpen = false;
    if (returnFocus !== false) { trigger.focus(); }
  }

  function togglePanel() {
    if (panelOpen) { closePanel(); } else { openPanel(); }
  }

  // ── Reset all ────────────────────────────────────────────────────────────────
  function resetAll() {
    removePref(KEYS.theme);
    removePref(KEYS.fontSize);
    removePref(KEYS.reducedMotion);
    initTheme();
    initFontSize();
    initReducedMotion();
    announce('All display preferences reset to defaults');
  }

  // ── Wire up events ───────────────────────────────────────────────────────────
  function setupEvents() {
    // Panel toggle trigger
    var trigger = getTrigger();
    if (trigger) { trigger.addEventListener('click', togglePanel); }

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (panelOpen && (e.key === 'Escape' || e.key === 'Esc')) {
        closePanel();
      }
    });

    // Close when focus leaves the wrapper entirely
    var wrapper = document.getElementById('personalization-wrapper');
    if (wrapper) {
      wrapper.addEventListener('focusout', function (e) {
        if (panelOpen && !wrapper.contains(e.relatedTarget)) {
          closePanel(false); // don't return focus (user tabbed away)
        }
      });
    }

    // Close when clicking outside the wrapper
    document.addEventListener('click', function (e) {
      var w = document.getElementById('personalization-wrapper');
      if (panelOpen && w && !w.contains(e.target)) {
        closePanel(false);
      }
    });

    // Theme buttons
    document.querySelectorAll('.pref-theme-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setTheme(this.dataset.theme);
      });
    });

    // Font-size controls
    var dec = document.getElementById('font-decrease');
    var inc = document.getElementById('font-increase');
    if (dec) { dec.addEventListener('click', function () { changeFontSize(-1); }); }
    if (inc) { inc.addEventListener('click', function () { changeFontSize(+1); }); }

    // Reduced-motion toggle
    var motionToggle = document.getElementById('reduce-motion-toggle');
    if (motionToggle) {
      motionToggle.addEventListener('change', function () {
        setReducedMotion(this.checked);
      });
    }

    // Reset all button
    var resetBtn = document.getElementById('pref-reset-all');
    if (resetBtn) { resetBtn.addEventListener('click', resetAll); }
  }

  // ── Initialise ────────────────────────────────────────────────────────────────
  // Apply CSS preferences immediately (before DOM ready) to avoid visible flash
  initTheme();
  applyFontSizeCss(currentFontLevel());
  applyReducedMotionCss(
    (function () {
      var s = getPref(KEYS.reducedMotion);
      return s !== null ? s === 'true' : !!(reducedMQ && reducedMQ.matches);
    }())
  );

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initFontSize();
      initReducedMotion();
      setupEvents();
    });
  } else {
    initFontSize();
    initReducedMotion();
    setupEvents();
  }
}());
