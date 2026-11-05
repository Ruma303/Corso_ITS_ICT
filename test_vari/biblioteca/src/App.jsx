import { useState } from 'react'
import './App.css'

import { useLoadingLibri } from './hook/useLoadLibri'
import MostraLibri from './components/MostraLibri'
import RicercaLibri from './components/RicercaLibri';

function App() {
  const { libri, loading, errore } = useLoadingLibri()

  // Al momento solo 2 filtri
  const [filtri, setFiltri] = useState({
    titolo: "",
    autore: ""
  });

  const libriFiltrati = libri.filter(libro => {
    const titoloMatch = libro.titolo
      .toLowerCase()
      .includes(filtri.titolo.toLowerCase());

    const autoreMatch = libro.autore
      .toLowerCase()
      .includes(filtri.autore.toLowerCase());

    return titoloMatch && autoreMatch;
  });

  if (errore) {
    return <h1>Si è verificato un errore. Contattare l'assistenza.</h1>;
  }

  if (loading) {
    return <h1>Caricamento libri...</h1>;
  }

  return (
    <>
      <RicercaLibri onFiltri={setFiltri}>
        Ricerca un libro
      </RicercaLibri>
      <MostraLibri libri={libriFiltrati} />
    </>
  )
}

export default App
