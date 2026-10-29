import { useEffect, useState } from "react";
import type Persona from "../types/Persona";
import { API_BASE_URL } from "../config";

function isPersonaValida(persona: unknown): persona is Persona {
    if (!persona || typeof persona !== "object") {
        console.warn("Persona scartata: non è un oggetto", persona);
        return false;
    }

    const {
        id,
        nome,
        cognome,
        eta,
        sesso,
        email,
        telefono,
        dataNascita,
    } = persona as Record<string, unknown>;

    const checks: Record<string, boolean> = {
        id: typeof id === "string" && id.trim() !== "",
        nome: typeof nome === "string" && nome.trim() !== "",
        cognome: typeof cognome === "string" && cognome.trim() !== "",
        eta: typeof eta === "number" && eta >= 18 && eta <= 100,
        sesso:
            typeof sesso === "string" &&
            ["male", "female"].includes(sesso.toLowerCase().trim()),
        email:
            typeof email === "string" &&
            email.trim() !== "" &&
            email.includes("@") &&
            email.includes("."),
        telefono:
            telefono === undefined || typeof telefono === "string",
        dataNascita:
            dataNascita === undefined ||
            typeof dataNascita === "string",
    };

    const fallito = Object.entries(checks)
        .filter(([, ok]) => !ok)
        .map(([campo]) => campo);

    if (fallito.length > 0) {
        console.warn(
            "Persona scartata, campi non validi:",
            fallito,
            persona,
        );
        return false;
    }

    return true;
}

interface UseLoadPersoneResult {
    persone: Persona[];
    loading: boolean;
    error: string | null;
}

export let dataLength: number;

export function useLoadPersone(): UseLoadPersoneResult {
    const [persone, setPersone] = useState<Persona[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        let ignoraRisultato = false;
        const controller = new AbortController();

        async function caricaDati() {
            try {
                const response = await fetch(
                    `${API_BASE_URL}/persone`,
                    {
                        signal: controller.signal,
                    },
                );
                if (!response.ok)
                    throw new Error(
                        `Richiesta fallita (status ${response.status})`,
                    );

                const data: unknown = await response.json();
                if (!Array.isArray(data)) {
                    throw new Error(
                        "Risposta del server non valida: atteso un array",
                    );
                }
                dataLength = data.length;
                console.log("Persone trovate: ", dataLength);

                const validati = data.filter(isPersonaValida);
                if (!ignoraRisultato) setPersone(validati);
            } catch (e) {
                if (
                    e instanceof DOMException &&
                    e.name === "AbortError"
                )
                    return;
                console.error("Errore nel caricamento dei dati:", e);
                if (!ignoraRisultato)
                    setError(
                        e instanceof Error
                            ? e.message
                            : "Errore sconosciuto",
                    );
            } finally {
                if (!ignoraRisultato) setLoading(false);
            }
        }

        caricaDati();

        return () => {
            ignoraRisultato = true;
            controller.abort();
        };
    }, []);

    return { persone, loading, error };
}
