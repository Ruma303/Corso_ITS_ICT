import type PrenotazioneStruct from "./PrenotazioneStruct";

// I dati che arrivano dal form: tutto tranne ciò che genera l'app (id e stato)
export type NuovaPrenotazione = Omit<PrenotazioneStruct, "id" | "stato">;