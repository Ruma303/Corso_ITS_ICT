# Istruzioni

Crea una pagina HTML con:

## HTML:
1. Un <header> con il titolo "La mia scheda" e un <nav> con 2 link (es. Home, Contatti)
2. Un <main> con:
      Un <h2> con il tuo nome
      Una lista <ul> con 3 hobby
      Un link <a> al tuo sito preferito
3. Un <footer> con il copyright

## CSS (in un tag <style> dentro <head>):
4. Header con sfondo scuro e testo bianco
5. Contenitore principale (main) con padding, margin, bordo e colore di sfondo
6. Header con flexbox: titolo a sinistra, nav a destra

## JavaScript (in un tag <script> prima di </body>):
7. Crea un array con 3 hobby
8. Usa for...of per stamparli in console
9. Crea una variabile nome e stampa "Ciao, mi chiamo [nome]"


## Bootstrap
10. Collega Bootstrap tramite CDN nel tag <head>
11. Trasforma il <main> in una card Bootstrap (card, card-body)
12. Usa un container per centrare il contenuto (container mt-4)
13. Trasforma i link del menu in pulsanti Bootstrap (btn btn-outline-light btn-sm)
14. Trasforma il link a Google in un pulsante Bootstrap (btn btn-primary)


# Secondo file:

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