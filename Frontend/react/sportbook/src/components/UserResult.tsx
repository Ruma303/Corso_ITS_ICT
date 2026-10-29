import type { ReactNode } from "react";
import type Persona from "../types/Persona";
import User from "./User";

interface UserResultProps {
    risultati: Persona[] | null;
    children: ReactNode;
}

export default function UserResult({
    risultati,
    children,
}: UserResultProps) {
    if (risultati === null) return null;

    const colonne: string[] = [
        "Nome",
        "Cognome",
        "Età",
        "Sesso",
        "Email",
        "Telefono",
        "Data Nascita",
    ];

    return (
        <section id="result-section">
            <h2 className="h4 mb-3">{children}</h2>

            {risultati.length === 0 ? (
                <div className="alert alert-warning" role="alert">
                    Nessun risultato trovato.
                </div>
            ) : (
                <div className="table-responsive">
                    <table className="table table-striped table-hover align-middle">
                        <thead className="table-dark">
                            <tr>
                                {colonne.map((col, i) => (
                                    <th key={i} scope="col">
                                        {col}
                                    </th>
                                ))}
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
                </div>
            )}
        </section>
    );
}
