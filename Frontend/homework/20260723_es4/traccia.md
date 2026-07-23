Scrivi una pagina HTML completa con stili CSS personalizzati, struttura Bootstrap e una sezione JavaScript che elabori i dati degli studenti stampando i risultati in console.

### Requisiti dell'esercizio:

1. **HTML & Bootstrap:**
  - Crea la struttura semantica con `<header>`, `<main>` e `<footer>`.
  - Collega la libreria **Bootstrap** nel `<head>` tramite `<link>`.
  - Nel `<main>`, usa la griglia Bootstrap (`container`, `row`, `col`) e inserisci una `<table>` statica con le informazioni generali del corso (es. Nome Corso, Docente, Anno).

2. **CSS Personalizzato:**
  - Imposta la regola `box-sizing: border-box` su tutti gli elementi (`*`).
  - Scegli un colore di sfondo in formato HEX per il `body` (es. `#f4f6f9`).
  - Centra i contenuti dell'`<header>` usando `display: flex`, `justify-content: center` e `align-items: center`.

3. **JavaScript (Script a fondo pagina):**
  - Dichiara un array `studenti` contenente 3 oggetti con le proprietà: `nome` (stringa), `voto` (numero), `assenze` (numero).
  - Aggiungi un 4° studente all'array usando il metodo `.push()`.
  - Usa un ciclo `for...of` per scorrere tutti gli studenti:
    - Verifica se lo studente è promosso (`voto >= 18 && assenze < 5`).
    - Stampa il risultato in console usando `console.log()` e i **Template Literal**:
      `"<nome> - Voto: <voto> | Assenze: <assenze> -> Promosso!"` oppure `"<nome> - Voto: <voto> | Assenze: <assenze> -> Non promosso."`
  - Alla fine del ciclo, stampa in console il totale degli studenti analizzati usando la proprietà `.length`.  