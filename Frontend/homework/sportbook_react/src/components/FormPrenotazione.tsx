import { useState, type FormEvent } from "react";
import type CampoStruct from "../types/CampoStruct";
import type { NuovaPrenotazione } from "../types/NuovaPrenotazione";
import { MAX_NOTE } from "../constants/formConstants";
import { formattaData, oggiISO } from "../utils/date";

interface FormPrenotazioneProps {
  campi: CampoStruct[];
  onPrenota: (dati: NuovaPrenotazione) => void;
}

export default function FormPrenotazione({ campi, onPrenota }: FormPrenotazioneProps) {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [campoId, setCampoId] = useState("");
  const [data, setData] = useState("");
  const [ora, setOra] = useState("");
  // Un input restituisce SEMPRE una stringa: la teniamo così e convertiamo solo al submit
  const [partecipanti, setPartecipanti] = useState("1");
  const [note, setNote] = useState("");

  const campoScelto = campi.find((c) => c.id === campoId);

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    // Se un campo required è vuoto il browser blocca il submit: qui i dati sono già validi
    onPrenota({
      nome: nome.trim(),
      email,
      campoId,
      data,
      ora,
      partecipanti: Number(partecipanti),
      note: note.trim() || undefined,
    });
    azzera();
  }

  function azzera() {
    setNome("");
    setEmail("");
    setCampoId("");
    setData("");
    setOra("");
    setPartecipanti("1");
    setNote("");
  }

  return (
    <section id="prenota" className="py-5">
      <h2 className="mb-4">Prenota il tuo campo</h2>

      <div className="row g-4">
        <div className="col-md-7">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="nome-form" className="form-label">
                Il tuo nome
              </label>
              <input
                type="text"
                id="nome-form"
                className="form-control"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="email-form" className="form-label">
                La tua email
              </label>
              <input
                type="email"
                id="email-form"
                className="form-control"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="campo-form" className="form-label">
                Scegli il tuo campo
              </label>
              <select
                id="campo-form"
                className="form-select"
                value={campoId}
                onChange={(e) => setCampoId(e.target.value)}
                required
              >
                <option value="">Seleziona un campo…</option>
                {campi.map((campo) => (
                  <option key={campo.id} value={campo.id}>
                    {campo.nome}
                  </option>
                ))}
              </select>
            </div>

            <div className="row g-3 mb-3">
              <div className="col-sm-5">
                <label htmlFor="data-form" className="form-label">
                  Data
                </label>
                <input
                  type="date"
                  id="data-form"
                  className="form-control"
                  min={oggiISO()}
                  value={data}
                  onChange={(e) => setData(e.target.value)}
                  required
                />
              </div>
              <div className="col-sm-4">
                <label htmlFor="ora-form" className="form-label">
                  Ora
                </label>
                <input
                  type="time"
                  id="ora-form"
                  className="form-control"
                  value={ora}
                  onChange={(e) => setOra(e.target.value)}
                  required
                />
              </div>
              <div className="col-sm-3">
                <label htmlFor="partecipanti-form" className="form-label">
                  Giocatori
                </label>
                <input
                  type="number"
                  id="partecipanti-form"
                  className="form-control"
                  min={1}
                  max={campoScelto?.posti}
                  value={partecipanti}
                  onChange={(e) => setPartecipanti(e.target.value)}
                  required
                />
              </div>
            </div>

            <div className="mb-3">
              <label htmlFor="note-form" className="form-label">
                Note
              </label>
              <textarea
                id="note-form"
                className="form-control"
                rows={3}
                maxLength={MAX_NOTE}
                value={note}
                onChange={(e) => setNote(e.target.value)}
              />
              <div className="form-text">{MAX_NOTE - note.length} caratteri rimanenti</div>
            </div>

            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">
                Prenota
              </button>
              <button type="button" className="btn btn-outline-secondary" onClick={azzera}>
                Azzera
              </button>
            </div>
          </form>
        </div>

        <div className="col-md-5">
          <div className="card">
            <div className="card-body">
              <h3 className="h5 card-title">Riepilogo</h3>
              <dl className="mb-0 text-break">
                <dt>Nome</dt>
                <dd>{nome || "—"}</dd>
                <dt>Email</dt>
                <dd>{email || "—"}</dd>
                <dt>Campo</dt>
                <dd>{campoScelto?.nome ?? "—"}</dd>
                <dt>Data e ora</dt>
                <dd>{data ? `${formattaData(data)} ${ora}`.trim() : "—"}</dd>
                <dt>Giocatori</dt>
                <dd>{partecipanti || "—"}</dd>
                <dt>Note</dt>
                <dd className="mb-0">{note || "—"}</dd>
              </dl>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}