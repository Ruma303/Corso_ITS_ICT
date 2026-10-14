import re
from datetime import datetime, timedelta
from enum import auto
from pathlib import Path
from typing import Any, Self

from _typeshed import StrEnum

from src.python_code.exceptions.exceptions import TypeInvalidException


class TimeDelta_GZ(timedelta):
    """Durata strettamente positiva (> 0). Immutabile, come timedelta.

    Il parsing di input testuali (es. ISO 8601) spetta alla UI: qui arrivano
    solo valori già tipizzati e si controlla il vincolo di dominio.
    """

    def __new__(cls, value: timedelta) -> TimeDelta_GZ:
        if not isinstance(value, timedelta):
            raise TypeInvalidException("timedelta")
        if value <= timedelta(0):
            raise ValueError("La durata dev'essere maggiore di zero")
        return super().__new__(cls, value.days, value.seconds, value.microseconds)

    @classmethod
    def from_scadenza(cls, istante_pubbl: datetime, scadenza: datetime) -> TimeDelta_GZ:
        """Se la UI raccoglie una data di scadenza invece di una durata."""
        for d in (istante_pubbl, scadenza):
            if not isinstance(d, datetime):
                raise TypeInvalidException("datetime")
        return cls(scadenza - istante_pubbl)  # scadenza <= istante -> ValueError

    def __reduce__(self):
        # timedelta ricostruisce con (days, seconds, microseconds): con il
        # nostro __new__(value) copy/deepcopy/pickle altrimenti fallirebbero
        return (type(self), (timedelta(self.days, self.seconds, self.microseconds),))


class Condizione(StrEnum):
    """Enumerazione per la condizione di annuncio post.

    Supporta la ricerca case-insensitive e la normalizzazione
    di formati stringa alternativi.
    """

    OTTIMO = auto()
    BUONO = auto()
    DISCRETO = auto()
    DA_SISTEMARE = auto()

    @classmethod
    def _missing_(cls, value: object) -> "Condizione":
        """Gestisce la risoluzione dei valori non direttamente corrispondenti ai membri.

        Esegue la validazione del tipo, la pulizia della stringa e la mappatura
        degli alias noti prima di sollevare un ValueError.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"Il valore passato deve essere una stringa, ricevuto: {type(value).__name__}"
            )

        normalized_value = value.strip().upper()

        if normalized_value == "OTTIMO":
            return cls.OTTIMO

        if normalized_value == "BUONO":
            return cls.BUONO

        if normalized_value == "DISCRETO":
            return cls.DISCRETO

        if normalized_value == ("DA_SISTEMARE", "DA SISTEMARE"):
            return cls.DA_SISTEMARE

        for member in cls:
            if member.value == normalized_value:
                return member

        valid_choices = ", ".join([repr(m.value) for m in cls])
        raise ValueError(
            f"Valore '{value}' non valido per {cls.__name__}. "
            f"I valori accettati sono: {valid_choices} (o varianti equivalenti)."
        )


class StatoPost(StrEnum):
    """Enumerazione per lo stato di annuncio post.

    Supporta la ricerca case-insensitive e la normalizzazione
    di formati stringa alternativi.
    """

    NUOVO = auto()
    USATO = auto()

    @classmethod
    def _missing_(cls, value: object) -> "StatoPost":
        """Gestisce la risoluzione dei valori non direttamente corrispondenti ai membri.

        Esegue la validazione del tipo, la pulizia della stringa e la mappatura
        degli alias noti prima di sollevare un ValueError.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"Il valore passato deve essere una stringa, ricevuto: {type(value).__name__}"
            )

        normalized_value = value.strip().upper()

        if normalized_value == "NUOVO":
            return cls.NUOVO

        if normalized_value == "USATO":
            return cls.USATO

        for member in cls:
            if member.value == normalized_value:
                return member

        valid_choices = ", ".join([repr(m.value) for m in cls])
        raise ValueError(
            f"Valore '{value}' non valido per {cls.__name__}. "
            f"I valori accettati sono: {valid_choices} (o varianti equivalenti)."
        )


class TipologiaPost(StrEnum):
    """Enumerazione per la tipologia di annuncio post.

    Supporta la ricerca case-insensitive e la normalizzazione
    di formati stringa alternativi.
    """

    ASTA = "ASTA"
    COMPRALO_SUBITO = "COMPRALO_SUBITO"

    @classmethod
    def _missing_(cls, value: Any) -> "TipologiaPost":
        """Gestisce la risoluzione dei valori non direttamente corrispondenti ai membri.

        Esegue la validazione del tipo, la pulizia della stringa e la mappatura
        degli alias noti prima di sollevare un ValueError.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"Il valore passato deve essere una stringa, ricevuto: {type(value).__name__}"
            )

        normalized_value = value.strip().upper()

        # Gestione degli alias o varianti formattate
        if normalized_value in ("COMPRALO SUBITO", "COMPRALO_SUBITO"):
            return cls.COMPRALO_SUBITO

        if normalized_value == "ASTA":
            return cls.ASTA

        # Mappatura generica se il valore normalizzato corrisponde esattamente a un membro
        for member in cls:
            if member.value == normalized_value:
                return member

        valid_choices = ", ".join([repr(m.value) for m in cls])
        raise ValueError(
            f"Valore '{value}' non valido per {cls.__name__}. "
            f"I valori accettati sono: {valid_choices} (o varianti equivalenti)."
        )


class IntGZ(int):
    def __new__(cls, value: int | float) -> Self:
        if not value:
            raise ValueError("Il valore non può essere vuoto")
        if type(value) not in (int, float):
            raise TypeError("Il tipo del numero dev'essere un 'int' oppure un 'float'")
        value = int(value)
        if value <= 0:
            raise ValueError("Il numero non può essere negativo o zero")
        return super().__new__(cls, value)


class IntGEZ(int):
    def __new__(cls, value: int | float) -> Self:
        if not value:
            raise ValueError("Il valore non può essere vuoto")
        if type(value) not in (int, float):
            raise TypeError("Il tipo del numero dev'essere un 'int' oppure un 'float'")
        value = int(value)
        if value < 0:
            raise ValueError("Il numero non può essere negativo")
        return super().__new__(cls, value)


class Float_GEZ(float):
    def __new__(cls, value: int | float):
        if not value:
            raise ValueError("Il valore non può essere vuoto")
        if not isinstance(value, float):
            raise TypeError("Il valore dev'essere un float")
        value = float(value)
        if value < 0:
            raise ValueError("Il valore non può essere minore di 0")

        return super().__new__(cls, value)


class Float_GZ(float):
    def __new__(cls, value: int | float):
        if not value:
            raise ValueError("Il valore non può essere vuoto")
        if not isinstance(value, float):
            raise TypeError("Il valore dev'essere un float")
        value = float(value)
        if value <= 0:
            raise ValueError("Il valore non può essere minore o uguale di 0")

        return super().__new__(cls, value)
