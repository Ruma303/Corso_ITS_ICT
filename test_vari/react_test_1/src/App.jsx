import { useState } from 'react';
import './App.css';
import Form from './Form';
import Utente from './Utente';

function App() {
  // Array che conterrà tutti gli utenti creati
  const [utenti, setUtenti] = useState([]);
  // Stato per gestire la schermata di caricamento
  const [loading, setLoading] = useState(false);

  // Funzione chiamata al submit del form
  const handleCreateUtente = (nuovoUtente) => {
    setLoading(true); // 1. Mostra il caricamento

    // 2. Simula un'attesa di 3 secondi (3000 millisecondi)
    setTimeout(() => {
      setUtenti(prevUtenti => [...prevUtenti, nuovoUtente]); // Aggiunge l'utente all'array
      setLoading(false); // 3. Spegne il caricamento
    }, 3000);
  };

  return (
    <>
      <Form createUtente={handleCreateUtente}>
        Creazione utente
      </Form>

      {/* Rendering condizionale in base a loading e alla presenza di utenti */}
      {loading && <Loading />}

      {!loading && utenti.length > 0 && (
        <div>
          <h2>Lista Utenti Creati:</h2>
          {utenti.map((utente, index) => (
            <Utente key={index} utente={utente} />
          ))}
        </div>
      )}
    </>
  );
}

export default App;

function Loading() {
  return (
    <div>
      <h1>Loading... ⏳</h1>
    </div>
  );
}