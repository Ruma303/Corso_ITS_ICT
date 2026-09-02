Mini-esercizio — Catalogo film (DOM + render lista da array)

Crea una pagina a parte `catalogo.html` + `catalogo.js` (scollegata dalla dashboard). Hai un array di oggetti `film` già inizializzato in `catalogo.js`. Renderizzalo in una `<ul>` presente in HTML, costruendo ogni `<li>` con `createElement` + `textContent` (mai `innerHTML` con i dati dei film, anche se sono fidati: alleniamo la regola ferrea).

### Dati di partenza

```js
const film = [
  { id: "f1", titolo: "Blade Runner 2049", regista: "Denis Villeneuve", anno: 2017, genere: "Sci-fi" },
  { id: "f2", titolo: "Parasite",          regista: "Bong Joon-ho",   anno: 2019, genere: "Dramma" },
  { id: "f3", titolo: "La La Land",        regista: "Damien Chazelle", anno: 2016, genere: "Musical" }
];
```

HTML di base:

```html
<ul id="lista-film" class="list-group"></ul>
```

### Consegna

- Seleziona il container `#lista-film` con `querySelector` e salvalo in una variabile.
- Scrivi una funzione `renderFilm(lista)` che: svuota il container con `replaceChildren()`, poi con un `forEach` crea un `<li class="list-group-item">` per ogni film e lo appende.
- Ogni `<li>` mostra `"Titolo — regista (anno) · genere"` tramite `textContent` + template literal.
- Chiama `renderFilm(film)` per mostrare la lista al caricamento.
- Aggiungi poi un quarto film all'array (`film.push({...})`) e richiama `renderFilm(film)`: verifica che la lista si aggiorni senza duplicati.

**Criteri di accettazione:**
- [ ] La lista si renderizza in `#lista-film` con 3 `<li>` al primo `renderFilm(film)`.
- [ ] Ogni `<li>` è costruito con `createElement` + `textContent` (niente `innerHTML`).
- [ ] Il container è svuotato con `replaceChildren()` prima del ciclo.
- [ ] Dopo `film.push(...)` + `renderFilm(film)`, la lista mostra 4 film (non 7: niente duplicati).
- [ ] Niente eventi, niente timer, niente localStorage: solo DOM + render lista.