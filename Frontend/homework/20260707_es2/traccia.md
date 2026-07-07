# Esercizio Finale - Lezione Javascript Parte 1
Scade domani alle 19:00

## Istruzioni
Rifai sul tuo PC la stessa trasformazione che hai visto nel live coding — scrivere il validatore di prenotazione in JavaScript — ma partendo dai tuoi file della Lezione 4 (la dashboard Bootstrap centro-sportivo.html + style.css) ed evolvendoli con un file prenotazione.js, passo per passo.

Partenza:
- Apri i tuoi file L4 (dashboard Bootstrap).
- Crea un file prenotazione.js e collegalo in fondo al <body> di centro-sportivo.html (prima di </body>), come nella Macro 19 del live coding.
- Lavori su questi file (in loco — se vuoi conservare la versione docente, fanne una copia prima).
- Non creare una nuova pagina scollegata: ripercorri lo stesso percorso visto nel live coding (variabili, tipi, logica, cicli sui dati della prenotazione, solo console.log).
- L'obiettivo è consolidare esattamente i concetti di oggi, applicandoli da capo da soli. Niente DOM: si lavora solo con dati in console.

---

## Dati di partenza (incolla in cima al file)

```js
const campi = [
  { id: "c1", nome: "Calcio",  prezzoOrario: 50, coperto: true  },
  { id: "c2", nome: "Padel",   prezzoOrario: 30, coperto: true  },
  { id: "c3", nome: "Tennis",  prezzoOrario: 25, coperto: false }
];


// Prenotazione in arrivo dal form (per ora: variabili, non DOM)

// Nota: il nome arriva "sporco" (spazi + minuscolo) — va normalizzato con trim + capitalizza const nome = "  mario  "; const email = "mario@example.com"; const campoId = "c1"; const data = "2026-07-01"; const ore = 3;
```

---

## Consegna (il compito principale)

Ricostruisci, dalle tue note + la documentazione MDN, gli stessi passi visti nel live coding, applicati al validatore di prenotazione:

- **Dichiarazione variabili** con const/let per i dati della prenotazione (nome, email, campoId, data, ore).

- **Normalizza nome** con metodi stringa: nome.trim() → capitalizza la prima lettera (pulito[0].toUpperCase() + pulito.slice(1)); valida email con email.includes("@") + email.split("@").length === 2.

- **Validazione nome**: nome non vuoto (dopo trim) → se invalido, stampa motivo con console.log.

- **Validazione campo**: verifica che il campoId esista tra i campi (ciclo for…of); se non trovato, stampa motivo.

- **Validazione data con Date**: costruisci new Date(data) e verifica NON sia nel passato (data < new Date()); se lo è, stampa motivo.
Formatta la data in gg/mm/aaaa con getDate/getMonth()+1/getFullYear.

- **ID prenotazione casuale** con Math.floor(Math.random() * 100000), anteposto a "p-" (es. "p-42173"); stampa l'ID nel report.

- **Riepilogo campi con for…of**: per ogni campo stampa "Calcio: €50/h, coperto" oppure "Tennis: €25/h, scoperto" usando un ternary su coperto.

- **Default valori** con ?? / || dove serve (es. nome vuoto → "Ospite" solo per display).

### Report finale in console del tipo:
=== RISULTATO VALIDAZIONE ===
ID: p-42173
Esito: ✅ Valida / ❌ Invalida Motivo: ...
Data: 01/07/2026
Totale: €<totale calcolato con sconto, 2 decimali>


## Criteri di accettazione (cosa deve risultare)
- Il file prenotazione.js è collegato a centro-sportivo.html in fondo al <body>, prima di </body>.

- Il nome viene normalizzato con trim() + capitalizzazione (" mario " → "Mario"); la email è validata con includes("@") + split("@").length === 2.

- Con nome = "Mario", campoId = "c1", ore = 3, data futura: esito Valida, totale €150.00 (prezzo pieno), ID generato tipo p-42173.

- Con nome = "Mario", campoId = "c1", ore = 6, data futura: esito Valida, totale con sconto 10% (€270.00).

- Con nome = "": esito Invalida, motivo "Nome mancante".

- Con campoId = "c9" (inesistente): esito Invalida, motivo "Campo non trovato".

- Con data = "2020-01-01" (passata): esito Invalida, motivo "Data nel passato".

- Il totale è stampato con toFixed(2) (es. €150.00), e ore è convertito con Number() se trattato come stringa.

- Il riepilogo cicla tutti e 3 i campi con un for…of e usa un ternary per "coperto"/"scoperto".

- Niente var, niente == (solo ===), niente if (x === NaN).

- Niente manipolazione del DOM: solo console.log.