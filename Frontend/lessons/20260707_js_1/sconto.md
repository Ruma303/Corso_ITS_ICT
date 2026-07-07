Scrivi un piccolo programma che genera uno **sconto** per un ordine e ne stampa il riepilogo. Lavora nella **console del browser** (F12 → Console) o in un file `sconto.js`. Usa **solo** le cose viste in questo blocco: `const`/`let`, tipi primitivi, `toFixed`, `Math.*`. **Niente template literals** (prossimo blocco): usa `console.log("...", x)` e `+`.

### Consegna
- Dati: `prezzoListino = 49.956`, `percentualeSconto = 20`, `speseSpedizione = 5`
- Genera un **ID ordine** casuale con `Math.floor(Math.random() * 100000)`, anteposto a `"ord-"` (es. `"ord-42173"`)
- Genera un **codice sconto** con `Math`, anteposto a `"SCN-"` (es. `"SCN-8812"`)
- **Arrotonda** il prezzo a 2 decimali con `Math.round(prezzo * 100) / 100` (evita il trabocchetto `0.1 + 0.2`)
- **Calcola** lo sconto (`prezzo * percentuale / 100`) e il **totale** (prezzo scontato + spedizione)
- Stampa il **riepilogo** in console: ID, codice sconto, prezzo listino, sconto, spedizione, totale — tutti i soldi con `toFixed(2)`
- Trova il **prezzo più basso** di un catalogo con `Math.min(49.96, 12.50, 30.00)`
- Un **contatore** `let ordiniOggi` incrementato due volte con `++`

### Criteri di accettazione
- [ ] ID ordine e codice sconto generati con `Math.floor(Math.random() * 100000)` + prefisso.
- [ ] Il prezzo è arrotondato con `Math.round(prezzo * 100) / 100` (non con `toFixed`, che ritorna stringa).
- [ ] Il totale è mostrato con `toFixed(2)` (es. `€44.97`).
- [ ] `Math.min` trova il prezzo più basso del catalogo.
- [ ] Il contatore usa `let` (non `const`) e si incrementa con `++`.
- [ ] Niente `var`, niente template literals.

### Svolgimento (15 min, può sforare) / Regole
- Niente DOM, niente template literals: solo `console.log` con `+` e virgola.
