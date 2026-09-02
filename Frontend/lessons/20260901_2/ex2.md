Crea una pagina a parte `newsletter.html` + `newsletter.js` (scollegata dalla dashboard). Un form con un campo email e un bottone "Iscriviti". Al submit, intercetta l'evento con `addEventListener` + `preventDefault` (la pagina NON deve ricaricare), poi avvia un **countdown da 5 a 0** con `setInterval` e, quando arriva a 0, mostra un banner di conferma che si auto-nasconde dopo 3s con `setTimeout`.

### HTML di base

```html
<form id="form-news">
  <label>Email: <input type="email" name="email" id="email" required></label>
  <button type="submit" class="btn btn-primary">Iscriviti</button>
</form>
<p id="countdown" class="badge bg-secondary"></p>
<p id="messaggio" class="d-none"></p>
```

### Consegna

- Seleziona il form, registra un listener `submit` con `e.preventDefault()` come **prima riga**.
- Leggi l'email con `FormData` (o `document.querySelector("#email").value`); valida minima con `includes("@")`.
- Se l'email è valida: avvia un **countdown da 5 a 0** con `setInterval` (aggiorna il testo di `#countdown` a ogni tick). Quando arriva a 0, **ferma l'intervallo con `clearInterval(id)`**.
- A countdown finito, mostra in `#messaggio` il testo `"✅ Iscrizione confermata per <email>"` (con `textContent`).
- Nascondi il messaggio dopo 3 secondi con `setTimeout` (aggiungi la classe `d-none` con `classList.add`).
- Se l'email non è valida, mostra in `#messaggio` un errore (con `classList` per colorarlo di rosso) senza avviare il countdown.

**Criteri di accettazione:**
- [ ] Il submit **non ricarica** la pagina (`preventDefault` in cima al listener).
- [ ] Il countdown parte da 5 e si aggiorna ogni secondo fino a 0.
- [ ] A 0 il `setInterval` è fermato con `clearInterval(id)` (niente tick infiniti, niente numeri negativi).
- [ ] Il messaggio di conferma appare e si nasconde dopo 3s (`setTimeout` + `classList.add("d-none")`).
- [ ] I dati utente (email) sono inseriti con `textContent`, mai `innerHTML`.
- [ ] Niente `localStorage`, niente `fetch`, niente event delegation: solo eventi + timer.