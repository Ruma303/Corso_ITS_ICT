import { useState, useRef } from "react";
import type Prenotazione from "./models/Prenotazione";
import Header from "./components/Header";
import ListaCampi from "./components/ListaCampi";
import Prenotazioni from "./components/Prenotazioni";
import type Campo from "./models/Campo";

const nome: string = "Matteo";
const numero: number = 20;
const eta: number = 32;
const user = { nome: nome, numero: numero, eta };
const nomeCentro: string = "Centro anti-sociale";
const numeroCampi: number = 22;
const anno: number = 2026;

const campi: Campo[] = [];

function App() {
  const [prenotazioni, setPrenotazioni] = useState<Prenotazione[]>([]);
  const nextId = useRef(1);

  function addPrenotazione(campoId: string) {
      const campo = campi.find((c) => c.id === campoId);
      if (!campo) return;
  
      const id = nextId.current++;
  
      setPrenotazioni((prev) => [
        ...prev,
        { id, campo: campo.nome, ora: new Date() },
      ]);
    }

  function removePrenotazione(id: number) {
    setPrenotazioni((prev) => prev.filter((p) => p.id !== id));
  }

  return (
    <>
      <Header user={user}/>
      <main>
        <ListaCampi
          nomeCentro={nomeCentro}
          anno={anno} 
          numeroCampi={numeroCampi}
          addPrenotazione={addPrenotazione}
        />
        <Prenotazioni
          prenotazioni={prenotazioni}
          removePrenotazione={removePrenotazione}
        />
      </main>
    </>
  );
}

export default App;
