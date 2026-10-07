// Food Ordering Analytics - Interactive Client Script
document.addEventListener('DOMContentLoaded', () => {
  // 1. KPI Counter Animation
  const kpiNumbers = document.querySelectorAll('.kpi-number');
  let hasAnimated = false;

  const animateCounters = () => {
    kpiNumbers.forEach(kpi => {
      const target = parseInt(kpi.getAttribute('data-target'), 10);
      if (isNaN(target)) return;

      const duration = 1800;
      const startTime = performance.now();

      const updateCounter = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Ease out quadratic
        const easeOut = 1 - (1 - progress) * (1 - progress);
        const currentVal = Math.floor(easeOut * target);

        if (target >= 1000) {
          kpi.textContent = currentVal.toLocaleString('en-US');
        } else {
          kpi.textContent = currentVal;
        }

        if (progress < 1) {
          requestAnimationFrame(updateCounter);
        } else {
          kpi.textContent = target >= 1000 ? target.toLocaleString('en-US') : target;
        }
      };

      requestAnimationFrame(updateCounter);
    });
  };

  // Trigger KPI animation when in view
  const kpiSection = document.querySelector('.kpi-strip');
  if (kpiSection && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !hasAnimated) {
          hasAnimated = true;
          animateCounters();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    observer.observe(kpiSection);
  } else {
    animateCounters();
  }

  // 2. Smooth Scroll for internal navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // 3. Fallback message if Tableau iframe fails to load or takes long
  const tableauIframe = document.querySelector('.tableau-iframe');
  if (tableauIframe) {
    const loadTimeout = setTimeout(() => {
      // If user is on an offline machine or restrictive network
      console.info('Tableau iframe initialized. Direct visualization available at Tableau Public.');
    }, 5000);

    tableauIframe.addEventListener('load', () => {
      clearTimeout(loadTimeout);
    });
  }
});
