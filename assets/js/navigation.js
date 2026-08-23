document.addEventListener('DOMContentLoaded', () => {
  const navigation = document.querySelector('.site-nav');
  const toggle = navigation?.querySelector('.menu-icon');

  if (!navigation || !toggle) return;

  const close = () => {
    navigation.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const open = !navigation.classList.contains('is-open');
    navigation.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
  });

  document.addEventListener('click', (event) => {
    if (!navigation.contains(event.target)) close();
  });

  navigation.addEventListener('focusout', (event) => {
    if (!navigation.contains(event.relatedTarget)) close();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      close();
      toggle.focus();
    }
  });
});
