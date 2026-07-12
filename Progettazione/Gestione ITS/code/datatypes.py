import re
from typing import Self

class CodiceFiscale(str):
    def __new__(cls, s: str) -> Self:
        if not re.fullmatch('[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[0-9A-Za-z]{5}', s):
            raise ValueError(f"La stringa {s} non è un codice fiscale valido")
        return super().__new__(cls, s.upper())


class IntGEZ(int):
    def __new__(cls, v: int | float) -> Self:
        v = int(v)
        if v < 0:
            raise ValueError(f"Il valore {v} non può essere minore di 0")
        return super().__new__(cls, v)


class IntGZ(int):
    def __new__(cls, v: int | float) -> Self:
        v = int(v)
        if v <= 0:
            raise ValueError(f"Il valore {v} deve essere maggiore di 0")
        return super().__new__(cls, v)


class Voto(int):
    def __new__(cls, v: int | float) -> Self:
        v = int(v)
        if v < 6 or v > 10:
            raise ValueError(f"Il valore {v} deve essere compreso tra 6 e 10")
        return super().__new__(cls, v)


class RealGEZ(float):
    def __new__(cls, v: int | float) -> Self:
        # Essendo un float, non facciamo il cast a int
        if v < 0:
            raise ValueError(f"Il valore {v} non può essere minore di 0")
        return super().__new__(cls, v)