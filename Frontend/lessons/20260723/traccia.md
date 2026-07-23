PT1:
**Consegna:** Crea un file HTML con:
1. Un titolo `<h1>`: "I miei sport preferiti" (e lo stesso per il `<title>` nella testata)
2. Struttura base (doctype, html, head, body)
3. Un paragrafo `<p>` con una frase
4. Una lista `<ul>` con 3 sport
5. Un link `<a>` a Google

PT2:
**Consegna:** Parti dal file dell'esercizio 1. Ora devi aggiungere la struttura:
1. Metti l'`<h1>` dentro un `<header>`
2. Metti tutto il resto (p, ul, a) dentro un `<main>`
3. Aggiungi un `<footer>` con il copyright
4. Crea un div con all'interno una table

Nessun template — devi scrivere tu dove mettere i tag!

PT3:
# Aggiungi CSS a questo HTML per colorare le card:

```html
<div class="card">
  <h3>Campo da calcio</h3>
  <p>Prezzo: 50€</p>
</div>
<div class="card">
  <h3>Campo da tennis</h3>
  <p>Prezzo: 30€</p>
</div>
```

Utilizza:
 bg-color, padding, margin, border

PT4:
Usa flexbox per mettere logo a sinistra e menu a destra:

```html
<header class="header">
  <div class="logo">Sport Center</div>
  <nav class="menu">
    <a href="#">Home</a>
    <a href="#">Campi</a>
    <a href="#">Contatti</a>
  </nav>
</header>
```

PT5:
Prendi la pagina HTML dell'esercizio precedente e crea un file `style.css`.

Applica questi stili:

1. Cambia il colore di sfondo della pagina.
2. Rendi il titolo blu e centrato.
3. Dai uno sfondo chiaro al `<main>`.
4. Aggiungi `padding` e `margin` al `<main>`.
5. Metti un bordo alla tabella.
6. Cambia il colore del footer.

PT6:
Scrivi un programma che:
1. Crea una variabile `prezzo` con valore 100
2. Crea una variabile `sconto` con valore 20
3. Calcola `prezzoFinale = prezzo - sconto`
4. Se `prezzoFinale < 50`, stampa "Ottimo affare!"
5. Altrimenti stampa "Prezzo normale"

PT7:
Scrivi un programma che:
1. Crea un array `spesa` con 3 elementi: "pane", "latte", "uova"
2. Aggiungi "formaggio" con `push`
3. Stampa il numero di elementi con `console.log`
4. Usa `for...of` per stampare ogni elemento


PT8:
Scrivi un programma che:

1. Crea una variabile `nome` con il nome di uno studente.
2. Crea una variabile `voto` con valore `27`.
3. Crea una variabile `assenze` con valore `2`.
4. Lo studente è promosso se:
    - il voto è **maggiore o uguale a 18**
    - **e** le assenze sono **minori di 5**.
5. Stampa:
    - `"<nome> è promosso!"`
    - oppure `"<nome> non è promosso."`

PT9:
Crea 3 card in una griglia responsive utilizzando bootstrap:
- Su mobile: 1 card per riga
- Su tablet: 2 card per riga
- Su desktop: 3 card per riga