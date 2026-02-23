(function() {
  'use strict';

  // Get stored theme preference or default to system preference
  function getStoredTheme() {
    return localStorage.getItem('theme');
  }

  // Set theme preference in localStorage
  function setStoredTheme(theme) {
    localStorage.setItem('theme', theme);
  }

  // Get the current theme considering stored preference and system preference
  function getCurrentTheme() {
    const storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }
    
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    
    return 'light';
  }

  // Apply theme to document
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // Update button aria-label and content
    const button = document.getElementById('theme-toggle');
    if (button) {
      if (theme === 'dark') {
        button.setAttribute('aria-label', 'Switch to light mode');
        button.textContent = '☀️';
      } else {
        button.setAttribute('aria-label', 'Switch to dark mode');
        button.textContent = '🌙';
      }
    }
  }

  // Toggle between light and dark themes
  function toggleTheme() {
    const currentTheme = getCurrentTheme();
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setStoredTheme(newTheme);
    applyTheme(newTheme);
  }

  // Initialize theme on page load
  function initTheme() {
    const theme = getCurrentTheme();
    applyTheme(theme);
  }

  // Set up button event listener
  function setupButton() {
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.addEventListener('click', toggleTheme);
    }
  }

  // Set up event listeners when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initTheme();
      setupButton();
    });
  } else {
    initTheme();
    setupButton();
  }

  // Listen for system theme changes when no preference is stored
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      if (!getStoredTheme()) {
        applyTheme(e.matches ? 'dark' : 'light');
      }
    });
  }
})();
