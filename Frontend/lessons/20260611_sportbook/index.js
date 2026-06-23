var themeButton = window.document.getElementById("change-theme-btn")
var body = document.body;

themeButton.addEventListener('click', (e) => {
  console.log(e);
  body.classList.toggle("dark-mode");
})