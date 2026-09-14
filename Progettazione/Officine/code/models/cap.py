from __future__ import annotations

import re
from typing import Self

from models.cap import CAP
from models.citta import Citta

from Progettazione.Officine.code.exceptions.link import (
    InvalidLinkException,
    InvalidLinkOwnerException,
)
from Progettazione.Officine.code.types.validators import DataValidator
from Progettazione.Officine.prof.main import Citta

from .associations import citta_cap


class CAP(str):
    # __objects_by_citta: dict[Citta, Self] = dict()
    __set_of_caps: set[Self] = set()

    # INFO: CLASSMETHODS

    @classmethod
    # def get_cap_by_citta(cls):
    #     return cls.__objects_by_citta

    @classmethod
    def all_caps(cls):
        return cls.__set_of_caps

    # INFO: GETTERS

    def get_value(self) -> str:
        return self.__value

    def get_links_cap(self):
      return frozenset(x for x in self.__links_cap if x.is_valid())

    # INFO: ASSOCIATIONS

    # 0..*
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

    # 0..*
    def _add_cap_off(): ...

    def _remove_cap_off(): ...

    # INFO: CONSTRUCTORS

    def __new__(cls, value: str) -> Self:
        DataValidator.validate_cap(value)
        if value in cls.__set_of_caps:
            raise KeyError(f"CAP '{value}' già registrato")
        return super().__new__(cls, value)

    def __init__(self, value: str):
        self.__value = value
        type(self).__set_of_caps.add(self)

    # INFO: UTILITIES

    def __str__(self):
        return self

    def __repr__(self) -> str:
        return f"CAP(codice='{self.get_value()}')"
