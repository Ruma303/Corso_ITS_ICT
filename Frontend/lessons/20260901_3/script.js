"use strict";

console.log("SportBook JS caricato");

// Inizializza con dati di default se il localStorage è vuoto, assicurandosi di avere gli 'id'
if (prenotazioni.length === 0) {
  prenotazioni = [
    { id: "p1", nome: "Mario", campo: "calcio", data: "2026-07-01", ora: "10:00" },
    { id: "p2", nome: "Anna", campo: "padel", data: "2026-07-02", ora: "18:00" }
  ];
  salvaPrenotazioni(prenotazioni);
}

const form = document.querySelector("form");
const toastElement = document.querySelector(".toast");
const listaPrenotazioni = document.querySelector("#lista-prenotazioni");
const counter = document.querySelector("#sessione");

function renderPrenotazioni(lista) {
  listaPrenotazioni.replaceChildren();

  lista.forEach(ele => {
    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";

    const spanInfo = document.createElement("span");
    spanInfo.textContent = `${ele.nome} - ${ele.campo.toUpperCase()} il ${ele.data} alle ${ele.ora}`;

    const annullaBtn = document.createElement("button");
    annullaBtn.className = "btn btn-outline-danger btn-sm";
    annullaBtn.textContent = "Annulla";
    annullaBtn.dataset.id = ele.id; // Assegna data-id="<id-prenotazione>"

    li.append(spanInfo, annullaBtn);
    listaPrenotazioni.appendChild(li);
  });
}

renderPrenotazioni(prenotazioni);

// EVENT DELEGATION
listaPrenotazioni.addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-id]");

  if (btn) {
    const idDaRimuovere = btn.dataset.id;
    prenotazioni = prenotazioni.filter(p => p.id !== idDaRimuovere);
    salvaPrenotazioni(prenotazioni);
    renderPrenotazioni(prenotazioni);
  }
});


form.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(form);

  // Creazione prenotazione
  const nuovaPrenotazione = {
    id: "p" + Date.now(),
    nome: formData.get("nome"),
    campo: formData.get("campo"),
    data: formData.get("data"),
    ora: formData.get("ora")
  }

  prenotazioni.push(nuovaPrenotazione);
  salvaPrenotazioni(prenotazioni);
  renderPrenotazioni(prenotazioni);
  form.reset();

  if (window.bootstrap && bootstrap.Toast) {
    const toast = bootstrap.Toast.getOrCreateInstance(toastElement);
    toast.show();
  } else {
    // Fallback manuale
    toastElement.classList.add("show");
    setTimeout(() => {
      toastElement.classList.remove("show");
    }, 3000);
  }
})

// 5: Contatore
let secondiSessione = 0;
counter.textContent = `Sessione: ${secondiSessione}s`;

const timerSessioneId = setInterval(() => {
  secondiSessione++;
  counter.textContent = `Sessione: ${secondiSessione}s`;

  // Nota per eventuale interruzione:
  // clearInterval(timerSessioneId);
}, 1000);


// 6. Fetch JSON e render dinamico
const campiContainer = document.querySelector("#campi-container");

function renderCampi(lista) {
  campiContainer.replaceChildren();

  // Creazione elementi Bootstrap
  lista.forEach(c => {
    const col = document.createElement("div");
    col.className = "col-12 col-md-6 col-lg-4";

    const card = document.createElement("article");
    card.className = "card h-100 shadow-sm";

    const body = document.createElement("div");
    body.className = "card-body d-flex flex-column";

    const h3 = document.createElement("h3");
    h3.className = "card-title h5";
    h3.textContent = c.nome;

    const p = document.createElement("p");
    p.className = "card-text";
    p.textContent = `${c.tipo} - ${c.posti} posti - ${c.coperto ? "coperto" : "scoperto"}`;

    body.append(h3, p);
    card.appendChild(body);
    col.appendChild(card);

    campiContainer.appendChild(col);
  });
}

async function caricaCampi() {
  campiContainer.textContent = "⏳ Caricamento campi…";

  try {
    const res = await fetch("campi.json");
    if (!res.ok) {
      throw new Error(`Errore HTTP: ${res.status}`);
    }
    const campi = await res.json();
    renderCampi(campi);

  } catch (err) {
    console.error("Errore fetch:", err);
    campiContainer.textContent = "⚠️ Errore di caricamento";
  }
}

const LOCAL_PRENOTAZIONI = "sportbook:prenotazioni";

function salvaPrenotazioni(lista) {
  const toJSON = JSON.stringify(lista);
  localStorage.setItem(LOCAL_PRENOTAZIONI, toJSON);
}

function caricaPrenotazioni() {
  const dataStorage = localStorage.getItem(LOCAL_PRENOTAZIONI);

  if (!dataStorage) return [];
  try {
    return JSON.parse(dataStorage);
  } catch (e) {
    console.error("Dati in localStorage non validi:", e);
    return [];
  }
}

let prenotazioni = caricaPrenotazioni();

caricaCampi();