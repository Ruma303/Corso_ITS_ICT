from __future__ import annotations

from typing import Self

from Progettazione.Officine.code.types.datatypes import Targa
from Progettazione.Officine.code.types.validators import DataValidator


class Nazione:
    __objects_by_nome: dict[str, Self] = dict()
    __objects_by_targhe: dict[Targa, Self] = dict() 
    __set_regex_targhe: set[Targa] = set() 

    # INFO: VALIDATORS

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls) -> dict[str, Self]:
        return cls.__objects_by_nome

    @classmethod
    def all_targhe_in_nazioni(cls) -> dict[Targa, Self]:
        return cls.__objects_by_targhe

    @classmethod
    def set_targhe_nazione(cls) -> set[Targa]:
        return cls.__set_regex_targhe

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_nome.get(nome)

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_regex_targa(self) -> frozenset[str]:
        """Restituisce l'insieme delle targhe associate a questa specifica istanza"""
        return frozenset(self.__regex_targhe)

    # INFO: SETTERS

    def __set_regex_targa(self, regex: str):
        DataValidator.validate_str(regex)
        nuova_targa = Targa(regex)
        DataValidator.validate_targa(nuova_targa)
        if nuova_targa in type(self).all_targhe_in_nazioni():
            raise ValueError(f"Questa targa '{regex}' è già registrata in una nazione")
        # Aggiunta al set di questa nazione
        self.__regex_targhe.add(regex)

        # Aggiunta al set di tutte le regex per nazioni
        type(self).all_targhe_in_nazioni()[nuova_targa] = self
        # Aggiuunta al set statico di classe
        type(self).set_targhe_nazione().add(nuova_targa)

    def __remove_regex_targa(self, regex: str) -> None:
        if len(self.__regex_targhe) <= 1:
            raise KeyError(
                "Non è possibile rimuovere tutte le regex. Almeno una è obbligatoria"
            )
        if regex in self.__regex_targhe:
            self.__regex_targhe.remove(regex)
            targa_obj = Targa(regex)
            type(self).all_targhe_in_nazioni().pop(targa_obj, None)
            type(self).set_targhe_nazione().discard(targa_obj)

    # INFO: ASSOCIATIONS

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str, regex_targa: set[str] | str):
        DataValidator.validate_str(nome)

        # Converte tutto in un set[str] o utilizza set[str] se già viene passato
        targhe_da_validare = (
            {regex_targa} if isinstance(regex_targa, str) else regex_targa
        )

        if not targhe_da_validare:
            raise ValueError("È necessario fornire almeno una targa/regex.")
        for targa_str in targhe_da_validare:
            DataValidator.validate_str(targa_str)

        return super().__new__(cls)

    def __init__(self, nome: str, regex_targa: set[str] | str):
        self.__nome = nome
        type(self).__objects_by_nome[self.__nome] = self
        self.__regex_targhe: set[str] = set()

        targhe_set = {regex_targa} if isinstance(regex_targa, str) else regex_targa
        for targa in targhe_set:
            self.__set_regex_targa(targa)

    # INFO: UTILITIES

    def __str__(self):
        return f"{self.__nome}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_nome()),
    #         {"nome": self.get_nome(), "regex": self.get_regex_targa()},
    #     )
