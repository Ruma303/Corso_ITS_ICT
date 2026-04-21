"""
Progetto: Sistema di Gestione Conti Correnti
Obiettivo: Sviluppare un'applicazione che permetta di gestire le operazioni fondamentali di un conto bancario attraverso un menu interattivo.

Requisiti del Progetto: Il programma dovrà permettere all'utente di:

Creare un conto: Inserire il nome del titolare e definire un saldo iniziale.

Effettuare un deposito: Aggiungere una cifra al saldo attuale.

Effettuare un prelievo: Sottrarre una cifra dal saldo, con un controllo che impedisca di prelevare più di quanto disponibile.

Visualizzare il saldo: Mostrare il riepilogo del nome del titolare e la disponibilità attuale.

Trasferire fondi a un altro utente

Specifiche Tecniche:

Struttura Dati: Utilizzare variabili semplici o un dizionario per memorizzare i dati del conto (es. conto = {"titolare": "Nome", "saldo": 100.0}).

Logica di Controllo: Implementare un ciclo while per mantenere attivo il menu principale finché l'utente non sceglie l'opzione di uscita.

Implementazione: È possibile procedere scrivendo il codice Python completo oppure strutturando la logica tramite pseudocodice dettagliato, concentrandosi sulla correttezza dei passaggi logici (input, calcolo, controllo, output).
"""

correntisti = dict()

# Creazione utente
def crea():
    titolare = input("Inserire nome correntista: ").strip()
    saldo_iniziale = float(input("Inserire il saldo iniziale: ").strip())
    # Salva o aggiorna il saldo del correntista
    correntisti[titolare] = saldo_iniziale
    print(f"\n***Correntista {titolare} con saldo iniziale {saldo_iniziale} creato con successo!***\n")


# Funzione di cortesia per verificare se esiste un correntista
def trova_correntista():
  titolare = input("\nInserire il nome del correntista per depositare nel proprio saldo: ").strip().lower()

  # Il metodo keys ritorna tutte le chiavi di un dizionario
  # Se il nome non si trova nel dizionario, usciamo
  if titolare not in correntisti.keys():
    print(f"\nCorrentista {titolare} non trovato. Visualizzare i correntisti disponibili.")
    return False, None
  return True, titolare


# Effettuare deposito
def deposita():
    esiste, correntista = trova_correntista()
    if esiste:
        try:
            ammontare = float(input("\nInserire un ammontare superiore a 0 da depositare: ").strip())
        except ValueError:
            print("\nImporto non valido: inserire un numero.")
            return
        if ammontare > 0:
            correntisti[correntista] += ammontare
            deposito = correntisti[correntista]
            print(f"\nDepositati {ammontare:.2f}€ su {correntista}. Saldo attuale: {correntisti[correntista]:.2f}€")
            return deposito
        else:
            print("\nIl nuovo deposito non può essere negativo o zero.")


# Effettuare prelievo
def preleva():
    esiste, correntista = trova_correntista()
    if esiste:
        try:
            importo = float(input("\nInserire una cifra da prelevare: ").strip())
        except ValueError:
            print("\nImporto non valido: inserire un numero.")
            return
        saldo = correntisti.get(correntista)
        if saldo is None:
            print("\nErrore interno: saldo non trovato.")
            return
        if importo <= 0:
            print("\nIl prelievo deve essere maggiore di zero.")
        elif importo > saldo:
            print(f"\nPrelievo non consentito: saldo disponibile {saldo:.2f}€, richiesto {importo:.2f}€.")
        else:
            correntisti[correntista] -= importo
            prelievo = correntisti[correntista]
            print(f"\nPrelevati {importo:.2f}€ da {correntista}. Saldo attuale: {correntisti[correntista]:.2f}€")
            return prelievo


# Funzione di cortesia per visualizzare tutti i correntisti
def tutti_correntisti():
  print("\n--- Lista dei correntisti e saldi ---")
  if not correntisti:
      print("Nessun correntista presente.")
  else: # Lista di tutti i correntisti e loro saldo
    for i, (nome, saldo) in enumerate(correntisti.items()):
      print(f"\t{i+1}. {nome} : {saldo:.2f}€")


# Visualizzare il saldo
def visualizza():
  tutti_correntisti()

  titolare = input("\nInserire il nome del correntista per visualizzare il suo saldo: ").strip().lower()
  saldo = correntisti.get(titolare)

  if saldo is not None:
      print(f"\nIl saldo del correntista {titolare} è di {saldo:.2f}€\n")
  else:
      print(f"\n404 - Correntista '{titolare}' non trovato.\n")


# Trasferire saldo ad altro utente
def trasferisci():
    tutti_correntisti()
    print("\n*** Trasferimento tra correntisti ***")

    pagante = input("Correntista da cui prelevare: ").strip()
    beneficiario = input("Correntista destinatario: ").strip()

    if pagante not in correntisti:
        print(f"\nCorrentista '{pagante}' non trovato.")
        return
    if beneficiario not in correntisti:
        print(f"\nCorrentista '{beneficiario}' non trovato.")
        return

    # Trasferimento effettivo dell'importo tra correntisti
    try:
        ammontare = float(input("Ammontare del trasferimento: ").strip())
    except ValueError:
        print("\nImporto non valido: inserire un numero.")
        return
    if ammontare <= 0:
        print("\nNon è possibile trasferire importi nulli o negativi.")
        return
    saldo_pagante = correntisti[pagante]
    if ammontare > saldo_pagante:
        print(f"\nTrasferimento non eseguibile: saldo disponibile {saldo_pagante:.2f}€, richiesto {ammontare:.2f}€.")
        return

    # Aggiornamento dei saldi dei correntisti
    correntisti[pagante] -= ammontare # Riduzione del saldo del pagante
    correntisti[beneficiario] += ammontare # Aumento del saldo del beneficiario

    print(f"\nTrasferiti {ammontare:.2f}€ da '{pagante}' a '{beneficiario}'.")
    print(f"Nuovo saldo di '{pagante}': {correntisti[pagante]:.2f}€")
    print(f"Nuovo saldo di '{beneficiario}': {correntisti[beneficiario]:.2f}€\n")


# Menu delle opzioni disponibili
def menu():
  esci = True
  while esci:

    print("""
      ****************************************
      Selezionare un'opzione tra le seguenti:
      \t- 1: Creare un nuovo utente
      \t- 2: Depositare nel proprio saldo
      \t- 3: Prelevare dal proprio saldo
      \t- 4: Visualizzare il proprio saldo
      \t- 5: Trasferire fondi ad un altro utente
      \t- 0: Uscire
      ****************************************
      """)

    # Gestione delle scelte di menu tramite un costrutto match
    # che richiama le funzioni precedentemente definite

    try:
      scelta = int(input("Inserire un numero da 1 a 5 per le operazioni, 0 per uscire: ").strip())

      match scelta:
        case 1: crea()
        case 2: deposita()
        case 3: preleva()
        case 4: visualizza()
        case 5: trasferisci()
        case 0:
          print("\nGrazie per aver usato la nostra applicazione!\n")
          esci = False
        case _:
          print(f"\n===== Input {scelta} non valido. Riprovare. ======\n")
          continue # Qualsiasi altro input -> il ciclo si ripete

    except ValueError as ve:
      print("\n===========================")
      print("L'input non è corretto! Inserire esclusivamente un numero intero!", ve)
      print("===========================\n")

# Esecuzione del programma
menu()