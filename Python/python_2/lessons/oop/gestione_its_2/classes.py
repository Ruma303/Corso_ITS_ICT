from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Self
from uuid import UUID, uuid4
from weakref import KeyedRef

from class_utils import ClassUtilsCF, ClassUtilsNomi, ClassUtilsUUID
from datatypes import CodiceFiscale, IntGEZ, IntGZ, RealGEZ, Voto

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


class Citta(ClassUtilsUUID, ClassUtilsNomi):
    __tuple_registry: dict[tuple[str, Regione], Self] = {}

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


class Persona(ABC, ClassUtilsNomi, ClassUtilsCF):
    # Prototipi da implementare nelle sottoclassi
    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> Self: ...

    @classmethod
    @abstractmethod
    def create_from_dict(cls, cf: CodiceFiscale, data: dict) -> Self: ...

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
        # se viene richiamato questo inizializzatore
        type(self)._objects_by_cf[self.__cf] = self

    def get_nome(self) -> str:
        return self.__nome

    def get_cognome(self) -> str:
        return self.__cognome

    def get_codice_fiscale(self) -> CodiceFiscale:
        return self.__cf

    def get_citta_nascita(self) -> Citta:
        return self.__citta_nascita

    def __str__(self) -> str:
        return f"{self.get_nome()}, {self.get_cognome()}"


class Docente(Persona):
  
    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ) -> Self:
        if cf in cls.all_objects_by_cf():
            raise KeyError(f"Il codice fiscale '{cf}' già esiste. Dev'essere univoco")
        return cls(nome, cognome, cf, citta_nascita)

    @classmethod
    def create_from_dict(
        cls,
        cf: CodiceFiscale,
        data: dict,
    ) -> Self:
        citta_uuid = UUID(data["citta_nascita"])
        citta = Citta.get_object_by_uuid(citta_uuid)
        if not citta:
            raise KeyError(f"La città di nascita con UUID '{citta_uuid}' non esiste")
        return cls(data["nome"], data["cognome"], cf, citta)

    def __init__(
        self,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ):
        super().__init__(nome, cognome, cf, citta_nascita)

    def get_moduli(self) -> set[Modulo]: ...

    def add_modulo(self, modulo: Modulo): ...

    def __str__(self) -> str:
      return f"{self.get_nome()}, {self.get_cognome()} | CF: {self.get_codice_fiscale()} | nato a {self.get_citta_nascita()}"
      
    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_codice_fiscale()),
            {
                "nome": self.get_nome(),
                "cognome": self.get_cognome(),
                "codice_fiscale": str(self.get_codice_fiscale()),
                "citta_nascita": str(self.get_citta_nascita().get_id()),
            },
        )


class Studente(Persona):
    __esami_superati: set = set()
    __all_objects_by_matricole: dict[str, Self] = dict()

    @classmethod
    def create(
        cls,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
        matricola: str,
        data_nascita: datetime,
    ) -> Self:
        if cf in cls.all_objects_by_cf():
            raise KeyError(f"Il codice fiscale '{cf}' già esiste. Dev'essere univoco")
        if matricola in cls.__all_objects_by_matricole:
            raise KeyError(f"La matricola {matricola} esiste già e dev'essere univoca")
        return cls(nome, cognome, cf, citta_nascita, matricola, data_nascita)

    @classmethod
    def create_from_dict(
        cls,
        cf: CodiceFiscale,
        data: dict,
    ) -> Self:
        citta_uuid = UUID(data["citta_nascita"])
        citta = Citta.get_object_by_uuid(citta_uuid)
        if not citta:
            raise KeyError(f"La città di nascita con UUID '{citta_uuid}' non esiste")
        data_nascita_dt = datetime.fromisoformat(data['data_nascita'])
        return cls(data["nome"], data["cognome"], cf, citta, data['matricola'], data_nascita_dt)

    """ 
    @classmethod
    def search_for_matricola(cls, matricola: str) -> set[Self]:
      return {(_id, st) for st in cls.__all_objects_by_matricole if st.get_matricola() == matricola}
      """
    def __init__(
        self,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
        matricola: str,
        data_nascita: datetime,
    ):
        super().__init__(nome, cognome, cf, citta_nascita)
        self.__matricola = matricola
        self.__data_nascita = data_nascita
        self.__esami_superati = set()  # Inizializziamo un set vuoto di esami
        type(self).__all_objects_by_matricole[self.__matricola] = self

    # TODO: Implementare
    def get_moduli_voto_piu_alto(self) -> set[Modulo]:
      return set()

    def get_matricola(self) -> str:
        return self.__matricola

    def get_data_nascita(self) -> datetime:
      return self.__data_nascita
  
    def get_esame(self, modulo: Modulo) -> Voto: ...

    def add_esame(self, modulo: Modulo, voto: Voto): ...

    def get_corso(self) -> CorsoITS: ...

    def __str__(self) -> str:
      return f"[{self.get_matricola()}] | {self.get_nome()}, {self.get_cognome()} | CF: {self.get_codice_fiscale()} | nato a {self.get_citta_nascita()} il {self.get_data_nascita()}"
    
    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_codice_fiscale()),
            {
                "nome": self.get_nome(),
                "cognome": self.get_cognome(),
                "codice_fiscale": str(self.get_codice_fiscale()),
                "citta_nascita": str(self.get_citta_nascita().get_id()),
                "matricola": str(self.get_matricola()),
                "data_nascita": self.get_data_nascita().isoformat()
            },
        )


class CorsoITS(ClassUtilsNomi):
    __objects_by_keys: dict[tuple[str, IntGZ], Self]

    """ @classmethod
    def create(cls, nome, edizione) -> Self:
      for (nome, edizione) in { k: v for corso in cls.get_corsi()}:
        if nome == k and edizione == v:
          raise KeyError(f"Esiste già un corso con il nome '{nome}' e edizione '{edizione}'.")
      return cls(nome, edizione) """
      

    @classmethod 
    def get_corsi(cls) -> dict[tuple[str, IntGZ], Self]:
      return cls.__objects_by_keys

    def numero_medio_esami(): ...


  


    
    """
    def moduli_con_voto_piu_alto() -> set[Modulo]:
       algoritmo:
                   # i moduli per i quali lo studente 'this' ha preso voto_max
                   result = {}

                   # il voto di tutti gli esami per i moduli in 'result'
                   voto_max = None

                   per ogni link (self, m) in self.esame_superato:

                           se voto_max is None or
                                   (this, m).voto > voto_max:

                                           result = { m }

                           altrimenti se (this,m).voto == voto_max:

                                           result = result unione { m }

                   return result

    """


class Modulo(ClassUtilsNomi):
    __docenti_by_modulo: dict[str, Docente] = {}
    __all_objects_by_codice: dict[str, Self] = {}

    """ @classmethod
    def get_all_objects_by_codice(cls) -> set[Self]:
      return { cls.__all_objects_by_codice} 
    """

    @classmethod
    def create(cls, codice, nome, ore) -> Self:
      if codice in cls.__all_objects_by_codice:
        raise KeyError(f"Esiste già un modulo con questo codice '{codice}'")
      return cls(codice, nome, ore)

    @classmethod
    def create_from_dict(cls, codice, data) -> Self:
      if codice in cls.__all_objects_by_codice:
        raise KeyError(f"Esiste già un modulo con questo codice '{codice}'")
      return cls(codice, data['nome'], data['ore'])
      

    def __init__(self, 
      codice: str,
      nome: str,
      ore: IntGZ
    ): 
      self.__codice = codice
      self.__nome = nome
      self.__ore = ore

      type(self)._objects_by_name[self.__codice] = self

    def get_codice(self) -> str:
      return self.__codice

    def get_nome(self) -> str:
      return self.__nome

    def get_ore(self) -> IntGZ:
      return self.__ore

    def add_docenti(self, docenti: set[Docente]):
      for cf in docenti:
        self.__docenti_by_modulo[cf.get_codice_fiscale()] = cf
  
    """
    def numero_esami(self) -> IntGEZ:
      return len(self.__esami_superati)
    """

    
    def get_docenti(self) -> set[Docente]:
      docenti = set()
      for docente in self.get_docenti():
        docenti.add(docente)
      return docenti
    
      
    def __str__(self) -> str: 
      base_str = f"{self.get_nome()} | durata {str(self.get_ore())}"
      if not self.get_docenti():
        base_str += " | NESSUN DOCENTE ASSOCIATO\n"
      else: 
        base_str += " | con docenti:\n"
        for docente in self.get_docenti():
          base_str += f"\t- {docente}"

      return base_str