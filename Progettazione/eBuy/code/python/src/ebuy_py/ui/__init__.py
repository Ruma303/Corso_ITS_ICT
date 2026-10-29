"""Modulo di testing CLI. Il frontend utilizzerà REST API"""

from datetime import datetime

from src.ebuy_py.datatypes import datatypes, validators
from src.ebuy_py.exceptions import exceptions
from src.ebuy_py.models import (
    asta,
    categoria,
    compralosubito,
    met_pag,
    post,
    utente,
    valuta,
)


def list_db():
    print("Categorie:")
    for n in post.Categoria.get_set_name_objects():
        print(f" - {n}")
    print("Valute:")
    for n in valuta.Valuta.get_set_name_objects():
        print(f" - {n}")
    print("MetodiPagamento:")
    for n in met_pag.MetodoPagamento.get_set_name_objects():
        print(f" - {n}")
    print("Posts:")
    for n in post.Post.get_all_posts():
        print(f" - {n}")
    print("Utenti:")
    for n in utente.Utente.get_set_name_objects():
        print(f" - {n}")


# Completare refactoring

def crea_categoria():
    Nazione.create(nome)
    print(f"Nazione {nome} creata!")


def crea_valuta():
    nome = input("Nome della città? ")
    reg_nome = input("Nome della regione associata? ")
    reg = Regione.get_object_by_nome(reg_nome)
    if reg is None:
        print(f'Errore: regione "{reg_nome}" non trovata.')
        return
    Citta.create(nome, reg)
    print(f"Città {nome} creata!")


def ui_ask_what_to_do(u: utente.Utente):
    # TODO: potremmo mostrare solo le azioni di uno specifico utente (es solo i suoi post) 
    # Da lasciare libere le operazioni generali come il login.

    print(f"Welcome {u.get_nome()}")
    
    menu_actions = {
        "1": {"item": "Mostra database", "function": list_db},
        "2": {"item": "Crea nazione", "function": crea_categoria},
        "4": {"item": "Crea città", "function": crea_valuta},
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
