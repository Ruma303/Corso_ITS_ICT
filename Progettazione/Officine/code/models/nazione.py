from __future__ import annotations

from typing import Self

from .associations import naz_veic


class Nazione:
    __objects_by_nome: dict[str, Self] = dict()
    # __set_naz_veic: set[naz_veic]

    # INFO: VALIDATORS

    @staticmethod
    def __validate_nome(nome: str):
        if not nome or not isinstance(nome, str):
            raise TypeError("Il nome deve essere una stringa valida e non vuota")

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls) -> dict[str, Self]:
        return cls.__objects_by_nome
        
    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_nome.get(nome)

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_regex_targa(self) -> frozenset[str]:
        return frozenset(self.__regex_targa)

    # INFO: SETTERS

    def __set_nome(self, nome: str) -> None:
        Nazione.__validate_nome(nome)
        if nome in type(self).all_objects_by_nome():
            raise KeyError(f"La nazione '{nome}' già è presente nel sistema")

        # Se il nome inviato è identico a quello attuale, non occorre fare nulla
        if hasattr(self, "_Nazione__nome") and self.__nome == nome:
            return

        # Per consentire la mutabilità, va rimossa la chiave dal dizionario
        if hasattr(self, "_Nazione__nome"):
          del type(self).__objects_by_nome[self.__nome]

        # Per poi aggiungere la nuova chiave con il nuovo nome
        self.__nome = nome
        type(self).__objects_by_nome[self.__nome] = self


    # INFO: ASSOCIATIONS
    # TODO: il setter per aggiornare __regex_targa è l'associazione

    def add_regex_targa(self, regex: str):
        if not regex or not isinstance(regex, str):
            raise TypeError("La regex dev'essere una stringa")
        if regex in self.__regex_targa:
            print("Questa regex era già presente per questa nazione")
        self.__regex_targa.add(regex)

    def remove_regex_targa(self, regex: str):
        if len(self.__regex_targa) <= 1:
            raise KeyError(
                "Non è possibile rimuovere tutte le regex. Almeno una è obbligatoria"
            )
        self.__regex_targa.discard(regex)

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str):
        Nazione.__validate_nome(nome)
        return super().__new__(cls)

    def __init__(self, nome: str):
        self.__set_nome(nome)
        self.__regex_targa = set() # [1..*]
        # TODO: Richiedere almeno una regex per la targa della nazione valida e inserirla

        type(self).all_objects_by_nome()[self.__nome] = self


    # INFO: UTILITIES

    def __str__(self):
        return f"{self.__nome}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_nome()),
    #         {"nome": self.get_nome(), "regex": self.get_regex_targa()},
    #     )
