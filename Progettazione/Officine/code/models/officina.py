from __future__ import annotations

from types.datatypes import CodiceFiscale, Indirizzo, Telefono
from types.validators import AssociationValidator, DataValidator
from typing import Self

from associations import dirige, lavora
from exceptions.link import InvalidLinkException
from exceptions.model import (
    IsNotDipendenteException,
    IsNotDirettoreException,
    IsNotValidPersonaException,
)
from cap import CAP
from persona import Persona


class Officina:
    __objects_by_nome: dict[str, Self] = dict()
    __objects_by_registry: dict[tuple[str, Indirizzo], Self] = dict()
    __objects_by_telefono: dict[Telefono, Self] = dict()
    __objects_by_direttore: dict[CodiceFiscale, Self] = dict()

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_nome.get(nome)

    @classmethod
    def all_objects_by_telefono(cls) -> dict[Telefono, Self]:
        return cls.__objects_by_telefono

    # @classmethod
    # def get_object_by_telefono(cls, numero_tel: str) -> Telefono | None:
    #     if numero_tel in cls.__objects_by_telefono:
    #         return cls.__objects_by_telefono.get(numero_tel)

    @classmethod
    def all_objects_by_direttore(cls) -> dict[CodiceFiscale, Self]:
        return cls.__objects_by_direttore

    """
    @classmethod
    def get_object_by_direttore(cls, direttore: Persona) -> Persona:
        return cls.__objects_by_direttore.get(direttore)
    """

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def get_telefono(self) -> Telefono:
        return self.__telefono

    def get_link_dirige(self) -> dirige:
        if self.__link_dirige is None or not self.__link_dirige.is_valid():
            raise InvalidLinkException("L'officina è priva di un link dirige valido.")
        return self.__link_dirige

    def get_direttore(self) -> Persona:
        """Delegazione al link associativo per ottenere l'istanza di Persona.

        Risolve l'accesso pulito per la UI senza duplicare lo stato interno.
        """
        return self.get_link_dirige().get_persona()

    def get_links_lavora(self) -> frozenset[lavora]:
        return frozenset(x for x in self.__links_lavora if x.is_valid())

    def get_lavoratori(self) -> frozenset[Persona]:
        return frozenset(l.get_persona() for l in self.__links_lavora if l.is_valid())

    # INFO: SETTERS

    def __set_nome(self, nome: str):
        DataValidator.validate_str(nome)
        self.__nome = nome

    def __set_telefono(self, telefono: Telefono) -> None:
        DataValidator.validate_telefono(telefono)
        self.__telefono = telefono

    def __set_indirizzo(self, indirizzo: Indirizzo) -> None:
        DataValidator.validate_indirizzo(indirizzo)
        self.__indirizzo = indirizzo

    # INFO: ASSOCIATIONS

    # IMPORTANT: Gestione asimmetrica, officina è l'unica deputata a creare il link
    # Un direttore dev'essere 1..1, quindi sostituire il vecchio link
    def change_direttore(self, persona: Persona):
        DataValidator.validate_instance(persona, Persona, "Persona")
        """Interfaccia pubblica per l'assegnazione o sostituzione del direttore."""
        if not persona.is_direttore():
            raise IsNotDirettoreException

        # Se il link già esiste, l'operazione termina
        if self.__link_dirige is not None and self.__link_dirige.is_valid():
            if self.__link_dirige.get_persona() == persona:
                print("WARNING: link già esistente con questo direttore")
                return
            # Rimuove atomicamente il vecchio link su entrambi i lati
            dirige._remove(self.__link_dirige)

        # Creazione del nuovo link mediante la classe associativa
        dirige._create(self, persona)

    def _add_dirige(self, link: dirige):
        AssociationValidator.validate_dirige(self, link)
        if not link.get_persona().is_direttore():
            raise IsNotDirettoreException
        # Assegnazione dell'unico riferimento per la molteplicità 1..1
        self.__link_dirige = link

    def _remove_dirige(self, link: dirige):
        if self.__link_dirige == link:
            self.__link_dirige = None  # Inoltre, qui è None

    def _add_lavora(self, link: lavora):
        """Metodo protetto invocato da dirige._create."""
        AssociationValidator.validate_lavora(self, link)
        if not link.get_persona().is_dipendente():
            raise IsNotDipendenteException
        for l in self.__links_lavora:
            if link == l and l.is_valid():
                raise InvalidLinkException(
                    "Esiste già un link di 'lavora' attivo tra la persona e l'officina specificata."
                )
        self.__links_lavora = self.__links_lavora | frozenset([link])

    def _remove_lavora(self, link: lavora):
        """Metodo protetto invocato da dirige._remove."""
        if link in self.__links_lavora:
            self.__links_lavora = frozenset(l for l in self.__links_lavora if l != link)

    def add_cap(self, cap: CAP): 
      DataValidator.validate_instance(cap, CAP, "cap")
      DataValidator.validate_cap(cap)
      if self.__link_cap_off is not None and self.__link_cap_off.is_valid():
        print("WARNING: link già esistente con questo cap")
        cap_off._remove(self, cap)
      
      cap_off._create(self, cap)


    def _add_cap_off(self, link: cap_off): ...
      
    def _remove_cap_off(self, link: cap_off): ...

    # INFO: CONSTRUCTORS

    def __new__(
        cls,
        nome: str,
        indirizzo: Indirizzo,
        telefono: Telefono,
        direttore: Persona,  # 1..1 Serve per creare il vincolo "dirige"
    ):
        DataValidator.validate_str(nome)
        DataValidator.validate_indirizzo(indirizzo)
        DataValidator.validate_telefono(telefono)
        DataValidator.validate_indirizzo(indirizzo)

        return super().__new__(cls)

    def __init__(
        self,
        nome: str,
        indirizzo: Indirizzo,
        telefono: Telefono,
        direttore: Persona,
    ):
        self.__set_nome(nome)  # <<imm>> {id}
        self.__set_indirizzo(indirizzo)  # <<imm>> {id}
        self.__set_telefono(telefono)

        # Associazioni

        self.change_direttore(direttore)  # 1..1 obbligatorio ma mutabile
        self.__links_lavora = set()  # 0..*

        type(self).__objects_by_nome[self.__nome] = self
        # Salvataggio con vincolo composto (nome, indirizzo)
        type(self).__objects_by_registry[(self.__nome, self.__indirizzo)] = self
        type(self).__objects_by_telefono[self.__telefono] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.get_nome()} ({self.get_indirizzo()}) | tel: [{self.get_telefono()}] - Direttore: {self.get_direttore()}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_nome()),
    #         {
    #             "nome": self.get_nome(),
    #             "indirizzo": {
    #                 "via": self.get_indirizzo().get_via(),
    #                 "civico": self.get_indirizzo().get_civico(),
    #             },
    #         },
    #     )

    # def numero_dipendenti(self) -> IntGEZ: ...
