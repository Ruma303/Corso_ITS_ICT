import { useCallback, useState } from "react";
import type Persona from "../types/Persona";
import { API_BASE_URL } from "../config";

export interface FiltriRicerca {
  nome: string;
  cognome: string;
  eta: string;
  sesso: string;
}

interface UseSearchPersoneResult {
  cerca: (filtri: FiltriRicerca) => Promise<Persona[]>;
  searching: boolean;
  searchError: string | null;
}

function buildQueryParams(filtri: FiltriRicerca): URLSearchParams {
  const params = new URLSearchParams();

  if (filtri.nome.trim() !== "") {
    params.set("nome:contains", filtri.nome.trim());
  }
  if (filtri.cognome.trim() !== "") {
    params.set("cognome:contains", filtri.cognome.trim());
  }
  if (filtri.eta.trim() !== "") {
    params.set("eta", filtri.eta.trim()); // nessun operatore => eq
  }
  if (filtri.sesso.trim() !== "") {
    params.set("sesso", filtri.sesso.trim());
  }
  params.set("_sort", "cognome,nome");

  return params;
}

export default function useSearchPersone(): UseSearchPersoneResult {
  const [searching, setSearching] = useState(false);
  const [searchError, setSearchError] = useState<string | null>(null);

  const cerca = useCallback(async (filtri: FiltriRicerca): Promise<Persona[]> => {
    setSearching(true);
    setSearchError(null);

    try {
      const params = buildQueryParams(filtri);
      const response = await fetch(`${API_BASE_URL}/persone?${params.toString()}`);

      if (!response.ok) {
        throw new Error(`Richiesta fallita (status ${response.status})`);
      }

      const data: unknown = await response.json();
      if (!Array.isArray(data)) {
        throw new Error("Risposta del server non valida");
      }

      return data as Persona[];
    } catch (e) {
      const message = e instanceof Error ? e.message : "Errore sconosciuto durante la ricerca";
      setSearchError(message);
      throw e;
    } finally {
      setSearching(false);
    }
  }, []);

  return { cerca, searching, searchError };
}