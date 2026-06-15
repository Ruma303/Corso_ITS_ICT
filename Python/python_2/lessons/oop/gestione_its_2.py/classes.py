from __future__ import annotations

import uuid
from typing import Optional, Self

# Class di interesse per il programma

"""
livelli di visibilità (nei linguaggi "standard", come Java)
 - pubblico: visibile (R/W) da chiunque
 - privato: visibile (R/W) da tutti gli oggetti della clase
"""


class Nazione:
    __objects_by_uuid: dict[uuid.UUID, Nazione] = dict()

    # TODO: per ogni classe aggiunge anche __objects_by_name
    # Quando si aggiunge un nuovo oggetto, si aggiunge anche in __objects_by_name
    # Quando si crea un oggetto, verificare sia se il nome è già presente in __objects_by_name
    # e se è presente sia la UUID

    @classmethod
    def all_objects(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object(cls, k: uuid.UUID):
        return cls.__objects_by_uuid[k]

    @classmethod
    def get_by_nome(cls, nome: str) -> Self | None:
        for obj in cls.all_objects():
            if obj.get_nome() == nome:
                return obj
        return None

    def __init__(self, name: str, _id: uuid.UUID) -> None:
        if name is None or name == "":
            raise ValueError("Nazione.nome non può essere None")
        if _id in type(self).__objects_by_uuid:
            raise KeyError("Nazione.__uuid già esiste")

        self.__nome = name
        self.__uuid = _id

        type(self).__objects_by_uuid[self.__uuid] = self

    @classmethod
    def create(cls, nom: str) -> Self:
        if nom is None or nom == "":
            raise ValueError("Nazione.nome non può essere None")
        if nom in [n.get_nome() for n in cls.all_objects()]:
            raise ValueError("Nazione.nome già esistente")
        obj = cls(nom, uuid.uuid4())
        return obj

    @classmethod
    def create_from_dict(cls, uuid_obj: uuid.UUID, data: dict) -> Self:
        obj = cls(data["nome"], uuid_obj)
        return obj

    def get_nome(self) -> str:
        return self.__nome

    def get_uuid(self) -> uuid.UUID:
        return self.__uuid

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_uuid()), {"nome": self.get_nome()})


class Regione:
    __objects_by_uuid: dict[uuid.UUID, Regione] = dict()

    @classmethod
    def all_objects(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object(cls, k: uuid.UUID):
        return cls.__objects_by_uuid[k]

    @classmethod
    def get_by_nome(cls, nome: str) -> Optional[Self]:
        for obj in cls.all_objects():
            if obj.get_nome() == nome:
                return obj
        return None

    def __init__(self, nom: str, naz: Nazione, uuid_obj: uuid.UUID) -> None:
        if nom is None or nom == "":
            raise ValueError("Regione.nome non può essere None")

        self.__nome = nom
        self.__nazione = naz
        self.__uuid = uuid_obj

        type(self).__objects_by_uuid[self.__uuid] = self

    @classmethod
    def create_from_dict(cls, _id: uuid.UUID, data: dict) -> Self:
        naz = Nazione.get_object(uuid.UUID(data["nazione"]))
        obj = cls(data["nome"], naz, _id)
        return obj

    @classmethod
    def create(cls, nom: str, naz: Nazione) -> Self:
        if nom is None or nom == "":
            raise ValueError("Regione.nome non può essere None")
        if naz not in Nazione.all_objects():
            raise ValueError("Regione.nazione non è una Nazione valida")
        obj = cls(nom, naz, uuid.uuid4())
        return obj

    def get_nome(self) -> str:
        return self.__nome

    def get_nazione(self) -> Nazione:
        return self.__nazione

    def get_uuid(self) -> uuid.UUID:
        return self.__uuid

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_uuid()),
            {"nome": self.get_nome(), "nazione": str(self.get_nazione().get_uuid())},
        )


class Citta:
    __objects_by_uuid: dict[str, Citta] = dict()
    __next_id: int = 0

    @classmethod
    def all_objects(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object(cls, k: str):
        return cls.__objects_by_uuid[k]

    @classmethod
    def get_by_nome(cls, nome: str) -> Optional[Self]:
        for obj in cls.all_objects():
            if obj.get_nome() == nome:
                return obj
        return None

    # da considerarsi privato
    def __init__(self, nom: str, reg: Regione, _id: int) -> None:
        if nom is None or nom == "":
            raise ValueError("Citta.nome non può essere None")

        if reg is None:
            raise ValueError("Citta.regione non può essere None")

        if str(_id) in type(self).__objects_by_uuid:
            raise KeyError(f"Errore: Citta.id {_id} già esistente")

        self.__nome = nom
        self.__regione = reg
        self._id = _id

        type(self).__objects_by_uuid[str(self._id)] = self

    @classmethod
    def create(cls, nom: str, reg: Regione) -> Self:
        obj = None
        while obj is None:
            try:
                obj = cls(nom, reg, cls.__next_id)
            except KeyError:
                cls.__next_id += 1
        cls.__next_id += 1
        return obj

    @classmethod
    def create_from_dict(cls, _id: int, data: dict) -> Self:
        reg = Regione.get_object(uuid.UUID(data["regione"]))
        if _id >= cls.__next_id:
            cls.__next_id = _id + 1
        obj = cls(data["nome"], reg, _id)
        return obj

    def get_nome(self) -> str:
        return self.__nome

    def get_regione(self) -> Regione:
        return self.__regione

    def get_id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"{self.__nome}, {self.__regione}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {"nome": self.get_nome(), "regione": str(self.get_regione().get_uuid())},
        )
