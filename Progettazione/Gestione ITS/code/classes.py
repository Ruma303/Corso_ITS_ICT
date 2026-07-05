from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Self
from uuid import UUID, uuid4

from class_utils import ClassUtilsCF, ClassUtilsNomi, ClassUtilsUUID
from datatypes import CodiceFiscale, IntGEZ, IntGZ, RealGEZ, Voto

# Class di interesse per il programma

"""
livelli di visibilità (nei linguaggi "standard", come Java)
 - pubblico: visibile (R/W) da chiunque
 - privato: visibile (R/W) da tutti gli oggetti della classe
"""

class Nazione(ClassUtilsNomi):
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
        type(self)._objects_by_name[self.__nome] = self

    def get_nome(self) -> str:
        return self.__nome

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (str(self.get_nome()), {"nome": self.get_nome()})


"""
Il sistema deve garantire l'inserimento di più regioni con lo stesso nome (ma UUID sempre diverso), purché la nazione (il suo UUID) sia diverso. Esempio, possono esistere due Lazio, purché in nazioni diverse: (Lazio, Francia) e (Lazio, Italia) è corretto
"""


class Regione(ClassUtilsUUID, ClassUtilsNomi):
    # Registro per garantire l'univocità della coppia (NomeRegione, OggettoNazione)
    __tuple_registry: dict[tuple[str, Nazione], Self] = {}

    @classmethod
    def get_objects_by_name(cls, name: str) -> set[Self]:
        """Restituisce tutte le regioni con quel nome"""
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
          raise KeyError(f"Impossibile caricare la regione: la nazione '{naz_nome}' non esiste.")

      nome_regione = data["nome"]
      return cls(nome_regione, naz, _id)

    def __init__(self, nome: str, naz: Nazione, _id: UUID) -> None:
        self.__nome = nome
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
        return f"{self.__nome} ({self.__nazione.get_nome()})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_uuid()),
            {"nome": self.get_nome(), "nazione": self.get_nazione().get_nome()},
        )


class Citta(ClassUtilsUUID, ClassUtilsNomi):
    # Registro per garantire l'univocità della coppia (NomeCittà, OggettoRegione)
    __tuple_registry: dict[tuple[str, Regione], Self] = {}

    def __init__(self, nome: str, reg: Regione, _id: UUID) -> None:
        self.__nome = nome
        self.__regione = reg
        self.__id = _id

        type(self)._objects_by_uuid[self.__id] = self
        type(self)._objects_by_name[self.__nome] = self
        type(self).__tuple_registry[(self.__nome, self.__regione)] = self

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
                        input("Seleziona la nazione corretta digitando il numero associato: ")
                    )
                    if 1 <= scelta <= len(matching_regions_list):
                        reg = matching_regions_list[scelta - 1]
                        break
                    else:
                        print(f"Indice fuori scala. Inserisci un numero tra 1 e {len(matching_regions_list)}.")
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
            raise KeyError(f"Impossibile caricare la città: la regione con uuid {reg_uuid} non esiste")

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


class AreaDisciplinare(ClassUtilsNomi):
    @classmethod
    def create(cls, nome: str) -> Self:
        if nome is None or nome == "":
            raise ValueError("Il nome dell'area disciplinare non può essere vuoto")
        
        if cls.get_object_by_nome(nome) is not None:
            raise ValueError(f"Esiste già un'area disciplinare con il nome '{nome}'")
            
        return cls(nome)

    @classmethod
    def create_from_dict(cls, nome: str, data: dict) -> Self:
        istanza_esistente = cls.get_object_by_nome(nome)
        if istanza_esistente is not None:
            return istanza_esistente
            
        return cls(data.get("nome", nome))

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        type(self)._objects_by_name[self.__nome] = self

    def get_nome(self) -> str:
        return self.__nome

    def __str__(self) -> str:
        return self.__nome

    def to_json(self) -> tuple[str, dict]:
        return (self.get_nome(), {"nome": self.get_nome()})


class Modulo(ClassUtilsNomi):
    __all_objects_by_codice: dict[str, Self] = {}

    @classmethod
    def get_object_by_codice(cls, codice: str) -> Optional[Self]:
        return cls.__all_objects_by_codice.get(codice)

    @classmethod
    def all_objects_by_codice(cls) -> list[Self]:
        return list(cls.__all_objects_by_codice.values())

    @classmethod
    def create(cls, codice: str, nome: str, ore: IntGZ) -> Self:
        if codice in cls.__all_objects_by_codice:
            raise KeyError(f"Esiste già un modulo con il codice '{codice}'")
        return cls(codice, nome, ore)

    @classmethod
    def create_from_dict(cls, codice: str, data: dict) -> Self:
        if codice in cls.__all_objects_by_codice:
            obj = cls.__all_objects_by_codice[codice]
        else:
            obj = cls(codice, data["nome"], IntGZ(data["ore"]))
        
        # Ripristiniamo l'associazione con i docenti partendo dai loro Codici Fiscali
        if "docenti" in data:
            for cf_str in data["docenti"]:
                docente_obj = Docente.get_object_by_cf(CodiceFiscale(cf_str))
                if docente_obj:
                    obj.add_docente(docente_obj)
                    
        return obj

    def __init__(self, codice: str, nome: str, ore: IntGZ):
        self.__codice = codice
        self.__nome = nome
        self.__ore = ore

        # Dizionario specifico di docenti per ogni modulo (Chiave: CF, Valore: Docente)
        self.__docenti_by_modulo: dict[CodiceFiscale, Docente] = {}

        # Registrazione nei dizionari di classe
        type(self)._objects_by_name[self.__nome] = self 
        type(self).__all_objects_by_codice[self.__codice] = self

    def get_codice(self) -> str:
        return self.__codice

    def get_nome(self) -> str:
        return self.__nome

    def get_ore(self) -> IntGZ:
        return self.__ore

    """=== Gestione docenti ==="""
    def add_docenti(self, docenti: set[Docente]) -> None:
        for docente in docenti:
            self.__docenti_by_modulo[docente.get_codice_fiscale()] = docente
            
    def add_docente(self, docente: Docente) -> None:
        self.__docenti_by_modulo[docente.get_codice_fiscale()] = docente

    def get_docenti(self) -> set[Docente]:
        return set(self.__docenti_by_modulo.values())

    def __str__(self) -> str:
        base_str = f"[{self.__codice}] {self.get_nome()} | durata {self.get_ore()} ore"
        docenti = self.get_docenti()
        
        if not docenti:
            base_str += " | NESSUN DOCENTE ASSOCIATO"
        else:
            base_str += " | con docenti:\n"
            for docente in docenti:
                base_str += f"\t- {docente.get_nome()} {docente.get_cognome()} ({docente.get_codice_fiscale()})"
        return base_str

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_codice()),
            {
                "codice": self.get_codice(),
                "nome": self.get_nome(),
                "ore": self.get_ore(),
                "docenti": [str(cf) for cf in self.__docenti_by_modulo.keys()]
            },
        )


class CorsoITS(ClassUtilsUUID, ClassUtilsNomi):
    __objects_by_keys: dict[tuple[str, IntGEZ], Self] = {}

    @classmethod
    def get_corsi(cls) -> dict[tuple[str, IntGEZ], Self]:
        """Restituisce il dizionario di tutti i corsi indicizzati per (nome, edizione)."""
        return cls.__objects_by_keys

    @classmethod
    def create(cls, nome: str, edizione: IntGEZ) -> Self:
        # Controllo di integrità sulla coppia univoca
        chiave = (nome, edizione)
        if chiave in cls.__objects_by_keys:
            raise KeyError(
                f"Esiste già un corso con il nome '{nome}' e edizione '{edizione}'."
            )
        nuovo_id = uuid4()
        return cls(nome, edizione, nuovo_id)

    @classmethod
    def create_from_dict(cls, _id: UUID, data: dict) -> Self:
        nome = data["nome"]
        edizione = IntGEZ(data["edizione"])

        chiave = (nome, edizione)
        if chiave in cls.__objects_by_keys:
            return cls.__objects_by_keys[chiave]

        # Ricostruiamo il set di moduli associati partendo dai codici salvati nel JSON
        moduli_associati = set()
        if "moduli" in data:
            for codice_modulo in data["moduli"]:
                modulo_obj = Modulo.get_object_by_codice(codice_modulo)
                if modulo_obj:
                    moduli_associati.add(modulo_obj)

        return cls(nome, edizione, _id, moduli_associati)

    def __init__(
        self,
        name: str,
        edition: IntGEZ,
        _id: UUID,
        modules: Optional[set[Modulo]] = None,
    ):
        self.__name = name
        self.__edition = edition
        self.__id = _id
        # Se non vengono passati moduli, inizializziamo un set vuoto
        self.__modules = modules if modules is not None else set()

        # Popolamento dei registri di classe e delle superclassi utili
        type(self)._objects_by_uuid[self.__id] = self
        type(self)._objects_by_name[self.__name] = self
        type(self).__objects_by_keys[(self.__name, self.__edition)] = self

    def get_id(self) -> UUID:
        return self.__id

    def get_nome(self) -> str:
        return self.__name

    def get_edizione(self) -> IntGEZ:
        return self.__edition

    def get_moduli(self) -> set[Modulo]:
        return self.__modules

    def get_num_moduli(self) -> int:
        return len(self.__modules)

    def add_modulo(self, modulo: Modulo) -> None:
        self.__modules.add(modulo)

    def __str__(self) -> str:
        return f"Corso: {self.get_nome()} [Edizione: {self.get_edizione()}] - Moduli totali: {self.get_num_moduli()}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_id()),
            {
                "nome": self.get_nome(),
                "edizione": self.get_edizione(),
                "moduli": [m.get_codice() for m in self.get_moduli()],
            },
        )


    # TODO: completa funzione
    """ 
    def numero_medio_esami_per_modulo(self):
        # da implementare get_voto()
        voti = [mod.get_voto() for mod in self.get_moduli()]
        somma_voti = sum(voti)
        return somma_voti / self.get_num_moduli() 
    """


class Persona(ABC, ClassUtilsNomi, ClassUtilsCF):
    # INFO: Prototipi da implementare nelle sottoclassi
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
        type(self)._objects_by_cf[self.__cf] = self
        
        # Avendo ereditato da ClassUtilsNomi, registriamo l'oggetto anche per nome completo
        type(self)._objects_by_name[f"{self.__nome} {self.__cognome}"] = self

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
        if cf in cls._objects_by_cf:
          return cls._objects_by_cf[cf]
        citta_uuid = UUID(data["citta_nascita"])
        citta = Citta.get_object_by_uuid(citta_uuid)
        if not citta:
            raise KeyError(f"La città di nascita con UUID '{citta_uuid}' non esiste")
        return cls(nome=data["nome"], cognome=data["cognome"], cf=cf, citta_nascita=citta)

    def __init__(
        self,
        nome: str,
        cognome: str,
        cf: CodiceFiscale,
        citta_nascita: Citta,
    ):
        super().__init__(nome, cognome, cf, citta_nascita)

    def __str__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()} | CF: {self.get_codice_fiscale()} | nato a {self.get_citta_nascita()}"

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
        if cf in cls._objects_by_cf:
            return cls._objects_by_cf[cf]
        citta_uuid = UUID(data["citta_nascita"])
        citta = Citta.get_object_by_uuid(citta_uuid)
        if not citta:
            raise KeyError(f"La città di nascita con UUID '{citta_uuid}' non esiste")
        data_nascita_dt = datetime.fromisoformat(data["data_nascita"])
        return cls(
            nome=data["nome"], 
            cognome=data["cognome"], 
            cf=cf, 
            citta_nascita=citta, 
            matricola=data["matricola"], 
            data_nascita=data_nascita_dt
        )


    @classmethod
    def get_objects_by_matricole(cls): 
      return cls.__all_objects_by_matricole
    
        
    @classmethod
    def search_for_matricola(cls, matricola: str) -> Optional[Self]:
      for m, student in cls.get_objects_by_matricole().items():
        if m == matricola:
          return student
      return None
    

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
        self.__esami_superati: set = set()  # Inizializziamo un set vuoto di esami
        type(self).__all_objects_by_matricole[self.__matricola] = self

    """=== Gestione esami e voti ==="""
    # TODO: Implementare
    """
    def moduli_con_voto_piu_alto() -> set[Modulo]:

    """

    def get_matricola(self) -> str:
        return self.__matricola

    def get_data_nascita(self) -> datetime:
        return self.__data_nascita

    def get_esame(self, modulo: Modulo) -> Voto: ...

    def add_esame(self, modulo: Modulo, voto: Voto): ...

    def get_corso(self) -> CorsoITS: ...

    def __str__(self) -> str:
        return f"[{self.get_matricola()}] | {self.get_cognome()}, {self.get_nome()} | CF: {self.get_codice_fiscale()} | nato a {self.get_citta_nascita()} il {self.get_data_nascita()}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_codice_fiscale()),
            {
                "nome": self.get_nome(),
                "cognome": self.get_cognome(),
                "codice_fiscale": str(self.get_codice_fiscale()),
                "citta_nascita": str(self.get_citta_nascita().get_id()),
                "matricola": str(self.get_matricola()),
                "data_nascita": self.get_data_nascita().isoformat(),
            },
        )
