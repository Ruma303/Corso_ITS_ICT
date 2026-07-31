from datetime import datetime
from uuid import NAMESPACE_DNS, uuid5

from models import (
    citta,
    marca,
    modello,
    nazione,
    officina,
    persona,
    riparazione,
    tipo_veicolo,
    veicolo,
)
from models.types.datatypes import CodiceFiscale, IntGEZ, IntGZ, Targa


def list_db():
    print("Nazioni:")
    for n in Nazione.all_objects_by_nome():
        print(f" - {n}")
    print("Città:")
    for n in Citta.all_objects_by_uuid():
        print(f" - {n}")


def crea_nazione():
    nome = input("Nome della nazione? ")
    Nazione.create(nome)
    print(f"Nazione {nome} creata!")


def crea_citta():
    nome = input("Nome della città? ")
    reg_nome = input("Nome della regione associata? ")
    reg = Regione.get_object_by_nome(reg_nome)
    if reg is None:
        print(f'Errore: regione "{reg_nome}" non trovata.')
        return
    Citta.create(nome, reg)
    print(f"Città {nome} creata!")


def ui_ask_what_to_do():
    menu_actions = {
        "1": {"item": "Mostra database", "function": list_db},
        "2": {"item": "Crea nazione", "function": crea_nazione},
        "4": {"item": "Crea città", "function": crea_citta},
        "0": {"item": "Esci", "function": None},
    }

    while True:
        print("\n\n\n----------\n\nScegli un'azione:\n")
        for key, action in menu_actions.items():
            print(f"\t{key}) {action['item']}")

        while True:
            try:
                choice = input("\n\nAzione (scrivi il numero)? ").strip()
                if choice in menu_actions:
                    break
                print("Scelta non valida, scrivi un numero.")

            except ValueError as e:
                print("Il valore inserito non è valido:")
                e.add_note(str(e))
            except TypeError:
                print("Il valore inserito dev'essere una stringa")

        if choice == "0":
            print("Arrivederci!")
            raise InterruptedError

        fn = menu_actions[choice]["function"]
        if fn is not None:
            fn()
        else:
            print(f"Funzione '{menu_actions[choice]['item']}' non ancora implementata.")
