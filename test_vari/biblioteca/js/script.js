const playlist = {
    titolo: "Voci per la Pace",
    artisti: ["Bob Dylan", "John Lennon", "Bob Marley"],
    tracce: [
        {
            titolo: "Blowing in the Wind",
            artista: "Bob Dylan",
            secondi: 230,
        },
        {
            titolo: "The Times They Are a-Changin'",
            artista: "Bob Dylan",
            secondi: 328,
        },
        {
            titolo: "Like a Rolling Stone",
            artista: "Bob Dylan",
            secondi: 365,
        },
        {
            titolo: "Knockin' on Heaven's Door",
            artista: "Bob Dylan",
            secondi: 250,
        },
        { titolo: "Imagine", artista: "John Lennon", secondi: 183 },
        {
            titolo: "Give Peace a Chance",
            artista: "John Lennon",
            secondi: 238,
        },
        {
            titolo: "Beautiful Boy (Darling Boy)",
            artista: "John Lennon",
            secondi: 252,
        },
        {
            titolo: "Redemption Song",
            artista: "Bob Marley",
            secondi: 220,
        },
        { titolo: "One Love", artista: "Bob Marley", secondi: 233 },
        {
            titolo: "Three Little Birds",
            artista: "Bob Marley",
            secondi: 195,
        },
    ],
};

// Metodi di utilità

// Mostra tutti gli artisti
const allArtisti = () => {
    return playlist.artisti.join(", ");
};

console.log(allArtisti());

// Aggiunta altri artisti

const altriArtisti = ["Oasis", "Cold Play", "Vasco Rossi"];

const tuttiGliArtisti = playlist.artisti.concat(altriArtisti);

console.log(tuttiGliArtisti);

// Da array a stringa
const tuttiGliArtistiInFila = tuttiGliArtisti.join(", ");
console.log(tuttiGliArtisti.join(", "));

// Da stringa a array
const arrayDiArtisti = tuttiGliArtistiInFila.split(", ");

console.log(arrayDiArtisti);

// Porzione di array
const primi5 = arrayDiArtisti.slice(0, 5);
console.log(primi5);

//
const daAggiungere = [...arrayDiArtisti];

// Aggiunge in posizione indicata (2) gli elementi passati
daAggiungere.splice(2, 0, "Santana", "Micheal Jackson", "EVH");
console.log(daAggiungere);

const rimossi = [...daAggiungere];

rimossi.splice(4, 3); // Ne rimuove 3
console.log(rimossi);

// Sostituire
// Toglie 2 elementi e ne mette 1 "UNKNOWN"
const sostituiti = [...rimossi];
sostituiti.splice(3, 2, "UNKNOWN");
console.log(sostituiti);

// Imposta tutti a valore comune
// sostituiti.fill("UNKNOWN", 0)
// console.log(sostituiti)

// Metodi di aggiunta e rimozione

sostituiti.push("Negramaro");
console.log(sostituiti);

const ultimoArtista = sostituiti.pop();
console.log("rimosso", ultimoArtista);

sostituiti.unshift("Lorna Shore");
console.log(sostituiti);

const rimossoInTesta = sostituiti.shift();
console.log(rimossoInTesta);

console.log(sostituiti);

// Method Chaining

// 1. Metodi iterativi
console.log("METODI ITERATIVI");

const tracce = () =>
    playlist.tracce.forEach(function (e) {
        console.log(e);
    });

tracce();

console.log("\nTracce 2\n");
const tracce2 = () =>
    playlist.tracce.forEach((e, i) => {
        const valore = 0;
        console.log(`${i + 1} -> ${e.titolo.toLocaleUpperCase()}`);
        return valore;
    });
tracce2();

// 2. Metodi di mutazione

// Array di titoli
const titoli = () => {
    return playlist.tracce.map((obj) => obj.artista);
};

console.log(titoli());

// Filtrare solo canzoni di Bob Dylan

const bobsSong = () =>
    playlist.tracce
        // Filtrato per artista
        .filter((e) => e.artista === "Bob Dylan")
        // Recuperato solo il campo "titolo"
        .map((canzone) => canzone.titolo);

console.log(bobsSong());

// Ordinamento alfabetico delle canzoni

const canzoniOrdinate = () => {
    return (
        playlist.tracce
            // a - b // ascendente
            // b - a // discendente
            .sort((a, b) =>
                a.titolo.localeCompare(b.titolo, {
                    sensitivity: "base",
                }),
            )
            // Se mi servono solo i titoli, posso mappare
            .map((canzone) => canzone.titolo)
    );
};

console.log(canzoniOrdinate());


// Metodi di riduzione ...