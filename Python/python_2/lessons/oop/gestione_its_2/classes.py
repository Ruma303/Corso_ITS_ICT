from __future__ import annotations

from datetime import datetime
from typing import Self
from uuid import UUID, uuid4

from class_utils import ClassUtilsNomi, ClassUtilsUUID
from datatypes import CodiceFiscale

# Class di interesse per il programma

"""
livelli di visibilità (nei linguaggi "standard", come Java)
 - pubblico: visibile (R/W) da chiunque
 - privato: visibile (R/W) da tutti gli oggetti della classe
"""


class Nazione(ClassUtilsNomi, ClassUtilsUUID):
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
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        return cls(data["nome"], _id)

    def __init__(self, name: str, _id: UUID) -> None:
        self.__nome = name
        self.__id = _id

        type(self)._objects_by_uuid[self.__id] = self
        type(self)._objects_by_name[self.__nome] = self

    def get_nome(self) -> str:
        return self.__nome

    def get_uuid(self) -> UUID:
        return self.__id

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_uuid()), {"nome": self.get_nome()})


"""
Il sistema deve garantire l'inserimento di più regioni con lo stesso nome (ma UUID sempre diverso), purché la nazione (il suo UUID) sia diverso. Esempio, possono esistere due Lazio, purché in nazioni diverse: (Lazio, Francia) e (Lazio, Italia) è corretto
"""


class Regione(ClassUtilsUUID, ClassUtilsNomi):
    __tuple_registry: dict[tuple[str, Nazione], Self] = {}

    @classmethod
    def get_objects_by_name(cls, name: str) -> set[Self]:
        trovati = set()

        for (value, _), obj in cls.__tuple_registry.items():
            if name == value:
                trovati.add(obj)

        return trovati

        # return {r for (n, naz), r in cls.__tuple_registry.items() if n == name}

    @classmethod
    def create(cls, nome: str, naz: Nazione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Regione.nome non può essere None")
        if naz.get_uuid() not in [n.get_uuid() for n in Nazione.all_objects_by_uuid()]:
            raise ValueError(f"La nazione con uuid {naz.get_uuid()} non è valida")
        reg_id = uuid4()
        if reg_id in cls.all_objects_by_uuid():
            raise KeyError("Regione.__uuid già presente")
        # Verifica della coppia (regione.nome, nazione) non sia già creata
        if (nome, naz) in cls.__tuple_registry:
            raise ValueError(
                f"La regione '{nome}' è già associata alla nazione '{naz.get_nome()}'"
            )
        return cls(nome, naz, reg_id)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        naz_uuid = UUID(data["nazione"])
        naz = Nazione.get_object_by_uuid(naz_uuid)
        if not naz:
            raise KeyError(f"La nazione con uuid '{naz_uuid}' non esiste")
        else:
            return cls(data["nome"], naz, _id)

    def __init__(self, nom: str, naz: Nazione, _id: UUID) -> None:
        self.__nome = nom
        self.__nazione = naz
        self.__id = _id

        type(self)._objects_by_uuid[self.__id] = self
        type(self)._objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__nazione)] = self

    def get_nazione(self) -> Nazione:
        return self.__nazione

    def get_nome(self) -> str:
        return self.__nome

    def get_uuid(self) -> UUID:
        return self.__id

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_uuid()),
            {"nome": self.get_nome(), "nazione": str(self.get_nazione().get_uuid())},
        )


class Citta(ClassUtilsUUID):
    __tuple_registry: dict[tuple[str, Regione], Self] = {}
    __objects_by_names: dict[str, Self] = {}

    # da considerarsi privato
    def __init__(self, nome: str, reg: Regione, _id: UUID) -> None:
        self.__nome = nome
        self.__regione = reg
        self.__id = _id

        type(self)._objects_by_uuid[self.__id] = self
        type(self).__tuple_registry[(self.__nome, self.__regione)] = self

    @classmethod
    def create(cls, nome: str, reg: Regione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Il nome della città non può essere vuoto")

        if reg.get_uuid() not in [n.get_uuid() for n in Regione.all_objects_by_uuid()]:
            raise ValueError(
                f"La regione con uuid {reg.get_uuid()} non è una regione valida"
            )

        # Cerchiamo tutte le regioni che hanno lo stesso nome di quello fornito
        reg_nome = reg.get_nome()
        matching_regions = Regione.get_objects_by_name(reg_nome)
        matching_regions_list = list(matching_regions)

        # Se esistono più regioni con lo stesso nome in nazioni diverse, chiediamo all'utente
        if len(matching_regions) > 1:
            print(f"Esistono più nazioni per la regione '{reg_nome}':")
            for i, r in enumerate(matching_regions):
                print(f"\t{i + 1}) {r.get_nazione().get_nome()}")

            while True:
                try:
                    scelta = int(
                        input("Seleziona la nazione digitando il numero associato: ")
                    )
                    if 1 <= scelta <= len(matching_regions):
                        reg = matching_regions_list[scelta - 1]
                        break
                    else:
                        print(
                            f"Indice fuori scala, inserisci un numero tra 1 e {len(matching_regions)}."
                        )
                except ValueError:
                    print("Input non valido. Inserisci un numero.")

        citta_id = uuid4()
        if citta_id in cls.all_objects_by_uuid():
            raise KeyError(f"La città con uuid '{citta_id}' già esiste")

        if not (citta_id, reg.get_uuid(), reg.get_nazione().get_uuid()):
            return cls(nome, reg, citta_id)
        else:
            raise ValueError(
                f"La città {nome} è già associata alla regione {reg.get_nome()} in ({reg.get_nazione().get_nome()})"
            )

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        reg_uuid = UUID(data["regione"])
        reg = Regione.get_object_by_uuid(reg_uuid)
        if not reg:
            raise KeyError(f"La regione con uuid {reg_uuid} non esiste")
        else:
            return cls(data["nome"], reg, _id)

    def get_nome(self) -> str:
        return self.__nome

    def get_regione(self) -> Regione:
        return self.__regione

    def get_id(self) -> UUID:
        return self.__id

    def __str__(self) -> str:
        return f"{self.__nome}, {self.__regione}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {
                "nome": self.get_nome(),
                "regione": str(self.get_regione().get_uuid()),
            },
        )


class AreaDisciplinare(ClassUtilsUUID, ClassUtilsNomi):
  
    @classmethod
    def create(cls, nome: str) -> Self:
        if nome in [n.get_nome() for n in cls.all_objects_by_nome()]:
            raise ValueError("Esiste già un'area disciplinare con questo nome")
        area_id = uuid4()
        if area_id in [n for n in AreaDisciplinare.all_objects_by_uuid()]:
            raise ValueError(f"L'area disciplinare con uuid '{area_id}' già esiste")
        return cls(nome, area_id)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        return cls(data["nome"], _id)

    def __init__(self, nome: str, _id: UUID):
        self.__nome = nome
        self.__id = _id

        type(self)._objects_by_uuid[self.__id] = self
        type(self)._objects_by_name[self.__nome] = self

    def get_nome(self) -> str:
        return self.__nome

    def get_id(self) -> UUID:
        return self.__id

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_id()), {"nome": self.get_nome()})


class CorsoITS: ...


class Modulo: ...


class Persona(ClassUtilsUUID, ClassUtilsNomi):
    def __init__(
        self,
        _uuid: UUID,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ):
        self.__uuid = _uuid
        self.__nome = nome
        self.__cognome = cognome
        self.__cf = cf
        self.__citta_nascita = citta_nascita

        type(self)._objects_by_uuid[self.__uuid] = self

    @classmethod
    def create(
        cls,
        _uuid: UUID,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ): ...

    @classmethod
    def create_from_dict(
        cls,
        _uuid: UUID,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ): ...

    def get_nome(self): ...
    def get_conome(self): ...
    def get_codice_fiscale(self): ...
    def get_citta_nascita(self): ...
    def __str__(self) -> str: ...
    def to_json(self): ...


# class Docente(Persona): ...

"""
class Studente(Persona):
    __matricola: str
    __nascita: datetime
    esami: set[Self]

    def __init__(): ...

    def get_esame(self, modulo: Modulo) -> Voto: ...

    def add_esame(self, modulo: Modulo, voto: Voto): ...
 """
