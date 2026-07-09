Gestisci un **registro dipendenti** come array di oggetti (`id`, `nome`, `ruolo`, `stipendio`, `assunzione` come `new Date(...)`, `attivo`). Lavora in console o in un file `hr.js`. Serializza e deserializza l'array con `JSON.stringify`/`JSON.parse`, e scopri cosa succede alla `Date` dopo il round-trip.

### Dati di partenza
```js
const dipendenti = [
  { id: "e1", nome: "Alice", ruolo: "dev",    stipendio: 2500, assunzione: new Date("2021-03-01"), attivo: true  },
  { id: "e2", nome: "Bob",   ruolo: "dev",    stipendio: 2200, assunzione: new Date("2022-09-15"), attivo: true  },
  { id: "e3", nome: "Carla", ruolo: "hr",      stipendio: 2000, assunzione: new Date("2020-06-10"), attivo: false },
  { id: "e4", nome: "Dario", ruolo: "design", stipendio: 2100, assunzione: new Date("2023-01-20"), attivo: true  }
];
```

### Consegna
- **Aggiungi "Eve"** con spread (immutabile): `const conEve = [...dipendenti, { id: "e5", nome: "Eve", ruolo: "dev", stipendio: 2400, assunzione: new Date("2024-04-01"), attivo: true }]`. Stampa le lunghezze di `dipendenti` (4, intatto) e `conEve` (5).
- **`find` per id**: trova il dipendente con `id === "e2"` e stampalo (con guard `if (bob)`).
- **`filter` attivi**: i dipendenti con `attivo === true`; estrai i nomi con `map` e stampali.
- **`reduce` stipendio totale** degli attivi (somma dei `stipendio` dove `attivo === true`).
- **`reduce` raggruppa per ruolo**: oggetto `{ dev: 2, hr: 1, design: 1 }` (conteggio, valore iniziale `{}`).
- **Report con `Object.entries`**: itera il conteggio per ruolo con `for (const [ruolo, n] of Object.entries(...))` e stampa righe `"Ruolo dev: 2 dipendenti"`.
- **Rimuovi "e3"** (mutabile) con `findIndex` + `splice` (con guard `-1`); stampa la nuova lunghezza.
- **`JSON.stringify`**: serializza `dipendenti` in una stringa `json`; stampa `typeof json` (deve essere `"string"`).
- **`JSON.parse`**: ricostruisci l'array con `const ricostrutti = JSON.parse(json)`; verifica `ricostrutti.length` e `ricostrutti[0].nome === "Alice"`.
- **Trappola `Date`**: stampa `ricostrutti[0].assunzione` e il suo `typeof` → è una **stringa** (non più un Date). Tenta (commentato) `ricostrutti[0].assunzione.getFullYear()` → `TypeError`. Recupera la data con `new Date(ricostrutti[0].assunzione)` e chiama `.getFullYear()` per mostrare che funziona di nuovo.

### Criteri di accettazione
- [ ] Spread aggiunge "Eve" senza mutare l'originale (originale resta 4, nuovo 5).
- [ ] `find` per id con guard `if (bob)`; `filter` + `map` stampano i nomi degli attivi (`["Alice", "Bob", "Dario"]`).
- [ ] `reduce` calcola lo stipendio totale degli attivi (6800) con valore iniziale `0`.
- [ ] `reduce` raggruppa per ruolo con valore iniziale `{}` → `{ dev: 2, hr: 1, design: 1 }`.
- [ ] `Object.entries` itera il conteggio e stampa 3 righe (una per ruolo).
- [ ] `findIndex` + `splice` rimuovono "e3" con guard `if (i !== -1)`; la lunghezza scende a 3.
- [ ] `JSON.stringify(dipendenti)` ritorna una stringa (`typeof` === `"string"`).
- [ ] `JSON.parse` ricostruisce l'array: `ricostrutti.length === 3` e `ricostrutti[0].nome === "Alice"`.
- [ ] **Trappola gestita**: `ricostrutti[0].assunzione` è una stringa dopo il round-trip (`typeof` === `"string"`); il codice mostra `new Date(ricostrutti[0].assunzione).getFullYear()` per riottenerla come Date.
 