from __future__ import annotations

from datetime import date
from types.datatypes import IntGEZ
from typing import Any

from exceptions.link import InvalidLinkException
from models.cap import CAP
from models.citta import Citta
from models.officina import Officina
from models.persona import Persona

from Progettazione.Officine.code.exceptions.model import IsNotValidPersonaException
from Progettazione.Officine.code.types.validators import DataValidator


class dirige:
    """Classe associativa per la gestione della relazione bidirezionale 'dirige'."""

    # INFO: CLASSMETHODS

    @classmethod
    def _create(cls, officina: Officina, persona: Persona):
        """Factory method protetto che crea ed iscrive il link su entrambe le entità."""
        link = cls(officina, persona)
        persona._add_dirige(link)
        officina._add_dirige(link)
        return link

    @classmethod
    def _remove(cls, link: dirige):
        """Scollega e invalida in maniera deterministica il link bidirezionale."""
        if link is None or not link.is_valid():
            return
        link.get_persona()._remove_dirige(link)
        link.get_officina()._remove_dirige(link)

        link._set_is_valid(False)
        link.__officina = None
        link.__persona = None

    # INFO: GETTERS

    def get_officina(self) -> Officina:
        if not self.__is_valid or self.__officina is None:
            raise InvalidLinkException(
                "Impossibile accedere all'officina: link non valido o distrutto."
            )
        return self.__officina

    def get_persona(self) -> Persona:
        if not self.__is_valid or self.__persona is None:
            raise InvalidLinkException(
                "Impossibile accedere alla persona: link non valido o distrutto."
            )
        return self.__persona

    def is_valid(self) -> bool:
        return self.__is_valid

    # INFO: SETTERS

    def __set_officina(self, officina: Officina):
        if not isinstance(officina, Officina):
            raise IsNotValidPersonaException
        if not self.is_valid():
            raise InvalidLinkException
        self.__officina = officina

    def __set_persona(self, persona: Persona):
        if not isinstance(persona, Persona):
            raise IsNotValidPersonaException
        if not self.is_valid():
            raise InvalidLinkException
        self.__persona = persona

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    # INFO: CONSTRUCTORS

    def __init__(self, officina: Officina, persona: Persona):
        self._set_is_valid(True)  # Qui viene impostato il link come valido
        self.__set_officina(officina)
        self.__set_persona(persona)

    # INFO: UTILITIES

    def __hash__(self):
        if not self.__is_valid:
            return hash(0)
        return hash((self.get_officina(), self.get_persona()))

    def __eq__(self, other: Any):
        # Evitiamo il confronto tra hash per efficenza
        if type(self) is not type(other):
            return False
        if not self.is_valid() or not other.is_valid():
            return False
        return (
            self.get_officina() == other.get_officina()
            and self.get_persona() == other.get_persona()
        )


class lavora:
    """Classe associativa per la gestione della relazione bidirezionale 'lavora'."""

    # INFO: CLASSMETHODS

    @classmethod
    def _create(cls, officina: Officina, persona: Persona, assunzione: date):
        """Factory method protetto che crea ed iscrive il link su entrambe le entità."""
        link = cls(officina, persona, assunzione)
        persona._add_lavora(link)
        officina._add_lavora(link)
        return link

    @classmethod
    def _remove(cls, link):
        """Scollega e invalida in maniera deterministica il link bidirezionale."""
        link.get_persona()._remove_lavora(link)
        link.get_officina()._remove_lavora(link)
        link.__is_valid = False

    # INFO: GETTERS

    def get_officina(self) -> Officina:
        if not self.__is_valid or self.__officina is None:
            raise InvalidLinkException(
                "Impossibile accedere all'officina: link non valido o distrutto."
            )
        return self.__officina

    def get_persona(self) -> Persona:
        if not self.__is_valid or self.__persona is None:
            raise InvalidLinkException(
                "Impossibile accedere alla persona: link non valido o distrutto."
            )
        return self.__persona

    def get_assunzione(self):
        if not self.is_valid() or self.__persona is None:
            raise InvalidLinkException
        return self.__assunzione

    def is_valid(self) -> bool:
        return self.__is_valid

    # INFO: SETTERS

    def __set_officina(self, officina: Officina):
        if not self.is_valid():
            raise InvalidLinkException
        if not isinstance(officina, Officina):
            raise IsNotValidPersonaException
        self.__officina = officina

    def __set_persona(self, persona: Persona):
        if not self.is_valid():
            raise InvalidLinkException
        if not isinstance(persona, Persona):
            raise IsNotValidPersonaException
        self.__persona = persona

    def __set_assunzione(self, assunzione: date):
        DataValidator.validate_date(assunzione)
        self.__assunzione = assunzione

    def _set_is_valid(self, value: bool):
        self.__is_valid = value

    # INFO: CONSTRUCTORS

    def __init__(self, officina: Officina, persona: Persona, assunzione: date):
        self._set_is_valid(True)
        self.__set_officina(officina)
        self.__set_persona(persona)
        self.__set_assunzione(assunzione)

    # INFO: UTILITIES

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

    # INFO: OPERATIONS
    # TODO: da fare dopo

    def anni_servizio(self) -> IntGEZ:
        if not self.is_valid():
            raise InvalidLinkException

        oggi = date.today()
        data_assunzione = self.get_assunzione()

        # Se get_assunzione() restituisce un datetime completo, convertilo in date:
        # if hasattr(data_assunzione, 'date'):
        #   data_assunzione = data_assunzione.date()

        # 3. Calcola la differenza in anni accademici/solari reali
        # Sottrae gli anni e controlla se il compleanno lavorativo non è ancora avvenuto quest'anno
        anni = (
            oggi.year
            - data_assunzione.year
            - ((oggi.month, oggi.day) < (data_assunzione.month, data_assunzione.day))
        )

        # Forza il ritorno a 0 se per qualche motivo il calcolo è negativo (per garantire >= 0)
        return IntGEZ(max(0, anni))


class citta_cap:
    """Classe associativa per la gestione della relazione bidirezionale 'citta_cap'."""

    # INFO: CLASSMETHODS

    @classmethod
    def _create(cls, citta: Citta, cap: CAP):
        """Factory method protetto che crea ed iscrive il link su entrambe le entità."""
        link = cls(citta, cap)
        citta._add_citta_cap(link)
        cap._add_citta_cap(link)

    @classmethod
    def _remove(cls, link: citta_cap):
        """Scollega e invalida in maniera deterministica il link bidirezionale."""
        link.get_citta()._remove_citta_cap(link)
        link.get_cap()._remove_citta_cap(link)
        link._set_is_valid(False)
        link.__citta = None
        link.__cap = None

    # INFO: SETTERS

    def __set_citta(self, citta: Citta):
        DataValidator.validate_citta(citta)
        self.__citta = citta

    def __set_cap(self, cap: CAP):
        DataValidator.validate_cap(cap)
        self.__cap = cap

    def _set_is_valid(self, value: bool):
        DataValidator.validate_bool(value)
        self.__is_valid = value

    # INFO: GETTERS

    def get_citta(self):
        return self.__citta

    def get_cap(self):
        return self.__cap

    def is_valid(self):
        return self.__is_valid

    # INFO: CONSTRUCTORS

    def __init__(self, citta: Citta, cap: CAP):
        self.__set_citta(citta)
        self.__set_cap(cap)
        self._set_is_valid(True)

    # INFO: COMPARISONS

    def __hash__(self):
        return hash((self.get_citta(), self.get_cap()))

    def __eq__(self: citta_cap, other: Any):
        if not self or not other:
            raise TypeError("Passare le istanze di tipo 'citta_cap' per creare il link")
        if type(self) is not type(other):
            return False

        return (
            self.get_citta() == other.get_citta() and self.get_cap() == other.get_cap()
        )


class citta_off: 

  @classmethod
  def _create(cls, officina: Officina, cap: CAP):
    link = cls(officina, cap)
    officina._add_cap_off(link)
    cap._add_cap_off(link)
    return link

  @classmethod
  def _remove(cls, link: citta_off):
    DataValidator.validate_link(link)

    link.get_officina()._remove_cap_off(link)
    link.get_cap()._remove_cap_off(link)
    
    link.__set_validate(False)
    link.get_officina() = None
    link.get_cap() = None

  def __init__(self, officina: Officina, cap: CAP):
    self.__set_is_valid(True)
    self.__set_officina(officina)
    self.__set_cap(cap)
    