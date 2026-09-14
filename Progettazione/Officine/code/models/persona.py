from __future__ import annotations

from datetime import date
from types.datatypes import CodiceFiscale, Indirizzo, Telefono
from types.validators import AssociationValidator, DataValidator
from typing import Self

from associations import dirige, lavora
from citta import Citta
from exceptions.link import (
    InvalidLinkException,
)
from exceptions.model import (
    IsNotDipendenteException,
    IsNotDirettoreException,
    IsNotValidPersonaException,
)
from models.officina import Officina


class Persona:
    __objects_by_codice_fiscale: dict[CodiceFiscale, Self] = dict()
    __objects_by_name: dict[str, Self] = dict()

    # INFO: VALIDATORS

    @staticmethod  # Validazione senza classe o istanza
    def __validate_persona_params(
        is_cliente: bool,
        is_dipendente: bool,
        is_direttore: bool,
    ):
        if not (is_cliente or is_dipendente or is_direttore):
            raise IsNotValidPersonaException(
                "La persona deve obbligatoriamente avere almeno un ruolo 'cliente', 'dipendente' e/o 'direttore'"
            )

    # Validazione con istanza
    def __validate_persona(self) -> bool:
        if not (self.is_cliente() or self.is_dipendente() or self.is_direttore()):
            raise IsNotValidPersonaException
        return True

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_codice_fiscale(cls):
        return cls.__objects_by_codice_fiscale.values()

    @classmethod
    def get_object_by_codice_fiscale(cls, codice_fiscale: CodiceFiscale) -> Self | None:
        return cls.__objects_by_codice_fiscale.get(codice_fiscale)

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_name.get(nome)

    # INFO: GETTERS

    def get_nascita(self) -> date | None:
        return self.__nascita

    def get_nome(self) -> str:
        return self.__nome

    def get_cognome(self) -> str:
        return self.__cognome

    def get_codice_fiscale(self) -> CodiceFiscale | str:
        return self.__codice_fiscale

    def get_indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def get_telefono(self) -> Telefono:
        return self.__telefono

    def get_citta_nascita(self) -> Citta | None:
        return self.__citta

    def is_dipendente(self) -> bool:
        return self.__is_dipendente

    def is_direttore(self) -> bool:
        return self.__is_direttore

    def is_cliente(self) -> bool:
        return self.__is_cliente

    def get_links_dirige(self) -> frozenset[dirige]:
        """Restituisce la collezione immutabile dei link associativi 'dirige'."""
        return self.__links_dirige

    def get_direttori(self) -> frozenset[Persona]:
        """Restituisce la collezione immutabile dei direttori con associazione 'dirige' valida."""
        return frozenset(d.get_persona() for d in self.__links_dirige if d.is_valid())

    def get_officine_dirette(self) -> frozenset[Officina]:
        """Restituisce l'insieme delle Officine dirette dall'istanza corrente.
        
        Realizza il pattern della delegazione navigando la classe associativa 'dirige'.
        """
        return frozenset(link.get_officina() for link in self.__links_dirige if link.is_valid())

    def get_lavora(self) -> frozenset[lavora]:
        return frozenset(link for link in self.__links_lavora if link.is_valid())

    # INFO: SETTERS

    def __set_codice_fiscale(self, codice_fiscale: CodiceFiscale):
        DataValidator.validate_codice_fiscale(codice_fiscale)
        self.__codice_fiscale = codice_fiscale
        
    def __set_nome(self, nome: str):
        DataValidator.validate_str(nome)
        self.__nome = nome

    def __set_cognome(self, cognome: str):
        DataValidator.validate_str(cognome)
        self.__cognome = cognome

    def __set_nascita(self, nascita: date | None):
        if nascita:
            DataValidator.validate_date(nascita)
        else:
            self.__nascita = nascita

    def __set_indirizzo(self, indirizzo: Indirizzo, citta: Citta):
        DataValidator.validate_indirizzo(indirizzo)
        DataValidator.validate_citta(citta)
        self.__indirizzo = indirizzo
        self.__citta = citta

    def __set_telefono(self, telefono: Telefono):
        DataValidator.validate_telefono(telefono)
        self.__telefono = telefono

    # Setter per associazione con attributi vincolanti
    # Impostare il campo "nascita" solo se "is_direttore" == True
    def _set_direttore(self, nascita: date):
        self.__validate_persona()
        DataValidator.validate_date(nascita)
        self.__nascita = nascita
        self.__is_direttore = True

        # [V.Persona.nascita_se_direttore]
        # Per ogni p:Persona, deve essere:
        #   - p.nascita ha un valore se e solo se p.is_direttore = TRUE
        assert (self.__nascita is not None) == (self.is_direttore == True)

    def _reset_direttore(self):
        if not self.is_dipendente() and not self.is_cliente():
            raise IsNotValidPersonaException(
                f"Non puoi eliminare il ruolo di direttore della persona {self}"
            )

        self.__nascita = None
        self.__is_direttore = False

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        #   p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.__validate_persona()

        # [V.Persona.nascita_se_direttore]
        # Per ogni p:Persona, deve essere:
        #   p.nascita ha un valore se e solo se p.is_direttore = TRUE
        assert (self.get_nascita() is not None) == (self.is_direttore())

    def _set_is_cliente(self, value: bool):
        self.__validate_persona()
        DataValidator.validate_bool(value)
        self.__is_cliente = value

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        #   p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.__validate_persona()

    def _set_is_dipendente(self, value: bool):
        self.__validate_persona()
        DataValidator.validate_bool(value)
        self.__is_dipendente = value

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        #   p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.__validate_persona()

    # INFO: ASSOCIAZIONI

    def _add_dirige(self, link: dirige) -> None:
        """Metodo protetto invocato da dirige._create."""
        AssociationValidator.validate_dirige(self, link)
        if not self.is_direttore():
          raise IsNotDirettoreException("Impossibile associare la funzione di direzione ad una Persona non direttore.")        # Aggiornamento immutabile del frozenset tramite unione insiemistica
        self.__links_dirige = self.__links_dirige | frozenset([link])

    def _remove_dirige(self, link: dirige) -> None:
        """Metodo protetto invocato da dirige._remove."""
        if not self.is_direttore():
            raise IsNotDirettoreException
        # Filtra il set rimuovendo il link passato
        if link in self.__links_dirige:
            self.__links_dirige = frozenset(l for l in self.__links_dirige if l != link)

    # IMPORTANT: Interfaccia pubblica
    def add_lavoratore(self, officina: Officina, assunzione: date): 
      """Interfaccia pubblica per l'assegnazione o sostituzione del ruolo 'lavora' al dipendente."""
      if self is None or not self.__validate_persona():
        raise IsNotValidPersonaException
      if not self.is_dipendente():
        raise IsNotDipendenteException
      if officina is None:
        raise InvalidLinkException("L'officina passata non è valida")
      DataValidator.validate_date(assunzione)
      for link in self.__links_lavora:
          if link is not None and link.is_valid() and link.get_officina() == officina:
              raise InvalidLinkException("Esiste già un link di 'lavora' attivo tra la persona e l'officina specificata.")

      lavora._create(officina, self, assunzione)


    def _add_lavora(self, link: lavora):
        AssociationValidator.validate_lavora(self, link)
        if not self.is_dipendente():
            raise IsNotDipendenteException

        # Per aggiungere elementi a un frozenset, creiamo un nuovo frozenset
        # unendo i dati del precedente
        self.__links_lavora = self.__links_lavora | frozenset([link])

    def _remove_lavora(self, link: lavora):
        if link in self.__links_lavora: 
          self.__links_lavora = frozenset(x for x in self.__links_lavora if x != link)

    # INFO: CONSTRUCTORS

    def __new__(
        cls,
        codice_fiscale: CodiceFiscale,
        nome: str,
        cognome: str,
        indirizzo: Indirizzo,
        citta: Citta,
        telefono: Telefono,
        nascita: date | None,
        is_cliente: bool,
        is_dipendente: bool,
        is_direttore: bool,
    ):

        DataValidator.validate_codice_fiscale(codice_fiscale)
        DataValidator.validate_str(nome)
        DataValidator.validate_str(cognome)
        DataValidator.validate_indirizzo(indirizzo)
        DataValidator.validate_citta(citta)
        DataValidator.validate_telefono(telefono)
        Persona.__validate_persona_params(is_cliente, is_dipendente, is_direttore)

        if is_direttore and nascita:
            DataValidator.validate_date(nascita)

        return super().__new__(cls)

    def __init__(
        self,
        codice_fiscale: CodiceFiscale,
        nome: str,
        cognome: str,
        indirizzo: Indirizzo,
        citta: Citta,
        telefono: Telefono,
        nascita: date | None,
        is_cliente: bool,
        is_dipendente: bool,
        is_direttore: bool,
    ):
        # [V.Persona.nascita_se_direttore] p.nascita ha un valore se e solo se p.is_direttore = TRUE
        if (nascita is not None) != (is_direttore):
            raise IsNotDirettoreException(
                "I valori degli argomenti 'nascita' e 'is_direttore' non sono coerenti tra di loro"
            )

        self.__set_codice_fiscale(codice_fiscale)
        self.__set_nome(nome)
        self.__set_cognome(cognome)
        self.__set_indirizzo(indirizzo, citta)
        self.__set_telefono(telefono)

        if self.is_direttore() and nascita:
            self.__set_nascita(nascita)
        else:
            self.__set_nascita(None)

        self.__links_lavora: frozenset[lavora] = frozenset()  # [0..*]
        self.__links_dirige: frozenset[dirige] = frozenset()  # [0..*]

        type(self).__objects_by_name[f"{self}"] = self
        type(self).__objects_by_codice_fiscale[self.__codice_fiscale] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()}"

    def __repr__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()} residente in {self.get_indirizzo()}"

    # def to_json(self) -> tuple[str, dict]:
    #     return (
    #         str(self.get_codice_fiscale()),
    #         {
    #             "nome": self.get_nome(),
    #             "cognome": self.get_cognome(),
    #             "codice_fiscale": str(self.get_codice_fiscale()),
    #             "citta_nascita": str(self.get_citta_nascita()),
    #             "indirizzo": str(self.get_indirizzo()),
    #             "data_nascita": str(self.get_nascita())
    #         },
    #     )
