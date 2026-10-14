import { useState } from "react";
import type CampoStruct from "../types/CampoStruct";

interface CampoCardProps {
  campo: CampoStruct;
  onPrenota: (idCampo: string, partecipanti: number) => void;
}

export default function CampoCard({ campo, onPrenota }: CampoCardProps) {
  const { id, nome, descrizione, prezzo, coperto, posti } = campo;

  // Stato LOCALE: interessa solo a questa card finché non si preme "Prenota"
  const [partecipanti, setPartecipanti] = useState(1);

  const decrementa = () => setPartecipanti((prev) => Math.max(1, prev - 1));
  const incrementa = () => setPartecipanti((prev) => Math.min(posti, prev + 1));
  const azzera = () => setPartecipanti(1);

  function prenota() {
    onPrenota(id, partecipanti); // comunica verso l'alto: lo stato globale vive in App
    azzera();
  }

  return (
    <div className="card h-100 shadow-sm">
      <div className="card-body">
        <div className="d-flex justify-content-between align-items-start mb-2">
          <h3 className="h5 card-title mb-0">{nome}</h3>
          <span className={`badge ${coperto ? "text-bg-primary" : "text-bg-success"}`}>
            {coperto ? "Al chiuso" : "All'aperto"}
          </span>
        </div>
        <p className="card-text text-body-secondary">{descrizione}</p>
        <p className="fw-semibold mb-0">{prezzo} €/ora</p>
      </div>

      <div className="card-footer bg-transparent border-0 pb-3">
        <div className="d-flex align-items-center justify-content-between mb-3">
          <span>
            Giocatori: <strong>{partecipanti}</strong> / {posti}
          </span>
          <div className="btn-group btn-group-sm" role="group" aria-label="Numero di giocatori">
            <button
              type="button"
              className="btn btn-outline-secondary"
              onClick={decrementa}
              disabled={partecipanti <= 1}
              aria-label="Un giocatore in meno"
            >
              −
            </button>
            <button
              type="button"
              className="btn btn-outline-secondary"
              onClick={incrementa}
              disabled={partecipanti >= posti}
              aria-label="Un giocatore in più"
            >
              +
            </button>
            <button type="button" className="btn btn-outline-secondary" onClick={azzera}>
              Reset
            </button>
          </div>
        </div>
        <button type="button" className="btn btn-primary w-100" onClick={prenota}>
          Prenota
        </button>
      </div>
    </div>
  );
}
