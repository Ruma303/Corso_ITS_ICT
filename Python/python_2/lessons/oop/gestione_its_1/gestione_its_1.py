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
from datetime import date
from pathlib import Path
from typing import Optional, Self

# Class di interesse per il programma

# --- Classi e metodi di supporto


def _require_instance(value, expected_type: type, field_name: str):
    assert isinstance(value, expected_type), (
        f"'{field_name}' must be an instance of {expected_type.__name__}"
    )


def _require_list(values: Optional[list], expected_type: type, field_name: str) -> list:
    if values is None:
        return []

    assert isinstance(values, list), f"'{field_name}' must be a list"
    for value in values:
        _require_instance(value, expected_type, field_name)

    return list(values)


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
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]
        result = cls(idx, nome)

        if cls.prossima <= idx:
            cls.prossima = idx

        return result

    def to_db(self) -> dict:
        return {"nome": self.nome}

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
        _require_instance(nazione, Nazione, "nazione")
        self.nazione = nazione

        type(self).regioni[self.idx] = self

    @classmethod
    def create(cls, nome: str, nazione: Nazione) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome, nazione)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]

        # MODIFICA QUI: Recuperiamo l'oggetto Nazione reale usando l'ID dal database
        id_nazione = entity["nazione"]
        nazione = Nazione.get(id_nazione)
        if nazione is None:
            raise ValueError(
                f"Nazione ID {id_nazione} non trovata per la regione {nome}"
            )

        result = cls(idx, nome, nazione)

        if cls.prossima <= idx:
            cls.prossima = idx

        return result

    def to_db(self) -> dict:
        return {"nome": self.nome, "nazione": self.nazione.idx}

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
        _require_instance(regione, Regione, "regione")
        self.regione = regione

        type(self).citta[self.idx] = self

    @classmethod
    def create(cls, nome: str, regione: Regione) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome, regione)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]

        # MODIFICA QUI: Recuperiamo l'oggetto Regione reale usando l'ID dal database
        id_regione = entity["regione"]
        regione = Regione.get(id_regione)
        if regione is None:
            raise ValueError(f"Regione ID {id_regione} non trovata per la città {nome}")

        result = cls(idx, nome, regione)

        if cls.prossima <= idx:
            cls.prossima = idx

        return result

    def to_db(self) -> dict:
        return {"nome": self.nome, "regione": self.regione.idx}

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


class Persona:
    persone: dict[str, Self] = dict()

    def __init__(
        self,
        idx: int,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ):
        self.idx = idx
        self.nome = nome
        self.cognome = cognome

        # TODO: CONTROLLARE CHE CODICE FISCALE NON SIA RIPETUTO SIA TRA DOCENTI CHE TRA STUDENTI
        # NON DEVONO TROVARSI NEL SET

        self.codice = type(self).check_cf(codice_fiscale)
        self.citta_nascita = Citta

    def __str__(self) -> str:
        return f"{self.cognome}, {self.nome} - CF: {self.codice} - {self.citta_nascita}"

    @classmethod
    def check_cf(cls, codice_fiscale: str) -> str:
        # INFO: sarebbero 16 caratteri, consentiamo anche 0 per fare test rapidi

        codice_clean = codice_fiscale.strip().upper()
        assert bool(re.match(r"^[A-Z0-9]{0,16}$", codice_clean)), (
            "Provided fiscal code format is not valid"
        )
        return codice_fiscale


class Docente(Persona):
    docenti: dict[int, Self] = dict()
    prossimo = 0

    def __init__(
        self,
        idx: int,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ):
        self.idx = idx
        super().__init__(idx, nome, cognome, codice_fiscale, citta_nascita)

        type(self).docenti[self.idx] = self

    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ) -> Self:
        cls.prossimo += 1
        return cls(cls.prossimo, nome, cognome, codice_fiscale, citta_nascita)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]
        cognome = entity["cognome"]
        codice_fiscale = Persona.check_cf(entity["codice_fiscale"])
        id_citta = entity["citta_nascita"]
        citta_nascita = Citta.get(id_citta)

        if citta_nascita is None:
            raise ValueError(
                f"City with ID {id_citta} cannot be found for teacher {cognome} {nome}"
            )

        result = cls(idx, nome, cognome, codice_fiscale, citta_nascita)

        if cls.prossimo <= idx:
            cls.prossimo = idx

        return result

    def to_db(self) -> dict:
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "codice_fiscale": self.codice_fiscale.codice,
            "citta_nascita": self.citta_nascita.idx,
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for docente in cls.docenti.values():
            if docente.nome.lower() == nome.lower():
                return docente
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.docenti.get(idx, None)

    def __str__(self) -> str:
        return "[Docente] " + super().__str__()


class Modulo:
    moduli: dict[int, Self] = dict()
    prossimo = 0

    def __init__(
        self,
        idx: int,
        codice: str,
        nome: str,
        ore: int,
        docenti: Optional[list[Docente]] = None,
    ):
        assert ore > 0, "Module hours cannot be 0 or negative"
        self.idx = idx
        self.codice = codice
        self.nome = nome
        self.ore = ore

        self.docenti = _require_list(docenti, Docente, "docenti")

        type(self).moduli[self.idx] = self

    @classmethod
    def create(
        cls, codice: str, nome: str, ore: int, docenti: Optional[list[Docente]] = None
    ) -> Self:
        cls.prossimo += 1
        return cls(cls.prossimo, codice, nome, ore, docenti)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        codice = entity["codice"]
        nome = entity["nome"]
        ore = entity["ore"]

        lista_id_docenti = entity.get("docenti", [])
        docenti_obj = []
        for id_doc in lista_id_docenti:
            doc_obj = Docente.get(id_doc)
            if doc_obj:
                docenti_obj.append(doc_obj)

        result = cls(idx, codice, nome, ore, docenti_obj)

        if cls.prossimo <= idx:
            cls.prossimo = idx

        return result

    def to_db(self) -> dict:
        return {
            "codice": self.codice,
            "nome": self.nome,
            "ore": self.ore,
            "docenti": [d.idx for d in self.docenti],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for modulo in cls.moduli.values():
            if modulo.nome.lower() == nome.lower():
                return modulo
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.moduli.get(idx, None)

    def __str__(self) -> str:
        return f"Modulo: {self.nome}"


class AreaDisciplinare:
    aree_disciplinari: dict[int, Self] = dict()
    prossima = 0

    def __init__(self, idx: int, nome: str):
        self.idx = idx
        self.nome = nome

        type(self).aree_disciplinari[self.idx] = self

    @classmethod
    def create(cls, nome: str) -> Self:
        cls.prossima += 1
        return cls(cls.prossima, nome)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]
        result = cls(idx, nome)

        if cls.prossima <= idx:
            cls.prossima = idx

        return result

    def to_db(self) -> dict:
        return {"nome": self.nome}

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for area_disciplinare in cls.aree_disciplinari.values():
            if area_disciplinare.nome.lower() == nome.lower():
                return area_disciplinare
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.aree_disciplinari.get(idx, None)

    def __str__(self) -> str:
        return f"Area disciplinare: {self.nome}"


class CorsoITS:
    corsi: dict[int, Self] = dict()
    prossimo = 0

    def __init__(
        self,
        idx: int,
        nome: str,
        edizione: int,
        area_disciplinare: AreaDisciplinare,
        moduli: Optional[list[Modulo]] = None,
    ):
        self.idx = idx
        self.nome = nome
        self.edizione = edizione
        assert edizione > 0, "Edition can only be a positive integer number"

        _require_instance(area_disciplinare, AreaDisciplinare, "area_disciplinare")
        self.area_disciplinare = area_disciplinare
        self.moduli = _require_list(moduli, Modulo, "moduli")

        type(self).corsi[self.idx] = self

    @classmethod
    def create(
        cls,
        nome: str,
        edizione: int,
        area_disciplinare: AreaDisciplinare,
        moduli: Optional[list[Modulo]] = None,
    ) -> Self:
        cls.prossimo += 1
        return cls(cls.prossimo, nome, edizione, area_disciplinare, moduli)

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]
        edizione = entity["edizione"]

        area = AreaDisciplinare.get(entity["area_disciplinare"])
        if area is None:
            raise ValueError(
                f"Area Disciplinare ID {entity['area_disciplinare']} non trovata"
            )

        lista_id_moduli = entity.get("moduli", [])
        moduli: list[Modulo] = []
        for m in lista_id_moduli:
            mod_obj = Modulo.get(m)
            if mod_obj is not None:
                moduli.append(mod_obj)

        result = cls(idx, nome, edizione, area, moduli)

        if cls.prossimo <= idx:
            cls.prossimo = idx

        return result

    def to_db(self) -> dict:
        return {
            "nome": self.nome,
            "edizione": self.edizione,
            "area_disciplinare": self.area_disciplinare.idx,
            "moduli": [m.idx for m in self.moduli],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for corso in cls.corsi.values():
            if corso.nome.lower() == nome.lower():
                return corso
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.corsi.get(idx, None)

    def __str__(self) -> str:
        return f"Corso ITS: {self.nome}"


class Studente(Persona):
    studenti: dict[int, Self] = dict()
    prossimo = 0

    def __init__(
        self,
        idx: int,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        matricola: str,
        nascita: date,
        citta_nascita: Citta,
        corso: CorsoITS,
        moduli_superati: Optional[list[Modulo]] = None,
    ):
        super().__init__(idx, nome, cognome, codice_fiscale, citta_nascita)
        self.matricola = matricola
        _require_instance(nascita, date, "nascita")
        self.nascita = nascita
        _require_instance(corso, CorsoITS, "corso")
        self.corso = corso
        self.moduli_superati = _require_list(moduli_superati, Modulo, "moduli_superati")

        type(self).studenti[self.idx] = self

    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        matricola: str,
        nascita: date,
        citta_nascita: Citta,
        corso: CorsoITS,
        moduli_superati: Optional[list[Modulo]] = None,
    ) -> Self:
        cls.prossimo += 1
        return cls(
            cls.prossimo,
            nome,
            cognome,
            codice_fiscale,
            matricola,
            nascita,
            citta_nascita,
            corso,
            moduli_superati,
        )

    @classmethod
    def create_from_db(cls, idx: int, entity: dict) -> Self:
        nome = entity["nome"]
        cognome = entity["cognome"]
        matricola = entity["matricola"]
        nascita = date.fromisoformat(entity["nascita"])

        cf_obj = Persona.check_cf(entity["codice_fiscale"])

        # 1. Gestione relazioni 1..1 (Gestiamo i potenziali None)
        citta_obj = Citta.get(entity["citta_nascita"])
        if citta_obj is None:
            raise ValueError(f"Citta ID {entity['citta_nascita']} non trovata")

        corso_obj = CorsoITS.get(entity["corso"])
        if corso_obj is None:
            raise ValueError(f"CorsoITS ID {entity['corso']} non trovato")

        # 2. Gestione relazione 0..* per il Type Checker
        lista_mod_sup = entity.get("moduli_superati", [])
        moduli_obj: list[Modulo] = []
        for m in lista_mod_sup:
            mod_obj = Modulo.get(m)
            if mod_obj is not None:
                moduli_obj.append(mod_obj)

        result = cls(
            idx,
            nome,
            cognome,
            cf_obj,
            matricola,
            nascita,
            citta_obj,
            corso_obj,
            moduli_obj,
        )

        if cls.prossimo <= idx:
            cls.prossimo = idx

        return result

    def to_db(self) -> dict:
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "matricola": self.matricola,
            "codice_fiscale": self.codice_fiscale.codice,
            "nascita": self.nascita.isoformat(),
            "citta_nascita": self.citta_nascita.idx,
            "corso": self.corso.idx,
            "moduli_superati": [m.idx for m in self.moduli_superati],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for studente in cls.studenti.values():
            if studente.nome.lower() == nome.lower():
                return studente
        return None

    @classmethod
    def get(cls, idx: int) -> Optional[Self]:
        return cls.studenti.get(idx, None)

    def __str__(self) -> str:
        return "[Studente] " + super().__str__()

    def aggiungi_moduli_superati(self, codici_str: str):
        """Riceve una stringa di codici separati da virgola (es: 'py1, java1'),
        cerca i moduli corrispondenti e li aggiunge evitando i duplicati."""

        parti = codici_str.split(",")
        for parte in parti:
            codice_pulito = parte.strip()
            if not codice_pulito:
                continue

            modulo_trovato = None
            for m in Modulo.moduli.values():
                if m.codice.lower() == codice_pulito.lower():
                    modulo_trovato = m
                    break

            if modulo_trovato is None:
                print(
                    f"\n\r\t-> Warning: Module with code '{codice_pulito}' was not found in the system."
                )
                continue

            # Simula il comportamento del SET
            if modulo_trovato not in self.moduli_superati:
                self.moduli_superati.append(modulo_trovato)
                print(f"\n\r\t-> Module '{modulo_trovato.nome}' successfully added.")
            else:
                print(
                    f"\n\r\t-> Info: The module '{modulo_trovato.nome}' is already present."
                )


# --- User Interface (UI) Functions ---


def ui_add_nazione():
    print("\n--- NEW NATION ---")
    nome = input("Nation name: ").strip()
    if Nazione.search(nome):
        print(f"Error: The nation '{nome}' already exists.")
        return

    nazione = Nazione.create(nome)
    print(f"\nSuccess! {nazione} created with ID {nazione.idx}.")


def ui_add_regione():
    print("\n--- NEW REGION ---")
    if not Nazione.nazioni:
        print("Error: You must create at least one Nation first.")
        return

    nome = input("Region name: ").strip()
    if Regione.search(nome):
        print(f"Error: The region '{nome}' already exists.")
        return

    nome_naz = input("Belonging nation name: ").strip()
    nazione = Nazione.search(nome_naz)

    if not nazione:
        print(f"Error: Nation '{nome_naz}' not found.")
        return

    regione = Regione.create(nome, nazione)
    print(f"\nSuccess! {regione} created with ID {regione.idx}.")


def ui_add_citta():
    print("\n--- NEW CITY ---")
    if not Regione.regioni:
        print("Error: You must create at least one Region first.")
        return

    nome = input("City name: ").strip()
    if Citta.search(nome):
        print(f"Error: The city '{nome}' already exists.")
        return

    nome_reg = input("Belonging region name: ").strip()
    regione = Regione.search(nome_reg)

    if not regione:
        print(f"Error: Region '{nome_reg}' not found.")
        return

    citta = Citta.create(nome, regione)
    print(f"\nSuccess! {citta} created with ID {citta.idx}.")


def ui_add_area_disciplinare():
    print("\n--- NEW DISCIPLINARY AREA ---")
    nome = input("Disciplinary area name: ").strip()
    if AreaDisciplinare.search(nome):
        print(f"Error: The area '{nome}' already exists.")
        return

    area = AreaDisciplinare.create(nome)
    print(f"\nSuccess! {area} created with ID {area.idx}.")


def ui_add_corso():
    print("\n--- NEW ITS COURSE ---")
    if not AreaDisciplinare.aree_disciplinari:
        print("Error: You must create at least one Disciplinary Area first.")
        return

    nome = input("Course name: ").strip()

    # MODIFICA: Controllo duplicati per il corso
    if CorsoITS.search(nome):
        print(f"Error: The course '{nome}' already exists.")
        return

    try:
        edizione = int(input("Edition (integer number > 0): ").strip())
    except ValueError:
        print("Error: The edition must be an integer number.")
        return

    nome_area = input("Disciplinary area name: ").strip()
    area = AreaDisciplinare.search(nome_area)

    if not area:
        print(f"Error: Disciplinary area '{nome_area}' not found.")
        return

    try:
        corso = CorsoITS.create(nome, edizione, area, moduli=[])
        print(f"\nSuccess! {corso} (Ed. {edizione}) created with ID {corso.idx}.")
    except AssertionError as e:
        print(f"Validation error: {e}")


def ui_add_modulo():
    print("\n--- NEW MODULE ---")
    nome = input("Module name: ").strip()

    if Modulo.search(nome):
        print(f"Error: The module '{nome}' already exists.")
        return

    codice = input("Module code: ").strip()

    try:
        ore = int(input("Hours (integer number > 0): ").strip())
    except ValueError:
        print("Error: Hours must be an integer number.")
        return

    docenti_selezionati = []
    if Docente.docenti:
        print("\nAvailable teachers:")
        for idx, doc in Docente.docenti.items():
            print(f"  [{idx}] {doc.nome} {doc.cognome}")

        ids_str = input(
            "Enter teacher IDs separated by comma (e.g., 1,2) or leave empty: "
        ).strip()
        if ids_str:
            for id_str in ids_str.split(","):
                try:
                    t_id = int(id_str.strip())
                    docente_obj = Docente.get(t_id)
                    if docente_obj:
                        docenti_selezionati.append(docente_obj)
                    else:
                        print(f"Warning: Teacher ID {t_id} not found. Skipping.")
                except ValueError:
                    print(f"Warning: Invalid ID '{id_str}'. Skipping.")

    try:
        modulo = Modulo.create(codice, nome, ore, docenti_selezionati)
        print(f"\nSuccess! {modulo} created with ID {modulo.idx}.")
    except AssertionError as e:
        print(f"Validation error: {e}")


def ui_add_docente():
    print("\n--- NEW TEACHER ---")
    if not Citta.citta:
        print("Error: You must create at least one City for the birth place first.")
        return

    nome = input("First name: ").strip()
    cognome = input("Last name: ").strip()
    cf_str = input("Fiscal Code (Codice Fiscale): ").strip()

    try:
        cf = CodiceFiscale(cf_str)
    except AssertionError as e:
        print(f"Fiscal Code error: {e}")
        return

    nome_citta = input("City of birth: ").strip()
    citta = Citta.search(nome_citta)

    if not citta:
        print(f"Error: City '{nome_citta}' not found.")
        return

    docente = Docente.create(nome, cognome, cf, citta)
    print(f"\nSuccess! {docente} created with ID {docente.idx}.")


def ui_add_studente():
    print("\n--- NEW STUDENT ---")
    if not Citta.citta:
        print("Error: You must create at least one City for the birth place first.")
        return
    if not CorsoITS.corsi:
        print(
            "Error: You must create at least one ITS Course to enroll the student first."
        )
        return

    nome = input("First name: ").strip()
    cognome = input("Last name: ").strip()
    matricola = input("Student ID (Matricola): ").strip()
    cf_str = input("Fiscal Code (Codice Fiscale): ").strip()
    cf = Persona.check_cf(cf_str)
    if not cf:
        return

    data_str = input("Birth date (YYYY-MM-DD): ").strip()
    try:
        nascita = date.fromisoformat(data_str)
    except ValueError:
        print("Error: Invalid date format.")
        return

    nome_citta = input("City of birth: ").strip()
    citta = Citta.search(nome_citta)
    if not citta:
        print(f"Error: City '{nome_citta}' not found.")
        return

    nome_corso = input("ITS Course name: ").strip()
    corso = CorsoITS.search(nome_corso)
    if not corso:
        print(f"Error: Course '{nome_corso}' not found.")
        return

    studente = Studente.create(
        nome, cognome, cf, matricola, nascita, citta, corso, moduli_superati=[]
    )
    print(f"\nSuccess! {studente} created with ID {studente.idx}.")

    # RICHIESTA DEI MODULI SUPERATI
    if Modulo.moduli:
        print("\nAvailable modules in the system:")
        for mod in Modulo.moduli.values():
            print(f"  [{mod.codice}] {mod.nome}")

        codici_input = input(
            "\nEnter the codes of passed modules separated by comma (e.g., py1,java1) or leave empty: "
        ).strip()
        if codici_input:
            studente.aggiungi_moduli_superati(codici_input)
    else:
        print("\nNote: No modules available in the system yet to assign as passed.")


def ui_show_all():
    print("\n--- CURRENT DATA SUMMARY ---")
    print(f"\nNations: {len(Nazione.nazioni)}")
    print(f"\nRegions: {len(Regione.regioni)}")
    print(f"\nCities: {len(Citta.citta)}")
    print(f"\nDisciplinary Areas: {len(AreaDisciplinare.aree_disciplinari)}")
    print(f"\nITS Courses: {len(CorsoITS.corsi)}")
    print(f"\nModules: {len(Modulo.moduli)}")
    print(f"\nTeachers: {len(Docente.docenti)}")
    print(f"\nStudents: {len(Studente.studenti)}")


def ui_ask_what_to_do():
    print(initial_greetings())

    while True:
        print(
            "\n======================\n"
            "\nChoose an action:\n\n"
            "\r\t1 - Add Nation\n"
            "\r\t2 - Add Region\n"
            "\r\t3 - Add City\n"
            "\r\t4 - Add Disciplinary Area\n"
            "\r\t5 - Add ITS Course\n"
            "\r\t6 - Add Module\n"
            "\r\t7 - Add Teacher\n"
            "\r\t8 - Add Student\n"
            "\r\t9 - View current data summary\n"
            "\r\t0 - Exit\n"
        )

        choice = input("Enter a number:\n\r\t> ").strip()

        if choice == "1":
            ui_add_nazione()
        elif choice == "2":
            ui_add_regione()
        elif choice == "3":
            ui_add_citta()
        elif choice == "4":
            ui_add_area_disciplinare()
        elif choice == "5":
            ui_add_corso()
        elif choice == "6":
            ui_add_modulo()
        elif choice == "7":
            ui_add_docente()
        elif choice == "8":
            ui_add_studente()
        elif choice == "9":
            ui_show_all()
        elif choice == "0" or choice.lower() == "exit":
            print(goodbye())
            break
        else:
            print(f"\nCommand '{choice}' unknown. Please try again.\n")


def load_all(datafile, load_sequence):
    print(f"\nLoading data file '{datafile}':\n")

    try:
        with open(datafile, "rt", encoding="utf-8") as f:
            datajson: dict = json.load(f)
    except FileNotFoundError:
        print(f"\nError: File not found at '{datafile}'\n")
        return
    except json.JSONDecodeError:
        print("\nError: Failed to decode JSON. File might be corrupted.\n")
        return

    # Un unico ciclo pulito per elaborare tutte le entità
    for key, cls, _ in load_sequence:
        if key not in datajson:
            print(f"\nWarning: Key '{key}' missing in data file. Skipping.\n")
            continue

        print(f"\n\r-> Loading {key}...\n")
        for i, obj in datajson[key].items():
            try:
                # Invochiamo le factory delle specifiche classi
                instance = cls.create_from_db(int(i), obj)
                print(f"\r\t- [{i}] {instance} created")
            except Exception as e:
                print(f"\tError while reading {cls.__name__} ID {i}: {e}")


def save_all(datafile, load_sequence):
    print(f"\nSaving data to file '{datafile}':")

    data_structure: dict = {}

    # Iteriamo sulla struttura passata esternamente
    for key, _, registry in load_sequence:
        print(f"\n\t-> Serializing {key}...")

        # Prepariamo il sotto-dizionario per la classe corrente (es: data_structure['Nazioni'] = {})
        data_structure[key] = {}

        # Prendiamo ogni istanza salvata nel registro di classe (es. Nazione.nazioni)
        for idx, instance in registry.items():
            # Invochiamo il metodo to_db() dell'oggetto per ottenere il dizionario pulito
            data_structure[key][str(idx)] = instance.to_db()

    try:
        with open(datafile, "wt", encoding="utf-8") as fp:
            json.dump(data_structure, fp, indent=2)
        print("\nSuccess! Data saved successfully.\nGoodbye!\n")
    except Exception as e:
        print(f"Error during save execution: {type(e).__name__}: {e}")


def main():

    # HACK: principio DRY - Do not Repeat Yourself
    # questa lista contiene delle tuple di tre elementi che consentono
    # ai metodi I/O di essere totalmente generici. I tre valori sono:

    # 1. Nome della chiave all'interno del file JSON
    # 2. La classe, in modo che nel ciclo si attivi il factory method di quella classe
    # 3. Dizionario di memoria utilizzato in scrittura da save_all() ES. ogni volta che creiamo una nazione, il costruttore salva dentro il dizionario Nazione.nazioni. Viene usato lo stesso
    # dizionario per sapere dove iterare e creare oggetti JSON di quella classe.

    load_sequence = [
        # (Chiave JSON, Classe, Dizionario delle istanze in memoria)
        ("Nations", Nazione, Nazione.nazioni),
        ("Regions", Regione, Regione.regioni),
        ("Cities", Citta, Citta.citta),
        ("DisciplinaryAreas", AreaDisciplinare, AreaDisciplinare.aree_disciplinari),
        ("Teachers", Docente, Docente.docenti),
        ("Modules", Modulo, Modulo.moduli),
        ("ITSCourses", CorsoITS, CorsoITS.corsi),
        ("Students", Studente, Studente.studenti),
    ]
    try:
        datafile = Path.cwd() / "data.json"

        load_all(datafile, load_sequence)
        ui_ask_what_to_do()
        save_all(datafile, load_sequence)
    except Exception as e:
        print(f"Error kind: {type(e).__name__}: {e}")

    return 0


def initial_greetings():
    return """
\r\t░██████╗░███████╗░██████╗████████╗██╗░█████╗░███╗░░██╗███████╗  ██╗████████╗░██████╗
\r\t██╔════╝░██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝  ██║╚══██╔══╝██╔════╝
\r\t██║░░██╗░█████╗░░╚█████╗░░░░██║░░░██║██║░░██║██╔██╗██║█████╗░░  ██║░░░██║░░░╚█████╗░
\r\t██║░░╚██╗██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░██║██║╚████║██╔══╝░░  ██║░░░██║░░░░╚═══██╗
\r\t╚██████╔╝███████╗██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║███████╗  ██║░░░██║░░░██████╔╝
\r\t░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝  ╚═╝░░░╚═╝░░░╚═════╝░
  """


def goodbye():
    return """
\r\t░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
\r\t██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
\r\t██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
\r\t██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
\r\t╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
\r\t░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝
  """


if __name__ == "__main__":
    sys.exit(main())
