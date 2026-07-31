from __future__ import annotations

from typing import Self

from datatypes import IntGEZ, Targa


class Veicolo:
    __objects_by_targa: dict[Targa, Self] = dict()

    # INFO: VALIDATORS
    
    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_targa(cls):
        return cls.__objects_by_targa

    @classmethod
    def create(cls, targa: Targa, immatricolazione: IntGEZ):
        return cls(targa, immatricolazione)

    @classmethod
    def create_from_dict(cls, targa: Targa, data: dict):
        targa_obj = Targa(data["targa"])
        immatricolazione_obj = IntGEZ(data["immatricolazione"])
        return cls(targa_obj, immatricolazione_obj)


    # INFO: GETTERS

    def get_targa(self) -> Targa:
        return self.__targa

    def get_immatricolazione(self) -> IntGEZ:
        return self.__immatricolazione

    # INFO: SETTERS

    # INFO: ASSOCIATIONS

    # INFO: CONSTRUCTORS

    def __new__(cls): ...

    def __init__(self, targa: Targa, immatricolazione: IntGEZ):
        if not targa:
            raise ValueError("La targa non può essere vuota")

        if not immatricolazione:
            raise ValueError("L'anno di immatricolazione non può essere vuoto")

        self.__targa = targa
        self.__immatricolazione = immatricolazione

        type(self).all_objects_by_targa()[self.__targa] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"Targa: {self.__targa} - Immatricolazione {self.__immatricolazione}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_targa()),
            {
                "targa": str(self.get_targa()),
                "immatricolazione": self.get_immatricolazione(),
            },
        )
