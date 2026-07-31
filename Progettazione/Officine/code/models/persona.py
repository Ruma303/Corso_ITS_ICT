from __future__ import annotations

from datetime import date
from types.datatypes import CodiceFiscale, Indirizzo, Telefono
from types.validators import DataValidator
from typing import Self

from associations import dirige, lavora
from citta import Citta
from exceptions.link import InvalidLinkException
from exceptions.model import (
    IsNotDipendenteException,
    IsNotDirettoreException,
    IsNotValidPersonaException,
)
from models.officina import Officina


class Persona:
    __objects_by_codice_fiscale: dict[CodiceFiscale | str, Self] = dict()
    __objects_by_name: dict[str, Self] = dict()

    # INFO: VALIDATORS

    @staticmethod
    def __validate_nome(nome: str):
        DataValidator.__validate_str(nome)

    @staticmethod
    def __validate_cognome(cognome: str):
        DataValidator.__validate_str(cognome)

    @staticmethod
    def __validate_codice_fiscale(codice_fiscale: CodiceFiscale | str):
        if not codice_fiscale:
            raise TypeError("Il codice fiscale non può essere None o vuoto")
        if not isinstance(codice_fiscale, CodiceFiscale):
            raise TypeError(
                f"'{codice_fiscale}' deve essere una istanza di CodiceFiscale o una stringa"
            )

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
    def __validate_persona(self):
        if not (self.is_cliente() or self.is_dipendente() or self.is_direttore()):
            raise IsNotValidPersonaException

    @staticmethod
    def __validate_indirizzo(indirizzo: Indirizzo):
        if not indirizzo:
            raise ValueError("indirizzo non può essere None o vuoto")
        if not isinstance(indirizzo, Indirizzo):
            raise TypeError("indirizzo deve essere una istanza di Indirizzo")

    @staticmethod
    def __validate_citta(citta: Citta):
        if not citta:
            raise ValueError("citta non può essere None o vuoto")
        if not isinstance(citta, Citta):
            raise TypeError("citta deve essere una istanza di Citta")

    @staticmethod
    def __validate_telefono(telefono: Telefono):
        if not telefono:
            raise ValueError("telefono non può essere None o vuoto")
        if not isinstance(telefono, Telefono):
            raise TypeError("telefono deve essere una istanza di Telefono")

    @staticmethod
    def __validate_nascita(nascita: date | None):
        if not isinstance(nascita, date) or nascita is not None:
            raise TypeError("nascita deve essere una istanza di date oppure vuota")

    def __validate_link(self, link):
        if link is None:
            raise InvalidLinkException
        if not isinstance(link, dirige):
            raise InvalidLinkException
        if link.get_persona() != self:
            raise InvalidLinkException
        if not link.is_valid():
            raise ValueError("Il link non è valido!")

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

    def get_lavora(self) -> frozenset[lavora]:
        return frozenset(self.__lavora)

    def get_dirige(self) -> set[dirige] | None:
        return self.__dirige

    def is_dipendente(self) -> bool:
        return self.__is_dipendente

    def is_direttore(self) -> bool:
        return self.__is_direttore

    def is_cliente(self) -> bool:
        return self.__is_cliente

    # INFO: SETTERS

    def __set_codice_fiscale(self, codice_fiscale: CodiceFiscale | str):
        Persona.__validate_codice_fiscale(codice_fiscale)
        # Se viene passata una str, usiamo il costruttore per il dato CodiceFiscale
        if type(codice_fiscale) is str:
            self.__codice_fiscale = CodiceFiscale(codice_fiscale)
        else:
            self.__codice_fiscale = codice_fiscale

    def __set_nome(self, nome: str):
        Persona.__validate_nome(nome)
        self.__nome = nome

    def __set_cognome(self, cognome: str):
        Persona.__validate_cognome(cognome)
        self.__cognome = cognome

    def __set_nascita(self, nascita: date | None):
        Persona.__validate_nascita(nascita)
        self.__nascita = nascita

    def __set_indirizzo(self, indirizzo: Indirizzo, citta: Citta):
        Persona.__validate_indirizzo(indirizzo)
        Persona.__validate_citta(citta)
        self.__indirizzo = indirizzo
        self.__citta = citta

    def __set_telefono(self, telefono: Telefono):
        Persona.__validate_telefono(telefono)
        self.__telefono = telefono

    # Setter per associazione con attributi vincolanti
    # Impostare il campo "nascita" solo se "is_direttore" == True
    def _set_direttore(self, nascita: date):
        self.__validate_persona()
        Persona.__validate_nascita(nascita)
        self.__nascita = nascita
        self.__is_direttore = True

        # [V.Persona.nascita_se_direttore]
        # Per ogni p:Persona, deve essere:
        #   - p.nascita ha un valore se e solo se p.is_direttore = TRUE
        assert (self.__nascita is not None) == (self.is_direttore == True)

    def _reset_direttore(self):
        if not self.is_dipendente() and not self.is_cliente():
            raise ValueError(
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
        DataValidator.__validate_bool(value)
        self.__is_cliente = value

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        #   p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.__validate_persona()

    def _set_is_dipendente(self, value: bool):
        self.__validate_persona()
        DataValidator.__validate_bool(value)
        self.__is_dipendente = value

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        #   p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.__validate_persona()

    # INFO: ASSOCIAZIONI

    def _add_lavora(self, link: lavora):
        if not self.is_dipendente():
            raise ValueError("self non è un dipendente")
        if link is None:
            raise ValueError("link non può essere None o vuoto")
        if not isinstance(link, lavora):
            raise TypeError("link deve essere di class lavora")
        if link.get_persona() != self:
            raise ValueError("Il link non appartiene a questa istanza")
        if not link.is_valid():
            raise ValueError("link non è valido!")

        # Per aggiungere elementi a un frozenset, creiamo un nuovo frozenset
        # unendo i dati del precedente
        self.__lavora = self.__lavora | frozenset([link])

    def _remove_lavora(self, link: lavora):
        # Vincolo: Almeno un link deve rimanere
        if len(self.__lavora) <= 1 and link in self.__lavora:
            raise ValueError(
                "Impossibile rimuovere il link: deve esserci almeno un link 'lavora'"
            )

        # Creiamo un nuovo frozenset escludendo l'elemento
        # Sfruttiamo una list comprehension per creare un frozenset di tutti i link meno quello passato
        self.__lavora = frozenset(x for x in self.__lavora if x != link)

    def _add_dirige(self, link: dirige):
        if not self.is_direttore():
            raise IsNotDirettoreException
        self.__validate_link(link)
        self.__dirige.add(link)

    def _remove_dirige(self, link: dirige):
        if not self.is_direttore():
            raise ValueError("self non è un dipendente")
        self.__validate_link(link)
        self.__dirige = None

    # Interfaccia pubblica da richiamare nelle classi
    # Le officine aggiunte alle persone hanno 0..*
    def add_officina(self, officina: Officina, assunzione: date):
        if not self.is_dipendente():
            raise IsNotDipendenteException
        if self.get_lavora():
            lavora._remove(self.get_lavora())
        lavora._create(officina, self, assunzione)

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

        Persona.__validate_codice_fiscale(codice_fiscale)
        Persona.__validate_nome(nome)
        Persona.__validate_cognome(cognome)
        Persona.__validate_indirizzo(indirizzo)
        Persona.__validate_citta(citta)
        Persona.__validate_telefono(telefono)
        Persona.__validate_persona_params(is_cliente, is_dipendente, is_direttore)

        if is_direttore:
            Persona.__validate_nascita(nascita)

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

        if self.is_direttore():
            self.__set_nascita(nascita)
        else:
            self.__set_nascita(None)

        self.__lavora = set()  # [0..*]
        self.__dirige = set()  # [0..*]

        type(self).__objects_by_codice_fiscale[self.__codice_fiscale] = self
        type(self).__objects_by_name[f"{self.__nome} {self.__cognome}"] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.get_cognome()}, {self.get_nome()} residente in {self.get_indirizzo()}"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_codice_fiscale()),
            {
                "nome": self.get_nome(),
                "cognome": self.get_cognome(),
                "codice_fiscale": str(self.get_codice_fiscale()),
                "citta_nascita": str(self.get_citta_nascita()),
                "indirizzo": str(self.get_indirizzo()),
            },
        )
