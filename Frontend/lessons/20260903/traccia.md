# Esercizio: Form di Ricerca e Filtraggio Dati Persona

## Obiettivo

Realizzare un'applicazione web in HTML e JavaScript (poi TypeScript) che consenta di caricare un elenco di persone da un file JSON, validare i dati, e permettere all'utente di filtrarli tramite un form di ricerca dinamico, mostrando i risultati in una tabella HTML.

---

## Traccia dei Punti da Svolgere

### Punto 1: Caricamento Dati Asincrono da File JSON

* Effettua una chiamata asincrona via `fetch` al file `persone.json`.
* Verifica la risposta HTTP e gestisci eventuali errori di rete o file vuoto.
* Converti i dati in un array di oggetti e salvali in una variabile globale `risultati` **solo dopo averli filtrati** tramite la funzione di validazione.
* **Nota:** Al caricamento iniziale della pagina, la sezione dei risultati deve rimanere nascosta.

### Punto 2: Validazione dei Dati JSON

* Crea una funzione `validaDati(person)` che riceva un oggetto e restituisca un booleano.
* Verifica che l'oggetto contenga le seguenti proprietà valide:
  * `nome`: stringa non vuota.
  * `cognome`: stringa non vuota.
  * `eta`: numero compreso tra `18` e `100`.
  * `sesso`: stringa pari a `"male"` o `"female"` (case-insensitive).
* Inserire altri campi come `telefono` ma, non avendo i corrispettivi dati negli oggetti JSON, dovranno ritornare valori nulli accedendo in sicurezza.

### Punto 3: Intercettazione dell'Invio Form (Submit)

* Aggiungi un event listener per l'evento `submit` del form `#form`.
* Previeni il comportamento di default dell'invio con `e.preventDefault()`.
* Estrai i valori dei campi (`nome`, `cognome`, `eta`, `sesso`) utilizzando l'oggetto `FormData` (o singoli campi con `.value` se preferisci).
* Pulisci e formatta le stringhe estratte (rimozione spazi ed eventuale conversione in minuscolo) e gestisci i valori numerici o opzionali.

### Punto 4: Filtraggio Dati del Form

* Crea una funzione `risultatiFiltrati(filtri)` che accetti i criteri estrapolati dal form.
* Filtra l'array globale `risultati` verificando che:
  * Il nome/cognome del record includa il testo cercato (ricerca parziale/case-insensitive).
  * L'età del record corrisponda esattamente a quella inserita (se presente).
  * Il sesso corrisponda esattamente a quello selezionato (se presente).
  * Se un campo del form viene lasciato vuoto, non deve applicare alcun vincolo di filtraggio per quel parametro.

### Punto 5: Rendering Dinamico dei Risultati in HTML

* Crea una funzione `creaRisultati(data)` che riceva l'array di risultati filtrati.
* Svuota il contenuto precedente del `<tbody>`.
* Per ogni oggetto nell'array:
  * Crea un elemento `<tr>`.
  * Crea le celle `<td>` per `nome`, `cognome`, `eta`, `sesso` (convertendo `"male"`/`"female"` in `"Maschio"`/`"Femmina"`) e `telefono`.
  * Gestisci i valori opzionali/mancanti (come il telefono) inserendo una stringa vuota `""`.
* Aggiungi le righe alla tabella e rendi visibile la sezione `#result-section` rimuovendo la classe `.hidden`.

### Punto 6: Gestione del Reset

* Aggiungi un event listener per l'evento `click` sul pulsante di reset (`button[type="reset"]`).
* All'azione di reset:
  * Svuota i dati inseriti nella tabella (`tbody.replaceChildren()`).
  * Nascondi la sezione `#result-section` riapplicando la classe `.hidden`.
  * **Attenzione:** Mantieni intatti sia l'array globale dei dati caricati sia la struttura HTML della tabella.

---

## 🌟 BONUS: Convertire l'applicazione in TypeScript

Traduci l'intera logica da JavaScript a **TypeScript** applicando le tipizzazioni rigide:

1. **Definizione dei Tipi e Interfacce:**
* Crea un tipo personalizzato per il sesso: `type Sesso = "male" | "female";`.
* Definisci un'interfaccia `Persona` per modellare la struttura dei dati JSON:
  * `nome: string;`
  * `cognome: string;`
  * `eta: number;`
  * `sesso: Sesso | string;`
  * `telefono?: string;` (proprietà opzionale)
* Definisci un'interfaccia `FiltriForm` per la tipizzazione dei criteri di ricerca.

2. **Tipizzazione del DOM e Null-Safety:**
* Seleziona gli elementi DOM mediante casting sicuro (`as HTMLFormElement | null`, `as HTMLElement | null`).
* Gestisci la presenza dei nodi evitando l'uso dell'operatore non-null `!` (usa controlli con `if`).

3. **Eventi e Form:**
* Tipizza correttamente l'evento del form come `SubmitEvent` e l'evento di reset.
* Estrai i dati da `FormData` con il cast appropriato (`as string`).

4. **Compilazione:**
* Configura un file `tsconfig.json` con `"strict": true` per verificare l'assenza di `any` impliciti ed errori di tipo.