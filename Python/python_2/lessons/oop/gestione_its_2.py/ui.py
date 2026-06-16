from classes import Citta, Nazione, Regione


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


def ui_ask_what_to_do():
    while True:
        print(
            "\n\n\n----------\n\nScegli un'azione:\n"
            + "1. - elenca database\n"
            + "2. - crea nazione\n"
            + "3. - crea regione\n"
            + "4. - crea città\n"
            + "0. - exit: Exit\n"
        )

        choice = input("Azione? ")

        if choice in ("nazioni", "1"):
            list_db()
        elif choice in ("crea nazione", "2"):
            crea_nazione()
        elif choice in ("crea regione", "3"):
            crea_regione()
        elif choice in ("crea città", "4"):
            crea_citta()
        elif choice in ("exit", "0"):
            print("Arrivederci!")
            raise InterruptedError
        else:
            print(f"{choice}? mmm, unknown command...")
