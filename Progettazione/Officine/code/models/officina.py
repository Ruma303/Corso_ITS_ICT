from __future__ import annotations

from types.datatypes import Indirizzo, Telefono
from types.validators import DataValidator
from typing import Self

from associations import dirige, lavora
from exceptions.link import InvalidLinkException
from exceptions.model import IsNotDirettoreException
from persona import Persona

from Progettazione.Officine.prof.main import CodiceFiscale


class Officina:
    __objects_by_nome: dict[str, Self] = dict()
    __objects_by_registry: dict[tuple[str, Indirizzo], Self] = dict()
    __objects_by_telefono: dict[Telefono, Self] = dict()
    __objects_by_direttore: dict[CodiceFiscale, Self] = dict()

    # INFO: VALIDATORS

    def __validate_lavora(self, link: lavora):
        if not isinstance(link, lavora):
            raise InvalidLinkException
        if link.get_persona() != self:
            raise InvalidLinkException

    def __validate_dirige(self, link: dirige):
        if not isinstance(link, dirige):
            raise InvalidLinkException
        if link.get_persona() != self:
            raise InvalidLinkException

    # INFO: CLASSMETHODS

    @classmethod
    def all_objects_by_nome(cls):
        return cls.__objects_by_nome.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Self | None:
        return cls.__objects_by_nome.get(nome)

    @classmethod
    def all_objects_by_telefono(cls) -> dict[Telefono, Self]:
        return cls.__objects_by_telefono

    @classmethod
    def get_object_by_telefono(cls, numero_tel: str) -> Telefono | None:
        if numero_tel in cls.__objects_by_telefono:
            return cls.__objects_by_telefono.get(numero_tel)

    @classmethod
    def all_objects_by_direttore(cls) -> dict[CodiceFiscale, Self]:
        return cls.__objects_by_direttore

    """
    @classmethod
    def get_object_by_direttore(cls, direttore: Persona) -> Persona:
        return cls.__objects_by_direttore.get(direttore)
    """

    # INFO: GETTERS

    def get_nome(self) -> str:
        return self.__nome

    def get_indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def get_telefono(self) -> Telefono:
        return self.__telefono

    def get_direttore(self) -> Persona:
        return self.__direttore

    def get_lavora(self) -> frozenset[lavora]:
        return frozenset(self.__lavora)

    def get_dirige(self) -> dirige | None:
        return self.__dirige

    # INFO: SETTERS

    def __set_telefono(self, telefono: Telefono) -> None:
        DataValidator.__validate_telefono(telefono)
        self.__telefono = telefono

    def __set_indirizzo(self, indirizzo: Indirizzo) -> None:
        DataValidator.__validate_indirizzo(indirizzo)
        self.__indirizzo = indirizzo

    # INFO: ASSOCIATIONS

    def _add_lavora(self, link: lavora):
        self.__validate_lavora(link)
        if not link.get_persona().is_dipendente():
            raise TypeError("La persona passata non è un dipendente e on può lavorare")
        self.__lavora.add(link)

    def _remove_lavora(self, link: lavora):
        self.__lavora.remove(link)

    def _add_dirige(self, link: dirige):
        self.__validate_dirige(link)
        if not link.get_persona().is_direttore():
            raise TypeError("La persona passata non è un direttore e on può dirigere")

        # IMPORTANT: gestione asimmetrica, officina è l'unica deputata a creare il link
        self.__dirige = link

    def _remove_dirige(self, link: dirige):
        self.__validate_dirige(link)
        self.__dirige = None

    # Un direttore dev'essere 1..1, quindi sostituire il vecchio link
    def change_direttore(self, persona: Persona):
        # Verificare che il link non esista
        if not persona.__is_direttore:
            raise IsNotDirettoreException
        if self.get_dirige():
            dirige._remove(self.get_dirige())  # Se esiste lo rimuove
        dirige._create(self, persona)

    # INFO: CONSTRUCTORS

    def __new__(
        cls,
        nome: str,
        indirizzo: Indirizzo,
        telefono: Telefono,
        direttore: Persona,  # 1..1 Serve per creare il vincolo "dirige"
    ):
        DataValidator.__validate_str(nome)
        DataValidator.__validate_indirizzo(indirizzo)
        DataValidator.__validate_telefono(telefono)
        DataValidator.__validate_indirizzo(indirizzo)

    def __init__(
        self,
        nome: str,
        indirizzo: Indirizzo,
        telefono: Telefono,
        direttore: Persona,
    ):
        self.__nome = nome  # <<imm>> {id}
        self.__set_indirizzo(indirizzo)  # <<imm>> {id}
        self.__set_telefono(telefono)
        self.__direttore = direttore

        # Associazioni

        self.__lavora = set()  # 0..*
        self.change_direttore(direttore)  # 1..1 obbligatorio ma mutabile

        type(self).__objects_by_nome[self.__nome] = self
        # Salvataggio con vincolo composto (nome, indirizzo)
        type(self).__objects_by_registry[(self.__nome, self.__indirizzo)] = self
        type(self).__objects_by_telefono[self.__telefono] = self
        type(self).__objects_by_direttore[self.__direttore.get_codice_fiscale()] = self

    # INFO: UTILITIES

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__indirizzo})"

    def to_json(self) -> tuple[str, dict]:
        return (
            str(self.get_nome()),
            {
                "nome": self.get_nome(),
                "indirizzo": {
                    "via": self.get_indirizzo().get_via(),
                    "civico": self.get_indirizzo().get_civico(),
                },
            },
        )

    # def numero_dipendenti(self) -> IntGEZ: ...
