import { useState } from "react";
import "./App.css";
import UserSearch from "./components/UserSearch";
import UserResult from "./components/UserResult";
import { useLoadPersone, dataLength } from "./hooks/useLoadPersone";
import type Persona from "./types/Persona";

export default function App() {
    const { persone, loading, error } = useLoadPersone();
    const [risultati, setRisultati] = useState<Persona[] | null>(
        null,
    );

    return (
        <div className="container py-4">
            <UserResult risultati={persone}>
                Database (debug)
            </UserResult>
            {!loading && !error && (
                <div className="d-flex flex-column">
                    <p className="text-success">
                        ✅ Persone disponibili nel database:{" "}
                        {persone.length}
                    </p>
                    <p className="text-muted">
                        Persone totali nel database: {dataLength}
                    </p>
                    <p className="text-danger">
                        ⚠️ Persone non valide nel database:{" "}
                        {dataLength - persone.length}
                    </p>
                </div>
            )}
            <hr className="my-4" />
            <UserSearch
                onSearch={setRisultati}
                onReset={() => setRisultati(null)}
            >
                Form di ricerca
            </UserSearch>

            <hr className="my-4" />

            {loading && (
                <div className="d-flex align-items-center gap-2 text-secondary">
                    <div
                        className="spinner-border spinner-border-sm"
                        role="status"
                    >
                        <span className="visually-hidden">
                            Caricamento...
                        </span>
                    </div>
                    <span>Caricamento dati...</span>
                </div>
            )}

            {error && (
                <div className="alert alert-danger" role="alert">
                    Errore: {error}
                </div>
            )}

            <UserResult risultati={risultati}>
                Utenti trovati
            </UserResult>
        </div>
    );
}
