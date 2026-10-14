import CampoCard from "./CampoCard";
import type Campo from "../models/Campo";

// TODO: Spostare poi in backend
const campi: Campo[] = [
  {
    id: "c1",
    nome: "San Paolo",
    tipo: "calcio",
    coperto: true,
    posti: 22,
  },
  {
    id: "c2",
    nome: "Bernabei",
    tipo: "padel",
    coperto: false,
    posti: 4,
  },
  {
    id: "c3",
    nome: "Oto Melara",
    tipo: "tennis",
    coperto: false,
    posti: 4,
  },
];

export default function ListaCampi({nomeCentro, anno, numeroCampi, addPrenotazione}) {
  return (
    <section>
      <h2>
        Campo {nomeCentro} - {anno}
      </h2>
      <p>{numeroCampi} disponibili</p>

      <ul>
        {campi.map((campo) => (
          <CampoCard
            key={campo.id}
            campo={campo}
            onPrenota={addPrenotazione}
          />
        ))}
      </ul>
    </section>
  );
}