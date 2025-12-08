// Loader JavaScript amélioré pour Tamam Business
(function() {
  'use strict';
  
  const loader = document.getElementById('loading');
  
  if (!loader) {
    return;
  }
  
  let isHidden = false;
  
  // Fonction pour masquer le loader avec animation fluide
  function hideLoader() {
    if (isHidden) {
      return;
    }
    
    isHidden = true;
    loader.classList.add('hidden');
    
    // Retirer complètement du DOM après l'animation
    setTimeout(function() {
      loader.style.display = 'none';
      loader.remove();
    }, 600);
  }
  
  // Masquer le loader quand la page est complètement chargée
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    // Petit délai pour que l'animation soit visible
    setTimeout(hideLoader, 500);
  } else {
    window.addEventListener('load', function() {
      setTimeout(hideLoader, 500);
    });
    
    // Fallback : masquer après 3 secondes maximum pour éviter un loader bloquant
    setTimeout(hideLoader, 3000);
  }
  
  // Masquer aussi lors du DOMContentLoaded avec un délai minimum
  document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
      if (!isHidden && document.readyState === 'complete') {
        hideLoader();
      }
    }, 1000);
  });
})();

