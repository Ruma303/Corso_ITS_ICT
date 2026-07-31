from __future__ import annotations

from typing import Optional, Self

from nazione import Nazione


class Citta:
    __tuple_registry: dict[tuple[str, Nazione], Self] = dict()
    __objects_by_nome: dict[str, Self] = dict()

    # INFO: VALIDATORS

    @staticmethod
    def __validate_nome(nome: str):
        if not nome or not isinstance(nome, str):
            raise TypeError("Il nome deve essere una stringa valida e non vuota")

    @staticmethod
    def __validate_nazione(nazione: Nazione):
        if not Nazione.get_object_by_nome(nazione.get_nome()):
            raise KeyError(f"La nazione {nazione} non esiste nel registro")

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_nome.get(nome)

    @classmethod
    def all_objects_by_registry(cls) -> dict[tuple[str, Nazione], Self]:
        return cls.__tuple_registry

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_nazione(self) -> Nazione:
        return self.__nazione

    # INFO: SETTERS

    def __set_nome(self, nome: str):
        Citta.__validate_nome(nome)
        self.__nome = nome

    def __set_nazione(self, nazione: Nazione):
        Citta.__validate_nazione(nazione)
        self.__nazione = nazione

    # INFO: ASSOCIATIONS

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str, nazione: Nazione):
        Citta.__validate_nome(nome)
        Citta.__validate_nazione(nazione)
        return super().__new__(cls)

    def __init__(self, nome: str, nazione: Nazione):
        self.__set_nome(nome)
        self.__set_nazione(nazione)

        type(self).__objects_by_nome[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__nazione)] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_nome()),
            {
                "nome": self.get_nome(),
                "nazione": str(self.get_nome()),
            },
        )
