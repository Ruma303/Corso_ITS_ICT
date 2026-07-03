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

# TODO: Durante la creazione di Docenti e Studenti cambiare la chiave non con numero intero,
# ma con il codice fiscale stesso.
# In questo modo avremmo Persone.persone con chiavi i codici fiscali, e valori le istanze.

from __future__ import annotations

import json
import re
import sys
from abc import ABC
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
    __nazioni: dict[str, Self] = dict()
    __prossima = 0

    def __init__(self, nome: str):
        self.set_nome(nome)
        type(self).get_nazioni()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    @classmethod
    def get_nazioni(cls) -> dict[str, Self]:
        return cls.__nazioni

    @classmethod
    def set_nazioni(cls, nazioni: dict[str, Self]):
        cls.__nazioni = nazioni

    @classmethod
    def create(cls, nome: str) -> Self:
        if nome in cls.get_nazioni():
            raise ValueError(f"Nazione '{nome}' already exists")
        return cls(nome)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        return cls(nome)

    def to_db(self) -> dict:
        return {"nome": self.get_nome()}

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for nazione in cls.get_nazioni().values():
            if nazione.get_nome().lower() == nome.lower():
                return nazione
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_nazioni().get(k, None)

    def __str__(self) -> str:
        return f"Nazione: {self.get_nome()}"


class Regione:
    __regioni: dict[str, Self] = dict()
    __prossima = 0

    def __init__(self, nome: str, nazione: Nazione):
        self.set_nome(nome)
        self.set_nazione(nazione)
        type(self).get_regioni()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_nazione(self) -> Nazione:
        return self._nazione

    def set_nazione(self, nazione: Nazione):
        _require_instance(nazione, Nazione, "nazione")
        self._nazione = nazione

    @classmethod
    def get_prossima(cls) -> int:
        return cls.__prossima

    @classmethod
    def set_prossima(cls, prossima: int):
        cls.__prossima = prossima

    @classmethod
    def get_regioni(cls) -> dict[str, Self]:
        return cls.__regioni

    @classmethod
    def set_regioni(cls, regioni: dict[str, Self]):
        cls.__regioni = regioni

    @classmethod
    def create(cls, nome: str, nazione: Nazione) -> Self:
        cls.set_prossima(cls.get_prossima() + 1)
        return cls(nome, nazione)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        id_nazione = entity["nazione"]
        nazione = Nazione.get(id_nazione)
        if nazione is None:
            raise ValueError(
                f"Nazione ID {id_nazione} non trovata per la regione {nome}"
            )

        return cls(nome, nazione)

    def to_db(self) -> dict:
        return {"nome": self.get_nome(), "nazione": self.get_nazione().get_nome()}

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for regione in cls.get_regioni().values():
            if regione.get_nome().lower() == nome.lower():
                return regione
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_regioni().get(k, None)

    def __str__(self) -> str:
        return f"Regione: {self.get_nome()}"


class Citta:
    __citta: dict[str, Self] = dict()
    __prossima = 0

    def __init__(self, nome: str, regione: Regione):
        self.set_nome(nome)
        self.set_regione(regione)
        type(self).get_citta()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_regione(self) -> Regione:
        return self._regione

    def set_regione(self, regione: Regione):
        _require_instance(regione, Regione, "regione")
        self._regione = regione

    @classmethod
    def get_prossima(cls) -> int:
        return cls.__prossima

    @classmethod
    def set_prossima(cls, prossima: int):
        cls.__prossima = prossima

    @classmethod
    def get_citta(cls) -> dict[str, Self]:
        return cls.__citta

    @classmethod
    def set_citta(cls, citta: dict[str, Self]):
        cls.__citta = citta

    @classmethod
    def create(cls, nome: str, regione: Regione) -> Self:
        return cls(nome, regione)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        id_regione = entity["regione"]
        regione = Regione.get(id_regione)
        if regione is None:
            raise ValueError(f"Regione ID {id_regione} non trovata per la città {nome}")

        return cls(nome, regione)

    def to_db(self) -> dict:
        return {"nome": self.get_nome(), "regione": self.get_regione().get_nome()}

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for c in cls.get_citta().values():
            if c.get_nome().lower() == nome.lower():
                return c
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_citta().get(k, None)

    def __str__(self) -> str:
        return f"Città: {self.get_nome()}"


# --- Classi primarie


# Ereditare da ABC trasforma in una classe astratta
class Persona(ABC):
    __persone: dict[str, Persona] = dict()

    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_citta_nascita(citta_nascita)
        self.set_codice_fiscale(codice_fiscale)

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_cognome(self) -> str:
        return self._cognome

    def set_cognome(self, cognome: str):
        assert isinstance(cognome, str), "'cognome' must be a string"
        self._cognome = cognome

    def get_codice_fiscale(self) -> str:
        return self._codice_fiscale

    def set_codice_fiscale(self, codice_fiscale: str):
        codice_clean = type(self).check_cf(codice_fiscale)
        persona_esistente = Persona.get_persone().get(codice_clean)
        assert persona_esistente is None or persona_esistente is self, (
            f"Fiscal code '{codice_clean}' already exists"
        )

        vecchio_codice = getattr(self, "_codice_fiscale", None)
        if (
            vecchio_codice is not None
            and Persona.get_persone().get(vecchio_codice) is self
        ):
            del Persona.get_persone()[vecchio_codice]

        self._codice_fiscale = codice_clean
        Persona.get_persone()[codice_clean] = self

    def get_citta_nascita(self) -> Citta:
        return self._citta_nascita

    def set_citta_nascita(self, citta_nascita: Citta):
        _require_instance(citta_nascita, Citta, "citta_nascita")
        self._citta_nascita = citta_nascita

    @classmethod
    def get_persone(cls) -> dict[str, Persona]:
        return cls.__persone

    @classmethod
    def set_persone(cls, persone: dict[str, Persona]):
        cls.__persone = persone

    def __str__(self) -> str:
        return (
            f"{self.get_nome()}. {self.get_cognome()}, {self.get_nome()} "
            f"- CF: {self.get_codice_fiscale()} - from:  {self.get_citta_nascita()}"
        )

    @classmethod
    def check_cf(cls, codice_fiscale: str) -> str:
        codice_clean = codice_fiscale.strip().upper()

        # INFO: sarebbero 16 caratteri, consentiamo anche 0 per fare test rapidi
        assert bool(re.match(r"^[A-Z0-9]{0,16}$", codice_clean)), (
            "Provided fiscal code format is not valid"
        )
        return codice_clean


class Docente(Persona):
    __docenti: dict[str, Self] = dict()
    __prossimo = 0

    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ):
        super().__init__(nome, cognome, codice_fiscale, citta_nascita)
        type(self).get_docenti()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    @classmethod
    def get_docenti(cls) -> dict[str, Self]:
        return cls.__docenti

    @classmethod
    def set_docenti(cls, docenti: dict[str, Self]):
        cls.__docenti = docenti

    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        citta_nascita: Citta,
    ) -> Self:
        return cls(nome, cognome, codice_fiscale, citta_nascita)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        cognome = entity["cognome"]
        codice_fiscale = Persona.check_cf(entity["codice_fiscale"])
        id_citta = entity["citta_nascita"]
        citta_nascita = Citta.get(id_citta)

        if citta_nascita is None:
            raise ValueError(
                f"City with ID {id_citta} cannot be found for teacher {cognome} {nome}"
            )

        return cls(nome, cognome, codice_fiscale, citta_nascita)

    def to_db(self) -> dict:
        return {
            "nome": self.get_nome(),
            "cognome": self.get_cognome(),
            "codice_fiscale": self.get_codice_fiscale(),
            "citta_nascita": self.get_citta_nascita().get_nome(),
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for docente in cls.get_docenti().values():
            if docente.get_nome().lower() == nome.lower():
                return docente
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_docenti().get(k, None)

    def __str__(self) -> str:
        return "[Docente] " + super().__str__()


class Modulo:
    __moduli: dict[str, Self] = dict()
    __prossimo = 0

    def __init__(
        self,
        codice: str,
        nome: str,
        ore: int,
        docenti: Optional[list[Docente]] = None,
    ):
        self.set_codice(codice)
        self.set_nome(nome)
        self.set_ore(ore)
        self.set_docenti(docenti)

        type(self).get_moduli()[self.get_codice()] = self

    def get_key(self) -> str:
        return self.get_codice()

    def get_codice(self) -> str:
        return self._codice

    def set_codice(self, codice: str):
        assert isinstance(codice, str), "'codice' must be a string"
        self._codice = codice

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_ore(self) -> int:
        return self._ore

    def set_ore(self, ore: int):
        assert isinstance(ore, int) and ore > 0, "Module hours cannot be 0 or negative"
        self._ore = ore

    def get_docenti(self) -> list[Docente]:
        return self._docenti

    def set_docenti(self, docenti: Optional[list[Docente]]):
        self._docenti = _require_list(docenti, Docente, "docenti")

    @classmethod
    def get_moduli(cls) -> dict[str, Self]:
        return cls.__moduli

    @classmethod
    def set_moduli(cls, moduli: dict[str, Self]):
        cls.__moduli = moduli

    @classmethod
    def create(
        cls, codice: str, nome: str, ore: int, docenti: Optional[list[Docente]] = None
    ) -> Self:
        return cls(codice, nome, ore, docenti)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        codice = entity["codice"]
        nome = entity["nome"]
        ore = entity["ore"]
        lista_id_docenti = entity.get("docenti", [])
        docenti_obj = []
        for id_doc in lista_id_docenti:
            doc_obj = Docente.get(id_doc)
            if doc_obj:
                docenti_obj.append(doc_obj)

        return cls(codice, nome, ore, docenti_obj)

    def to_db(self) -> dict:
        return {
            "codice": self.get_codice(),
            "nome": self.get_nome(),
            "ore": self.get_ore(),
            "docenti": [d.get_nome() for d in self.get_docenti()],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for modulo in cls.get_moduli().values():
            if modulo.get_nome().lower() == nome.lower():
                return modulo
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_moduli().get(k, None)

    def __str__(self) -> str:
        return f"Modulo: {self.get_nome()}"


class AreaDisciplinare:
    __aree_disciplinari: dict[str, Self] = dict()
    __prossima = 0

    def __init__(self, nome: str):
        self.set_nome(nome)
        type(self).get_aree_disciplinari()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    @classmethod
    def get_prossima(cls) -> int:
        return cls.__prossima

    @classmethod
    def set_prossima(cls, prossima: int):
        cls.__prossima = prossima

    @classmethod
    def get_aree_disciplinari(cls) -> dict[str, Self]:
        return cls.__aree_disciplinari

    @classmethod
    def set_aree_disciplinari(cls, aree_disciplinari: dict[str, Self]):
        cls.__aree_disciplinari = aree_disciplinari

    @classmethod
    def create(cls, nome: str) -> Self:
        cls.set_prossima(cls.get_prossima() + 1)
        return cls(nome)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        return cls(nome)

    def to_db(self) -> dict:
        return {"nome": self.get_nome()}

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for area_disciplinare in cls.get_aree_disciplinari().values():
            if area_disciplinare.get_nome().lower() == nome.lower():
                return area_disciplinare
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_aree_disciplinari().get(k, None)

    def __str__(self) -> str:
        return f"Area disciplinare: {self.get_nome()}"


class CorsoITS:
    __corsi: dict[str, Self] = dict()
    __prossimo = 0

    def __init__(
        self,
        nome: str,
        edizione: int,
        area_disciplinare: AreaDisciplinare,
        moduli: Optional[list[Modulo]] = None,
    ):
        self.set_nome(nome)
        self.set_edizione(edizione)
        self.set_area_disciplinare(area_disciplinare)
        self.set_moduli(moduli)
        type(self).get_corsi()[self.get_nome()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_edizione(self) -> int:
        return self._edizione

    def set_edizione(self, edizione: int):
        assert isinstance(edizione, int) and edizione > 0, (
            "Edition can only be a positive integer number"
        )
        self._edizione = edizione

    def get_area_disciplinare(self) -> AreaDisciplinare:
        return self._area_disciplinare

    def set_area_disciplinare(self, area_disciplinare: AreaDisciplinare):
        _require_instance(area_disciplinare, AreaDisciplinare, "area_disciplinare")
        self._area_disciplinare = area_disciplinare

    def get_moduli(self) -> list[Modulo]:
        return self._moduli

    def set_moduli(self, moduli: Optional[list[Modulo]]):
        self._moduli = _require_list(moduli, Modulo, "moduli")

    @classmethod
    def get_corsi(cls) -> dict[str, Self]:
        return cls.__corsi

    @classmethod
    def set_corsi(cls, corsi: dict[str, Self]):
        cls.__corsi = corsi

    @classmethod
    def create(
        cls,
        nome: str,
        edizione: int,
        area_disciplinare: AreaDisciplinare,
        moduli: Optional[list[Modulo]] = None,
    ) -> Self:
        return cls(nome, edizione, area_disciplinare, moduli)

    @classmethod
    def create_from_db(cls, entity: dict) -> Self:
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

        return cls(nome, edizione, area, moduli)

    def to_db(self) -> dict:
        return {
            "nome": self.get_nome(),
            "edizione": self.get_edizione(),
            "area_disciplinare": self.get_area_disciplinare().get_nome(),
            "moduli": [m.get_nome() for m in self.get_moduli()],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for corso in cls.get_corsi().values():
            if corso.get_nome().lower() == nome.lower():
                return corso
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_corsi().get(k, None)

    def __str__(self) -> str:
        return f"Corso ITS: {self.get_nome()}"


class Studente(Persona):
    __studenti: dict[str, Self] = dict()
    __prossimo = 0

    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        matricola: str,
        nascita: date,
        citta_nascita: Citta,
        corso: CorsoITS,
        moduli_superati: Optional[list[Modulo]] = None,
    ):
        self.set_matricola(matricola)
        self.set_nascita(nascita)
        self.set_corso(corso)
        self.set_moduli_superati(moduli_superati)
        super().__init__(nome, cognome, codice_fiscale, citta_nascita)
        type(self).get_studenti()[self.get_codice_fiscale()] = self

    def get_key(self) -> str:
        return self.get_nome()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        assert isinstance(nome, str), "'nome' must be a string"
        self._nome = nome

    def get_cognome(self) -> str:
        return self._cognome

    def set_cognome(self, cognome: str) -> None:
        assert isinstance(cognome, str), "'cognome' must be a string"
        self._cognome = cognome

    def get_matricola(self) -> str:
        return self._matricola

    def set_matricola(self, matricola: str):
        assert isinstance(matricola, str), "'matricola' must be a string"
        self._matricola = matricola

    def get_nascita(self) -> date:
        return self._nascita

    def set_nascita(self, nascita: date):
        _require_instance(nascita, date, "nascita")
        self._nascita = nascita

    def get_corso(self) -> CorsoITS:
        return self._corso

    def set_corso(self, corso: CorsoITS):
        _require_instance(corso, CorsoITS, "corso")
        self._corso = corso

    def get_moduli_superati(self) -> list[Modulo]:
        return self._moduli_superati

    def set_moduli_superati(self, moduli_superati: Optional[list[Modulo]]):
        self._moduli_superati = _require_list(
            moduli_superati, Modulo, "moduli_superati"
        )

    @classmethod
    def get_studenti(cls) -> dict[str, Self]:
        return cls.__studenti

    @classmethod
    def set_studenti(cls, studenti: dict[str, Self]):
        cls.__studenti = studenti

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
        return cls(
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
    def create_from_db(cls, entity: dict) -> Self:
        nome = entity["nome"]
        cognome = entity["cognome"]
        matricola = entity["matricola"]
        nascita = date.fromisoformat(entity["nascita"])
        codice_fiscale = Persona.check_cf(entity["codice_fiscale"])

        citta_obj = Citta.get(entity["citta_nascita"])
        if citta_obj is None:
            raise ValueError(f"Citta ID {entity['citta_nascita']} non trovata")

        corso_obj = CorsoITS.get(entity["corso"])
        if corso_obj is None:
            raise ValueError(f"CorsoITS ID {entity['corso']} non trovato")

        lista_mod_sup = entity.get("moduli_superati", [])
        moduli_obj: list[Modulo] = []
        for m in lista_mod_sup:
            mod_obj = Modulo.get(m)
            if mod_obj is not None:
                moduli_obj.append(mod_obj)

        result = cls(
            nome,
            cognome,
            codice_fiscale,
            matricola,
            nascita,
            citta_obj,
            corso_obj,
            moduli_obj,
        )
        return result

    def to_db(self) -> dict:
        return {
            "nome": self.get_nome(),
            "cognome": self.get_cognome(),
            "matricola": self.get_matricola(),
            "codice_fiscale": self.get_codice_fiscale(),
            "nascita": self.get_nascita().isoformat(),
            "citta_nascita": self.get_citta_nascita().get_nome(),
            "corso": self.get_corso().get_nome(),
            "moduli_superati": [m.get_nome() for m in self.get_moduli_superati()],
        }

    @classmethod
    def search(cls, nome: str) -> Optional[Self]:
        for studente in cls.get_studenti().values():
            if studente.get_nome().lower() == nome.lower():
                return studente
        return None

    @classmethod
    def get(cls, k: str) -> Optional[Self]:
        return cls.get_studenti().get(k, None)

    def __str__(self) -> str:
        moduli_superati = [m.get_nome() for m in self.get_moduli_superati()]
        return (
            "[Studente] "
            + super().__str__()
            + f" | Serial: {self.get_matricola()}"
            + f" | Course: {self.get_corso()}"
            + f" | Modules: {moduli_superati}\n"
        )

    def aggiungi_moduli_superati(self, codici_str: str):
        """Riceve una stringa di codici separati da virgola (es: 'py1, java1'),
        cerca i moduli corrispondenti e li aggiunge evitando i duplicati."""

        parti = codici_str.split(",")
        for parte in parti:
            codice_pulito = parte.strip()
            if not codice_pulito:
                continue

            modulo_trovato = None
            for m in Modulo.get_moduli().values():
                if m.get_codice().lower() == codice_pulito.lower():
                    modulo_trovato = m
                    break

            if modulo_trovato is None:
                print(
                    f"\n\r\t-> Warning: Module with code '{codice_pulito}' was not found in the system."
                )
                continue

            # Simula il comportamento del SET
            if modulo_trovato not in self.get_moduli_superati():
                self.get_moduli_superati().append(modulo_trovato)
                print(
                    f"\n\r\t-> Module '{modulo_trovato.get_nome()}' successfully added."
                )
            else:
                print(
                    f"\n\r\t-> Info: The module '{modulo_trovato.get_nome()}' is already present."
                )


# --- User Interface (UI) Functions ---


def ui_add_nazione():
    print("\n--- NEW NATION ---")
    nome = input("Nation name: ").strip()
    if Nazione.search(nome):
        print(f"Error: The nation '{nome}' already exists.")
        return

    nazione = Nazione.create(nome)
    print(f"\nSuccess! {nazione} created with ID {nazione.get_nome()}.")


def ui_add_regione():
    print("\n--- NEW REGION ---")
    if not Nazione.get_nazioni():
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
    print(f"\nSuccess! {regione} created with ID {regione.get_nome()}.")


def ui_add_citta():
    print("\n--- NEW CITY ---")
    if not Regione.get_regioni():
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
    print(f"\nSuccess! {citta} created with ID {citta.get_nome()}.")


def ui_add_area_disciplinare():
    print("\n--- NEW DISCIPLINARY AREA ---")
    nome = input("Disciplinary area name: ").strip()
    if AreaDisciplinare.search(nome):
        print(f"Error: The area '{nome}' already exists.")
        return

    area = AreaDisciplinare.create(nome)
    print(f"\nSuccess! {area} created with ID {area.get_nome()}.")


def ui_add_corso():
    print("\n--- NEW ITS COURSE ---")
    if not AreaDisciplinare.get_aree_disciplinari():
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
        print(
            f"\nSuccess! {corso} (Ed. {edizione}) created with ID {corso.get_nome()}."
        )
    except AssertionError as e:
        print(f"Validation error: {e}")


# FIXME: mostrare il corso appartenente
# TODO: far scegliere i docenti che insegnano
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
    if Docente.get_docenti():
        print("\nAvailable teachers:")
        for idx, doc in Docente.get_docenti().items():
            print(f"  [{idx}] {doc.get_nome()} {doc.get_cognome()}")

        ids_str = input(
            "Enter teacher IDs separated by comma (e.g., 1,2) or leave empty: "
        ).strip()
        if ids_str:
            for id_str in ids_str.split(","):
                try:
                    t_id = str(id_str.strip())
                    docente_obj = Docente.get(t_id)
                    if docente_obj:
                        docenti_selezionati.append(docente_obj)
                    else:
                        print(f"Warning: Teacher ID {t_id} not found. Skipping.")
                except ValueError:
                    print(f"Warning: Invalid ID '{id_str}'. Skipping.")

    try:
        modulo = Modulo.create(codice, nome, ore, docenti_selezionati)
        print(f"\nSuccess! {modulo} created with ID {modulo.get_nome()}.")
    except AssertionError as e:
        print(f"Validation error: {e}")


def ui_add_docente():
    print("\n--- NEW TEACHER ---")
    if not Citta.get_citta():
        print("Error: You must create at least one City for the birth place first.")
        return

    nome = input("First name: ").strip()
    cognome = input("Last name: ").strip()
    cf_str = input("Fiscal Code (Codice Fiscale): ").strip()

    try:
        cf = Persona.check_cf(cf_str)
    except AssertionError as e:
        print(f"Fiscal Code error: {e}")
        return

    nome_citta = input("City of birth: ").strip()
    citta = Citta.search(nome_citta)

    if not citta:
        print(f"Error: City '{nome_citta}' not found.")
        return

    docente = Docente.create(nome, cognome, cf, citta)
    print(f"\nSuccess! {docente} created with ID {docente.get_nome()}.")


def ui_add_studente():
    print("\n--- NEW STUDENT ---")
    if not Citta.get_citta():
        print("Error: You must create at least one City for the birth place first.")
        return
    if not CorsoITS.get_corsi():
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
    print(f"\nSuccess! {studente} created with ID {studente.get_nome()}.")

    # RICHIESTA DEI MODULI SUPERATI
    if Modulo.get_moduli():
        print("\nAvailable modules in the system:")
        for mod in Modulo.get_moduli().values():
            print(f"  [{mod.get_codice()}] {mod.get_nome()}")

        codici_input = input(
            "\nEnter the codes of passed modules separated by comma (e.g., py1,java1) or leave empty: "
        ).strip()
        if codici_input:
            studente.aggiungi_moduli_superati(codici_input)
    else:
        print("\nNote: No modules available in the system yet to assign as passed.")


def ui_show_all():
    print("\n--- CURRENT DATA SUMMARY ---")

    registri = [
        ("Nations", Nazione.get_nazioni()),
        ("Regions", Regione.get_regioni()),
        ("Cities", Citta.get_citta()),
        ("Disciplinary Areas", AreaDisciplinare.get_aree_disciplinari()),
        ("ITS Courses", CorsoITS.get_corsi()),
        ("Modules", Modulo.get_moduli()),
        ("Teachers", Docente.get_docenti()),
        ("Students", Studente.get_studenti()),
    ]

    for titolo, registro in registri:
        print(f"\n{titolo}: {len(registro)}")
        if not registro:
            print("\t- No records")
            continue

        for idx, entity in registro.items():
            print(f"\t[{idx}] {entity}")


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

    # all_data_to_save will hold all data for the JSON file
    all_data_to_save: dict = {}

    # Iterate through the externally passed structure
    for key, _, registry in load_sequence:
        print(f"\n\t-> Serializing {key}...")

        # Create a dictionary for the current class's instances
        class_data = {}
        for _, instance_obj in registry.items():
            class_data[instance_obj.get_key()] = instance_obj.to_db()

        all_data_to_save[key] = (
            class_data  # Add the serialized class data to the main dictionary
        )

    try:
        with open(datafile, "wt", encoding="utf-8") as fp:
            json.dump(all_data_to_save, fp, indent=2)
        print("\nSuccess! Data saved successfully.\nGoodbye!\n")
    except Exception as e:
        print(f"Error during save execution: {type(e).__name__}: {e}")


def main():

    # HACK: principio DRY - Do not Repeat Yourself
    # questa lista contiene delle tuple di tre elementi che consentono
    # ai metodi I/O di essere totalmente generici. I tre valori sono:

    # 1. Nome della chiave all'interno del file JSON
    # 2. La classe, in modo che nel ciclo si attivi il factory method di quella classe
    # 3. Dizionario di memoria utilizzato in scrittura da save_all() ES. ogni volta che creiamo una nazione, il costruttore salva dentro il dizionario Nazione.get_nazioni(). Viene usato lo stesso
    # dizionario per sapere dove iterare e creare oggetti JSON di quella classe.

    load_sequence = [
        # (Chiave JSON, Classe, Dizionario delle istanze in memoria)
        ("Nations", Nazione, Nazione.get_nazioni()),
        ("Regions", Regione, Regione.get_regioni()),
        ("Cities", Citta, Citta.get_citta()),
        (
            "DisciplinaryAreas",
            AreaDisciplinare,
            AreaDisciplinare.get_aree_disciplinari(),
        ),
        ("Teachers", Docente, Docente.get_docenti()),
        ("Modules", Modulo, Modulo.get_moduli()),
        ("ITSCourses", CorsoITS, CorsoITS.get_corsi()),
        ("Students", Studente, Studente.get_studenti()),
    ]
    try:
        datafile = Path.cwd() / "data.json"

        load_all(datafile, load_sequence)
        ui_ask_what_to_do()
        save_all(datafile, load_sequence)
        print(goodbye())
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
