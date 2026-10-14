import type Persona from "../types/Persona";
import User from "./User";

interface UserResultProps {
  risultati: Persona[] | null;
}

export default function UserResult({ risultati }: UserResultProps) {
  if (risultati === null) return null;

  const colonne: string[] = [
    "Nome",
    "Cognome",
    "Età",
    "Sesso",
    "Email",
    "Telefono",
    // "Data Nascita",
  ];

  return (
    <section id="result-section">
      <h2>Risultati</h2>
      {risultati.length === 0 ? (
        <p>Nessun risultato trovato.</p>
      ) : (
        <table>
          <thead>
            <tr>
              {colonne.map((col, i) => <th key={i}>{col}</th>)}
            </tr>
          </thead>
          <tbody>
            {risultati.map((persona, index) => (
              <User
                key={`${persona.nome}-${persona.cognome}-${index}`}
                persona={persona}
              />
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}
