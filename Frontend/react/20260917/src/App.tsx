import { useState } from "react";
import "./App.css";
import UserSearch from "./components/UserSearch";
import UserResult from "./components/UserResult";
import useLoadPersone from "./hooks/useLoadPersone";
import type Persona from "./types/Persona";

export default function App() {
  const { persone, loading, error } = useLoadPersone();
  const [risultati, setRisultati] = useState<Persona[] | null>(null);

  return (
    <>
      <UserSearch persone={persone} onSearch={setRisultati} onReset={() => setRisultati(null)} />
      <hr />
      {loading && <p>Caricamento dati...</p>}
      {error && <p>Errore: {error}</p>}
      <UserResult risultati={risultati} />
    </>
  );
}