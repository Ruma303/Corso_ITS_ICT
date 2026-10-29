Aggiungere un contatore di posti prenotati a ciascuna CampoCard.

Requisiti:
• Stato posti inizializzato a 0 dentro CampoCard
• Due pulsanti: + e -
• Il contatore non deve mai scendere sotto zero
• Usare sempre la forma prev =› ...
• Un pulsante Azzera che riporta il valore a 0

Obiettivi / verifica:
• Il numero cambia in pagina, non solo in console
• Ogni card ha il proprio contatore indipendente
• React DevTools mostra lo stato di ciascuna card

Estensione: aggiungere uno stato booleano che mostra o nasconde la descrizione, con un pulsante
'Dettagli.

---

Gestire un elenco di prenotazioni nello stato di App.

Requisiti:
• Stato prenotazioni inizializzato a array vuoto
• Un pulsante su ogni CampoCard aggiunge una
prenotazione all'elenco
• Ogni prenotazione e' un oggetto con id, campo e
ora
• Un pulsante rimuove una prenotazione dall'elenco
(filter)

Obiettivi / verifica:
• L'elenco si aggiorna in pagina a ogni aggiunta e
rimozione
• Nessun uso di push o di assegnazioni dirette
• Il contatore e' sempre coerente con l'elenco
• Mostrare il numero di prenotazioni calcolandolo,

Estensione: aggiungere un pulsante che modifica l'ora di una prenotazione esistente usando map().