# Istruzioni Esercizio finale

Rifai sul tuo PC la stessa trasformazione che hai visto nel live coding — modellare le prenotazioni come array di oggetti e manipolarle con filter / map / reduce / destrutturazione / arrow / JSON — ma partendo dai tuoi file della Lezione 5 (centro-sportivo.html + script.js con il validatore di prenotazione) ed evolvendoli in un servizio di report prenotazioni, passo per passo.

Partenza: apri i tuoi file L5. Lavori su questi file (in luogo — se vuoi conservare la versione docente, fanne una copia prima). Aggiungi al script.js un nuovo blocco con il modello dati prenotazioni (array di oggetti, la stessa "forma" usata nel live coding) e le funzioni di report qui sotto. Non creare una nuova pagina scollegata: ripercorri lo stesso percorso visto nel live coding (filter → map → reduce → destrutturazione → arrow → JSON). L'obiettivo è consolidare esattamente i concetti di oggi, applicandoli da capo da soli. Lavorate in console (console.log nel script.js, oppure un file report.js separato, oppure la console del browser).

## Consegna (il compito principale)
Usa questo array di partenza (la stessa "forma" del live coding, cambiano i dati):

```js
const prenotazioni = [   { nome: "Giulia", email: "giulia@x.it", campo: "padel",  data: "2026-08-01", ora: "10:00", stato: "prenotato",  prezzo: 30 },   { nome: "Marco",  email: "marco@x.it",  campo: "calcio", data: "2026-08-01", ora: "12:00", stato: "in attesa",  prezzo: 50 },   { nome: "Elena",  email: "elena@x.it",  campo: "tennis", data: "2026-08-02", ora: "09:00", stato: "prenotato",  prezzo: 25 },   { nome: "Roberto",email: "roberto@x.it",campo: "calcio", data: "2026-08-02", ora: "16:00", stato: "libero",     prezzo: 50 },   { nome: "Chiara", email: "chiara@x.it", campo: "padel",  data: "2026-08-03", ora: "18:00", stato: "prenotato",  prezzo: 30 },   { nome: "Andrea", email: "andrea@x.it", campo: "tennis", data: "2026-08-03", ora: "11:00", stato: "in attesa",  prezzo: 25 } ];
```

Ricostruite le funzioni di report viste nel live coding (le stesse categorie di trasformazione: filter per selezionare, map per trasformare, reduce per accumulare/raccogliere, sort per ordinare, some/every per quantificare, spread per copiare, findIndex+splice per rimuovere, Object.entries per iterare un oggetto, destrutturazione nei parametri, arrow functions, closure per incapsulare stato, JSON):

1. prenotazioniPerCampo(campo) → array di prenotazioni di quel campo (usa filter).
2. nomiPrenotanti(campo) → array di soli nomi di chi ha prenotato quel campo, in maiuscolo (usa filter + map).
3. incassoPerCampo(campo) → numero: somma dei prezzo delle prenotazioni prenotato di quel campo (usa filter + reduce).
4. totalePerCampo() → oggetto { calcio: N, padel: N, tennis: N } con il conteggio delle prenotazioni per campo (usa reduce con valore iniziale {}).
5. incassiPerCampo() → oggetto { calcio: N, padel: N, tennis: N } con l'incasso totale per campo, contando SOLO le prenotazioni prenotato (usa reduce).
6. riepilogo(prenotazione) → stringa "Giulia ha prenotato padel il 2026-08-01 alle 10:00 (stato: prenotato)" usando destrutturazione nei parametri.
7. salva(prenotazioni) e carica(json) → serializza/deserializza l'array in JSON; verifica che carica(salva(prenotazioni)) ricrea l'array identico.
8. ordinaPerData() → nuovo array ordinato per data crescente (usa sort con localeCompare); a parità di data, ordina per prezzo crescente come tie-breaker. Non mutare l'originale (copia con spread prima di sort).
9. esistePrenotata(campo) → booleano: c'è almeno una prenotazione prenotato per quel campo? (usa some). E tuttiHannoEmail() → booleano: tutte le prenotazioni hanno email truthy? (usa every).
10. aggiungiSicura(prenotazione) → NUOVO array con la prenotazione aggiunta in fondo, senza mutare l'originale (usa spread ...).
11. rimuovi(id) (mutabile) → usa findIndex + splice per togliere la prenotazione con quell'id; gestisci il caso id non presente (findIndex → -1, non rimuovere). E rimuoviImmutabile(id) → nuovo array senza quell'id (usa filter). Aggiungi un id numerico ai dati di partenza per testarle.
12. stampaReportConteggi() → itera totalePerCampo() con Object.entries e stampa righe "Campo calcio: 2 prenotazioni" (una per campo).
13. creaIdPrenotazione() → closure factory che ritorna una funzione generatrice di id progressivi (1, 2, 3, ...); usala per assegnare id unici a due nuove prenotazioni e verifica che siano indipendenti da un secondo generatore.


## Criteri di accettazione (cosa deve risultare)
- prenotazioniPerCampo("calcio") ritorna 2 prenotazioni (Marco, Roberto).
- nomiPrenotanti("padel") ritorna ["GIULIA", "CHIARA"] (solo prenotati — decidete voi se includere in attesa e commentatelo nel codice).
- incassoPerCampo("tennis") ritorna 25 (solo Elena è prenotato; Andrea è in attesa ed escluso).
- totalePerCampo() ritorna { calcio: 2, padel: 2, tennis: 2 }.
- incassiPerCampo() ritorna { calcio: 0, padel: 60, tennis: 25 } (calcio 0: Marco è in attesa, Roberto è libero; padel 30+30=60; tennis solo Elena 25).
- riepilogo(prenotazioni[0]) ritorna la stringa attesa, con destrutturazione visibile nei parametri della funzione.
- carica(salva(prenotazioni)) ritorna un array con length === 6 e il primo elemento ha nome === "Giulia".
- ordinaPerData() ritorna un array di 6 con il primo elemento con data === "2026-08-01"; l'originale prenotazioni resta non mutato (verifica length e ordine).
- esistePrenotata("tennis") → true (Elena); esistePrenotata("calcio") → false (Marco in attesa, Roberto libero); tuttiHannoEmail() → true.
- aggiungiSicura({ nome: "Zoe", campo: "padel" }) ritorna un array di 7 e prenotazioni.length resta 6.
- rimuovi(idDiMarco) lascia prenotazioni.length === 5; rimuovi(999) (non presente) lascia l'array invariato; rimuoviImmutabile(idDiMarco) ritorna un array di 5 e prenotazioni resta 6.
- stampaReportConteggi() stampa 3 righe (calcio, padel, tennis) — usa Object.entries visibile nel codice.
- Due generatori da creaIdPrenotazione() producono sequenze indipendenti (es. g1() → 1, g1() → 2, g2() → 1).

## Regole
Usa arrow functions per tutte le callback interne a filter/map/reduce/sort/some/every. Le 13 funzioni di report esterne (prenotazioniPerCampo, incassoPerCampo, ...) sono invece funzioni nominate: scrivile con function dichiarazione (function prenotazioniPerCampo(campo) { ... }) o espressione (const prenotazioniPerCampo = function(campo) { ... }) — sono il posto naturale per la forma classica vista a inizio lezione.