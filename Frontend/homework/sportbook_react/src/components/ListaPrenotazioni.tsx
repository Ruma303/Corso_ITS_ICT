import type CampoStruct from "../types/CampoStruct";
import type PrenotazioneStruct from "../types/PrenotazioneStruct";
import { formattaData } from "../utils/date";

interface ListaPrenotazioniProps {
  prenotazioni: PrenotazioneStruct[];
  campi: CampoStruct[];
  onRimuovi: (id: string) => void;
}

// Record + indexed access type: se aggiungi uno stato al tipo, TypeScript ti obbliga a gestirlo qui
const badgePerStato: Record<PrenotazioneStruct["stato"], string> = {
  "in attesa": "text-bg-warning",
  confermata: "text-bg-success",
  annullata: "text-bg-secondary",
};

export default function ListaPrenotazioni({ prenotazioni, campi, onRimuovi }: ListaPrenotazioniProps) {
  const nomeCampo = (campoId: string) => campi.find((c) => c.id === campoId)?.nome ?? "—";

  return (
    <section id="prenotazioni" className="py-5">
      <h2 className="mb-4">
        Prenotazioni <span className="badge text-bg-secondary align-middle">{prenotazioni.length}</span>
      </h2>

      {prenotazioni.length === 0 ? (
        <div className="alert alert-info mb-0">
          Nessuna prenotazione. Scegli un campo e premi "Prenota".
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped align-middle">
            <thead>
              <tr>
                <th scope="col">Nome</th>
                <th scope="col">Campo</th>
                <th scope="col">Data</th>
                <th scope="col">Ora</th>
                <th scope="col">Giocatori</th>
                <th scope="col">Stato</th>
                <th scope="col">
                  <span className="visually-hidden">Azioni</span>
                </th>
              </tr>
            </thead>
            <tbody>
              {prenotazioni.map((p) => (
                <tr key={p.id}>
                  <td>{p.nome}</td>
                  <td>{nomeCampo(p.campoId)}</td>
                  <td>{formattaData(p.data)}</td>
                  <td>{p.ora}</td>
                  <td>{p.partecipanti}</td>
                  <td>
                    <span className={`badge ${badgePerStato[p.stato]}`}>{p.stato}</span>
                  </td>
                  <td className="text-end">
                    <button
                      type="button"
                      className="btn btn-sm btn-outline-danger"
                      onClick={() => onRimuovi(p.id)}
                    >
                      Rimuovi
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}