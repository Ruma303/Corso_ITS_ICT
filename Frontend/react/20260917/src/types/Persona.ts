export default interface Persona {
    nome: string;
    cognome: string;
    eta: number;
    sesso: "male" | "female";
    email: string,
    telefono?: string;
}
