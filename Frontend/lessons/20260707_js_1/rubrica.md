Normalizza un contatto "sporco" di una rubrica e decidi se è **completo** o **incompleto**. Lavora in console o in un file `rubrica.js`. Usa i **template literals** per il riepilogo (ora li hai visti).

### Consegna
- Dati: `nomeSporco = "  mario  "`, `email = "mario@example.com"`, `telefono = ""`, `note = null`
- **Normalizza** il nome: `trim()` + capitalizza la prima lettera (`pulito[0].toUpperCase() + pulito.slice(1)`) → `"Mario"`
- **Valida** l'email con `email.includes("@")` + `email.split("@").length === 2`
- **Default**: il telefono vuoto (`""`) diventa `"non fornito"` con `||`; le note `null` diventano `"nessuna nota"` con `??` (la distinzione chiave del blocco)
- **Conta** i campi compilati con `if` + `===` (nome non vuoto, email valida, telefono non vuoto)
- **Stato** del contatto con un **ternary**: `"completo"` se ha almeno 2 campi compilati, altrimenti `"incompleto"`
- Usa **`Boolean()`** per ottenere un booleano esplicito (es. "ha note?")
- **Riepilogo** in console con i template literals

### Criteri di accettazione
- [ ] Il nome `"  mario  "` diventa `"Mario"` (`trim` + capitalizza).
- [ ] L'email è validata con `includes("@")` + `split("@").length === 2`.
- [ ] Il telefono vuoto → `"non fornito"` con `||`; le note `null` → `"nessuna nota"` con `??` (non `||` per null, non `??` per la stringa vuota).
- [ ] Lo stato è `"completo"` o `"incompleto"` via **ternary**.
- [ ] I confronti usano `===` (mai `==`).
- [ ] `Boolean()` è usato per un booleano esplicito.
- [ ] Il riepilogo usa i **template literals** (backtick + `${}`).