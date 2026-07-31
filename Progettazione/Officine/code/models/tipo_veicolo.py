from __future__ import annotations

from typing import Optional, Self


class TipoVeicolo:
    __objects_by_nome: dict[str, Self] = {}
    __set_of_models: set[Self] = set()

    # INFO: VALIDATORS
    
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
    
    # INFO: ASSOCIATIONS
    
    # INFO: CONSTRUCTORS

    def __init__(self, nome: str):
        if not nome:
            raise ValueError("Il nome del tipo del veicolo non può essere vuoto")
        self.__nome = nome
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
