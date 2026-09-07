(() => {
  const root = document.documentElement;
  const header = document.querySelector('[data-header]');
  const progress = document.querySelector('.scroll-progress span');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const onScroll = () => {
    const y = window.scrollY || root.scrollTop;
    if (header) header.classList.toggle('is-collapsed', y > 36);
    if (progress) {
      const max = Math.max(1, root.scrollHeight - window.innerHeight);
      progress.style.transform = `scaleX(${Math.min(1, y / max)})`;
    }
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const revealItems = document.querySelectorAll('[data-reveal]');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach(el => el.classList.add('is-visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealItems.forEach(el => revealObserver.observe(el));
  }

  const steps = [...document.querySelectorAll('[data-step]')];
  const images = [...document.querySelectorAll('[data-story-image]')];
  const stageTitle = document.querySelector('[data-stage-title]');
  const stageCount = document.querySelector('[data-stage-count]');
  const stageNames = { studio: 'STUDIO', compose: 'COMPOSE', pages: 'PAGES' };

  if (steps.length && images.length && 'IntersectionObserver' in window && window.innerWidth > 760) {
    const activate = (step) => {
      const key = step.dataset.screen;
      const index = steps.indexOf(step);
      steps.forEach(el => el.classList.toggle('is-active', el === step));
      images.forEach(img => img.classList.toggle('is-visible', img.dataset.storyImage === key));
      if (stageTitle) stageTitle.textContent = stageNames[key] || key.toUpperCase();
      if (stageCount) stageCount.textContent = `${String(index + 1).padStart(2, '0')} / ${String(steps.length).padStart(2, '0')}`;
    };

    const stepObserver = new IntersectionObserver((entries) => {
      const visible = entries
        .filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) activate(visible.target);
    }, { threshold: [0.25, 0.45, 0.65], rootMargin: '-20% 0px -30% 0px' });
    steps.forEach(step => stepObserver.observe(step));
  }

  if (!reduceMotion && window.matchMedia('(pointer:fine)').matches) {
    const hero = document.querySelector('.hero');
    const orbit = [...document.querySelectorAll('.orbit-card')];
    if (hero && orbit.length) {
      hero.addEventListener('pointermove', (event) => {
        const rect = hero.getBoundingClientRect();
        const nx = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
        const ny = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
        const bases = [
          'rotate(-10deg)',
          'rotate(11deg)',
          'rotate(7deg)'
        ];
        orbit.forEach((el, i) => {
          const strength = (i + 1) * 4;
          el.style.transform = `${bases[i]} translate(${nx * strength}px, ${ny * strength}px)`;
        });
      });
      hero.addEventListener('pointerleave', () => {
        const bases = ['rotate(-10deg)', 'rotate(11deg)', 'rotate(7deg)'];
        orbit.forEach((el, i) => { el.style.transform = bases[i]; });
      });
    }
  }
})();
