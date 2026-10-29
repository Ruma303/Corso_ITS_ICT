export default interface Persona {
    id: string;
    nome: string;
    cognome: string;
    eta: number;
    sesso: "male" | "female";
    email: string;
    telefono?: string;
    dataNascita?: string;
}