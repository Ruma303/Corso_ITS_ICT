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

from persistence import load_all, save_all
from ui import ui_ask_what_to_do


def main():
    load_all()
    while True:
        try:
            ui_ask_what_to_do()
        except (KeyboardInterrupt, InterruptedError):
            print()
            choice = input("Uscire dal programma? Y/N:\n")
            if choice.lower() in ("yes", "y", "si"):
                break
        except Exception as err:
            print(f"\nErrore di tipo {type(err).__name__}:\n{err}\n")
            choice = input("Ritentare? Y/N:\n")
            if choice.lower() not in ("yes", "y", "si"):
                break

    save_all()

    return 0


if __name__ == "__main__":
    sys.exit(main())
