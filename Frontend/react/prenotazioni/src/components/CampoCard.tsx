import { useState } from "react";
import type Campo from "../models/Campo";

export default function CampoCard({ campo, onPrenota }: Campo) {
  const [posti, setPosti] = useState<number>(campo.posti);

  function addPosto() {
    setPosti(prev => prev + 1);
  }

  function removePosto() {
    setPosti(prev => Math.max(0, prev - 1));
  }

  function azzera() {
    setPosti(0);
  }

  function reset() {
    setPosti(campo.posti);
  }

  return (
    <>
      <p>Nome: {campo.nome}</p>
      <p>Tipo: {campo.tipo}</p>
      <p>Stato: {campo.coperto ? "Coperto" : "Scoperto"}</p>
      <p>Posti disponibili: {posti}</p>

      <button onClick={removePosto} disabled={posti === 0}>-</button>
      <button onClick={addPosto}>+</button>
      <button onClick={azzera}>Azzera</button>
      <button onClick={reset}>Reset valori</button>
      <br />
      <button onClick={() => onPrenota(campo.id)}>Aggiungi Prenotazione</button>
      <hr />
    </>
  );
}