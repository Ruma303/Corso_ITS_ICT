from __future__ import annotations

from datetime import date
from types.datatypes import IntGEZ
from typing import Any

from citta import Citta
from exceptions.link import InvalidLinkException
from nazione import Nazione
from officina import Officina
from persona import Persona
from veicolo import Veicolo

from Progettazione.Officine.code.exceptions.model import IsNotValidPersonaException
from Progettazione.Officine.code.types.validators import DataValidator


class lavora:
    @classmethod
    def _create(cls, officina: Officina, persona: Persona, assunzione: date):
        link = cls(officina, persona, assunzione)
        persona._add_lavora(link)
        officina._add_lavora(link)

    @classmethod
    def _remove(cls, link):
        link.get_persona()._remove_lavora(link)
        link.get_officina()._remove_lavora(link)
        link.__is_valid = False

    def get_officina(self):
        return self.__officina

    def get_persona(self):
        return self.__persona

    def get_assunzione(self):
        if not self.is_valid():
            raise InvalidLinkException
        return self.__assunzione

    def __set_officina(self, officina: Officina):
        if not officina:
            raise TypeError("Non è un tipo Officina")
        if not self.is_valid():
            raise InvalidLinkException
        self.__officina = officina

    def __set_persona(self, persona: Persona):
        if not self.is_valid():
            raise InvalidLinkException
        if not persona:
            raise IsNotValidPersonaException
        self.__persona = persona

    def __set_assunzione(self, assunzione: date):
        DataValidator.__validate_date(assunzione)
        self.__assunzione = assunzione

    def is_valid(self) -> bool:
        return self.__is_valid

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    def __init__(self, officina: Officina, persona: Persona, assunzione: date):
        self.__set_officina(officina)
        self.__set_persona(persona)
        self.__set_assunzione(assunzione)
        self._set_is_valid(True)

    # Bisogna impedire che esistono due istanze lavora con
    # lo stesso campo officina e persona, sarebbero due officine diverse
    # È necessario implementare __eq__ e __hash__

    def __hash__(self):
        return hash((self.get_officina(), self.get_persona()))

    def __eq__(self, other: Any):
        # Evitiamo il confronto tra hash per efficenza
        if type(self) is not type(other):
            return False
        return (
            self.get_officina() == other.get_officina()
            and self.get_persona() == other.get_persona()
        )

    def anni_servizio(self) -> IntGEZ:
        if not self.is_valid():
            raise InvalidLinkException

        # 1. Prendi la data di oggi (solo anno, mese, giorno)
        oggi = date.today()

        # 2. Ottieni la data di assunzione (assumendo sia un oggetto datetime.date)
        data_assunzione = self.get_assunzione()

        # Se get_assunzione() restituisce un datetime completo, convertilo in date:
        # if hasattr(data_assunzione, 'date'): data_assunzione = data_assunzione.date()

        # 3. Calcola la differenza in anni accademici/solari reali
        # Sottrae gli anni e controlla se il compleanno lavorativo non è ancora avvenuto quest'anno
        anni = (
            oggi.year
            - data_assunzione.year
            - ((oggi.month, oggi.day) < (data_assunzione.month, data_assunzione.day))
        )

        # Forza il ritorno a 0 se per qualche motivo il calcolo è negativo (per garantire >= 0)
        return IntGEZ(max(0, anni))


class dirige:
    @classmethod
    def _create(cls, officina: Officina, persona: Persona):
        link = cls(officina, persona)
        persona._add_dirige(link)
        officina._add_dirige(link)

    @classmethod
    def _remove(cls, link: dirige):
        link.get_persona()._remove_dirige(link)
        link.get_officina()._remove_dirige(link)
        link._set_is_valid(False)
        link.__officina = None
        link.__persona = None

    def get_officina(self):
        return self.__officina

    def get_persona(self):
        return self.__persona

    def __set_officina(self, officina: Officina):
        if not officina:
            raise TypeError("Non è un tipo Officina")
        if not self.is_valid():
            raise InvalidLinkException
        self.__officina = officina

    def __set_persona(self, persona: Persona):
        if not self.is_valid():
            raise InvalidLinkException
        if not persona:
            raise IsNotValidPersonaException
        self.__persona = persona

    def is_valid(self) -> bool:
        return self.__is_valid

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    def __init__(self, officina: Officina, persona: Persona):
        self.__set_officina(officina)
        self.__set_persona(persona)
        self._set_is_valid(True)  # Qui viene impostato il link come valido

    def __hash__(self):
        return hash((self.get_officina(), self.get_persona()))

    def __eq__(self, other: Any):
        # Evitiamo il confronto tra hash per efficenza
        if type(self) is not type(other):
            return False
        return (
            self.get_officina() == other.get_officina()
            and self.get_persona() == other.get_persona()
        )


class vive_a:
    @classmethod
    def _create(cls, persona: Persona, citta: Citta):
        link = cls(persona, citta)
        persona._add_vive_a(link)
        citta._add_vive_a(link)

    @classmethod
    def _remove(cls, link: vive_a):
        link.get_persona()._remove_vive_a(link)
        link.get_citta()._remove_vive_a(link)
        link._set_is_valid(False)
        link.__persona = None
        link.__citta = None

    def get_citta(self):
        return self.__citta

    def get_persona(self):
        return self.__persona

    def is_valid(self) -> bool:
        return self.__is_valid

    def __set_persona(self, persona: Persona):
        self.__persona = persona

    def __set_citta(self, citta: Citta):
        self.__citta = citta

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    def __init__(self, persona: Persona, citta: Citta):
        self.__set_persona(persona)
        self.__set_citta(citta)
        self._set_is_valid(True)

    def __hash__(self):
        return hash((self.get_persona(), self.get_citta()))

    def __eq__(self, other: Any):
        if type(self) is not type(other):
            return False
        return (
            self.get_citta() == other.get_citta()
            and self.get_persona() == other.get_persona()
        )


class naz_veic:
    @classmethod
    def _create(cls, nazione: Nazione, veicolo: Veicolo):
        link = cls(nazione, veicolo)
        nazione._add_naz_veic(link)
        veicolo._add_naz_veic(link)

    @classmethod
    def _remove(cls, link: naz_veic):
        link.get_nazione()._remove_naz_veic(link)
        link.get_veicolo()._remove_naz_veic(link)
        link._set_is_valid(False)
        link.__nazione = None
        link.__veicolo = None

    def get_nazione(self):
        return self.__nazione

    def get_veicolo(self):
        return self.__veicolo

    def get_is_valid(self) -> bool:
        return self.__is_valid

    def __set_nazione(self, nazione: Nazione):
        self.__nazione = nazione

    def __set_veicolo(self, veicolo: Veicolo):
        self.__veicolo = veicolo

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    def __init__(self, nazione: Nazione, veicolo: Veicolo):
        self.__set_nazione(nazione)
        self.__set_veicolo(veicolo)
        self._set_is_valid(True)

    def __hash__(self):
        return hash((self.get_veicolo(), self.get_nazione()))

    def __eq__(self, other: Any):
        if type(self) is not type(other):
            return False
        return (
            self.get_nazione() == other.get_nazione()
            and self.get_veicolo() == other.get_veicolo()
        )
