import type { ReactNode } from "react";
import Nav, { type VoceMenu } from "./Nav";

// Fuori dal componente: è un dato costante, non va ricreato a ogni render
const menu: VoceMenu[] = [
  { id: "campi", voce: "Campi" },
  { id: "prenota", voce: "Prenota" },
  { id: "contatti", voce: "Contatti" },
];

interface IntestazioneProps {
  children: ReactNode;
}

export default function Intestazione({ children }: IntestazioneProps) {
  return (
    <header className="bg-dark text-white" data-bs-theme="dark">
      <Nav menu={menu} />
      <div className="container text-center py-5">
        <h1 className="display-4 fw-bold">{children}</h1>
        <p className="lead mb-0">Prenota in velocità il tuo campo</p>
      </div>
    </header>
  );
}