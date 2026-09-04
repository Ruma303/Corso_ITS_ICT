L'esercizio finale della L8 ti ha lasciato la **dashboard SportBook interattiva in JS** (render lista, form con FormData, toast, event delegation, contatore sessione, fetch di `campi.json`, localStorage). Oggi la **trasformi in TypeScript**: è la stessa trasformazione vista nel live coding, applicata al tuo progetto.

**Partenza**: apri i tuoi file della L8 (`centro-sportivo.html`, `script.js`, `campi.json`, `style.css`) nella cartella di lavoro. Rinomina `script.js` in `script.ts` e aggiungi i tipi, passo per passo.

### Consegna

1. **Setup**: crea `tsconfig.json` (strict, target ES2020, outDir dist) e `package.json` con scripts `build` e `watch`; rinomina `script.js` → `script.ts`; apri `tsc --watch`.
2. **Tipizza i dati**: definisci `type StatoPrenotazione = 'libero' | 'prenotato' | 'in attesa'` e le `interface` `Prenotazione` (id, nome, email, campo, data, ora, stato) e `Campo` (id, nome, tipo, coperto, posti); tipizza l'array `let prenotazioni: Prenotazione[]`.
3. **Tipizza il DOM**: `document.querySelector("#email") as HTMLInputElement | null` (e così per nome, lista, form); controlla il `null` con `if (el)` prima di leggere `.value`.
4. **Tipizza le funzioni**: `renderPrenotazioni(lista: Prenotazione[]): void`, `renderCampi(lista: Campo[]): void`, `caricaCampi(): Promise<void>`, `salvaPrenotazioni(lista: Prenotazione[]): void`, `caricaPrenotazioni(): Prenotazione[]`.
5. **Tipizza il FormData**: `const data = new FormData(form)` e `data.get("nome") as string` (mai `any`).
6. **Compila**: `tsc --watch` senza errori con `strict: true`; verifica che la pagina funzioni ancora (il browser esegue il `.js` generato).
7. **Prova il typo**: scrivi `stato = "liber"` da qualche parte, osserva l'errore rosso, poi correggilo: è il momento in cui TS ti salva.

**Criteri di accettazione**:
- [ ] `tsconfig.json` e `package.json` presenti con `strict: true`.
- [ ] `script.js` rinominato in `script.ts` e il `.js` generato non si tocca a mano.
- [ ] `type StatoPrenotazione` e `interface` `Prenotazione`/`Campo` definite.
- [ ] `prenotazioni: Prenotazione[]` — array tipizzato.
- [ ] Funzioni con parametri e ritorno tipizzati (`void` dove serve).
- [ ] DOM tipizzato con `as HTMLInputElement | null` + `if (el)` (niente `any`, niente `!` per zittire).
- [ ] `tsc --watch` compila senza errori con `strict: true`.
- [ ] La pagina funziona come alla fine della L8 (prova il form, il toast, l'annulla, il refresh).
- [ ] Niente `any`.