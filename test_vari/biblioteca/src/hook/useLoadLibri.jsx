import { useEffect, useState } from 'react'

function useLoadingLibri() {
  const [libri, setLibri] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null)

  useEffect(() => {
    // Caricamento dati da JSON tramite
    // funzione asincrona dentro

    setInterval(() => {
    async function jsonParse() {
      try {
        const res = await fetch('/data/libri.json')

        if (!res.ok) {
          throw new Error("Errore di caricamento dati JSON")
        }

        const dati = await res.json();

        setLibri(dati.libri)
      } catch (err) {
        setErrore(err.message)
      } finally {
        setLoading(false);
      }
    }
    jsonParse()}, 2000) // Simulazione caricamento 2s
  }, []);

  return { libri, loading, errore };
}

export { useLoadingLibri }