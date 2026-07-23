from __future__ import annotations

from datetime import datetime
from typing import Optional, Self
from uuid import NAMESPACE_DNS, UUID, uuid4, uuid5

from datatypes import CAP, CodiceFiscale, Indirizzo, IntGEZ, Targa


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
    # Registro per garantire l'univocità della coppia (NomeCittà, OggettoRegione)
    __tuple_registry: dict[tuple[str, Regione], Self] = {}

    __objects_by_name: dict[str, Self]
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

    def __init__(self, nome: str, reg: Regione, _id: UUID) -> None:
        self.__nome = nome
        self.__regione = reg
        self.__id = _id

        type(self).__objects_by_uuid[self.__id] = self
        type(self).__objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__regione)] = self

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


class Officina:
    __objects_by_name: dict[str, Self] = {}
    __objects_by_registry: dict[tuple[str, Indirizzo], Self] = {}
    __objects_by_uuid: dict[UUID, Self] = {}

    @classmethod
    def all_objects_by_uuid(cls):
        return cls.__objects_by_uuid.values()

    @classmethod
    def get_object_by_uuid(cls, _id: UUID) -> Optional[Self]:
        return cls.__objects_by_uuid.get(_id)

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
        return cls.__objects_by_name.get(nome)

    @classmethod
    def create(cls, nome: str, indirizzo: Indirizzo) -> Self:
        if nome is None or nome == "":
            raise ValueError("Il nome dell'officina non può essere vuoto")
        if indirizzo is None:
            raise ValueError("L'indirizzo non può essere vuoto.")
        if indirizzo not in cls.all_objects_by_uuid():
            # TODO: possibilità di miglioramento, es richiedi di nuovo o mostra altri
            raise KeyError("L'indirizzo non è registrato. Riprova")

        _id = uuid5(NAMESPACE_DNS, f"{nome} - {indirizzo}")
        return cls(_id, nome, indirizzo)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        nome = data["nome"]
        data_indirizzo = data["indirizzo"]

        # Deserializzazione del tipo di dato composto
        cap_obj = CAP(data_indirizzo["cap"])
        indirizzo_obj = Indirizzo(
            via=data_indirizzo["via"], civico=data_indirizzo["civico"], cap=cap_obj
        )
        return cls(_id, nome, indirizzo_obj)

    def __init__(self, _id: UUID, nome: str, indirizzo: Indirizzo):
        self.__id = _id
        self.__nome = nome
        self.__indirizzo = indirizzo

        type(self).__objects_by_uuid[self.__id] = self
        type(self).__objects_by_name[self.__nome] = self
        type(self).__objects_by_registry[(self.__nome, self.__indirizzo)] = self

    def get_id(self) -> UUID:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__indirizzo})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {
                "nome": self.get_nome(),
                "indirizzo": {
                    "via": self.get_indirizzo().get_via(),
                    "civico": self.get_indirizzo().get_civico(),
                    "cap": str(self.get_indirizzo().get_cap()),
                },
            },
        )

    # def numero_dipendenti(self): ...


class Veicolo:
    __objects_by_targa: dict[Targa, Self] = {}

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

    def __init__(self, targa: Targa, immatricolazione: IntGEZ):
        if targa is None:
            raise ValueError("La targa non può essere vuota")

        if immatricolazione is None:
            raise ValueError("L'anno di immatricolazione non può essere vuoto")

        self.__targa = targa
        self.__immatricolazione = immatricolazione

        type(self).all_objects_by_targa()[self.__targa] = self

    def to_json(): ...


class Marca:
    __objects_by_nome: dict[str, Self] = {}
    __set_of_models: set[Self] = set()

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

    def __init__(self, nome: str):
        if nome is None:
            raise ValueError("Il nome della marca del veicolo non può essere vuoto")
        self.__nome = nome
        type(self).all_objects_by_nome()[self.__nome] = self

    def to_json(): ...


class TipoVeicolo:
    __objects_by_nome: dict[str, Self] = {}
    __set_of_models: set[Self] = set()

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

    def __init__(self, nome: str):
        if nome is None:
            raise ValueError("Il nome del tipo del veicolo non può essere vuoto")
        self.__nome = nome
        type(self).all_objects_by_nome()[self.__nome] = self

    def to_json(): ...


class Modello:
    __objects_by_nome: dict[str, Self] = {}
    __set_of_models: set[Self] = set()

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

    def __init__(self, nome: str):
        if nome is None:
            raise ValueError("Il nome del modello dell'auto non può essere vuoto")
        self.__nome = nome

        type(self).all_objects_by_nome()[self.__nome] = self

    def to_json(): ...


class Persona:
    __objects_by_cf: dict[CodiceFiscale, Self]
    __objects_by_name: dict[str, Self]

    @classmethod
    def all_objects_by_cf(cls):
        return cls.__objects_by_cf.values()

    @classmethod
    def get_object_by_cf(cls, cf: CodiceFiscale) -> Optional[Self]:
        return cls.__objects_by_cf.get(cf)

    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
        indirizzo: Indirizzo,
    ) -> Self:
        if nome is None and cognome is None:
            raise ValueError("Nome e cognome non possono essere vuoti")
        if cf not in cls.all_objects_by_cf():
            raise KeyError(f"Non esiste un codice fiscale '{cf}'")
        if citta_nascita not in Citta.all_objects_by_uuid():
            raise KeyError(f"Non esiste una città '{cf}'")
        if indirizzo not in Citta.all_objects_by_uuid():
            raise KeyError(f"Non esiste un indirizzo '{cf}'")

        return cls(nome, cognome, cf, citta_nascita, indirizzo)

    @classmethod
    def create_from_dict(cls, cf: CodiceFiscale, data: dict) -> Self:
        nome = data["nome"]
        cognome = data["cognome"]

        cf_obj = CodiceFiscale(cf)
        if cf_obj is None:
            raise KeyError(f"Il codice fiscale '{cf}' non esiste nel database")

        citta_obj = data["citta_nascita"]
        if not citta_obj:
            raise KeyError(f"La città con l'identificatore '{citta_obj}' non esiste")

        ind_obj = data["indirizzo"]
        if not ind_obj:
            raise KeyError(f"L'indirizzo con l'identificatore '{ind_obj}' non esiste")

        return cls(nome, cognome, cf_obj, citta_obj, ind_obj)

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
        indirizzo: Indirizzo,
    ):
        self.__nome = nome
        self.__cognome = cognome
        self.__cf = cf
        self.__citta_nascita = citta_nascita
        self.__indirizzo = indirizzo

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

    def get_indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def __str__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()} residente in {self.get_indirizzo()}"


class Riparazione:
    __objects_by_codice: dict[str, Self] = {}
    __riparazioni_terminate: set[Self] = set()

    @classmethod
    def all_objects_by_codice(cls):
        return cls.__objects_by_codice

    @classmethod
    def all_riparazioni_terminate(cls):
      return cls.__riparazioni_terminate

    
    @classmethod
    def create(cls, codice: str, accettazione: datetime,  is_terminata: bool, riconsegna: datetime):
      if codice is None:
        raise ValueError("Il codice non può essere vuoto")

      if is_terminata:
        if riconsegna < accettazione:
          raise ValueError("La data di riconsegna non può essere antecedente all'accettazione")

      return cls(codice, accettazione, is_terminata, riconsegna)
          

    @classmethod
    def create_from_dict(cls, codice: str, data: dict):
      if codice not in cls.all_objects_by_codice():
        raise KeyError(f"Il codice inserito '{codice}' non si trova nel database")
      codice_obj = data["codice"]
      accettazione_obj = datetime.fromisoformat(data["accettazione"])
      is_terminata_obj = data["is_terminata"]
      riconsegna_obj = None
      if is_terminata_obj:
        riconsegna_obj = datetime.fromisoformat(data["riconsegna"])
      return cls(codice_obj, accettazione_obj, is_terminata_obj, riconsegna_obj)

    
    def __init__(
        self,
        codice: str,
        accettazione: datetime,
        is_terminata: bool,
        riconsegna: datetime | None,
    ):
        if codice is None:
            raise ValueError("Il codice della Riparazione non può essere vuoto")
        if type(accettazione) is not datetime:
            raise TypeError("La data accettazione dev'essere di tipo datetime")

        self.__codice = codice
        self.__accettazione = accettazione

        if is_terminata:
            self.__riconsegna = riconsegna
            type(self).all_riparazioni_terminate().add(self)
        else:
            self.__riconsegna = None

        type(self).all_objects_by_codice()[self.__codice] = self


    def to_json(): ...
