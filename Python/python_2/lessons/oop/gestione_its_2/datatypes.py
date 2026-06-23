import re
from typing import Self

class CodiceFiscale(str):
	def __new__(cls, s)->Self:
		if not re.fullmatch('[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[0-9A-Za-z]{5}', s):
			raise ValueError(f"La stringa {s} non è un codice fiscale valido")
		return super().__new__(cls, s.upper())


class IntGEZ(int):
	def __new__(cls, v:int|float)->Self:
		if not v >= 0:
			raise ValueError(f"Il valore {v} non è un IntGEZ valido")
		return super().__new__(cls, v)


class IntGZ(int):
	def __new__(cls, v:int|float)->Self:
		if not v > 0:
			raise ValueError(f"Il valore {v} non è un IntGZ valido")
		return super().__new__(cls, v)


class Voto(int):
	def __new__(cls, v:int|float)->Self:
		if not (v >= 6 and v <= 10):
			raise ValueError(f"Il valore {v} non è un Voto valido")
		return super().__new__(cls, v)


class RealGEZ(float):
	def __new__(cls, v:int|float)->Self:
		if not v >= 0:
			raise ValueError(f"Il valore {v} non è un RealGEZ valido")
		return super().__new__(cls, v)
