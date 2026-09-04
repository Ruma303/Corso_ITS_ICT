// Dichiarazione per la libreria globale Bootstrap (caricata da CDN nell'HTML)
declare const bootstrap: any;

console.log("SportBook TS caricato");

// ===== 1. TIPI E INTERFACCE =====
type StatoPrenotazione = 'libero' | 'prenotato' | 'in attesa';

interface Prenotazione {
  id: string;
  nome: string;
  email: string;
  campo: string;
  data: string;
  ora: string;
  stato: StatoPrenotazione;
}

interface Campo {
  id: string;
  nome: string;
  tipo: string;
  coperto: boolean;
  posti: number;
}

let prenotazioni: Prenotazione[] = [
  { id: "p1", nome: "Mario", email: "mario@e.it", campo: "calcio", data: "2026-07-01", ora: "10:00", stato: "libero" },
  { id: "p2", nome: "Anna",  email: "anna@e.it",  campo: "padel",  data: "2026-07-02", ora: "18:00", stato: "libero" }
];

const STORAGE_KEY = "sportbook:prenotazioni";

// ===== 2. TIPIZZAZIONE ELEMENTI DOM CON NULL-CHECK =====
const nomeInput = document.querySelector("#nome") as HTMLInputElement | null;
const emailInput = document.querySelector("#email") as HTMLInputElement | null;
const form = document.querySelector("#prenota form") as HTMLFormElement | null;
const lista = document.querySelector("#lista-prenotazioni") as HTMLElement | null;

// ===== 3. RENDER PRENOTAZIONI =====
function renderPrenotazioni(listaPrenotazioni: Prenotazione[]): void {
  const ul = document.querySelector("#lista-prenotazioni") as HTMLElement | null;
  if (!ul) return;

  ul.replaceChildren();
  listaPrenotazioni.forEach((p) => {
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

// ===== 4. RENDER CAMPI =====
function renderCampi(listaCampi: Campo[]): void {
  const row = document.querySelector("#campi-container") as HTMLElement | null;
  if (!row) return;

  row.replaceChildren();
  listaCampi.forEach((c) => {
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

// ===== 5. VALIDAZIONE LIVE =====
if (nomeInput) {
  nomeInput.addEventListener("input", () => {
    const ok = nomeInput.value.trim().length >= 2;
    nomeInput.classList.toggle("is-valid", ok);
    nomeInput.classList.toggle("is-invalid", !ok);
  });
}

if (emailInput) {
  emailInput.addEventListener("input", () => {
    const v = emailInput.value.trim();
    const ok = v.includes("@") && v.includes(".") && v.length >= 5;
    emailInput.classList.toggle("is-valid", ok);
    emailInput.classList.toggle("is-invalid", !ok && v.length > 0);
  });
}

// ===== 6. SUBMIT DEL FORM =====
if (form) {
  form.addEventListener("submit", (e: SubmitEvent) => {
    e.preventDefault();

    const data = new FormData(form);
    const nuova: Prenotazione = {
      id: "p" + Date.now(),
      nome: (data.get("nome") as string) ?? "",
      email: (data.get("email") as string) ?? "",
      campo: (data.get("campo") as string) ?? "",
      data: (data.get("data") as string) ?? "",
      ora: (data.get("ora") as string) ?? "",
      stato: "libero"
    };

    prenotazioni.push(nuova);
    renderPrenotazioni(prenotazioni);
    salvaPrenotazioni(prenotazioni);
    form.reset();

    // Reset classi validazione
    if (nomeInput) nomeInput.classList.remove("is-valid");
    if (emailInput) emailInput.classList.remove("is-valid");

    // Toast di conferma
    const toastEl = document.querySelector(".toast") as HTMLElement | null;
    if (toastEl && typeof bootstrap !== "undefined") {
      const toastInstance = bootstrap.Toast.getOrCreateInstance(toastEl);
      toastInstance.show();
      setTimeout(() => toastInstance.hide(), 3000);
    }
  });
}

// ===== 7. CONTATORE SESSIONE =====
let secondi = 0;
const spanSessione = document.querySelector("#sessione") as HTMLElement | null;
if (spanSessione) {
  setInterval(() => {
    secondi += 1;
    spanSessione.textContent = `Sessione attiva da ${secondi} secondi`;
  }, 1000);
}

// ===== 8. EVENT DELEGATION: ANNULLA PRENOTAZIONE =====
if (lista) {
  lista.addEventListener("click", (e: MouseEvent) => {
    const target = e.target as HTMLElement | null;
    if (!target) return;

    const btn = target.closest("button[data-id]") as HTMLButtonElement | null;
    if (!btn) return;

    const id = btn.dataset.id;
    if (!id) return;

    prenotazioni = prenotazioni.filter((p) => p.id !== id);
    renderPrenotazioni(prenotazioni);
    salvaPrenotazioni(prenotazioni);
  });
}

// ===== 9. FETCH CAMPI.JSON =====
async function caricaCampi(): Promise<void> {
  const box = document.querySelector("#campi-container") as HTMLElement | null;
  if (!box) return;

  box.replaceChildren();
  const loading = document.createElement("p");
  loading.textContent = "⏳ Caricamento campi…";
  box.appendChild(loading);

  try {
    const r = await fetch("campi.json");
    if (!r.ok) throw new Error("HTTP " + r.status);
    const campi: Campo[] = await r.json();
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

// ===== 10. LOCAL STORAGE =====
function salvaPrenotazioni(listaPrenotazioni: Prenotazione[]): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(listaPrenotazioni));
}

function caricaPrenotazioni(): Prenotazione[] {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return [];
  try {
    return JSON.parse(raw) as Prenotazione[];
  } catch (e) {
    console.error("Dati localStorage non validi, riparto da vuoto:", e);
    return [];
  }
}

// ===== 11. INIT =====
function init(): void {
  prenotazioni = caricaPrenotazioni();
  renderPrenotazioni(prenotazioni);
}

init();
caricaCampi();