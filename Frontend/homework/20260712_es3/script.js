const prenotazioni = [
  { nome: "Giulia", email: "giulia@x.it", campo: "padel", data: "2026-08-01", ora: "10:00", stato: "prenotato", prezzo: 30 },
  { nome: "Marco", email: "marco@x.it", campo: "calcio", data: "2026-08-01", ora: "12:00", stato: "in attesa", prezzo: 50 },
  { nome: "Elena", email: "elena@x.it", campo: "tennis", data: "2026-08-02", ora: "09:00", stato: "prenotato", prezzo: 25 },
  { nome: "Roberto", email: "roberto@x.it", campo: "calcio", data: "2026-08-02", ora: "16:00", stato: "libero", prezzo: 50 },
  { nome: "Chiara", email: "chiara@x.it", campo: "padel", data: "2026-08-03", ora: "18:00", stato: "prenotato", prezzo: 30 },
  { nome: "Andrea", email: "andrea@x.it", campo: "tennis", data: "2026-08-03", ora: "11:00", stato: "in attesa", prezzo: 25 }
];

console.log("\nEs 1\n");

const prenotazioniPerCampo = (campo) => {
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

const nomiPrenotanti = (campo) => {
  const arrayDiNomi = prenotazioniPerCampo(campo)
    .filter(c => c.stato === "prenotato")
    .map(ele => ele.campo.toUpperCase());
  return arrayDiNomi;
}

console.log("nomiPrenotanti: ", nomiPrenotanti("tennis").length, "trovate");
nomiPrenotanti("tennis")
  .forEach(element => {
    console.log(element)
  });


console.log("\nEs 3\n");

const incassoPerCampo = (campo) => {
  const sommaIncasso = prenotazioni.filter(c =>
    c.campo === campo)
    .filter(c => c.stato === "prenotato")
    .reduce((somma, c) => somma + c.prezzo, 0);
  return sommaIncasso;
}

console.log("incassoPerCampo: \"tennis\"", incassoPerCampo("tennis"), "€");


console.log("\nEs 4\n");

const totalePerCampo = () => {
  return prenotazioni.reduce((numPrenotazioni, prenotazione) => {
    if (!numPrenotazioni[prenotazione.campo])
      numPrenotazioni[prenotazione.campo] = 0;
    numPrenotazioni[prenotazione.campo]++;
    return numPrenotazioni;
  }, {});
};

console.log("totalePerCampo:", totalePerCampo());



console.log("\nEs 5\n");

const incassiPerCampo = () => {
  return prenotazioni.reduce((incasso, prenotazione) => {
    if (prenotazione.stato !== "prenotato"){
      return incasso;
    }
    const campo = prenotazione.campo;
    const prezzo = prenotazione.prezzo;
    if (!incasso[campo]) {
      incasso[campo] = 0;
    }
    incasso[campo] += prezzo;
    return incasso;
  }, {});
};

console.log("incassiPerCampo:", incassiPerCampo());


console.log("\nEs 6\n");




console.log("\nEs 7\n");




console.log("\nEs 8\n");




console.log("\nEs 9\n");




console.log("\nEs 10\n");




console.log("\nEs 11\n");




console.log("\nEs 12\n");




console.log("\nEs 13\n");




