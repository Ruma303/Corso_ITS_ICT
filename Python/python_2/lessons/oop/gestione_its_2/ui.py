from classes import AreaDisciplinare, Citta, Nazione, Regione


def list_db():
    print("Nazioni:")
    for n in Nazione.all_objects_by_uuid():
        print(f" - {n}")

    print("Regioni:")
    for n in Regione.all_objects_by_uuid():
        print(f" - {n}")

    print("Città:")
    for n in Citta.all_objects_by_uuid():
        print(f" - {n}")


# Funzioni di interfaccia ("ui": "User interface")


def crea_nazione():
    nome = input("Nome della nazione? ")
    Nazione.create(nome)
    print(f"Nazione {nome} creata!")


def crea_regione():
    nome = input("Nome della regione? ")
    naz_nome = input("Nome della nazione associata? ")
    naz = Nazione.get_object_by_nome(naz_nome)
    if naz is None:
        print(f'Errore: nazione "{naz_nome}" non trovata.')
        return
    Regione.create(nome, naz)
    print(f"Regione {nome} creata!")


def crea_citta():
    nome = input("Nome della città? ")
    reg_nome = input("Nome della regione associata? ")
    reg = Regione.get_object_by_nome(reg_nome)
    if reg is None:
        print(f'Errore: regione "{reg_nome}" non trovata.')
        return
    Citta.create(nome, reg)
    print(f"Città {nome} creata!")


def crea_area_disciplinare():
    nome = input("Nome area disciplinare? ")
    if not nome:
        raise ValueError("Il nome non può essere vuoto.")
    AreaDisciplinare.create(nome)
    print(f"Area disciplinare '{nome}' creata!")

def ui_ask_what_to_do():
    menu_actions = {
        "1": {"item": "Mostra database", "function": list_db},
        "2": {"item": "Crea nazione", "function": crea_nazione},
        "3": {"item": "Crea regione", "function": crea_regione},
        "4": {"item": "Crea città", "function": crea_citta},
        "5": {"item": "Crea area disciplinare", "function": crea_area_disciplinare},
        "6": {"item": "Crea corso ITS (prossimamente)", "function": None},  # TODO
        "7": {"item": "Crea modulo (prossimamente)", "function": None},  # TODO
        "8": {"item": "Crea docente (prossimamente)", "function": None},  # TODO
        "9": {"item": "Crea studente (prossimamente)", "function": None},  # TODO
        "0": {"item": "Esci", "function": None},
    }

    while True:
        print("\n\n\n----------\n\nScegli un'azione:\n")
        for key, action in menu_actions.items():  # .items(), non enumerate()
            print(f"\t{key}) {action['item']}")  # key è "1","2"... non un indice

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
