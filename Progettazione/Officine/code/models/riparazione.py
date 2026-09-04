from __future__ import annotations

from datetime import datetime
from typing import Self


class Riparazione:
    __objects_by_codice: dict[str, Self] = dict()
    __riparazioni_terminate: set[Self] = set()

    # INFO: VALIDATORS

    
    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_codice(cls):
        return cls.__objects_by_codice

    @classmethod
    def all_riparazioni_terminate(cls):
        return cls.__riparazioni_terminate

    @classmethod
    def create(
        cls,
        codice: str,
        accettazione: datetime,
        is_terminata: bool,
        riconsegna: datetime | None = None,
    ) -> Self:
        if not codice:
            raise ValueError("Il codice non può essere vuoto o nullo")

        # Applicazione rigorosa del vincolo di dipendenza dello stato
        if not is_terminata:
            riconsegna = None
        else:
            if riconsegna is None:
                raise ValueError(
                    "Una riparazione terminata richiede una data di riconsegna"
                )
            if riconsegna < accettazione:
                raise ValueError(
                    "La data di riconsegna non può essere antecedente all'accettazione"
                )

        return cls(codice, accettazione, is_terminata, riconsegna)

    @classmethod
    def create_from_dict(cls, data: dict) -> Self:
        codice_obj = data.get("codice")
        if not codice_obj:
            raise ValueError("I dati forniti non contengono un codice valido")

        # Controllo di univocità per evitare duplicati nel database in memoria
        if codice_obj in cls.all_objects_by_codice():
            raise ValueError(f"Il codice '{codice_obj}' è già presente nel sistema")

        accettazione_obj = datetime.fromisoformat(data["accettazione"])
        is_terminata_obj = data["is_terminata"]

        riconsegna_obj = None
        if is_terminata_obj and data.get("riconsegna"):
            riconsegna_obj = datetime.fromisoformat(data["riconsegna"])

        return cls(codice_obj, accettazione_obj, is_terminata_obj, riconsegna_obj)

    # INFO: GETTERS

    def get_codice(self) -> str:
        return self.__codice

    def get_accettazione(self) -> datetime:
        return self.__accettazione

    def get_is_terminata(self) -> bool:
        return self.__is_terminata

    def get_riconsegna(self) -> datetime | None:
        return self.__riconsegna if self.__is_terminata else None


    # INFO: SETTERS

    # INFO: ASSOCIATIONS

    # INFO: CONSTRUCTORS

    def __new__(
        cls,
        codice: str,
        accettazione: datetime,
        is_terminata: bool,
        riconsegna: datetime | None
    ):

      


    def __init__(
        self,
        codice: str,
        accettazione: datetime,
        is_terminata: bool,
        riconsegna: datetime | None,
    ):
        if not codice:
            raise ValueError("Il codice della Riparazione non può essere vuoto")
        if type(accettazione) is not datetime:
            raise TypeError("La data accettazione dev'essere di tipo datetime")

        self.__codice = codice
        self.__accettazione = accettazione
        self.__is_terminata = is_terminata

        if self.__is_terminata:
            self.__riconsegna = riconsegna
            type(self).all_riparazioni_terminate().add(self)
        else:
            self.__riconsegna = None

        type(self).all_objects_by_codice()[self.__codice] = self

    # INFO: UTILITIES

    # def to_json(self) -> tuple[str, dict]:
    #     riconsegna_val = self.get_riconsegna()
    #     return (
    #         self.get_codice(),
    #         {
    #             "codice": self.get_codice(),
    #             "accettazione": self.get_accettazione().isoformat(),
    #             "is_terminata": self.get_is_terminata(),
    #             "riconsegna": riconsegna_val.isoformat() if riconsegna_val else None,
    #         },
    #     )
