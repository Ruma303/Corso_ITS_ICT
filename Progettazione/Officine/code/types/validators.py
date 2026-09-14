import re
from datetime import date
from types.datatypes import CodiceFiscale, Indirizzo, Targa, Telefono
from typing import Any

from exceptions.link import InvalidLinkException
from models.associations import dirige, lavora
from models.cap import CAP
from models.citta import Citta
from models.nazione import Nazione

from Progettazione.Officine.code.exceptions.model import IsNotValidPersonaException


class DataValidator:
    """Classe di utilità per la validazione centralizzata dei dati di dominio.

    I metodi utilizzano un singolo underscore per consentire l'accesso
    ai moduli all'interno del package pur segnalando la natura protetta.
    """

    @staticmethod
    def validate_bool(value: Any):
        if type(value) is not bool or value is None:
            raise TypeError(f"'{value}' deve essere un booleano")

    @staticmethod
    def validate_str(value: Any):
        if not isinstance(value, str) or not value.strip():
            raise TypeError(f"'{value}' deve essere una stringa valida e non vuota")

    @staticmethod
    def validate_instance(obj: Any, target_class: type, name: str) -> None:
        """Validatore generico per oggetti di dominio non nulli."""
        if obj is None:
            raise ValueError(f"'{name}' non può essere None")
        if not isinstance(obj, target_class):
            raise TypeError(f"'{name}' deve essere una istanza di {target_class.name}")

    @staticmethod
    def validate_codice_fiscale(codice_fiscale: CodiceFiscale):
        if not codice_fiscale:
            raise TypeError("Il codice fiscale non può essere None o vuoto")
        if not isinstance(codice_fiscale, CodiceFiscale):
            raise TypeError(
                f"'{codice_fiscale}' deve essere una istanza di CodiceFiscale o una stringa"
            )

    @staticmethod
    def validate_indirizzo(indirizzo: Indirizzo) -> None:
        DataValidator.validate_instance(indirizzo, Indirizzo, "indirizzo")

    @staticmethod
    def validate_citta(citta: Citta) -> None:
        DataValidator.validate_instance(citta, Citta, "citta")

    @staticmethod
    def validate_nazione(nazione: Nazione) -> None:
        DataValidator.validate_instance(nazione, Nazione, "nazione")

    @staticmethod
    def validate_cap(cap_value: str) -> None:
        DataValidator.validate_str(cap_value)
        if not re.fullmatch(r"[0-9]{5}", cap_value):
            raise ValueError(
                f"Il CAP '{cap_value}' inserito non è valido. Deve essere composto da esattamente 5 cifre."
            )

    @staticmethod
    def validate_telefono(telefono: Telefono) -> None:
        DataValidator.validate_instance(telefono, Telefono, "telefono")

    @staticmethod
    def validate_targa(targa: Targa) -> None:
        DataValidator.validate_instance(targa, Targa, "targa")

    @staticmethod
    def validate_date(value: date) -> None:
        DataValidator.validate_instance(value, date, "data")

    @staticmethod
    def validate_link(link: Any) -> None:
        """Valida un oggetto di tipo Link fornito come argomento senza richiedere self."""
        if link is None:
            raise InvalidLinkException("Il link non può essere None o vuoto")
        if not link.is_valid():
            raise InvalidLinkException("Il link non è valido!")


class AssociationValidator:
    @staticmethod
    def validate_lavora(instance: Any, link: lavora):
        if not isinstance(link, lavora):
            raise InvalidLinkException
        if link.get_persona() != instance:
            raise IsNotValidPersonaException
        if not link.is_valid():
            raise InvalidLinkException

    @staticmethod
    def validate_dirige(instance: Any, link: dirige):
        if not isinstance(link, dirige):
            raise InvalidLinkException
        if link.get_officina() != instance:
            raise InvalidLinkException
        if not link.is_valid():
            raise InvalidLinkException
