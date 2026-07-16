from datetime import datetime
from uuid import NAMESPACE_DNS, uuid5
from utils import yes

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
        print("Errore: Il nome non può essere vuoto.")
        return

    try:
        ore_input = int(input("Ore modulo? ").strip())
        ore = IntGZ(ore_input)
    except ValueError as te:
        print(f"Errore: {te}")
        return

    codice = str(uuid5(NAMESPACE_DNS, f"{nome.strip().lower()}:{ore}"))

    # Inizializziamo il set temporaneo che conterrà i docenti
    docenti_da_associare = set()

    while True:
        user_choice = input("Vuoi aggiungere dei docenti? Y/N: ").strip().lower()
        if user_choice in yes:
            cf_docente = input("Inserisci il codice fiscale: ").strip().upper() 
            try:
                cf_valido = CodiceFiscale(cf_docente)
                docente = Docente.get_object_by_cf(cf_valido)
                if not docente:
                    print(f"Non esiste un docente con questo codice fiscale '{cf_docente}'. Riprova.")
                    continue
                
                docenti_da_associare.add(docente)
                print(f"Docente '{docente}' aggiunto in coda per questo modulo.")
            except ValueError as e:
                print(f"Errore formato CF: {e}")
        else:
            break

    Modulo.create(codice, nome, ore, docenti=docenti_da_associare)
    print(f"Modulo '{nome}' creato con {len(docenti_da_associare)} docenti associati!")


def crea_corso_its():
    nome = input("Nome Corso? ")
    if not nome:
        raise ValueError("Il nome non può essere vuoto.")
    try:
        edizione = int(input("Anno di edizione del corso? ").strip())
    except ValueError as te:
        print(f"Errore: {te}")
        return

    # INFO: controlla se l'area disciplinare esiste, OBBLIGATORIO
    area_disciplinare = None
    while True:
        area_disciplinare_nome = input("Inserisci nome area disciplinare associata: ").strip()
        area_disciplinare = AreaDisciplinare.get_object_by_nome(area_disciplinare_nome)
        if area_disciplinare is None:
            print(f'Errore: area disciplinare "{area_disciplinare_nome}" non trovata.')
            print("Non è possibile creare un Corso ITS senza associare un'area disciplinare ad esso.")
            crea = input("Vuoi creare l'area disciplinare adesso? Y/N ").strip().lower()
            if crea in yes:
              crea_area_disciplinare()
            print("\nNota: verrà richiesto di inserire l'area disciplinare da associare al corso.\n")
            continue
        break
      
    # INFO: aggiungere moduli opzionali
    moduli_trovati = set()
    user_choice = input("Vuoi aggiungere dei Moduli? Y/N: ").strip().lower()
    if user_choice in yes:
      print("Moduli:")
      for n in Modulo.all_objects_by_nome():
          print(f" - {n.get_nome()}")
      moduli_scelti = input("Inserisci i moduli scrivendo i loro nomi separati da virgole:\n ").lower().strip()
      # Togliamo lo spazio anche tra i singoli moduli
      moduli = [m.strip().lower() for m in moduli_scelti.split(",") if m.strip()]
      
      for nome_modulo in moduli:
        obj_modulo = Modulo.get_object_by_nome(nome_modulo)
        if obj_modulo:
            moduli_trovati.add(obj_modulo)
            print(f"Modulo trovato: {obj_modulo.get_nome()}")
        else:
            print(f'Modulo "{nome_modulo}" non trovato, ignorato.')
        
        
    CorsoITS.create(nome, IntGEZ(edizione), area_disciplinare, moduli_trovati)
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
            raise InterruptedError

        fn = menu_actions[choice]["function"]
        if fn is not None:
            fn()
        else:
            print(f"Funzione '{menu_actions[choice]['item']}' non ancora implementata.")
