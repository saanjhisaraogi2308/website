document.querySelectorAll('.cta-button').forEach(button => {
  button.addEventListener('click', (e) => {
    const modal = document.getElementById('enquiryModal');
    const categoryInput = document.getElementById('categoryInput');

    modal.style.display = 'block';

    // Determine category based on button context
    if (e.target.closest('.hero-overlay')) {
      categoryInput.value = 'Main Banner';
    } else if (e.target.closest('.card')) {
      const cardTitle = e.target.closest('.card').querySelector('h3')?.textContent;
      categoryInput.value = `Service - ${cardTitle || 'Unknown'}`;
    } else {
      categoryInput.value = 'Unknown';
    }
  });
});


document.querySelector('.close').addEventListener('click', () => {
  document.getElementById('enquiryModal').style.display = 'none';
  resetModal();
});

document.getElementById('continueBtn')?.addEventListener('click', () => {
  document.getElementById('enquiryModal').style.display = 'none';
  resetModal();
});

window.addEventListener('click', e => {
  if (e.target === document.getElementById('enquiryModal')) {
    document.getElementById('enquiryModal').style.display = 'none';
    resetModal();
  }
});

function getQueryParam(param) {
  const params = new URLSearchParams(window.location.search);
  return params.get(param);
}

function resetModal() {
  document.getElementById('modalSuccessPopup').style.display = 'none';
  document.getElementById('enquiryForm').style.display = 'block';
}

window.addEventListener('load', () => {
  if (getQueryParam('submitted') === 'true') {
    const modal = document.getElementById('enquiryModal');
    const successPopup = document.getElementById('modalSuccessPopup');
    const form = document.getElementById('enquiryForm');

    modal.style.display = 'block';
    successPopup.style.display = 'block';
    form.style.display = 'none';

    // Remove query param immediately so refresh won't show popup again
    window.history.replaceState({}, document.title, window.location.pathname);
  }
});
