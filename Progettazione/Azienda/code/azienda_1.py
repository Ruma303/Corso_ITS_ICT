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

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

# Class di interesse per il programma


class Dipartimento:
    dipartimenti: dict[str, Dipartimento] = {}

    def __init__(self, n: str, t: str, d: Impiegato | None, id_: str | None = None):
        self.id = id_
        self.nome = n
        self.telefono = t
        self.direttore = d

    def to_str(self) -> str:
        dir_str = (
            f"{self.direttore.cognome} {self.direttore.nome}"
            if self.direttore
            else "Nessuno"
        )
        return (
            f"Dipartimento: {self.nome} (Tel: {self.telefono} | Direttore: {dir_str})"
        )

    def imposta_direzione(self, nuovo_direttore: Impiegato):
        precedente_direttore = self.direttore

        if self.direttore:
            self.direttore.direttore = False

        self.direttore = nuovo_direttore
        nuovo_direttore.direttore = True

        if precedente_direttore and precedente_direttore is not nuovo_direttore:
            precedente_direttore.direttore = any(
                d.direttore is precedente_direttore
                for d in Dipartimento.dipartimenti.values()
            )

    @classmethod
    def cerca(cls, nome: str) -> Dipartimento | None:
        return cls.dipartimenti.get(nome.lower(), None)

    @classmethod
    def cerca_per_telefono(cls, telefono: str) -> Dipartimento | None:
        for dip in cls.dipartimenti.values():
            if dip.telefono == telefono:
                return dip
        return None


class Impiegato:
    impiegati: dict[str, Impiegato] = {}

    def __init__(
        self,
        nome: str,
        cognome: str,
        stipendio: float,
        data_nascita: date,
        data_afferenza: date,
        dipartimento: Dipartimento | None,
        direttore: bool = False,
        id_: str | None = None,
    ):
        assert stipendio > 0.0, "Lo stipendio deve essere maggiore di zero."
        self.id = id_
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        self.data_nascita = data_nascita
        self.data_afferenza = data_afferenza
        self.dipartimento = dipartimento  # Relazione afferenza 1..1
        self.direttore = direttore  # di default è False

    def to_str(self) -> str:
        nome_dip = self.dipartimento.nome if self.dipartimento else "Nessuno"

        if self.direttore:
            info_ruolo = (
                f"Direttore del dipartimento '{nome_dip}' dal {self.data_afferenza}"
            )
        else:
            info_ruolo = f"Afferisce a: {nome_dip} dal {self.data_afferenza}"

        return (
            f"{self.cognome}, {self.nome}\n"
            f"Stipendio: {self.stipendio} €\n"
            f"Nato il: {self.data_nascita}\n"
            f"{info_ruolo}\n"
        )

    @staticmethod
    def genera_chiave(nome: str, cognome: str) -> str:
        return f"{cognome}_{nome}".lower()

    @classmethod
    def cerca(cls, nome: str, cognome: str) -> Impiegato | None:
        chiave = cls.genera_chiave(nome, cognome)
        return cls.impiegati.get(chiave, None)


# --- Metodi di Inserimento ed Interfaccia (UI) ---


def ui_set_director():
    print("\n--- ASSEGNA DIRETTORE A DIPARTIMENTO ---")

    nome_dip = input("Nome del dipartimento: ").strip().lower()
    dip = Dipartimento.cerca(nome_dip)

    if not dip:
        print("Errore: Dipartimento non trovato.")
        return

    print(f"Dipartimento selezionato: {dip.nome}")
    scelta_emp = (
        input("Inserisci la chiave dell'impiegato (es. rossi_mario): ").strip().lower()
    )
    emp = Impiegato.impiegati.get(scelta_emp)

    if not emp:
        print("Errore: Impiegato non trovato.")
        return

    dip.imposta_direzione(emp)
    print(f"Successo! {emp.nome} {emp.cognome} ora dirige il dipartimento {dip.nome}.")


def ui_empoloyees_show(direttori=False):
    if not direttori:
        return [e for e, v in Impiegato.impiegati.items() if not v.direttore]
    else:
        return [e for e, v in Impiegato.impiegati.items() if v.direttore]


def ui_departments_show():
    return [d for d in Dipartimento.dipartimenti.keys()]


def ui_add_department(nome_predefinito="") -> Dipartimento | None:
    print("\n--- NUOVO DIPARTIMENTO ---")
    if nome_predefinito == "":
        nome = input("Inserisci il nome del dipartimento: ").strip()
    else:
        nome = nome_predefinito

    if Dipartimento.cerca(nome):
        print(f"Errore: Il dipartimento '{nome}' esiste già.")
        return None

    telefono = input("Inserisci il telefono: ").strip()

    if Dipartimento.cerca_per_telefono(telefono):
        print(
            f"Errore: Il telefono '{telefono}' è già associato a un altro dipartimento."
        )
        return None

    print("\nImpiegati disponibili per la direzione:")
    candidati = list(Impiegato.impiegati.keys())

    if not candidati:
        print("Nessun impiegato disponibile al momento.")
    else:
        for k in candidati:
            emp = Impiegato.impiegati[k]
            print(f" > {k} ({emp.cognome} {emp.nome})")

    scelta = (
        input("\nScrivi la chiave del direttore o premi Invio per nessuno: ")
        .strip()
        .lower()
    )

    obj_direttore = None

    if scelta:
        if scelta in Impiegato.impiegati:
            obj_direttore = Impiegato.impiegati[scelta]
        else:
            print("Impiegato non trovato.")
            choice = (
                input("Vuoi creare un nuovo impiegato ora? (Y/N): ").strip().lower()
            )
            if choice in ("y", "si", "sì"):
                ui_add_employee()
                print(
                    "Impiegato creato. Per assegnarlo come direttore, usa la funzione di modifica o ricomincia."
                )

    nuovo_dip = Dipartimento(nome, telefono, None)
    Dipartimento.dipartimenti[nome.lower()] = nuovo_dip

    if obj_direttore:
        nuovo_dip.imposta_direzione(obj_direttore)

    nome_direttore = (
        f"{obj_direttore.cognome} {obj_direttore.nome}"
        if obj_direttore
        else "Nessun direttore"
    )
    print(f"\nSuccesso! {nuovo_dip.to_str()}")
    print(f"Direttore assegnato: {nome_direttore}")

    return nuovo_dip


def ui_add_employee() -> Impiegato | None:
    print("\n--- NUOVO IMPIEGATO ---")
    nome = input("Inserisci il nome: ").strip()
    cognome = input("Inserisci il cognome: ").strip()

    if Impiegato.cerca(nome, cognome):
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

    nome_dip = input("Inserisci il nome del dipartimento: ").strip()
    dipartimento = Dipartimento.cerca(nome_dip)

    if dipartimento is None:
        print(
            f"Errore! Il dipartimento '{nome_dip}' non esiste!\n"
            f"Assicurati di creare un dipartimento prima di assegnarlo.\n"
        )
        return None

    data_afferenza = input("Inserisci la data di afferenza (YYYY-MM-DD): ").strip()
    try:
        data_afferenza = date.fromisoformat(data_afferenza)
    except ValueError:
        print("Errore: Formato data non valido. Usa YYYY-MM-DD.")
        return None

    dirige = (
        input(
            "Questo impiegato dirige il dipartimento? Scrivere Y per confermare, qualsiasi altra risposta indica che afferisce al dipartimento:\n"
        )
        .strip()
        .lower()
    )
    assegna_direttore = False

    if dirige in ("y", "yes", "si", "sì"):
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

    # Creazione impiegato
    nuovo_impiegato = Impiegato(
        nome,
        cognome,
        stipendio,
        data_nascita,
        data_afferenza,
        dipartimento,
        assegna_direttore,
    )

    if assegna_direttore:
        dipartimento.imposta_direzione(nuovo_impiegato)

    # Salvataggio diretto nell'attributo di classe usando il metodo statico per la chiave
    chiave = Impiegato.genera_chiave(nome, cognome)
    Impiegato.impiegati[chiave] = nuovo_impiegato

    if assegna_direttore:
        print(f"\nNuovo direttore aggiunto con successo:\n{nuovo_impiegato.to_str()}")
    else:
        print(f"\nNuovo impiegato aggiunto con successo:\n{nuovo_impiegato.to_str()}")

    return nuovo_impiegato


def ui_ask_what_to_do():
    while True:
        print(
            "\n======================\n"
            "\nScegli un'azione:\n"
            "\r\t1 - aggiungi dipartimento\n"
            "\r\t2 - aggiungi impiegato\n"
            "\r\t3 - mostra impiegati\n"
            "\r\t4 - mostra direttori\n"
            "\r\t5 - mostra dipartimenti\n"
            "\r\t6 - cambia direttore\n"
            "\r\t7 - esci\n\n"
        )

        choice = input("Digita un numero o l'azione corrispondente: ").strip().lower()

        if choice in ("aggiungi dipartimento", "1"):
            ui_add_department()
        elif choice in ("aggiungi impiegato", "2"):
            ui_add_employee()
        elif choice in ("mostra impiegati", "3"):
            print(ui_empoloyees_show(False))
        elif choice in ("mostra direttori", "4"):
            print(ui_empoloyees_show(True))
        elif choice in ("mostra dipartimenti", "5"):
            print(ui_departments_show())
        elif choice in ("cambia direttore", "6"):
            ui_set_director()
        elif choice in ("esci", "7"):
            print("Arrivederci!")
            break
        else:
            print(f"\nComando '{choice}' sconosciuto. Riprova.\n")


def iter_record_json(dati: dict | list):
    if isinstance(dati, dict):
        return dati.items()
    return ((str(i), record) for i, record in enumerate(dati))


def valore_id_json(id_: str | None) -> int | str | None:
    if id_ is None:
        return None
    if id_.isdigit():
        return int(id_)
    return id_


def prossimo_id(id_usati: set[str]) -> str:
    id_numerici = [int(id_) for id_ in id_usati if id_.isdigit()]
    nuovo_id = max(id_numerici, default=-1) + 1
    while str(nuovo_id) in id_usati:
        nuovo_id += 1
    return str(nuovo_id)


def assegna_id_mancanti():
    id_dipartimenti = {
        dip.id for dip in Dipartimento.dipartimenti.values() if dip.id is not None
    }
    for dip in Dipartimento.dipartimenti.values():
        if dip.id is None:
            dip.id = prossimo_id(id_dipartimenti)
            id_dipartimenti.add(dip.id)

    id_impiegati = {
        emp.id for emp in Impiegato.impiegati.values() if emp.id is not None
    }
    for emp in Impiegato.impiegati.values():
        if emp.id is None:
            emp.id = prossimo_id(id_impiegati)
            id_impiegati.add(emp.id)


def aggiorna_flag_direttori():
    for emp in Impiegato.impiegati.values():
        emp.direttore = any(
            dip.direttore is emp for dip in Dipartimento.dipartimenti.values()
        )


def precarica_dati(data_dir: Path):
    """
    In questa versione ogni dizionario deriva da un file diverso
    """
    file_dip = data_dir / "departments.json"
    file_emp = data_dir / "employees.json"

    Dipartimento.dipartimenti.clear()
    Impiegato.impiegati.clear()

    if not file_dip.exists() or not file_emp.exists():
        print(
            "⚠️ Attenzione: File di configurazione JSON non trovati in 'data/'. Il programma partirà vuoto."
        )
        return

    # Phase 1: Carica i dipartimenti in memoria (senza direttore per ora)
    with open(file_dip, "r", encoding="utf-8") as f:
        dati_dipartimenti = json.load(f)

    mappa_direttori_temp = {}  # Memorizza momentaneamente quale impiegato deve dirigere cosa
    mappa_dipartimenti_per_id: dict[str, Dipartimento] = {}
    for id_dip, d in iter_record_json(dati_dipartimenti):
        nuovo_dip = Dipartimento(d["nome"], d["telefono"], None, str(id_dip))
        Dipartimento.dipartimenti[nuovo_dip.nome.lower()] = nuovo_dip
        mappa_dipartimenti_per_id[str(id_dip)] = nuovo_dip
        if d.get("direttore_id"):
            mappa_direttori_temp[nuovo_dip.nome.lower()] = d["direttore_id"]

    # Phase 2: Carica gli impiegati legandoli al rispettivo dipartimento oggetto
    with open(file_emp, "r", encoding="utf-8") as f:
        dati_impiegati = json.load(f)

    for id_emp, e in iter_record_json(dati_impiegati):
        id_dipartimento = e.get("dipartimento_id")
        dip_obj = mappa_dipartimenti_per_id.get(str(id_dipartimento))
        if dip_obj is None and id_dipartimento is not None:
            dip_obj = Dipartimento.cerca(str(id_dipartimento))

        nuovo_emp = Impiegato(
            nome=e["nome"],
            cognome=e["cognome"],
            stipendio=float(e["stipendio"]),
            data_nascita=date.fromisoformat(e["data_nascita"]),
            data_afferenza=date.fromisoformat(e["data_afferenza"]),
            dipartimento=dip_obj,
            direttore=bool(e.get("direttore", False)),
            id_=str(id_emp),
        )
        chiave_emp = Impiegato.genera_chiave(nuovo_emp.nome, nuovo_emp.cognome)
        Impiegato.impiegati[chiave_emp] = nuovo_emp

    # Phase 3: Ricostruisci i riferimenti ai direttori d'ufficio ora che tutti gli oggetti esistono
    for nome_dip_min, chiave_direttore in mappa_direttori_temp.items():
        dip_obj = Dipartimento.dipartimenti.get(nome_dip_min)
        emp_obj = Impiegato.impiegati.get(str(chiave_direttore).lower())
        if dip_obj and emp_obj:
            dip_obj.direttore = emp_obj

    aggiorna_flag_direttori()


def salva_dati(data_dir: Path):
    file_dip = data_dir / "departments.json"
    file_emp = data_dir / "employees.json"

    data_dir.mkdir(parents=True, exist_ok=True)
    assegna_id_mancanti()
    aggiorna_flag_direttori()

    dati_dipartimenti = {}
    for dip in Dipartimento.dipartimenti.values():
        dati_dipartimenti[dip.id] = {
            "nome": dip.nome,
            "telefono": dip.telefono,
            "direttore_id": (
                Impiegato.genera_chiave(dip.direttore.nome, dip.direttore.cognome)
                if dip.direttore
                else None
            ),
        }

    dati_impiegati = {}
    for emp in Impiegato.impiegati.values():
        dati_impiegati[emp.id] = {
            "nome": emp.nome,
            "cognome": emp.cognome,
            "stipendio": emp.stipendio,
            "data_nascita": emp.data_nascita.isoformat(),
            "data_afferenza": emp.data_afferenza.isoformat(),
            "dipartimento_id": valore_id_json(emp.dipartimento.id)
            if emp.dipartimento
            else None,
            "direttore": emp.direttore,
        }

    with open(file_dip, "w", encoding="utf-8") as f:
        json.dump(dati_dipartimenti, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(file_emp, "w", encoding="utf-8") as f:
        json.dump(dati_impiegati, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    dati_caricati = False

    try:
        precarica_dati(data_dir)
        dati_caricati = True
        ui_ask_what_to_do()
    except KeyboardInterrupt:
        print("\nUscita richiesta.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
    finally:
        if dati_caricati:
            try:
                salva_dati(data_dir)
                print("Dati salvati.")
            except Exception as e:
                print(f"Errore durante il salvataggio: {e.__class__.__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
