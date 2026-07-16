from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Self
from uuid import NAMESPACE_DNS, UUID, uuid4, uuid5

from datatypes import CodiceFiscale


class Nazione:
    __objects_by_name: dict[str, Self]

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_name.get(nome)

    @classmethod
    def create(cls, nome: str) -> Self:
        if nome is None or nome == "":
            raise ValueError("Nome nazione non può essere vuoto")
        if cls.get_object_by_nome(nome) is not None:
            raise ValueError(f"Nazione '{nome}' già esistente")
        return cls(nome)

    @classmethod
    def create_from_dict(cls, nome: str, data: dict) -> Self:
        # Se l'oggetto è già presente nel registro, lo restituisce
        istanza_esistente = cls.get_object_by_nome(nome)
        if istanza_esistente is not None:
            return istanza_esistente
        return cls(data.get("nome", nome))

    def __init__(self, name: str) -> None:
        self.__nome = name
        type(self).__objects_by_name[self.__nome] = self

    def get_nome(self) -> str:
        return self.__nome

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_nome()), {"nome": self.get_nome()})


class Regione:
    __objects_by_name: dict[str, Self]

    # INFO: Registro per garantire l'univocità della coppia (NomeRegione, OggettoNazione)
    __tuple_registry: dict[tuple[str, Nazione], Self] = {}

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_name.get(nome)

    __objects_by_uuid: dict[UUID, Self]
    
    @classmethod
    def all_objects_by_uuid(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object_by_uuid(cls, k: UUID) -> Optional[Self]:
        return cls.__objects_by_uuid.get(k)

    @classmethod
    def get_objects_by_name(cls, name: str) -> set[Self]:
        trovati = set()
        for (value, _), obj in cls.__tuple_registry.items():
            if name == value:
                trovati.add(obj)
        return trovati

    @classmethod
    def create(cls, nome: str, naz: Nazione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Regione.nome non può essere None")

        # Verifica che la nazione passata sia effettivamente censita nel sistema
        if Nazione.get_object_by_nome(naz.get_nome()) is None:
            raise ValueError(f"La nazione '{naz.get_nome()}' non è valida o non esiste")

        # Verifica della coppia (regione.nome, nazione)
        if (nome, naz) in cls.__tuple_registry:
            raise ValueError(
                f"La regione '{nome}' è già associata alla nazione '{naz.get_nome()}'"
            )

        reg_id = uuid4()
        return cls(nome, naz, reg_id)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        naz_nome = data["nazione"]
        naz = Nazione.get_object_by_nome(naz_nome)
        if not naz:
            raise KeyError(
                f"Impossibile caricare la regione: la nazione '{naz_nome}' non esiste."
            )

        nome_regione = data["nome"]
        return cls(nome_regione, naz, _id)

    def __init__(self, nome: str, naz: Nazione, _id: UUID) -> None:
        self.__nome = nome
        self.__nazione = naz
        self.__id = _id

        type(self).__objects_by_uuid[self.__id] = self
        type(self).__objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__nazione)] = self

    def get_nazione(self) -> Nazione:
        return self.__nazione

    def get_nome(self) -> str:
        return self.__nome

    def get_uuid(self) -> UUID:
        return self.__id

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__nazione.get_nome()})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_uuid()),
            {"nome": self.get_nome(), "nazione": self.get_nazione().get_nome()},
        )


class Citta:
    __objects_by_name: dict[str, Self]

    # Registro per garantire l'univocità della coppia (NomeCittà, OggettoRegione)
    __tuple_registry: dict[tuple[str, Regione], Self] = {}

    __objects_by_uuid: dict[UUID, Self]

    @classmethod
    def all_objects_by_uuid(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object_by_uuid(cls, k: UUID) -> Optional[Self]:
        return cls.__objects_by_uuid.get(k)

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_name.get(nome)

    def __init__(self, nome: str, reg: Regione, _id: UUID) -> None:
        self.__nome = nome
        self.__regione = reg
        self.__id = _id

        type(self).__objects_by_uuid[self.__id] = self
        type(self).__objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__regione)] = self

    @classmethod
    def all_objects_by_registry(cls) -> dict[tuple[str, Regione], Self]:
        return cls.__tuple_registry

    @classmethod
    def find_citta_by_nome(cls, nome: str) -> set[Self]:
        citta_trovate = set()
        for (nome_citta, reg), obj in cls.all_objects_by_registry().items():
            if nome_citta.lower() == nome.lower():
                citta_trovate.add(obj)
        return citta_trovate

    @classmethod
    def create(cls, nome: str, reg: Regione) -> Self:
        if nome is None or nome == "":
            raise ValueError("Il nome della città non può essere vuoto")

        if Regione.get_object_by_uuid(reg.get_uuid()) is None:
            raise ValueError(
                f"La regione con uuid {reg.get_uuid()} non è una regione valida o registrata"
            )

        reg_nome = reg.get_nome()
        matching_regions = Regione.get_objects_by_name(reg_nome)
        matching_regions_list = list(matching_regions)

        if len(matching_regions) > 1:
            print(f"\nEsistono più nazioni che possiedono la regione '{reg_nome}':")
            for i, r in enumerate(matching_regions_list):
                print(f"\t{i + 1}) {r.get_nazione().get_nome()}")

            while True:
                try:
                    scelta = int(
                        input(
                            "Seleziona la nazione corretta digitando il numero associato: "
                        )
                    )
                    if 1 <= scelta <= len(matching_regions_list):
                        reg = matching_regions_list[scelta - 1]
                        break
                    else:
                        print(
                            f"Indice fuori scala. Inserisci un numero tra 1 e {len(matching_regions_list)}."
                        )
                except ValueError:
                    print("Input non valido. Inserisci un numero intero.")

        citta_id = uuid4()
        if cls.get_object_by_uuid(citta_id) is not None:
            raise KeyError(f"La città con uuid '{citta_id}' esiste già nel registro.")

        # Verifica dell'univocità della coppia (Nome, Regione)
        if (nome, reg) in cls.__tuple_registry:
            raise ValueError(
                f"La città '{nome}' è già associata alla regione '{reg.get_nome()}' nella nazione ({reg.get_nazione().get_nome()})"
            )

        return cls(nome, reg, citta_id)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        reg_uuid = UUID(data["regione"])
        reg = Regione.get_object_by_uuid(reg_uuid)
        if not reg:
            raise KeyError(
                f"Impossibile caricare la città: la regione con uuid {reg_uuid} non esiste"
            )

        nome = data["nome"]
        # Se l'oggetto è già presente in memoria nel registro tuple, lo restituisce evitando duplicati
        if (nome, reg) in cls.__tuple_registry:
            return cls.__tuple_registry[(nome, reg)]

        return cls(nome, reg, _id)

    def get_nome(self) -> str:
        return self.__nome

    def get_regione(self) -> Regione:
        return self.__regione

    def get_id(self) -> UUID:
        return self.__id

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__regione})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {
                "nome": self.get_nome(),
                "regione": str(self.get_regione().get_uuid()),
            },
        )


class Persona(ABC):
    __objects_by_cf: dict[CodiceFiscale, Self]
    __objects_by_name: dict[str, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__objects_by_cf = {}

    @classmethod
    def all_objects_by_cf(cls):
        return cls.__objects_by_cf.values()

    @classmethod
    def get_object_by_cf(cls, cf: CodiceFiscale) -> Optional[Self]:
        return cls.__objects_by_cf.get(cf)

    # INFO: Prototipi da implementare nelle sottoclassi
    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> Self: ...
  
    @classmethod
    @abstractmethod
    def create_from_dict(cls, cf: CodiceFiscale, data: dict) -> Self: ...

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_name.get(nome)

  
    def __init__(
        self,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ):
        self.__nome = nome
        self.__cognome = cognome
        self.__cf = cf
        self.__citta_nascita = citta_nascita
  
        # Tutti gli oggetti delle sottoclassi verranno inserite qui automaticamente
        type(self).__objects_by_cf[self.__cf] = self
  
        # Avendo ereditato da ClassUtilsNomi, registriamo l'oggetto anche per nome completo
        type(self).__objects_by_name[f"{self.__nome} {self.__cognome}"] = self
  
    def get_nome(self) -> str:
        return self.__nome
  
    def get_cognome(self) -> str:
        return self.__cognome
  
    def get_codice_fiscale(self) -> CodiceFiscale:
        return self.__cf
  
    def get_citta_nascita(self) -> Citta:
        return self.__citta_nascita
  
    def __str__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()}"