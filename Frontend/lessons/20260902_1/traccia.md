Modella lo **stato di una spedizione** di un servizio di logistica. Crea un file `spedizioni.ts` con `tsc --watch` attivo.

### Consegna
- Definisci la literal union `type StatoSpedizione = "in-transito" | "giacenza" | "consegnato" | "fallito"`
- Definisci `type Spedizione = { id: string; destinatario: string; citta: string; stato: StatoSpedizione }` (usa `type`, non `interface`)
- Crea 3-4 spedizioni in un array `spedizioni: Spedizione[]` con stati diversi
- Scrivi `descriviSpedizione(s: Spedizione): string` che usa `if/else if` con `===` per ogni stato (dentro il ramo TS sa che `s.stato` è quel valore — **narrowing**)
- Scrivi `spedizioniInGiacenza(spedizioni: Spedizione[]): Spedizione[]` che filtra con `for…of` + `push`
- Prova ad assegnare `s.stato = "in transit"` (typo) e `"Consegnato"` (maiuscolo): devono dare **errore TS**

### Criteri di accettazione
- [ ] `StatoSpedizione` è una literal union con i 4 valori esatti
- [ ] `Spedizione` è un `type` alias con `stato: StatoSpedizione` (non `string`)
- [ ] Assegnare `"in transit"` o `"Consegnato"` produce errore TS
- [ ] `descriviSpedizione` usa `if/else if` con `===` e ritorna un messaggio per ogni stato
- [ ] `spedizioniInGiacenza` ritorna solo le spedizioni con `stato === "giacenza"`
- [ ] `tsc` compila senza errori; niente `any`, niente `enum`, niente `interface`