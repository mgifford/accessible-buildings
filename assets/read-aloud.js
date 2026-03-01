(function() {
  'use strict';

  // Check if Web Speech API is supported
  const speechSupported = 'speechSynthesis' in window;
  let currentUtterance = null;
  let isPaused = false;
  let isReading = false;

  // Get readable text from an element, excluding scripts and styles
  function getReadableText(element) {
    // Clone element to avoid modifying the DOM
    const clone = element.cloneNode(true);
    
    // Remove unwanted elements
    const unwanted = clone.querySelectorAll('script, style, [aria-hidden="true"], .no-read-aloud');
    unwanted.forEach(el => el.remove());
    
    // Get text content
    return clone.textContent.trim().replace(/\s+/g, ' ');
  }

  // Initialize read-aloud functionality
  function initReadAloud() {
    if (!speechSupported) {
      console.log('Web Speech API not supported in this browser');
      return;
    }

    // Add read-aloud button to sections with the class 'read-aloud-section'
    const sections = document.querySelectorAll('.read-aloud-section');
    
    sections.forEach(section => {
      const button = createReadAloudButton(section);
      
      // Insert button at the beginning of the section
      const heading = section.querySelector('h1, h2, h3, h4, h5, h6');
      if (heading) {
        heading.insertAdjacentElement('afterend', button);
      } else {
        section.insertAdjacentElement('afterbegin', button);
      }
    });

    // Add global read-aloud button if requested
    addGlobalReadAloudButton();
  }

  // Create a read-aloud button for a specific section
  function createReadAloudButton(section) {
    const button = document.createElement('button');
    button.className = 'read-aloud-btn';
    button.setAttribute('aria-label', 'Read this section aloud');
    button.innerHTML = '🔊 Read Aloud';
    
    button.addEventListener('click', function(e) {
      e.preventDefault();
      
      if (isReading && !isPaused) {
        pauseReading(button);
      } else if (isPaused) {
        resumeReading(button);
      } else {
        const text = getReadableText(section);
        startReading(text, button);
      }
    });
    
    return button;
  }

  // Add a global read-aloud button
  function addGlobalReadAloudButton() {
    const container = document.querySelector('.page-content, main, article');
    if (!container) return;

    const globalBtn = document.createElement('button');
    globalBtn.className = 'read-aloud-btn read-aloud-global';
    globalBtn.id = 'read-aloud-page';
    globalBtn.setAttribute('aria-label', 'Read this page aloud');
    globalBtn.innerHTML = '🔊 Read This Page';
    
    globalBtn.addEventListener('click', function(e) {
      e.preventDefault();
      
      if (isReading && !isPaused) {
        pauseReading(globalBtn);
      } else if (isPaused) {
        resumeReading(globalBtn);
      } else {
        const text = getReadableText(container);
        startReading(text, globalBtn);
      }
    });

    // Add at the top of content
    container.insertAdjacentElement('afterbegin', globalBtn);
  }

  // Start reading text aloud
  function startReading(text, button) {
    if (!text) {
      alert('No text to read');
      return;
    }

    // Stop any existing speech
    window.speechSynthesis.cancel();

    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.lang = document.documentElement.lang || 'en-US';
    currentUtterance.rate = 0.9; // Slightly slower for clarity
    currentUtterance.pitch = 1.0;
    currentUtterance.volume = 1.0;

    // Update button state when speech ends
    currentUtterance.onend = function() {
      resetButton(button);
    };

    currentUtterance.onerror = function(event) {
      console.error('Speech synthesis error:', event);
      resetButton(button);
      if (event.error === 'not-allowed') {
        alert('Text-to-speech permission was denied. Please check your browser settings.');
      }
    };

    window.speechSynthesis.speak(currentUtterance);
    isReading = true;
    isPaused = false;
    
    button.innerHTML = '⏸️ Pause';
    button.setAttribute('aria-label', 'Pause reading');
    button.classList.add('reading');
  }

  // Pause reading
  function pauseReading(button) {
    if (window.speechSynthesis.speaking) {
      window.speechSynthesis.pause();
      isPaused = true;
      button.innerHTML = '▶️ Resume';
      button.setAttribute('aria-label', 'Resume reading');
    }
  }

  // Resume reading
  function resumeReading(button) {
    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
      isPaused = false;
      button.innerHTML = '⏸️ Pause';
      button.setAttribute('aria-label', 'Pause reading');
    }
  }

  // Reset button to initial state
  function resetButton(button) {
    isReading = false;
    isPaused = false;
    currentUtterance = null;
    button.innerHTML = '🔊 Read Aloud';
    button.setAttribute('aria-label', 'Read this section aloud');
    button.classList.remove('reading');
  }

  // Stop all speech when page is hidden or unloaded
  function stopAllSpeech() {
    if (isReading) {
      window.speechSynthesis.cancel();
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initReadAloud);
  } else {
    initReadAloud();
  }

  // Clean up on page navigation
  window.addEventListener('beforeunload', stopAllSpeech);
  document.addEventListener('visibilitychange', function() {
    if (document.hidden && isReading) {
      stopAllSpeech();
    }
  });

  // Expose stop function globally for emergency use
  window.stopReadAloud = stopAllSpeech;
})();
