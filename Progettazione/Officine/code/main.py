"""Officine"""

import sys

from persistence import load_all, save_all
from ui import ui_ask_what_to_do


def main():
    load_all()
    while True:
        try:
            ui_ask_what_to_do()
        except KeyboardInterrupt:
            print()
            choice = input("Uscire dal programma? Y/N:\n")
            if choice.lower() in ("yes", "y", "si"):
                break
        except InterruptedError:
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
