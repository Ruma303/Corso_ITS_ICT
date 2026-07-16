const prenotazioni = [
  { id: 1, nome: "Giulia", email: "giulia@x.it", campo: "padel", data: "2026-08-01", ora: "10:00", stato: "prenotato", prezzo: 30 },
  { id: 2, nome: "Marco", email: "marco@x.it", campo: "calcio", data: "2026-08-01", ora: "12:00", stato: "in attesa", prezzo: 50 },
  { id: 3, nome: "Elena", email: "elena@x.it", campo: "tennis", data: "2026-08-02", ora: "09:00", stato: "prenotato", prezzo: 25 },
  { id: 4, nome: "Roberto", email: "roberto@x.it", campo: "calcio", data: "2026-08-02", ora: "16:00", stato: "libero", prezzo: 50 },
  { id: 5, nome: "Chiara", email: "chiara@x.it", campo: "padel", data: "2026-08-03", ora: "18:00", stato: "prenotato", prezzo: 30 },
  { id: 6, nome: "Andrea", email: "andrea@x.it", campo: "tennis", data: "2026-08-03", ora: "11:00", stato: "in attesa", prezzo: 25 }
];



console.log("\nEs 1\n");

const prenotazioniPerCampo = function(campo) {
  const arrayDiPrenotazione = prenotazioni.filter(c =>
    c.campo === campo
  );
  return arrayDiPrenotazione;
}

console.log("prenotazioniPerCampo: ", prenotazioniPerCampo("tennis").length, "trovate");
prenotazioniPerCampo("tennis")
  .forEach(element => {
    console.log(element)
  });



console.log("\nEs 2\n");

const nomiPrenotanti = function(campo) {
  const arrayDiNomi = prenotazioniPerCampo(campo)
    .filter(c => c.stato === "prenotato")
    .map(ele => ele.nome.toUpperCase());
  return arrayDiNomi;
}

console.log("nomiPrenotanti: ", nomiPrenotanti("tennis").length, "trovate");
nomiPrenotanti("tennis")
  .forEach(element => {
    console.log(element)
  });


console.log("\nEs 3\n");

const incassoPerCampo = function(campo) {
  const sommaIncasso = prenotazioni.filter(c =>
    c.campo === campo)
    .filter(c => c.stato === "prenotato")
    .reduce((somma, c) => somma + c.prezzo, 0);
  return sommaIncasso;
}

console.log("incassoPerCampo: \"tennis\"", incassoPerCampo("tennis"), "€");


console.log("\nEs 4\n");

const totalePerCampo = function() {
  return prenotazioni.reduce((numPrenotazioni, prenotazione) => {
    if (!numPrenotazioni[prenotazione.campo])
      numPrenotazioni[prenotazione.campo] = 0;
    numPrenotazioni[prenotazione.campo]++;
    return numPrenotazioni;
  }, {});
};

console.log("totalePerCampo:", totalePerCampo());



console.log("\nEs 5\n");

const incassiPerCampo = function() {
  return prenotazioni.reduce((incasso, prenotazione) => {
    const campo = prenotazione.campo;
    const prezzo = prenotazione.prezzo;
    if (!incasso[campo]) {
      incasso[campo] = 0;
    }
    if (prenotazione.stato !== "prenotato") {
      return incasso;
    }
    incasso[campo] += prezzo;
    return incasso;
  }, {});
};

console.log("incassiPerCampo:", incassiPerCampo());



console.log("\nEs 6\n");

const riepilogo = function({ nome, campo, data, ora, stato }) {
  return `${nome} ha prenotato il ${campo} il ${data} alle ${ora} (stato: ${stato})`;
};

console.log("riepilogo:", riepilogo(prenotazioni[0]));



console.log("\nEs 7\n");

const salva = function(prenotazioni) {
  return JSON.stringify(prenotazioni);
};

const carica = function(json) {
  return JSON.parse(json);
};

const testJSONarray = carica(salva(prenotazioni));
console.log("Verifica carica(salva(prenotazioni)) :", testJSONarray);

const sonoIdentici = JSON.stringify(testJSONarray) === JSON.stringify(prenotazioni);
console.log("È identico all'originale? ", sonoIdentici);



console.log("\nEs 8\n");

const ordinaPerData = function() {
  return [...prenotazioni].sort((a, b) => {
    const ordinatiPerData = a.data.localeCompare(b.data);
    if (ordinatiPerData !== 0) {
      return ordinatiPerData;
    }
    // Altrimenti, ordino per prezzo
    return a.prezzo - b.prezzo;
  });
};

// Versione più compatta con or logico
const ordinaPerData2 = function() {
  return [...prenotazioni].sort((a, b) =>
    a.data.localeCompare(b.data) || a.prezzo - b.prezzo
  );
};

console.log("Array ordinato per data: ", ordinaPerData2());



console.log("\nEs 9\n");

const esistePrenotata = function(campo) {
  return prenotazioni.some(obj => obj.campo === campo && obj.stato === "prenotato");
}
console.log("Esiste prenotata per padel?", esistePrenotata("padel"));

const tuttiHannoEmail = function() {
  return prenotazioni.every(campo => campo.email);
}
console.log("Tutti hanno l'email?", tuttiHannoEmail());



console.log("\nEs 10\n");

const aggiungiSicura = function(prenotazione) {
  return [...prenotazioni, prenotazione];
}

const nuovaPrenotazione = {
  id: 7, // Aggiunto per l'esercizio di dopo
  nome: "Ugo",
  email: "ugo@u.it",
  campo: "calcio",
  data: "2026-08-02",
  ora: "15:00",
  stato: "in attesa",
  prezzo: 45
}
console.log("aggiungiSicura", aggiungiSicura(nuovaPrenotazione));



console.log("\nEs 11\n");

const rimuovi = function(id) {
  const posizione = prenotazioni.findIndex(obj=> obj.id === id);
  if (posizione === -1) {
    return -1;
  }
  const [elementoRimosso] = prenotazioni.splice(posizione, 1);
  return prenotazioni;
}
console.log("Rimozione modificando l'array originale: ", rimuovi(6));
console.log("Rimozione modificando l'array originale: ", rimuovi(7)); // -1

const rimuoviImmutabile = function(id) {
  return prenotazioni.filter(obj => obj.id !== id);
};
console.log("Rimozione immutabile: ", rimuoviImmutabile(2));



console.log("\nEs 12\n");

const stampaReportConteggi = function() {
  Object.entries(totalePerCampo()).forEach(([campo, num]) => {
    console.log(`Campo ${campo}: ${num} prenotazioni`)
  });
};
stampaReportConteggi()



console.log("\nEs 13\n");


const creaIdPrenotazione = function() {
  let counter = 0;
  return () => {
    counter++;
    return counter;
  };
}

// Primo generatore
const genId = creaIdPrenotazione();

// Creazione nuovi campi di test
const nuova1 = { nome: "Luca", campo: "tennis" };
const nuova2 = { nome: "Sara", campo: "padel" };

nuova1.id = genId();
nuova2.id = genId();

console.log("Nuova 1:", nuova1);
console.log("Nuova 2:", nuova2);

// Secondo generatore indipendente
const genId2 = creaIdPrenotazione();

const nuova3 = { nome: "Fabio", campo: "calcio" };
nuova3.id = genId2();

console.log("Nuova 3:", nuova3); // È indipendente