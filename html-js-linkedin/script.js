const popup = document.getElementById("popup");
const meButton = document.getElementById("me-button");

meButton.addEventListener('click', () => {
  popup.classList.toggle('active')
});