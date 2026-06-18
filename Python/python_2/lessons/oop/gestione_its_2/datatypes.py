import re
from enum import StrEnum, auto
from typing import Self


class RealGEZ(float): ...


class IntGEZ(str): ...


class CodiceFiscale(str):
    __pattern = r"[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]"

    @classmethod
    def check(cls, string: str) -> bool:
        if not re.fullmatch(cls.__pattern, string, re.IGNORECASE):
            return False
        else:
            return True

    def __new__(cls, value: str):
        if not cls.check(value):
            raise ValueError("Il codice fiscale dato non soddisfa il pattern")
        else:
            super().__new__(cls, value.upper())


class NumeroPositivo(int):
    @classmethod
    def is_positive(cls, val: int) -> bool:
        """Verifica che un numero sia intero positivo, zero escluso"""
        return True if val > 0 else False

    @classmethod
    def is_positive_zero(cls, val: int) -> bool:
        """Verifica che un numero sia intero positivo, zero incluso"""
        return True if val >= 0 else False


class Voto8(int):
    # Va ridefinito il costruttore
    def __new__(cls, value: int | float) -> Self:
        if 6 < value > 10:
            raise ValueError(
                f"Il valore dev'essere compreso tra 6 e 10. {value} non è un valore accettato"
            )
        # restituisce un'istanza della superclasse
        return super().__new__(cls, value)


class Geneder(StrEnum):
    # auto() crea identificatori numerici auto-incrementati
    uomo = auto()
    donna = auto()
