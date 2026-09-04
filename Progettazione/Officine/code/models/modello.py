from __future__ import annotations

from typing import Self

from Progettazione.Officine.code.types.validators import DataValidator


class Modello:
    __objects_by_nome: dict[str, Self] = dict()
    __set_of_models: set[Self] = set()

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome

    @classmethod
    def all_models_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
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
        DataValidator.__validate_nome(nome)
        self.__nome = nome

    # INFO: ASSOCIATIONS

    # def marca_mod

    # def tipo_mod

    # INFO: CONSTRUCTORS

    def __new__(cls, nome: str):
        DataValidator.__validate_nome(nome)
        return super().__new__(cls)

    def __init__(self, nome: str):
        self.__set_nome(nome)

        type(self).all_objects_by_nome()[self.__nome] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.__nome}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         self.get_nome(),
    #         {
    #             "nome": str(self.get_nome()),
    #         },
    #     )
