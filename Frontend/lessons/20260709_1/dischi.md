Gestisci l'**inventario di un negozio di dischi**: un array di oggetti disco (`id`, `titolo`, `artista`, `prezzo`, `inStock`). Lavora in console o in un file `dischi.js`. Usa gli **oggetti letterali** con shorthand (`{ titolo, artista }`) per costruire un nuovo disco, `findIndex` + `splice` per rimuovere per `id` (mutabile, con guard `-1`), `filter` per la versione immutabile, e `reduce` per il valore totale dell'inventario.

### Dati di partenza
```js
const inventario = [
  { id: "d1", titolo: "Highway 61 Revisited", artista: "Bob Dylan",       prezzo: 25, inStock: true  },
  { id: "d2", titolo: "Abbey Road",            artista: "The Beatles",     prezzo: 30, inStock: true  },
  { id: "d3", titolo: "Kind of Blue",          artista: "Miles Davis",     prezzo: 35, inStock: false },
  { id: "d4", titolo: "Aretha Now",            artista: "Aretha Franklin",  prezzo: 28, inStock: true  }
];
```

### Consegna
- **Crea un nuovo disco** con oggetto letterale usando **shorthand**: dichiara `const titolo = "Blue";` e `const artista = "Joni Mitchell";` e costruisci `const nuovoDisco = { id: "d5", titolo, artista, prezzo: 22, inStock: true }` (le chiavi `titolo`/`artista` sono shorthand per `titolo: titolo`/`artista: artista`).
- **Aggiungi in fondo** con `push` (mutabile) e stampa la nuova lunghezza.
- **Applica uno sconto del 10%** al disco con `id === "d1"`: trova l'indice con `findIndex`, poi muta `inventario[i].prezzo = inventario[i].prezzo * 0.9` (con guard `if (i !== -1)`). Stampa il prezzo scontato con `toFixed(2)`.
- **Rimuovi per `id`** (mutabile): imposta `idDaRimuovere = "d2"`, trova l'indice con `findIndex`, rimuovi con `splice(i, 1)` SOLO se `i !== -1`. Stampa il titolo rimosso (ricorda: `splice` ritorna un array degli elementi rimossi).
- **Tenta con id inesistente**: `"d9"`. `findIndex` ritorna `-1`. Il guard `if (i !== -1)` deve impedire `splice(-1, 1)` che **toglierebbe l'ultimo disco per sbaglio**. Stampa `"d9 non trovato"` e verifica che la lunghezza è invariata.
- **Valore totale dell'inventario** con `reduce` (somma dei `prezzo`), stampato con `toFixed(2)`.
- **Versione immutabile**: rimuovi `d3` con `filter` (`const senzaD3 = inventario.filter(d => d.id !== "d3")`) — nuovo array di lunghezza 3, originale intatto (stampa entrambe le lunghezze).

### Criteri di accettazione
- [ ] Il nuovo disco è costruito con **shorthand** (`{ titolo, artista }`, non `{ titolo: titolo, artista: artista }`).
- [ ] `findIndex` trova l'indice di `d1` e lo sconto è applicato mutando `.prezzo` (con guard `if (i !== -1)`).
- [ ] `findIndex` + `splice` rimuovono `d2` (lunghezza -1); `splice` ritorna un array, ne stampi il primo elemento.
- [ ] `findIndex` su `"d9"` ritorna `-1`; il guard `if (i !== -1)` **impedisce** `splice(-1, 1)` (che toglierebbe l'ultimo) — la lunghezza resta invariata.
- [ ] `reduce` calcola il totale dei `prezzo` con valore iniziale `0`.
- [ ] `filter` per la versione immutabile lascia l'originale intatto (originale e nuovo hanno lunghezze diverse).
- [ ] Niente `Object.keys`, destrutturazione, closure, JSON (slide non ancora viste). Arrow functions e spread sono già viste: usale.