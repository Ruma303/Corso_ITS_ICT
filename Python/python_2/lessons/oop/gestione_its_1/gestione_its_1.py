"""
gestione_its_1.py

Prerequisiti:
Aver svolto l'Esercitazione "Gestione ITS 1" (modulo "Progettazione").


Si consideri lo schema concettuale prodotto dagli analisti
per il progetto "Gestione ITS 1".

Si scriva un programma Python orientato agli oggetti che implementi
lo schema concettuale per l'applicazione, con le seguenti
semplificazioni necessarie per permettere l'implementazione Python
con i costrutti che conosciamo già:
        - ammettiamo la navigazione delle associazioni in una unica direzione.

In particolare, l'applicazione deve:

1) permettere di rappresentare gli oggetti di ogni classe del diagramma
UML concettuale delle classi

2) implementare le associazioni esclusivamente nei seguenti versi:
        - reg_naz:  Regione -> Nazione
        - citta_reg: Citta -> Regione
        - stud_citta_nasc: Studente -> Citta
        - docente_citta_nasc: Docente -> Citta
        - studente_supera_modulo: Studente -> Modulo
        - studente_corso: Studente -> CorsoITS
        - corso_area: CorsoITS -> AreaDisciplinare
        - modulo_in_corso: CorsoITS -> Modulo
        - doc_insegna_modulo: Modulo -> Docente


3) gestire la persistenza dei dati tramite un file JSON.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Optional, Self

# Class di interesse per il programma

# --- Classi di supporto


class CodiceFiscale:
    def __init__(self, codice: str):
        codice_clean = codice.strip().upper()
        assert bool(re.match(r"^[A-Z0-9]{16}$", codice_clean)), (
            "Provided 'codice fiscale' format is not valid"
        )
        self.codice = codice_clean


# --- Classi Geografiche


class Nazione:
    nazioni: dict[int, Self] = dict()
    prossima = 0

    def __init__(self, idx: int, nome: str):
        self.idx = idx
        self.nome = nome

        type(self).nazioni[self.idx] = self

    @classmethod
    def create(cls, nome: str) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome)

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for nazione in cls.nazioni.values():
            if nazione.nome.lower() == nome.lower():
              return nazione
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        # HACK: .get() è un metodo sicuro dei dizionari e non lancia KeyError
        return cls.nazioni.get(idx, None)

    def __str__(self) -> str:
      return f"Nazione: {self.nome}"


class Regione:
    regioni: dict[int, Self] = dict()
    prossima = 0

    def __init__(self, idx: int, nome: str, nazione: Nazione):
        self.idx = idx
        self.nome = nome
        self.nazione = nazione

        type(self).regioni[self.idx] = self

    @classmethod
    def create(cls, nome: str, nazione: Nazione) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome, nazione)

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for regione in cls.regioni.values():
            if regione.nome.lower() == nome.lower():
              return regione
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.regioni.get(idx, None)
        
    def __str__(self) -> str:
      return f"Regione: {self.nome}"


class Citta:
    citta: dict[int, Self] = dict()
    prossima = 0
    
    def __init__(self, idx: int, nome: str, regione: Regione):
        self.idx = idx
        self.nome = nome
        self.regione = regione

        type(self).citta[self.idx] = self

    @classmethod
    def create(cls, nome: str, regione: Regione) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome, regione)

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for c in cls.citta.values():
          if c.nome.lower() == nome.lower():
            return c
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.citta.get(idx, None)
        
    def __str__(self) -> str:
      return f"Città: {self.nome}"


# --- Classi primarie


class Docente:
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: CodiceFiscale,
        citta_nascita: Citta,
    ):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.citta_nascita = citta_nascita


class Modulo:
    def __init__(
        self,
        codice: str,
        nome: str,
        ore: int,
        # HACK: assegna almeno None di default
        docenti: Optional[list[Docente]] = None,
    ):
        self.codice = codice
        self.nome = nome
        self.ore = ore
        assert ore > 0, "Module hours cannot be 0 or negative"

        # HACK: Meglio garantire almeno una lista vuota per evitare bug
        self.docenti = docenti if docenti is not None else []


class AreaDisciplinare:
    def __init__(self, nome: str):
        self.nome = nome


class CorsoITS:
    def __init__(
        self,
        nome: str,
        edizione: int,
        area_disciplinare: AreaDisciplinare,
        moduli: Optional[list[Modulo]] = None,
    ):
        self.nome = nome
        self.edizione = edizione
        assert edizione > 0, "Edition can only be a positive integer number"

        self.area_disciplinare = area_disciplinare
        self.moduli = moduli if moduli is not None else []


class Studente:
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: CodiceFiscale,
        matricola: str,
        citta_nascita: Citta,
        corso: CorsoITS,
        moduli_superati: Optional[list[Modulo]] = None,
    ):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.matricola = matricola
        self.citta_nascita = citta_nascita
        self.corso = corso
        self.moduli_superati = moduli_superati if moduli_superati is not None else []


# Funzioni di interfaccia ("ui": "User interface")


def ui_ask_what_to_do():
    while True:
        print(
            "\n****===========****\n"
            + "\nChoose an action:\n"
            + " - add ...: Add a new ...\n"
            + " - exit: Exit"
        )

        choice = input("Action? ")

        if choice == "add ...":
            pass
            # ui_add_...()
        elif choice == "exit":
            print("Arrivederci!")
            break
        else:
            print(f"{choice}? mmm, unknown command...")


def load_all(datafile):
    print(f"Loading data file '{datafile}':")
    # Implementala tu!


def save_all(datafile):
    print(f"Saving data to file '{datafile}' (nothing done, really)")
    # Implementala tu!


def main():
    # Costante globale: nome del file che mantiene i dati

    try:
        datafile = Path.cwd() / "data.json"

        load_all(datafile)
        ui_ask_what_to_do()
        save_all(datafile)
    except Exception as e:
        print(f"Error kind: {type(e).__name__}: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
