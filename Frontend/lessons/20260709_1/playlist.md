Gestisci una **playlist musicale**: un array di tracce (ogni traccia è un oggetto con `titolo`, `artista`, `secondi`, `riproducendo`). Lavora nella **console del browser** (F12 → Console) o in un file `playlist.js`. Usa **solo** le cose viste in questo blocco: array + indici + `length`, `push`/`pop`/`shift`, oggetti letterali `{ k: v }` + accesso `.prop`, function (dichiarazione/espressione), arrow functions, `forEach`, `map`, `filter`, `find`. Puoi usare i template literals di L5 per i riepiloghi.

### Dati di partenza
```js
const playlist = [
  { titolo: "Blowing in the Wind", artista: "Bob Dylan",   secondi: 230, riproducendo: false },
  { titolo: "Imagine",            artista: "John Lennon", secondi: 183, riproducendo: true  },
  { titolo: "Redemption Song",    artista: "Bob Marley",  secondi: 220, riproducendo: false },
  { titolo: "Blowin' Blues",      artista: "Bob Dylan",   secondi: 200, riproducendo: false }
];
```

### Consegna
- **Stampa la playlist** con `forEach`: una riga per traccia nel formato `"1. Imagine — John Lennon (3:03)"` (formatta i secondi in `m:ss` con `Math.floor(secondi / 60)` e `secondi % 60`, zero-padding sui secondi).
- **Estrai i titoli** con `map` → array di soli titoli; stampalo.
- **Filtra per artista** con `filter`: tutte le tracce di "Bob Dylan"; stampane i titoli (con un secondo `map`).
- **Trova la traccia in riproduzione** con `find` (la prima con `riproducendo === true`) → stampa titolo e artista.
- **Cerca per titolo esatto** con `find`: cerca `"Imagine"` (esiste) e poi `"blowing in the wind"` (case-sensitive: con `===` NON matcha perché minuscolo). Gestisci il caso non trovato: se `find` ritorna `undefined`, stampa `"Traccia non trovata"` — **NON accedere a `.artista` senza un guard**.
- **Aggiungi una traccia in fondo** con `push` (mutabile) e **togli l'ultima** con `pop`: salva il valore ritornato da `pop` e stampalo (non è l'array, è l'elemento rimosso).

### Criteri di accettazione
- [ ] La playlist è stampata con `forEach` e i secondi sono formattati `m:ss` (es. `3:03` per 183 secondi, con zero-padding).
- [ ] `map` produce un array di 4 soli titoli.
- [ ] `filter` su "Bob Dylan" ritorna 2 tracce; i titoli sono estratti con un secondo `map`.
- [ ] `find` sulla traccia in riproduzione ritorna l'oggetto "Imagine".
- [ ] La ricerca per titolo usa `===` (case-sensitive): `"Imagine"` matcha; `"blowing in the wind"` NO → stampi `"Traccia non trovata"` senza crashare (c'è un guard `if (trovata)`).
- [ ] `push` aggiunge una traccia (lunghezza 5); `pop` rimuove e ritorna l'elemento rimosso (salvi il valore, non l'array).
- [ ] Niente `findIndex`, `splice`, `sort`, `some`/`every`, `reduce`, `spread`, `Object.keys`, destrutturazione, shorthand/metodi oggetti (slide non ancora viste). Le **arrow functions** e l'accesso `.prop` agli oggetti sono invece consentiti (slide già viste).