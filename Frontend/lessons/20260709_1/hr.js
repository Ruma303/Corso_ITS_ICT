const dipendenti = [
  { id: "e1", nome: "Alice", ruolo: "dev", stipendio: 2500, assunzione: new Date("2021-03-01"), attivo: true },
  { id: "e2", nome: "Bob", ruolo: "dev", stipendio: 2200, assunzione: new Date("2022-09-15"), attivo: true },
  { id: "e3", nome: "Carla", ruolo: "hr", stipendio: 2000, assunzione: new Date("2020-06-10"), attivo: false },
  { id: "e4", nome: "Dario", ruolo: "design", stipendio: 2100, assunzione: new Date("2023-01-20"), attivo: true }
];


// 1. Aggiungi "Eve"
console.log("\n1. Aggiungi \"Eve\"\n");
const conEve = [...dipendenti, { id: "e5", nome: "Eve", ruolo: "dev", stipendio: 2400, assunzione: new Date("2024-04-01"), attivo: true }]
console.log(conEve);
console.log("Lunghezza senza Eve:", dipendenti.length);
console.log("Lunghezza con Eve:", conEve.length);


// 2. find per id (Corretto con la guard sull'esistenza dell'oggetto)
console.log("\n2. find per id\n");
const dipId2 = dipendenti.find(dip => dip.id === "e2");
if (dipId2) { console.log("Trovato:", dipId2.nome); }


// 3. filter attivi
console.log("\n3. filter attivi\n");
const attivi = dipendenti
  .filter(dip => dip.attivo)
  .map(dip => dip.nome);
console.log("Dipendenti attivi:", attivi);


// 4. reduce stipendio totale
console.log("\n4. reduce stipendio totale\n");
const stipendioTotaleAttivi = dipendenti
  .filter(dip => dip.attivo)
  .reduce((tot, dip) => tot + dip.stipendio, 0);
console.log("Totale stipendio attivi:", stipendioTotaleAttivi);


// 5. reduce raggruppa per ruolo
console.log("\n5. reduce raggruppa per ruolo\n");
const conteggioRuoli = dipendenti
  .reduce((dipendenti, dip) => {
    const ruolo = dip.ruolo;
    if (!dipendenti[ruolo]) {
      dipendenti[ruolo] = 0;
    }
    dipendenti[ruolo]++;
    return dipendenti;
  }, {});
console.log("Raggruppamento per ruolo:", conteggioRuoli);


// 6. Report con Object.entries
console.log("\n6. Report con Object.entries\n");
for (const [ruolo, n] of Object.entries(conteggioRuoli)) {
  console.log(`Ruolo ${ruolo} : ${n} dipendenti`);
}


// 7. Rimuovi "e3" (mutabile)
console.log("\n7. Rimuovi \"e3\"\n");
const dipE3Pos = dipendenti.findIndex(dip => dip.id === "e3");
if (dipE3Pos !== -1) {
  const dipE3Tolto = dipendenti.splice(dipE3Pos, 1);
  console.log("Rimosso:", dipE3Tolto[0]);
}


// 8. JSON.stringify
console.log("\n8. JSON.stringify\n");
const dipString = JSON.stringify(dipendenti);
console.log(typeof dipString);


// 9. JSON.parse
console.log("\n9. JSON.parse\n");
const ricostruiti = JSON.parse(dipString);
console.log("Lunghezza JSON ricostruiti;", ricostruiti.length);
if (ricostruiti[0].nome === "Alice") {
  console.log("Il primo nome è Alice");
}


// 10. Trappola Date
console.log("\n10. Trappola Date\n");
console.log("Valore:", ricostruiti[0].assunzione, "– Tipo:", typeof ricostruiti[0].assunzione);

// console.log(ricostruiti[0].assunzione.getFullYear()); ! TypeError !

const dataDip0 = new Date(ricostruiti[0].assunzione);
console.log(dataDip0.getFullYear());