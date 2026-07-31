from __future__ import annotations

from typing import Optional, Self


class Modello:
    __objects_by_nome: dict[str, Self] = dict()
    __set_of_models: set[Self] = set()

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
    def all_models_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_nome.get(nome)

    @classmethod
    def create(cls, nome: str):
        return cls(nome)

    @classmethod
    def create_from_dict(cls, data: dict):
        nome = data["nome"]
        return cls(nome)

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    # INFO: SETTERS

    def __set_nome(self, nome: str):
        Modello.__validate_nome(nome)
        self.__nome = nome

    # INFO: ASSOCIATIONS

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str):
        Modello.__validate_nome(nome)
        return super().__new__(cls)

    def __init__(self, nome: str):
        self.__set_nome(nome)

        type(self).all_objects_by_nome()[self.__nome] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.__nome}"

    def to_json(self) -> tuple[str, dict]:
        return (
            self.get_nome(),
            {
                "nome": str(self.get_nome()),
            },
        )
