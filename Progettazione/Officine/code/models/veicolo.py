from __future__ import annotations

from types.datatypes import IntGEZ, Targa
from typing import Self


class Veicolo:
    __objects_by_targa: dict[Targa, Self] = dict()

    # INFO: VALIDATORS

    @staticmethod
    def __validate_targa(targa: Targa):
      if not targa:
          raise ValueError("La targa non può essere vuota")
      if type(targa) is not Targa:
          raise TypeError("Il valore inserito non è di tipo 'Targa'")

    @staticmethod
    def __validate_immatricolazione(immatricolazione: IntGEZ):
      if not immatricolazione:
          raise ValueError("L'anno di immatricolazione non può essere vuoto")
      if type(immatricolazione) is not IntGEZ:
          raise TypeError("Il valore inserito non è di tipo 'IntGEZ'")
      

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

    def __set_targa(self, targa: Targa):
        Veicolo.__validate_targa(targa)
        self.__targa = targa

    def __set_immatricolazione(self, immatricolazione: IntGEZ):
         Veicolo.__validate_immatricolazione(immatricolazione)
         self.__immatricolazione = immatricolazione

    # INFO: ASSOCIATIONS

    # def mod_vei

    # INFO: CONSTRUCTORS

    def __new__(cls, targa: Targa, immatricolazione: IntGEZ): 
        Veicolo.__validate_targa(targa)
        Veicolo.__validate_immatricolazione(immatricolazione)
        return super().__new__(cls)

    def __init__(self, targa: Targa, immatricolazione: IntGEZ):

        self.__set_targa(targa)
        self.__set_immatricolazione(immatricolazione)

        type(self).all_objects_by_targa()[self.__targa] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"Targa: {self.get_targa()} - Immatricolazione: {self.get_immatricolazione()}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_targa()),
    #         {
    #             "targa": str(self.get_targa()),
    #             "immatricolazione": self.get_immatricolazione(),
    #         },
    #     )
