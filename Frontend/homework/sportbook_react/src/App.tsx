import Intestazione from "./components/Intestazione";
import ListaCampi from "./components/ListaCampi";
import FormPrenotazione from "./components/FormPrenotazione";
import ListaPrenotazioni from "./components/ListaPrenotazioni";
import Footer from "./components/Footer";
import useLocalStorage from "./hooks/useLocalStorage";
import campi from "./data/campi";
import prenotazioniIniziali from "./data/prenotazioni";
import type PrenotazioneStruct from "./types/PrenotazioneStruct";
import type { NuovaPrenotazione } from "./types/NuovaPrenotazione";
import { oggiISO } from "./utils/date";

function App() {
  // Lo stato condiviso vive nell'antenato comune: App lo passa ai figli via props
  const [prenotazioni, setPrenotazioni] = useLocalStorage<PrenotazioneStruct[]>(
    "sportbook:prenotazioni",
    prenotazioniIniziali,
  );

  // Unico punto in cui nasce una prenotazione: l'app aggiunge id e stato ai dati ricevuti
  function aggiungiPrenotazione(dati: NuovaPrenotazione) {
    const nuova: PrenotazioneStruct = {
      ...dati,
      id: crypto.randomUUID(),
      stato: "in attesa",
    };
    setPrenotazioni((previous) => [...previous, nuova]);
  }

  // Prenotazione rapida dalla card: completa i dati mancanti con dei default
  function prenotaDaCard(campoId: string, partecipanti: number) {
    aggiungiPrenotazione({
      nome: "Ospite",
      email: "",
      campoId,
      data: oggiISO(),
      ora: "18:00",
      partecipanti,
    });
  }

  function rimuoviPrenotazione(id: string) {
    setPrenotazioni((previous) => previous.filter((p) => p.id !== id));
  }

  return (
    <div className="d-flex flex-column min-vh-100">
      <Intestazione>SportBook Roma</Intestazione>
      <main className="container flex-grow-1">
        <ListaCampi campi={campi} onPrenotaCampo={prenotaDaCard} />
        <FormPrenotazione campi={campi} onPrenota={aggiungiPrenotazione} />
        <ListaPrenotazioni
          prenotazioni={prenotazioni}
          campi={campi}
          onRimuovi={rimuoviPrenotazione}
        />
      </main>
      <Footer />
    </div>
  );
}

export default App;