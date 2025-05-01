document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.querySelector('.toggle-button');
  const body = document.body;

  // Toggle theme
  toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    localStorage.setItem('theme', body.classList.contains('dark-theme') ? 'dark' : 'light');
  });

  // Load saved theme preference
  if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-theme');
  }

  // Highlight clicked button briefly
  const form = document.querySelector('form');
  form.addEventListener('submit', (event) => {
    const clickedButton = event.submitter;
    if (clickedButton) {
      clickedButton.classList.add('clicked');
      setTimeout(() => {
        clickedButton.classList.remove('clicked');
      }, 200);
    }
  });
});