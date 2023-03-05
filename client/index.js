const form = document.getElementById('flower-form');
const flowerContainer = document.getElementById('flower-type-prediction');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(Object.fromEntries(formData))
  });
  const { flower_type } = await response.json();
  flowerContainer.innerText = flower_type.charAt(0).toUpperCase() + flower_type.slice(1);
});
