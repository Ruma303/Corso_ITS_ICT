export default interface PrenotazioneStruct {
  id: string;
  nome: string;
  email: string;
  campoId: string; // riferimento a CampoStruct.id
  data: string; // formato ISO: YYYY-MM-DD
  ora: string; // formato HH:mm
  partecipanti: number;
  note?: string; // opzionale: le prenotazioni già salvate in localStorage non ce l'hanno
  stato: "in attesa" | "confermata" | "annullata";
}