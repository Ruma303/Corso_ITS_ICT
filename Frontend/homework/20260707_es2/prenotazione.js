// Data partenza: 07/07/2026 - 13:25

const campi = [
  { id: "c1", nome: "Calcio", prezzoOrario: 50, coperto: true },
  { id: "c2", nome: "Padel", prezzoOrario: 30, coperto: true },
  { id: "c3", nome: "Tennis", prezzoOrario: 25, coperto: false }
];
// Prenotazione in arrivo dal form (per ora: variabili, non DOM)

// Nota: il nome arriva "sporco" (spazi + minuscolo) — va normalizzato con trim + capitalizza const nome = " mario "; const email = "mario@example.com"; const campoId = "c1"; const data = "2026-07-01"; const ore = 3;

const nome = " mario " || "Ospite";
const email = "mario@example.com";
const campoId = "c1";
const data = "2026-07-01";
const ore = 3;

let nomePulito = nome.trim();
nomePulito = nomePulito[0].toUpperCase() + nomePulito.slice(1).toLowerCase();
console.log("Nome pulito: ", nomePulito);

let isEmailValid = email.includes("@") && email.split("@").length === 2;
let isNameValid = nomePulito !== "";
console.log(
  !isNameValid
  ? `Nome non valido: ${nomePulito}`
  : `Nome valido: ${nomePulito}`
);

let campoTrovato = null;
for (const campo of campi) {
  if (campo.id === campoId) {
    campoTrovato = campo;
  }
}
console.log(
  campoTrovato
  ? `Campo ${campoId} trovato: ${campoTrovato.nome}`
  : `Il campo ${campoId} NON è presente`
);

let isDateValid = false;
const testDate = new Date(data);
if (testDate >= new Date()) {
  isDateValid = true;
}
console.log(
  isDateValid
  ? `La data è valida: ${testDate}`
  : `La data NON è valida perché è nel passato: ${testDate}`
);
let formattedDate = `${testDate.getDate()}/${testDate.getMonth() + 1}/${testDate.getFullYear()}`;
console.log("Data formattata:", formattedDate);

// Test solo per il campo c1
let prezzoOrario = campoTrovato.prezzoOrario ?? 0;

let percentualeSconto = (ore >= 5) ? 10 : 0;
let totaleNonScontato = prezzoOrario * ore;
let sconto = totaleNonScontato * percentualeSconto / 100;
let totale = totaleNonScontato - sconto;

const ID_PRENOTAZIONE = "p-" + Math.floor(Math.random() * 100000);

const formValido =
      isNameValid
      &&
      isEmailValid
      &&
      campoTrovato !== null
      &&
      isDateValid

let motivo = "";
if (!isNameValid) {
    motivo = "Nome mancante";
}
else if (!isEmailValid) {
    motivo = "Email non valida";
}
else if (campoTrovato === null) {
    motivo = "Campo non trovato";
}
else if (!isDateValid) {
    motivo = "Data nel passato";
}

const campiPrenotazione = {
  "ID": ID_PRENOTAZIONE,
  "Esito": formValido ? "✅ Valida" : "❌ Invalida",
  "Motivo": motivo,
  "Data": formattedDate,
  "Totale": `€${totale.toFixed(2)}`
}

// Singolo riepilogo
console.table(campiPrenotazione);

// Riepilogo campi
for (const campo of campi) {
    console.log(
        `${campo.nome}: €${campo.prezzoOrario}/h, ${
            campo.coperto ? "coperto" : "scoperto"
        }`
    );
}