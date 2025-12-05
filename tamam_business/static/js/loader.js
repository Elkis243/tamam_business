// Loader JavaScript pour Tamam Business
(function() {
  'use strict';
  
  const loader = document.getElementById('loading');
  
  if (!loader) {
    return;
  }
  
  // Fonction pour masquer le loader
  function hideLoader() {
    loader.classList.add('hidden');
    setTimeout(function() {
      loader.style.display = 'none';
    }, 500);
  }
  
  // Masquer le loader quand la page est complètement chargée
  if (document.readyState === 'complete') {
    hideLoader();
  } else {
    window.addEventListener('load', hideLoader);
  }
  
  // Fallback de sécurité : masquer après 3 secondes maximum
  setTimeout(hideLoader, 3000);
})();

