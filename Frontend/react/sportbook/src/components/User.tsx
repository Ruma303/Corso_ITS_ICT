import type Persona from "../types/Persona";

interface UserProps {
  persona: Persona;
}

export default function User({ persona }: UserProps) {
  const { nome, cognome, eta, sesso, email, telefono, dataNascita } = persona;
  const sex = sesso === "male" ? "Maschio" : "Femmina";

  return (
    <tr>
      <td>{nome}</td>
      <td>{cognome}</td>
      <td>{eta}</td>
      <td>
        <span className={`badge ${sesso === "male" ? "text-bg-primary" : "text-bg-danger"}`}>
          {sex}
        </span>
      </td>
      <td>{email}</td>
      <td>{telefono ?? <span className="text-muted">—</span>}</td>
      <td>{dataNascita ?? <span className="text-muted">—</span>}</td>
    </tr>
  );
}