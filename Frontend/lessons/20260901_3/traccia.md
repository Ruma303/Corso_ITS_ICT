# Esercizio finale — La dashboard SportBook interattiva

Rifai sul tuo PC la **stessa trasformazione** della dashboard Centro Sportivo vista nel live coding: `centro-sportivo.html` (con `id="campi-container"`, `id="lista-prenotazioni"` e il form già collegato), `script.js` (con i dati e il log iniziale), `campi.json` e `style.css`. Alla fine avrai il **progetto SportBook funzionante in JS**: è lo stesso progetto che **domani lo tipizzeremo con TypeScript**.

**Partenza**: apri i file della cartella di SportBook (o il file zip passato in chat). L'HTML è già pronto: tu devi scrivere il JS che lo fa vivere, passo per passo, come nel live coding.

### Consegna

1. **Collega il JS e verifica**: in `script.js` lascia `"use strict";` e il `console.log("SportBook JS caricato")`; apri la pagina nel browser e verifica il log in console (F12).
2. **Render della lista prenotazioni**: scrivi `renderPrenotazioni(lista)` che svuota `#lista-prenotazioni` con `replaceChildren()`, cicla l'array con `forEach`, crea ogni `<li class="list-group-item d-flex justify-content-between align-items-center">` con `createElement` + `textContent` (mai `innerHTML`).
3. **Submit del form**: `addEventListener("submit", ...)` sul form con `e.preventDefault()` come **prima riga**, leggi i valori con `FormData`, crea l'oggetto prenotazione (con `id: "p" + Date.now()`), `push`, `renderPrenotazioni`, `form.reset()`, e mostra il toast di conferma (auto-hide dopo 3s con `setTimeout`).
4. **Bottone "Annulla"**: su ogni `<li>` aggiungi un bottone con `data-id`, gestito con **event delegation** sul container (`closest("button[data-id]")`), che rimuove la prenotazione con `filter` e ri-renderizza.
5. **Contatore sessione**: aggiungi nell'HTML (sopra la lista) un `<span id="sessione" class="badge bg-secondary ms-2"></span>` e in JS fallo aggiornare ogni secondo con `setInterval` (e commento su `clearInterval` per fermarlo).
6. **Fetch di `campi.json`**: `async function caricaCampi()` con `fetch`, `if (!r.ok) throw`, `await r.json()`, `renderCampi(campi)`; mostra "⏳ Caricamento campi…" PRIMA del fetch e "⚠️ Errore di caricamento" nel `catch`. Scrivi anche `renderCampi(lista)` (colonna → card → body → titolo/testo, come nella slide "Render delle card da array").
7. **localStorage**: `salvaPrenotazioni(lista)` con `JSON.stringify` e `caricaPrenotazioni()` con `JSON.parse` in `try/catch`; all'avvio carica le prenotazioni salvate.

**Criteri di accettazione**:
- [ ] Il JS è collegato e il log iniziale stampa in console.
- [ ] La lista si renderizza con `replaceChildren` + `forEach` + `createElement` + `textContent`.
- [ ] Il form aggiunge una prenotazione **senza ricaricare** la pagina (`preventDefault` in cima).
- [ ] Il bottone "Annulla" funziona anche sulle prenotazioni aggiunte dopo (event delegation con `closest`).
- [ ] Il toast di conferma si nasconde da solo dopo 3s (`setTimeout`).
- [ ] Le card dei campi si generano da `campi.json` via `fetch` + `async/await` + `try/catch`, con check `response.ok`.
- [ ] Dopo un refresh, le prenotazioni ci sono ancora (`localStorage` + `JSON.stringify`/`JSON.parse`).
- [ ] Nessun `innerHTML` con dati utente (solo `textContent`).
- [ ] Nessun errore in console.