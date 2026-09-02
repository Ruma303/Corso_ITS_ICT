const form = document.querySelector("#form-news");
const countdown = document.querySelector("#countdown");
const message = document.querySelector("#messaggio");

const eMailValida = (emailValue) => {
  return emailValue.includes("@") && emailValue.length >= 3;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const emailInput = formData.get("email");

  message.className = "";

  if (eMailValida(emailInput)) {
    let counter = 5;
    countdown.textContent = counter;

    const timerId = setInterval(() => {
      counter--;
      countdown.textContent = `Invio email in ${counter}s ...`;

      if (counter === 0) {
        clearInterval(timerId);
        countdown.textContent = ""; // Pulizia countdown

        message.classList.add("alert", "alert-success");
        message.textContent = `✅ Iscrizione confermata per ${emailInput}`;

        setTimeout(() => {
          message.classList.add("d-none");
        }, 3000);
      }
    }, 1000);

  } else {
    message.classList.add("alert", "alert-danger");
    message.textContent = "❌ Errore: email non valida.";
  }
});