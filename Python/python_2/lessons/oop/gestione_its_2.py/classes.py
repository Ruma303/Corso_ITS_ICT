from __future__ import annotations

from typing import Optional, Self
from uuid import UUID, uuid4

from class_utils import ClassUtilsNomi, ClassUtilsUUID

# Class di interesse per il programma

"""
livelli di visibilità (nei linguaggi "standard", come Java)
 - pubblico: visibile (R/W) da chiunque
 - privato: visibile (R/W) da tutti gli oggetti della classe
"""


class Nazione(ClassUtilsNomi, ClassUtilsUUID):
    def __init__(self, name: str, _id: UUID) -> None:
        self.__nome = name
        self.__uuid = _id

        type(self)._objects_by_uuid[self.__uuid] = self
        type(self)._objects_by_name[self.__nome] = self

    @classmethod
    def create(cls, nome: str) -> Self:
        if nome is None or nome == "":
            raise ValueError("Nome nazione non può essere vuoto")
        if nome in [n.get_nome() for n in cls.all_objects_by_nome()]:
            raise ValueError(f"Nazione '{nome}' già esistente")
        naz_id = uuid4()
        # INFO: Controllo superfluo, aggiunto per completezza
        if naz_id in cls.all_objects_by_uuid():
            raise KeyError("Nazione.__uuid già presente")
        obj = cls(nome, naz_id)
        return obj

    @classmethod
    def create_from_dict(cls, uuid_obj: UUID, data: dict) -> Self:
        obj = cls(data["nome"], uuid_obj)
        return obj

    def get_nome(self) -> str:
        return self.__nome

    def get_uuid(self) -> UUID:
        return self.__uuid

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_uuid()), {"nome": self.get_nome()})


"""
Il sistema deve garantire l'inserimento di più regioni con lo stesso nome (ma UUID sempre diverso), purché la nazione (il suo UUID) sia diverso. Esempio, possono esistere due Lazio, purché in nazioni diverse: (Lazio, Francia) e (Lazio, Italia) è corretto
"""


class Regione(ClassUtilsUUID, ClassUtilsNomi):
    __tuple_registry: dict[tuple[str, Nazione], Self] = {}

    def __init__(self, nom: str, naz: Nazione, uuid_obj: UUID) -> None:
        self.__nome = nom
        self.__nazione = naz
        self.__uuid = uuid_obj

        type(self)._objects_by_uuid[self.__uuid] = self
        type(self)._objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__nazione)] = self

    @classmethod
    def create(cls, nome: str, naz: Nazione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Regione.nome non può essere None")
        if naz.get_uuid() not in [n.get_uuid() for n in Nazione.all_objects_by_uuid()]:
            raise ValueError(f"La nazione con uuid {naz.get_uuid()} non è valida")
        reg_id = uuid4()
        if reg_id in cls.all_objects_by_uuid():
            raise KeyError("Regione.__uuid già presente")
        # Verifica della coppia (regione.nome, nazione.uuid) PRIMA di crearla
        if (nome, naz.get_uuid()) in cls.__tuple_registry:
          raise ValueError(f"La regione '{nome}' è già associata alla nazione '{naz.get_nome()}'")
        return cls(nome, naz, reg_id)

    @classmethod
    def create_from_dict(cls, _uuid: UUID, data: dict) -> Self:
        naz_uuid = UUID(data["nazione"])
        naz = Nazione.get_object_by_uuid(naz_uuid)
        if not naz:
            raise KeyError(f"La nazione con uuid '{naz_uuid}' non esiste")
        else:
            return cls(data["nome"], naz, _uuid)

    def get_nome(self) -> str:
        return self.__nome

    def get_nazione(self) -> Nazione:
        return self.__nazione

    def get_uuid(self) -> UUID:
        return self.__uuid

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_uuid()),
            {"nome": self.get_nome(), "nazione": str(self.get_nazione().get_uuid())},
        )


class Citta(ClassUtilsUUID):
    __tuple_registry: dict[tuple[str, Regione], Self] = {}

    # da considerarsi privato
    def __init__(self, nome: str, reg: Regione, uuid_obj: UUID) -> None:
        self.__nome = nome
        self.__regione = reg
        self.__uuid = uuid_obj

        type(self)._objects_by_uuid[self.__uuid] = self
        type(self).__tuple_registry[(self.__nome, self.__regione)] = self

    @classmethod
    def create(cls, nome: str, reg: Regione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Il nome della città non può essere vuoto")
        if reg.get_uuid() not in [n.get_uuid() for n in Regione.all_objects_by_uuid()]:
            raise ValueError(f"La regione con uuid {reg.get_uuid()} non è una regione valida")
        citta_id = uuid4()
        if citta_id in cls.all_objects_by_uuid():
          raise KeyError(f"La città con uuid '{citta_id}' già esiste")
        # Verificare che non esista già la coppia (città.nome, regione.uuid)
        if (nome, reg.get_uuid()) in cls.__tuple_registry:
          raise KeyError(f"Questa città é già associata con la regione con uuid '{reg.get_uuid()}'")
        return cls(nome, reg, citta_id)

    @classmethod
    def create_from_dict(cls, _uuid: UUID, data: dict) -> Self:
        reg_uuid = UUID(data['regione'])
        reg = Regione.get_object_by_uuid(reg_uuid)
        if not reg:
          raise KeyError(f"La regione con uuid {reg_uuid} non esiste")
        else:
          return cls(data['nome'], reg, _uuid)

    def get_nome(self) -> str:
        return self.__nome

    def get_regione(self) -> Regione:
        return self.__regione

    def get_id(self) -> UUID:
        return self.__uuid

    def __str__(self) -> str:
        return f"{self.__nome}, {self.__regione}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {"nome": self.get_nome(), "regione": str(self.get_regione().get_uuid())},
        )
