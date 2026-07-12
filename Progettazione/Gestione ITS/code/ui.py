from datetime import datetime
from uuid import NAMESPACE_DNS, uuid5

from classes import (
    AreaDisciplinare,
    Citta,
    CorsoITS,
    Docente,
    Modulo,
    Nazione,
    Regione,
    Studente,
)
from datatypes import CodiceFiscale, IntGEZ, IntGZ


def list_db():
    print("Nazioni:")
    for n in Nazione.all_objects_by_nome():
        print(f" - {n}")

    print("Regioni:")
    for n in Regione.all_objects_by_uuid():
        print(f" - {n}")

    print("Città:")
    for n in Citta.all_objects_by_uuid():
        print(f" - {n}")

    print("Aree disciplinari:")
    for n in AreaDisciplinare.all_objects_by_nome():
        print(f" - {n}")

    print("Moduli:")
    for n in Modulo.all_objects_by_nome():
        print(f" - {n}")

    print("Corsi ITS:")
    for n in CorsoITS.all_objects_by_nome():
        print(f" - {n}")

    print("Docenti:")
    for n in Docente.all_objects_by_nome():
        print(f" - {n}")

    print("Studenti:")
    for n in Studente.all_objects_by_nome():
        print(f" - {n}")


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


def crea_modulo():
    nome = input("Nome Modulo? ")
    if not nome:
        raise ValueError("Il nome non può essere vuoto.")
    try:
        ore = int(input("Ore modulo? ").strip())
    except ValueError as te:
        print(f"Errore: {te}")
        return
    # INFO: nell'esempio creiamo un codice DETERMINISTICO
    # a partire dalla stringa composta da nome e ore del modulo
    codice = uuid5(NAMESPACE_DNS, f"{nome.strip().lower()}:{ore}")
    Modulo.create(str(codice), nome, IntGZ(ore))

    # INFO: aggiunta docenti
    while True:
      user_choice = input("Vuoi aggiungere dei docenti? Y/N: ").strip().lower()
      if user_choice in ("y", "yes", "ok", "si", "sì"):
        cf_docente = input("Inserisci il codice fiscale: ").strip().lower()
        obj = Docente.get_object_by_cf(CodiceFiscale(cf_docente))
        if not obj:
          raise ValueError(f"Non esiste un docente con questo codice fiscale '{obj}'")
      else:
        break
    
    print(f"Modulo '{nome}' creato!")


def crea_corso_its():
    nome = input("Nome Corso? ")
    if not nome:
        raise ValueError("Il nome non può essere vuoto.")
    try:
        edizione = int(input("Anno di edizione del corso? ").strip())
    except ValueError as te:
        print(f"Errore: {te}")
        return
    CorsoITS.create(nome, IntGEZ(edizione))
    print(f"CorsoITS '{nome}' creato!")


def crea_docente():
    nome = input("Nome docente? ").strip()
    cognome = input("Cognome docente? ").strip()
    try:
        cf = CodiceFiscale(input("Codice fiscale? ").strip())
        nome_citta_nascita = input("Città di nascita? ").strip()
        
        set_citta = Citta.find_citta_by_nome(nome_citta_nascita)
        if not set_citta:
            raise KeyError(
                f"La città '{nome_citta_nascita}' non esiste nel sistema. Impossibile continuare."
            )
        
        lista_citta = list(set_citta)
        
        if len(lista_citta) == 1:
            citta_nascita = lista_citta[0]
        else:
            print(f"\nEsistono più città con il nome '{nome_citta_nascita}':")
            for i, citta in enumerate(lista_citta):
                print(f"\t{i + 1}) {citta.get_nome()} ({citta.get_regione()})")
                
            while True:
                try:
                    scelta = int(input("Seleziona la città corretta digitando il numero associato: "))
                    if 1 <= scelta <= len(lista_citta):
                        citta_nascita = lista_citta[scelta - 1]
                        break
                    else:
                        print(f"Indice non valido. Inserisci un numero tra 1 e {len(lista_citta)}.")
                except ValueError:
                    print("Input non valido. Inserisci un numero intero.")
                    
    except Exception as te:
        print(f"Errore: {te}")
        return
        
    Docente.create(nome, cognome, cf, citta_nascita)
    print(f"Docente {nome} creato!")



def crea_studente():
    nome = input("Nome studente? ").strip()
    cognome = input("Cognome studente? ").strip()
    try:
        cf = CodiceFiscale(input("Codice fiscale? ").strip())
        nome_citta_nascita = input("Città di nascita? ").strip()
        if nome_citta_nascita not in Citta.all_objects_by_nome():
            raise KeyError(
                f"La città {nome_citta_nascita} non esiste. Impossibile continuare"
            )
        citta_nascita = Citta.get_object_by_nome(nome_citta_nascita)
        if citta_nascita is None:
            raise KeyError(
                f"La città {nome_citta_nascita} non esiste. Impossibile continuare"
            )
        matricola = input("Inserisci la matricola:").strip()
        if Studente.search_for_matricola(matricola):
            raise KeyError(f"Lo studente con questa matricola {matricola} esiste già")
        data_nascita_str = input("Data nascita? gg/MM/AAAA").strip()
        data_nascita_dt = datetime.strptime(data_nascita_str, "%d/%m/%Y")
    except Exception as te:
        print(f"Errore: {te}")
        return
    Studente.create(nome, cognome, cf, citta_nascita, matricola, data_nascita_dt)
    print(f"Studente {nome} creato!")


def ui_ask_what_to_do():
    menu_actions = {
        "1": {"item": "Mostra database", "function": list_db},
        "2": {"item": "Crea nazione", "function": crea_nazione},
        "3": {"item": "Crea regione", "function": crea_regione},
        "4": {"item": "Crea città", "function": crea_citta},
        "5": {"item": "Crea area disciplinare", "function": crea_area_disciplinare},
        "6": {"item": "Crea modulo", "function": crea_modulo},
        "7": {"item": "Crea corso ITS", "function": crea_corso_its},
        "8": {"item": "Crea docente", "function": crea_docente},
        "9": {"item": "Crea studente", "function": crea_studente},
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
            break

        fn = menu_actions[choice]["function"]
        if fn is not None:
            fn()
        else:
            print(f"Funzione '{menu_actions[choice]['item']}' non ancora implementata.")
