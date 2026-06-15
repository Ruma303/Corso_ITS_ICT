"""
gestione_its_2.py

Prerequisiti:
 - Aver svolto l'Esercitazione "Gestione ITS 1" (modulo "Progettazione")
 - Aver implementato gestione_its_1.py

Si consideri lo schema concettuale prodotto dagli analisti
per il progetto "Gestione ITS 2".

Si modifichi l'implementazione di gestione_its_1.py per utilizzare il
costrutto di superclasse/sottoclasse in Python, producendo una
architettura di classi conforme al diagramma UML delle classi
concettuale proposto come soluzioen di "Gestione ITS 2".

Implementare le operazioni di classe modellate in "Gestione ITS 2".


L'implementazione fornita qui sotto è **parziale** e va corretta e completata.

"""

import sys

from classes import *
from persistence import *
from ui import *


def main():
    load_all()
    ui_ask_what_to_do()
    save_all()

    """
	ita = Nazione("Italia")
	laz = Regione("Lazio", ita)
	rom = Citta("Roma", laz)
	print(f"La città è {rom}")

	p1 = Persona("Ciccia", "Pasticcia", "PSTCCC00A41H501O", rom)
	print(f"La persona p1 è {p1}")

	s1 = Studente("Ciccio", "Pasticcio", "PSTCCC00A01H501O", rom, "123", date.fromisoformat('2000-01-01'))
	print(f"Lo studente s1 è {s1}")

	d1 = Docente("Andrei", "Peribowski", "PSTCCX00A01H5011", rom)
	print(f"Il docente d1 è {d1}")

	m1 = Modulo("ana1", "Analisi 1", 50)
	m1.add_docente(d1)
	print(f"Il modulo m1 è {m1}")
	"""

    return 0


if __name__ == "__main__":
    sys.exit(main())
