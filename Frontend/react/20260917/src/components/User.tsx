import type Persona from "../types/Persona";

interface UserProps {
  persona: Persona;
}

export default function User({ persona }: UserProps) {
  const { nome, cognome, eta, sesso, email, telefono } = persona;
  const sex = sesso === "male" ? "Maschio" : "Femmina";
  return (
    <tr>
      <td>{nome}</td>
      <td>{cognome}</td>
      <td>{eta}</td>
      <td>{sex}</td>
      <td>{email}</td>
      <td>{telefono ?? ""}</td>
    </tr>
  );
}