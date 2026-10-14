import { useEffect, useState } from "react";
import personeUrl from "../data/persone.json?url";
import type Persona from "../types/Persona";

function isPersonaValida(persona: unknown): persona is Persona {
  if (!persona || typeof persona !== "object") return false;

  const { nome, cognome, eta, sesso, email, telefono } = persona as Record<string, unknown>;

  const isNomeValid = typeof nome === "string" && nome.trim() !== "";
  const isCognomeValid = typeof cognome === "string" && cognome.trim() !== "";
  const isEtaValid = typeof eta === "number" && eta >= 18 && eta <= 100;
  const isSessoValid = typeof sesso === "string" && ["male", "female"].includes(sesso.toLowerCase().trim());

  // Niente regex al momento per flessibilità
  const isEmailValid = typeof email === "string" && email.trim() !== "" && email.includes("@") && email.includes(".");
  const isTelefonoValid = typeof telefono === "string" && telefono.trim() !== "";

  return isNomeValid && isCognomeValid && isEtaValid && isSessoValid && isEmailValid && isTelefonoValid;
}

interface UseLoadPersoneResult {
  persone: Persona[];
  loading: boolean;
  error: string | null;
}

export default function useLoadPersone(): UseLoadPersoneResult {
  const [persone, setPersone] = useState<Persona[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let ignoraRisultato = false;

    async function caricaDati() {
      try {
        const response = await fetch(personeUrl);
        if (!response.ok) throw new Error("Errore nella richiesta");

        const data: unknown = await response.json();
        if (!Array.isArray(data) || data.length === 0) {
          throw new Error("Non sono presenti dati in persone.json");
        }

        const validati = data.filter(isPersonaValida);
        if (!ignoraRisultato) setPersone(validati);
      } catch (e) {
        console.error("Errore nel caricamento dei dati:", e);
        if (!ignoraRisultato) setError(e instanceof Error ? e.message : "Errore sconosciuto");
      } finally {
        if (!ignoraRisultato) setLoading(false);
      }
    }

    caricaDati();

    return () => { ignoraRisultato = true; };
  }, []);

  return { persone, loading, error };
}