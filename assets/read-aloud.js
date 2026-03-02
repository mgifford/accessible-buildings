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

    // Add periods after headings that don't end with sentence-ending punctuation,
    // so TTS engines pause naturally between the heading and the following body text
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(function(h) {
      const trimmed = h.textContent.trim();
      if (trimmed && !/[.!?:;]$/.test(trimmed)) {
        const lastChild = h.lastChild;
        if (lastChild && lastChild.nodeType === Node.TEXT_NODE) {
          lastChild.textContent = lastChild.textContent.replace(/\s*$/, '') + '.';
        } else if (lastChild) {
          h.appendChild(document.createTextNode('.'));
        }
      }
    });

    // Insert a full stop after block-level elements that don't already end with
    // sentence-ending punctuation, preventing run-on speech across paragraphs/list items
    clone.querySelectorAll('p, li, blockquote, dt, dd, td, th').forEach(function(block) {
      const trimmed = block.textContent.trim();
      if (trimmed && !/[.!?:;]$/.test(trimmed)) {
        const lastChild = block.lastChild;
        if (lastChild && lastChild.nodeType === Node.TEXT_NODE) {
          lastChild.textContent = lastChild.textContent.replace(/\s*$/, '') + '.';
        } else if (lastChild) {
          block.appendChild(document.createTextNode('.'));
        }
      }
    });
    
    // Get text content
    return clone.textContent.trim().replace(/\s+/g, ' ');
  }

  // Show a persistent accessible hint when Web Speech API is unavailable,
  // directing the user to their browser's built-in reading mode instead
  function showUnsupportedHint() {
    const container = document.querySelector('.page-content, main, article');
    if (!container) return;

    const hint = document.createElement('p');
    hint.className = 'read-aloud-unsupported';
    hint.setAttribute('role', 'note');
    hint.appendChild(document.createTextNode('🔊 Read-aloud is not available in this browser. Try '));
    const edgeStrong = document.createElement('strong');
    edgeStrong.textContent = 'Microsoft Edge Immersive Reader';
    hint.appendChild(edgeStrong);
    hint.appendChild(document.createTextNode(' (press F9 or click the book icon), '));
    const safariStrong = document.createElement('strong');
    safariStrong.textContent = 'Safari Reader View';
    hint.appendChild(safariStrong);
    hint.appendChild(document.createTextNode(' (View → Show Reader, then Edit → Speech → Start Speaking), or install a Read Aloud browser extension for Chrome or Firefox.'));
    container.insertAdjacentElement('afterbegin', hint);
  }

  // Initialize read-aloud functionality
  function initReadAloud() {
    if (!speechSupported) {
      console.log('Web Speech API not supported in this browser');
      showUnsupportedHint();
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
      showMessage('No text to read', button);
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
      
      // Provide user-facing error messages for common issues
      let errorMessage = 'Unable to read text aloud. ';
      switch(event.error) {
        case 'not-allowed':
          errorMessage += 'Text-to-speech permission was denied. Please check your browser settings.';
          break;
        case 'network':
          errorMessage += 'Network connection required for text-to-speech.';
          break;
        case 'interrupted':
          errorMessage += 'Reading was interrupted.';
          break;
        case 'audio-busy':
          errorMessage += 'Audio system is busy. Please try again.';
          break;
        default:
          errorMessage += 'Please try using your browser\'s reading mode instead.';
      }
      showMessage(errorMessage, button);
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

  // Show accessible message near button
  function showMessage(message, button) {
    // Create or get existing message container
    let messageDiv = button.parentNode.querySelector('.read-aloud-message');
    
    if (!messageDiv) {
      messageDiv = document.createElement('div');
      messageDiv.className = 'read-aloud-message';
      messageDiv.setAttribute('role', 'status'); // role=status implies aria-live=polite
      button.parentNode.insertBefore(messageDiv, button.nextSibling);
    }
    
    messageDiv.textContent = message;
    messageDiv.style.display = 'block';
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
      messageDiv.style.display = 'none';
    }, 5000);
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
