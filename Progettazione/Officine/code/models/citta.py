from __future__ import annotations

from typing import Self

from Progettazione.Officine.code.exceptions.link import (
    InvalidLinkException,
    InvalidLinkOwnerException,
)
from Progettazione.Officine.code.types.validators import DataValidator

from .associations import citta_cap
from .cap import CAP
from .nazione import Nazione


class Citta:
    __tuple_registry: dict[tuple[str, Nazione], Self] = dict()
    __objects_by_nome: dict[str, Self] = dict()

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_nome.get(nome)

    @classmethod
    def all_objects_by_registry(cls) -> dict[tuple[str, Nazione], Self]:
        return cls.__tuple_registry

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_nazione(self) -> Nazione:
        return self.__nazione

    def get_links_cap(self):
        return frozenset(x for x in self.__links_cap if x.is_valid())
        
    def get_caps(self):
        return frozenset(x.get_cap() for x in self.__links_cap if x.is_valid())

    # INFO: SETTERS

    def __set_nome(self, nome: str):
        DataValidator.validate_str(nome)
        self.__nome = nome

    def __set_nazione(self, nazione: Nazione):
        DataValidator.validate_nazione(nazione)
        self.__nazione = nazione

    # INFO: ASSOCIATIONS

    # IMPORTANT: Interfaccia pubblica
    def add_cap(self, cap: CAP):
        """Interfaccia pubblica: Crea un link citta_cap"""
        DataValidator.validate_instance(self, CAP, "CAP")

        for link in self.__links_cap:
            if link is not None and link.is_valid() and link.get_cap() == cap:
                raise InvalidLinkException(
                    "Esiste già un link di 'cap_citta' attivo tra la città attuale e il cap passato."
                )
        citta_cap._create(self, cap)

    def _add_citta_cap(self, link: citta_cap):
        """Crea un link citta_cap"""
        DataValidator.validate_link(link)
        DataValidator.validate_instance(link, citta_cap, "citta_cap")
        if link.get_citta() != self:
            raise InvalidLinkOwnerException
        self.__links_cap = self.__links_cap | frozenset([link])

    def _remove_citta_cap(self, link: citta_cap):
        """Rimuove un link citta_cap"""
        DataValidator.validate_link(link)
        DataValidator.validate_instance(link, citta_cap, "citta_cap")
        if link.get_citta() != self:
            raise InvalidLinkOwnerException
        if link in self.__links_cap:
            self.__links_cap = self.__links_cap | frozenset([link])

    # def _add_citta_off(self, link: citta_off): ...

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str, nazione: Nazione, cap: CAP):
        DataValidator.validate_str(nome)
        DataValidator.validate_nazione(nazione)
        DataValidator.validate_cap(cap)
        return super().__new__(cls)

    def __init__(self, nome: str, nazione: Nazione, cap: CAP):
        self.__set_nome(nome)
        self.__set_nazione(nazione)  # 1..1

        self.__links_cap: frozenset[citta_cap] = frozenset()
        self.add_cap(cap)  # 1..*

        type(self).__objects_by_nome[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__nazione)] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione})"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_nome()),
    #         {
    #             "nome": self.get_nome(),
    #             "nazione": str(self.get_nome()),
    #         },
    #     )
