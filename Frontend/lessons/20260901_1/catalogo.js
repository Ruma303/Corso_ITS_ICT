const film = [
  { id: "f1", titolo: "Blade Runner 2049", regista: "Denis Villeneuve", anno: 2017, genere: "Sci-fi" },
  { id: "f2", titolo: "Parasite",          regista: "Bong Joon-ho",   anno: 2019, genere: "Dramma" },
  { id: "f3", titolo: "La La Land",        regista: "Damien Chazelle", anno: 2016, genere: "Musical" }
];

function renderFilm(lista) {
  const ul = document.querySelector('#lista-film');
  ul.replaceChildren(); // Svuota nodi interni

  lista.forEach(ele => {
    // Crea l'elemento nodo li
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = `${ele.titolo} (${ele.anno}) - ${ele.regista} [${ele.genere}]`;

    // Aggiunge il nodo li alla lista ul
    ul.appendChild(li);
  });

}

renderFilm(film);

film.push({ id: "f4", titolo: "Il silenzio degli innocenti", regista: "Jonathan Demme", anno: 1991, genere: "Crime, Drammatico, Thriller" });

renderFilm(film);