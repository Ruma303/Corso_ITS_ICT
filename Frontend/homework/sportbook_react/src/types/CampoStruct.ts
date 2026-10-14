export default interface CampoStruct {
  id: string;
  nome: string;
  tipo: string;
  descrizione?: string;
  prezzo?: number; // €/ora
  coperto: boolean;
  posti: number; // numero massimo di giocatori
}
