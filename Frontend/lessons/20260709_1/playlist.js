const playlist = [
  { titolo: "Blowing in the Wind", artista: "Bob Dylan", secondi: 230, riproducendo: false },
  { titolo: "Imagine", artista: "John Lennon", secondi: 183, riproducendo: true },
  { titolo: "Redemption Song", artista: "Bob Marley", secondi: 220, riproducendo: false },
  { titolo: "Blowin' Blues", artista: "Bob Dylan", secondi: 200, riproducendo: false }
];


// 1. Stampa la playlist
console.log("\n1. Stampa la playlist\n")
playlist.forEach((canzone, index) => {
  let secondi = canzone.secondi % 60;
  let secondiFormattati = String(secondi).padStart(2, '0');
  let minuti = Math.floor(canzone.secondi / 60);
  console.log(`${index}. ${canzone.titolo} - ${canzone.artista} (${minuti} : ${secondiFormattati})`)
})

// 2. Estrai titoli
console.log("\n2. Estrai titoli\n")
const titoli = playlist
  .map(canzone => canzone.titolo)
  .map(titolo => console.log(titolo))

// 3. Filtra per artista
console.log("\n3. Filtra per artista\n")
const canzoniBobDylan = playlist
  .filter(canzone => canzone.artista === "Bob Dylan")
  .map(canzone => console.log(canzone.titolo))

// 4. Trova la traccia in riproduzione
console.log("\n4. Trova la traccia in riproduzione\n")
const inRiproduzione = playlist
  .find(canzone => canzone.riproducendo === true)
console.log(inRiproduzione.titolo, inRiproduzione.artista)

// 5. Cerca per titolo esatto
console.log("\n5. Cerca per titolo esatto\n");
const imagine = playlist.find(canzone =>
  canzone.titolo === "Imagine");

const blowing = playlist.find(canzone =>
  canzone.titolo === "blowing in the Wind");
if (!blowing) {
  console.log("Traccia non trovata");
} else {
  console.log("Traccia trovata");
}

// 6. Aggiungi una traccia in fondo
console.log("\n6. Aggiungi una traccia in fondo\n");

const nuovaCanzone = { titolo: "Graphite", artista: "Sleep Token", secondi: 531, riproducendo: true };
playlist.push(nuovaCanzone);
console.log("Ho pushato: ", nuovaCanzone)
console.log(playlist);

for (const canzone of playlist) {
  console.log(canzone.titolo)
}

// Elimina
const ultimaCanzone = playlist.pop()
console.log("Rimosso:", ultimaCanzone);


// ES: Accumulatore
const result = playlist.reduce((acc, canzone) => {
  // Modifica dei singoli oggetti "canzone": Il titolo sarà in maiuscolo
  const canzoneModificata = { ...canzone, titolo: canzone.titolo.toUpperCase() };
  return [...acc, canzoneModificata];
},
// Array di oggetti iniziale, il cui titolo è in maiuscolo
[ { ...nuovaCanzone, titolo: nuovaCanzone.titolo.toUpperCase() } ]
);

console.log(result)