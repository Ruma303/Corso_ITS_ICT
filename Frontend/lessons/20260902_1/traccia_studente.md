Crea una classe `Studente` con campi privati e un voto gestito tramite getter/setter con validazione. File `studente.ts` a parte, scollegato dalla dashboard.

### Consegna
- Classe `Studente` con `readonly #matricola: string`, `#nome: string`, `#voto: number` (tutti `#privati`)
- **Costruttore** che assegna i campi e incrementa un contatore `static totaleIscritti = 0`
- **Getter/setter per `voto`** con **validazione**: fuori range 0-10 viene "clampato" (0 se <0, 10 se >10); `NaN` lancia `Error`
- **Getter/setter per `nome`**: il setter fa `trim()` e rifiuta la stringa vuota
- Metodo `esito(): "promosso" | "rimandato" | "bocciato"` (≥6 promosso, ≥4 rimandato, sotto bocciato) e `descrivi(): string` che ritorna `"Mario (mat. m1) — voto 7/10: promosso"`
- Prova: voto iniziale 12 → clamp a 10; `s.voto = -3` → clamp a 0; `new Studente("m3", "Anna", Number("abc"))` → `NaN` → throw

### Criteri di accettazione
- [ ] I campi sono `#privati`; `#matricola` è anche `readonly`
- [ ] Il setter di `voto` clampa nel range 0-10 e lancia su `NaN`
- [ ] Il **costruttore** valida il voto iniziale (stessa logica del setter o un helper privato)
- [ ] Il setter di `nome` fa `trim()` e rifiuta la stringa vuota
- [ ] `static totaleIscritti` si incrementa a ogni `new` e si legge via `Studente.totaleIscritti`
- [ ] `tsc` compila senza errori con `strict: true`; niente `any`