const inventario = [
  { id: "d1", titolo: "Highway 61 Revisited", artista: "Bob Dylan", prezzo: 25, inStock: true },
  { id: "d2", titolo: "Abbey Road", artista: "The Beatles", prezzo: 30, inStock: true },
  { id: "d3", titolo: "Kind of Blue", artista: "Miles Davis", prezzo: 35, inStock: false },
  { id: "d4", titolo: "Aretha Now", artista: "Aretha Franklin", prezzo: 28, inStock: true }
];

// 1. Crea un nuovo disco
console.log("\n1. Crea un nuovo disco\n");
const titolo = "Blue";
const artista = "Joni Mitchell";
const nuovoDisco = { id: "d5", titolo, artista, prezzo: 22, inStock: true }
console.table(nuovoDisco);


// 2. Aggiungi in fondo
console.log("\n2. Aggiungi in fondo\n");
inventario.push(nuovoDisco);
console.log(inventario.length);


// 3. Applica uno sconto del 10%
const indiceDiscoDaScontare = inventario
  .findIndex(({ id }) => id === "d1")

if (indiceDiscoDaScontare !== -1) {
  const prezzo = inventario[indiceDiscoDaScontare].prezzo * 0.9
  console.log(prezzo.toFixed(2));
}


// 4. Rimuovi per id mutabile
console.log("\n4. Rimuovi per id mutabile\n");
const idDaRimuovere = "d2";
const idxDaRimuovere = inventario.findIndex(({ id }) => id === "d2");

if (idxDaRimuovere !== -1) {
  const arrRimossi = inventario.splice(idxDaRimuovere, 1);
  arrRimossi.map(({ titolo }) => console.log(`Elemento rimosso: ${titolo}`));
}

// 5. Tenta con id inesistente
console.log("\n5. Tenta con id inesistente\n");
const idInesistente = inventario.findIndex(({ id }) => id === "d9");
if (idInesistente !== -1) {
  const arrRimossi = inventario.splice(idInesistente, 1);
  arrRimossi.map(({ titolo }) => console.log(`Elemento rimosso: ${titolo}`));
} else {
  console.log("d9 non trovato")
}


// 6. Versione immutabile
console.log("\n6. Versione immutabile\n");
const senzaD3 = inventario.filter(d => d.id !== "d3");
console.log("Array senza d3 ", senzaD3);