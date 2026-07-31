from __future__ import annotations

from typing import Optional, Self

from associations import naz_veic

# class GenericObjValidate:

#         def __init__(self, obj: any):

#             match (obj):
#                 case type(obj) == str:
#                     # tutte le validazioni sulle str
#                 case type(obj) == Nazione:
#                     if not Nazione.get_object_by_nome(nazione):
#                         raise KeyError(f"La nazione {nazione} non esiste nel registro")


class Nazione:
    __objects_by_nome: dict[str, Self]
    __set_name_nazioni: set[str]
    __set_naz_veic: set[naz_veic]

    # INFO: VALIDATORS

    @staticmethod
    def __validate_nome(nome: str):
        if not nome or not isinstance(nome, str):
            raise TypeError("Il nome deve essere una stringa valida e non vuota")

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome

    @classmethod
    def set_objects_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_nome.get(nome)

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_regex_targa(self) -> frozenset[str]:
        return frozenset(self.__regex_naz)

    # INFO: SETTERS

    def __set_nome(self, nome: str) -> None:
        if nome is None or nome == "":
            raise ValueError("Nome nazione non può essere vuoto")
        if not isinstance(nome, str):
            raise TypeError("Il nome della nazione dev'essere una stringa")
        if nome in type(self).all_objects_by_nome():
            raise KeyError(f"La nazione '{nome}' già è presente nel sistema")

        # Per consentire la mutabilità, va rimossa la chiave dal dizionario
        del type(self).__objects_by_nome[self.__nome]

        type(self).__objects_by_nome[self.__nome] = self
        self.__nome = nome

    # INFO: ASSOCIATIONS

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

    def __init__(self):
        self.__regex_targa = set()

        type(self).all_objects_by_nome()[self.__nome] = self

    # INFO: UTILITIES

    def __str__(self):
        return f"{self.__nome}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_nome()),
            {"nome": self.get_nome(), "regex": self.get_regex_targa()},
        )
