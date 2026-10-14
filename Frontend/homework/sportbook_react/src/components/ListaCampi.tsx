import CampoCard from "./CampoCard";
import type CampoStruct from "../types/CampoStruct";

// Esempio di tipizzazione delle prop tramite oggetto inline
export default function ListaCampi({
	campi,
	onPrenotaCampo,
} : {
	campi: CampoStruct[];
	onPrenotaCampo: (idCampo: string, partecipanti: number) => void;
}) {
	return (
		<section id="campi" className="py-5">
			<h2 className="mb-4">I nostri campi</h2>
			<div className="row row-cols-1 row-cols-md-2 row-cols-xl-4 g-4">
				{campi.map((campo) => (
					// La griglia (col) è responsabilità della lista, non della card
					<div className="col" key={campo.id}>
						<CampoCard campo={campo} onPrenota={onPrenotaCampo} />
					</div>
				))}
			</div>
		</section>
	);
}
