from datetime import date
from types.datatypes import Indirizzo, Telefono

from exceptions.link import InvalidLinkException
from models.citta import Citta


class DataValidator:
    @staticmethod
    def __validate_bool(value: bool):
        if type(value) is not bool or value is None:
            raise TypeError(f"'{value}' deve essere un booleano")

    @staticmethod
    def __validate_nome(nome: str):
        if not nome or not isinstance(nome, str):
            raise TypeError("Il nome deve essere una stringa valida e non vuota")

    @staticmethod
    def __validate_str(value: str):
        if type(value) is not str or value is None:
            raise TypeError(f"'{value}' deve essere una stringa valida e non vuota")

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
    def __validate_date(value: date):
        if not value:
            raise ValueError(f"'{value}' non può essere None o vuoto")
        if not isinstance(value, date):
            raise TypeError(f"'{value}' deve essere una istanza di datetime.date")

    # Copiare e incollare nella classe dove utilizzarlo per avere l'istanza self corretta
    """
    def __validate_link(self, link):
        if link is None:
            raise InvalidLinkException("Il link non può essere None o vuoto")
        if not link.is_valid():
            raise ValueError("Il link non è valido!")
    """
