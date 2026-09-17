(() => {
  'use strict';

  const initFaqAccordion = () => {
    const items = Array.from(document.querySelectorAll('.faq-list details.faq-item'));
    if (!items.length) return;

    if (!document.querySelector('style[data-faq-accordion]')) {
      const style = document.createElement('style');
      style.dataset.faqAccordion = '1';
      style.textContent = `
        .faq-list details.faq-item > summary.faq-question {
          list-style: none;
          cursor: pointer;
          position: relative;
          padding-left: 44px;
        }
        .faq-list details.faq-item > summary.faq-question::-webkit-details-marker {
          display: none;
        }
        .faq-list details.faq-item > summary.faq-question::after {
          content: '+';
          position: absolute;
          left: 14px;
          top: 50%;
          width: 22px;
          height: 22px;
          display: grid;
          place-items: center;
          transform: translateY(-50%) rotate(0deg);
          transition: transform .25s ease;
          font-size: 20px;
          font-weight: 500;
          line-height: 1;
        }
        .faq-list details.faq-item[open] > summary.faq-question::after {
          transform: translateY(-50%) rotate(45deg);
        }
        .faq-list details.faq-item > .faq-answer {
          display: grid !important;
          grid-template-rows: 0fr !important;
          overflow: hidden !important;
          transition: grid-template-rows .3s ease, opacity .25s ease;
          opacity: 0;
          margin: 0 !important;
        }
        .faq-list details.faq-item > .faq-answer > .faq-answer-inner {
          min-height: 0;
          overflow: hidden;
        }
        .faq-list details.faq-item[open] > .faq-answer {
          grid-template-rows: 1fr !important;
          opacity: 1;
        }
      `;
      document.head.appendChild(style);
    }

    items.forEach((item) => {
      if (item.dataset.faqAccordionReady === '1') return;
      item.dataset.faqAccordionReady = '1';

      const summary = item.querySelector(':scope > summary.faq-question');
      if (!summary) return;

      summary.addEventListener('click', () => {
        if (item.open) return;
        items.forEach((other) => {
          if (other !== item) other.removeAttribute('open');
        });
      });
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFaqAccordion, { once: true });
  } else {
    initFaqAccordion();
  }
})();
