export default function Libro({ isbn, titolo, autore, annoPubblicazione, disponibile, prezzo, quantita }) {

  return (<>
  <div>
    <h2>Titolo: {titolo}</h2>
    <p>ISBN: {isbn}</p>
    <p>Autore: {autore}</p>
    <p>Anno pubblicazione: {annoPubblicazione}</p>
    <p>Disponibile: {disponibile}</p>
    <p>Prezzo: {prezzo}</p>
    <p>Quantita: {quantita}</p>
  </div>
  </>)
}
