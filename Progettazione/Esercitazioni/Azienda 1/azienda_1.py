"""
azinda_1.py

Prerequisiti: Aver svolto l'Esercitazione "Azienda 1" (modulo "Progettazione").

Si consideri lo schema concettuale prodotto dagli analisti per il progetto "Azienda 1".

Si scriva un programma Python orientato agli oggetti che permetta di:

1) rappresentare impiegati con:
    - nome (str)
    - cognome (str),
    - stipendio attuale in Euro (float, impedendo che possano essere inseriti valori <= 0)
    - data di nascita (un valore del tipo Python datetime.date, v. seguito)

2) rappresentare dipartimenti con:
    - nome (str)
    - telefono (str)

3) il singolo dipartimento di afferenza di ogni impiegato e lasua data di afferenza.

4) l'impiegato direttore di ogni dipartimento.

Questi requisiti sono un frammento di quelli gestiti durante la fase di Analisi concettuale di "Azienda 1", con le seguenti semplificazioni, necessarie per permettere l'implementazione Python con i costrutti che conosciamo già:
    - un impiegato può dirigere anche più dipartimenti
      (l'analista ha invece imposto "al massimo uno")
    - ignoriamo i progetti aziendali.
"""

import sys

# Importiamo la class 'date' dal modulo 'datetime'.
# Le istanze di 'date' rappresentano valori del tipo 'Data'.
# https://docs.python.org/3/library/datetime.html#datetime.date
from datetime import date

# INFO: Relazioni UML
# INFO: Afferenza (1..1): Ogni impiegato appartiene a esattamente un dipartimento.
# INFO: Direzione (0..1): Un impiegato può dirigere un dipartimento (o nessuno).


# Class di interesse per il programma

class Dipartimento:
    nome: str
    telefono: str
    #  Per un dipartimento ci può essere un impiegato che lo dirige, 0..1
    direttore: "Impiegato | None"

    def __init__(self, n: str, t: str, d: "Impiegato | None"):
        self.nome = n
        self.telefono = t
        self.direttore = d

    def to_str(self) -> str:
        if self.direttore:
            dir_str = f"{self.direttore.cognome} {self.direttore.nome}"
        else:
            dir_str = "Nessuno"

        return (
            f"Dipartimento: {self.nome} (Tel: {self.telefono} | Direttore: {dir_str})"
        )


class Impiegato:
    nome: str
    cognome: str
    stipendio: float
    data_nascita: date
    data_afferenza: date
    dipartimento: Dipartimento
    direttore: bool

    def __init__(
        self,
        n: str,
        c: str,
        s: float,
        d: date,
        da: date,
        dip: Dipartimento,
        dir: bool = False,
    ):
        if s <= 0:
            raise ValueError("Lo stipendio deve essere maggiore di zero.")
        self.nome = n
        self.cognome = c
        self.stipendio = s
        self.data_nascita = d
        self.data_afferenza = da
        self.dipartimento = dip  # Relazione afferenza 1..1
        self.direttore = dir  # di default è False

    def to_str(self) -> str:
        if self.direttore:
            return (
                f"{self.cognome}, {self.nome}\n"
                + f"Stipendio: {self.stipendio} €\n"
                + f"Nato il: {self.data_nascita}\n"
                + f"Direttore del dipartimento '{self.dipartimento.nome}' dal {self.data_afferenza}\n"
            )

        else:
            return (
                f"{self.cognome}, {self.nome}\n"
                + f"Stipendio: {self.stipendio} €\n"
                + f"Nato il: {self.data_nascita}\n"
                + f"Afferisce a: {self.dipartimento.nome} dal {self.data_afferenza}\n"
            )


# --- Metodi di Ricerca ---


def cerca_dipartimento(nome: str, dipartimenti) -> Dipartimento | None:
    return dipartimenti.get(nome.lower(), None)


def cerca_dipartimento_per_telefono(telefono: str, dipartimenti) -> Dipartimento | None:
    for dip in dipartimenti.values():
        if dip.telefono == telefono:
            return dip
    return None


def cerca_impiegato(nome: str, cognome: str, impiegati) -> Impiegato | None:
    chiave = f"{cognome}_{nome}".lower()
    return impiegati.get(chiave, None)


# --- Metodi di Inserimento ---


def aggiungi_dipartimento(self, dipartimento: Dipartimento):
    self.dipartimenti[dipartimento.nome.lower()] = dipartimento


def aggiungi_impiegato(impiegato, impiegati):
    chiave = f"{impiegato.cognome}_{impiegato.nome}".lower()
    impiegati[chiave] = impiegato


def imposta_direzione(dipartimento: Dipartimento, impiegato: Impiegato):
    # Il precedente direttore diventa impiegato normale
    if dipartimento.direttore:
        dipartimento.direttore.direttore = False

    # Assegna il nuovo direttore al dipartimento
    dipartimento.direttore = impiegato
    impiegato.direttore = True

def ui_set_director(dipartimenti: dict[str, Dipartimento], impiegati: dict[str, Impiegato]):
    print("\n--- ASSEGNA DIRETTORE A DIPARTIMENTO ---")
    
    nome_dip = input("Nome del dipartimento: ").strip().lower()
    dip = cerca_dipartimento(nome_dip, dipartimenti)
    
    if not dip:
        print("Errore: Dipartimento non trovato.")
        return

    print(f"Dipartimento selezionato: {dip.nome}")
    scelta_emp = input("Inserisci la chiave dell'impiegato (es. rossi_mario): ").strip().lower()
    emp = impiegati.get(scelta_emp)

    if not emp:
        print("Errore: Impiegato non trovato.")
        return

    imposta_direzione(dip, emp)
    print(f"Successo! {emp.nome} {emp.cognome} ora dirige il dipartimento {dip.nome}.")


# Funzioni di interfaccia ("ui": "User interface")

def ui_empoloyees_show(impiegati: dict[str, Impiegato], direttori = False):
  if not direttori:
    return [e for e, v in impiegati.items() if not v.direttore]
  else:
    return [e for e, v in impiegati.items() if v.direttore]


def ui_departments_show(dipartimenti: dict[str, Dipartimento]):
  return [d for d, v in dipartimenti.items()]


def ui_add_department(dipartimenti: dict[str, Dipartimento], impiegati: dict[str, Impiegato], nome_predefinito = "") -> Dipartimento | None:
    print("\n--- NUOVO DIPARTIMENTO ---")
    if nome_predefinito == "":
      nome = input("Inserisci il nome del dipartimento: ").strip()
    else:
      nome = nome_predefinito 

    # Controllo univocità nome
    if cerca_dipartimento(nome, dipartimenti):
        print(f"Errore: Il dipartimento '{nome}' esiste già.")
        return None

    telefono = input("Inserisci il telefono: ").strip()

    # Controllo univocità telefono
    if cerca_dipartimento_per_telefono(telefono, dipartimenti):
        print(f"Errore: Il telefono '{telefono}' è già associato a un altro dipartimento.")
        return None

    # Mostra tutti gli impiegati non direttori
    print("\nImpiegati disponibili per la direzione:")
    candidati = ui_empoloyees_show(impiegati, direttori = False)

    if not candidati:
        print("Nessun impiegato disponibile al momento.")
    else:
        for k in candidati:
            emp = impiegati[k]
            print(f" > {k} ({emp.cognome} {emp.nome})")

    scelta = (
        input("\nScrivi la chiave del direttore o premi Invio per nessuno: ")
        .strip()
        .lower()
    )

    obj_direttore = None

    if scelta:
        if scelta in impiegati:
            emp_scelto = impiegati[scelta]

            if emp_scelto.direttore:
                print(f"Errore: {emp_scelto.nome} già dirige un altro dipartimento!")
                # Non usciamo con return, creiamo il dipartimento senza direttore
            else:
                obj_direttore = emp_scelto
                obj_direttore.direttore = True
        else:
            print("Impiegato non trovato.")
            choice = (
                input("Vuoi creare un nuovo impiegato ora? (Y/N): ").strip().lower()
            )
            if choice in ("y", "si", "sì"):
                # Nota: ui_add_employee aggiunge al dizionario 'impiegati'
                ui_add_employee(dipartimenti, impiegati)
                print(
                    "Impiegato creato. Per assegnarlo come direttore, usa la funzione di modifica (se prevista) o ricomincia."
                )

    # Creazione effettiva
    nuovo_dip = Dipartimento(nome, telefono, obj_direttore)
    dipartimenti[nome.lower()] = nuovo_dip

    # Conferma finale corretta
    nome_direttore = f"{obj_direttore.cognome} {obj_direttore.nome}" if obj_direttore else "Nessun direttore"
    print(f"\nSuccesso! {nuovo_dip.to_str()}")
    print(f"Direttore assegnato: {nome_direttore}")

    return nuovo_dip


def ui_add_employee(dipartimenti: dict[str, Dipartimento], impiegati: dict[str, Impiegato]) -> Impiegato | None:
    print("\n--- NUOVO IMPIEGATO ---")
    nome = input("Inserisci il nome: ").strip()
    cognome = input("Inserisci il cognome: ").strip()

    # Verifica univocità dell'impiegato
    if cerca_impiegato(nome, cognome, impiegati):
        print(f"Errore: L'impiegato {cognome} {nome} è già registrato.")
        return None

    try:
        stipendio = float(input("Inserisci lo stipendio: ").strip())
        if stipendio <= 0:
            print("Errore: Lo stipendio deve essere maggiore di 0.")
            return None
    except ValueError:
        print("Errore: Inserisci un numero valido per lo stipendio.")
        return None

    data_nascita = input("Inserisci la data di nascita (YYYY-MM-DD): ").strip()
    try:
        data_nascita = date.fromisoformat(data_nascita)
    except ValueError:
        print("Errore: Formato data non valido. Usa YYYY-MM-DD.")
        return None

    # Associazione Dipartimento (deve esistere)
    nome_dip = input("Inserisci il nome del dipartimento: ").strip()
    dipartimento = cerca_dipartimento(nome_dip, dipartimenti)

    if dipartimento is None:
        print(f"Errore! Il dipartimento '{nome_dip}' non esiste!" + \
          "Assicurati di creare un dipartimento prima di assegnarlo.\n")
        return None

    # Dopo che 'dipartimento' è stato valorizzato
    data_afferenza = input("Inserisci la data di afferenza (YYYY-MM-DD): ").strip()
    try:
        data_afferenza = date.fromisoformat(data_afferenza)
    except ValueError:
        print("Errore: Formato data non valido. Usa YYYY-MM-DD.")
        return None

    # HACK: Chiedere se è un impiegato semplice e quindi afferisce ad un dipartimento, oppure se lo dirige
    dirige = (
        input(
            "Questo impiegato dirige il dipartimento? Scrivere Y per confermare, qualsiasi altra risposta indica che afferisce al dipartimento:\n"
        )
        .strip()
        .lower()
    )
    assegna_direttore = False

    if dirige in ("y", "yes", "si", "sì"):
        # Verificare se c'è già un direttore. 
        # In quel caso chiedere se aggiornarlo con il nuovo oppure no.
        if dipartimento.direttore is not None:
            direttore_attuale = dipartimento.direttore
            choice = (
                input(
                    f"Esiste già un direttore per questo dipartimento: {direttore_attuale.cognome} {direttore_attuale.nome}. Vuoi aggiornarlo? (Y/N): "
                )
                .strip()
                .lower()
            )
            if choice in ("y", "yes", "si", "sì"):
                assegna_direttore = True
            else:
                print("L'impiegato verrà aggiunto come impiegato semplice.")
        else:
            assegna_direttore = True

    # Creazione e salvataggio impiegato
    nuovo_impiegato = Impiegato(
        nome,
        cognome,
        stipendio,
        data_nascita,
        data_afferenza,
        dipartimento,
        assegna_direttore,
    )

    # Se il nuovo impiegato è direttore, aggiorniamo il suo riferimento nell'oggetto Dipartimento
    if assegna_direttore:
        imposta_direzione(dipartimento, nuovo_impiegato)

    employee = aggiungi_impiegato(nuovo_impiegato, impiegati)
    if assegna_direttore:
      print(f"\nNuovo direttore aggiunto con successo:\n{nuovo_impiegato.to_str()}")
    else: 
      print(f"\nNuovo impiegato aggiunto con successo:\n{nuovo_impiegato.to_str()}")
    return employee


def ui_ask_what_to_do(dipartimenti: dict[str, Dipartimento], impiegati: dict[str, Impiegato]):
    while True:
        print(
            "\n\n\n----------\n\nScegli un'azione:\n"
            + " 1 - aggiungi dipartimento\n"
            + " 2 - aggiungi impiegato\n"
            + " 3 - mostra impiegati\n"
            + " 4 - mostra direttori\n"
            + " 5 - mostra dipartimenti\n"
            + " 6 - cambia direttore\n"
            + " 7 - esci\n"
        )

        choice = input("Digita un numero o l'azione corrispondente: ")

        if choice == "aggiungi dipartimento" or choice == "1":
            ui_add_department(dipartimenti, impiegati)
        elif choice == "aggiungi impiegato" or choice == "2":
            ui_add_employee(dipartimenti, impiegati)
        elif choice == "mostra impiegati" or choice == "3":
            print(ui_empoloyees_show(impiegati, False))
        elif choice == "mostra direttori" or choice == "4":
            print(ui_empoloyees_show(impiegati, True))
        elif choice == "mostra dipartimenti" or choice == "5":
            print(ui_departments_show(dipartimenti))
        elif choice == "cambia direttore" or choice == "6":
            ui_set_director(dipartimenti, impiegati)
        elif choice == "esci" or choice == "7":
            print("Arrivederci!")
            break
        else:
            print(f"Comando '{choice}' sconosciuto. Riprova.\n")


def main():

    # HACK: Creazione delle strutture e dati principali all'avvio del programma

    dipartimenti: dict[str, Dipartimento] = {}
    impiegati: dict[str, Impiegato] = {}

    def precarica_dati():
        dip_it = Dipartimento("IT", "123456", None)
        dip_hr = Dipartimento("HR", "654321", None)

        dipartimenti[dip_it.nome.lower()] = dip_it
        dipartimenti[dip_hr.nome.lower()] = dip_hr
        oggi = date.today()

        emp1 = Impiegato(
            "Mario", "Rossi", 2500.0, date(1985, 5, 20), oggi, dip_it, False
        )
        emp2 = Impiegato(
            "Luigi", "Verdi", 2200.0, date(1990, 11, 12), oggi, dip_it, True
        )
        dip_it.direttore = emp2
        emp3 = Impiegato(
            "Anna", "Bianchi", 2800.0, date(1988, 3, 5), oggi, dip_hr, False
        )

        # "cognome_nome" in minuscolo come chiave univoca per gli impiegati
        impiegati[f"{emp1.cognome}_{emp1.nome}".lower()] = emp1
        impiegati[f"{emp2.cognome}_{emp2.nome}".lower()] = emp2
        impiegati[f"{emp3.cognome}_{emp3.nome}".lower()] = emp3

    precarica_dati()

    ui_ask_what_to_do(dipartimenti, impiegati)
    return 0


if __name__ == "__main__":
    sys.exit(main())
