from abc import ABC
from typing import Self


class MetodoPagamento(ABC): 
    __all_objects_by_nome: dict[str, Self] = {}

    @classmethod
    def get_by_nome(cls, nome: str) -> Self | None:
        return cls.__all_objects_by_nome.get(nome)

    def __init__(self, nome: str):
        self.__nome: str | None = None
        self.set_nome(nome)

    def get_nome(self) -> str | None:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError(
                f"Il valore dev'essere di tipo str. Ora è '{type(nome).__name__}'"
            )
        nome = nome.strip()
        if not nome:
            raise ValueError("Il nome non può essere vuoto")
        if nome == self.__nome:
            return
        registry = type(self).__all_objects_by_nome
        if nome in registry:
            raise KeyError("Questo metodo di pagamento già esiste")

        if self.__nome is not None:
            del registry[self.__nome]
        self.__nome = nome
        registry[nome] = self

    def __hash__(self):
        return hash(self.__nome)

    def __eq__(self, other: object):
        if type(self) is not type(other):
            return False
        if hash(self) != hash(other):
            return False
        if type(other) == MetodoPagamento:
          return self.__nome == other.__nome
        return False

    def __repr__(self):
        return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self):
        return f"{self.get_nome()}"
