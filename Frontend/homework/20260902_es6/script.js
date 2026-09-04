"use strict";

console.log("SportBook JS caricato");

// ===== Modello dati (dalla L6/L8) =====
let prenotazioni = [
  { id: "p1", nome: "Mario", email: "mario@e.it", campo: "calcio", data: "2026-07-01", ora: "10:00", stato: "libero" },
  { id: "p2", nome: "Anna",  email: "anna@e.it",  campo: "padel",  data: "2026-07-02", ora: "18:00", stato: "libero" }
];

const STORAGE_KEY = "sportbook:prenotazioni";

// ===== Render lista prenotazioni =====
function renderPrenotazioni(lista) {
  const ul = document.querySelector("#lista-prenotazioni");
  ul.replaceChildren();
  lista.forEach(p => {
    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.textContent = `${p.nome} — ${p.campo} — ${p.data} ${p.ora} (${p.stato})`;
    const annulla = document.createElement("button");
    annulla.className = "btn btn-sm btn-outline-danger";
    annulla.textContent = "Annulla";
    annulla.dataset.id = p.id;
    li.appendChild(annulla);
    ul.appendChild(li);
  });
}

// ===== Render card campi =====
function renderCampi(lista) {
  const row = document.querySelector("#campi-container");
  row.replaceChildren();
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
    p.textContent = `${c.tipo} • ${c.posti} posti • ${c.coperto ? "coperto" : "scoperto"}`;
    body.append(h3, p);
    card.appendChild(body);
    col.appendChild(card);
    row.appendChild(col);
  });
}

// ===== Validazione live =====
const nomeInput = document.querySelector("#nome");
const emailInput = document.querySelector("#email");

nomeInput.addEventListener("input", () => {
  const ok = nomeInput.value.trim().length >= 2;
  nomeInput.classList.toggle("is-valid", ok);
  nomeInput.classList.toggle("is-invalid", !ok);
});

emailInput.addEventListener("input", () => {
  const v = emailInput.value.trim();
  const ok = v.includes("@") && v.includes(".") && v.length >= 5;
  emailInput.classList.toggle("is-valid", ok);
  emailInput.classList.toggle("is-invalid", !ok && v.length > 0);
});

// ===== Submit del form =====
const form = document.querySelector("#prenota form");
const lista = document.querySelector("#lista-prenotazioni");

form.addEventListener("submit", (e) => {
  e.preventDefault();   // PRIMA riga, sempre

  const data = new FormData(form);
  const nuova = {
    id: "p" + Date.now(),
    nome:  data.get("nome"),
    email: data.get("email"),
    campo: data.get("campo"),
    data:  data.get("data"),
    ora:   data.get("ora"),
    stato: "libero"
  };

  prenotazioni.push(nuova);
  renderPrenotazioni(prenotazioni);
  salvaPrenotazioni(prenotazioni);
  form.reset();

  // Toast di conferma (auto-hide dopo 3s)
  const toastEl = document.querySelector(".toast");
  bootstrap.Toast.getOrCreateInstance(toastEl).show();
  setTimeout(() => bootstrap.Toast.getOrCreateInstance(toastEl).hide(), 3000);
});

// ===== Contatore sessione =====
let secondi = 0;
const spanSessione = document.querySelector("#sessione");
setInterval(() => {
  secondi += 1;
  spanSessione.textContent = `Sessione attiva da ${secondi} secondi`;
}, 1000);

// ===== Event delegation: annulla prenotazione =====
lista.addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-id]");
  if (!btn) return;
  const id = btn.dataset.id;
  prenotazioni = prenotazioni.filter(p => p.id !== id);
  renderPrenotazioni(prenotazioni);
  salvaPrenotazioni(prenotazioni);
});

// ===== Fetch campi.json =====
async function caricaCampi() {
  const box = document.querySelector("#campi-container");
  box.replaceChildren();
  const loading = document.createElement("p");
  loading.textContent = "⏳ Caricamento campi…";
  box.appendChild(loading);

  try {
    const r = await fetch("campi.json");
    if (!r.ok) throw new Error("HTTP " + r.status);
    const campi = await r.json();
    renderCampi(campi);
  } catch (err) {
    box.replaceChildren();
    const errEl = document.createElement("p");
    errEl.className = "text-danger";
    errEl.textContent = "⚠️ Errore di caricamento";
    box.appendChild(errEl);
    console.error(err);
  }
}

// ===== localStorage =====
function salvaPrenotazioni(lista) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(lista));
}

function caricaPrenotazioni() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return [];
  try {
    return JSON.parse(raw);
  } catch (e) {
    console.error("Dati localStorage non validi, riparto da vuoto:", e);
    return [];
  }
}

// ===== Init =====
function init() {
  prenotazioni = caricaPrenotazioni();
  renderPrenotazioni(prenotazioni);
}

init();
caricaCampi();
