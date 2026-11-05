# Struttura app

js
└── script.js <- per esercizi esclusivi su JS
public
├── data
│   ├── libri.json <- db JSON utilizzato
src/
├── App.css
├── App.jsx
├── components
│   ├── Libro.jsx
│   └── MostraLibri.jsx
├── hook
│   └── useLoadLibri.jsx <- caricamento JSON
index.html <- potete abilitare il JS singolo per test

## Avviare app

1. Installare le dipendenze con npm install
2. Avviare il server di sviluppo con npm run dev

## Come funziona l'app a livello base

1. Caricamento dei dati dal'hook personalizzato useLoadLibri. Esporta il parsing JSON in array di oggetti JS + due variabili: loading e error
2. In App.jsx estrapoliamo questi tre elementi. Avviene un rendering condizionale dei messaggi di loading, errore o libri se caricati
3. Libri passati come props in MostraLibri.jsx. Qui dentro avviene il mapping di tutti i libri
4. Il singolo libro è renderizzato in Libro.jsx
5. Continuare con form, ricerca, mostrare solo libri filtrati... È possibile seguire todo.md