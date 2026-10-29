from __future__ import annotations

from typing import Self

from src.ebuy_py.associations.post_cat import post_cat
from src.ebuy_py.datatypes.validators import DataValidator
from src.ebuy_py.exceptions.exceptions import (
    AlreadyExistingLinkException,
    InvalidLinkException,
)
from src.ebuy_py.models.post import Post


class Categoria:
    __all_objects_by_nome: dict[str, Self] = dict()

    # INFO: CLASSMETHODS

    @classmethod
    def get_all_categories(cls) -> dict[str, Self]:
        return cls.__all_objects_by_nome

    @classmethod
    def get_set_name_objects(cls) -> frozenset[Self]:
        return frozenset({l for l in cls.__all_objects_by_nome.values()})

    @classmethod
    def get_by_nome(cls, nome: str) -> Self | None:
        return cls.__all_objects_by_nome.get(nome)

    @classmethod
    def _clear_registry(cls) -> None:
        """Solo per i test."""
        cls.__all_objects_by_nome.clear()

    # INFO: GETTERS
    def get_nome(self) -> str | None:
        return self.__nome

    def get_posts_links(self) -> frozenset[post_cat]:
        return frozenset(self.__set_post_links)

    def get_posts(self) -> frozenset[Post]:
        return frozenset(p._get_post() for p in self.get_posts_links())

    # INFO: SETTERS
    def __set_nome(self, nome: str) -> None:
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
            raise KeyError("Questa categoria già esiste")

        # Tutti i controlli sono passati: ora si può modificare lo stato
        if self.__nome is not None:
            del registry[self.__nome]
        self.__nome = nome
        registry[nome] = self

    # INFO: CONSTRUCTORS
    def __init__(self, nome: str):
        self.__nome: str | None = None
        self.__set_nome(nome)

        # ASSOCIAZIONI DOPPIE
        self.__set_post_links: set[post_cat] = set()

        # Aggiunto al dizionario di classe
        type(self).__all_objects_by_nome[nome] = self

    # INFO: ASSOCIAZIONI DOPPIE

    def _add_post_cat(self, link: post_cat):
        DataValidator._require_valid_link(link, post_cat)
        if (
            not isinstance(link, post_cat)
            or not link._get_is_valid()
            or link._get_categoria() is not self
        ):
            raise InvalidLinkException("post_cat")
        if link in self.__set_post_links:
            raise AlreadyExistingLinkException(
                "post_cat", "La categorai ha già questo post"
            )
        self.__set_post_links.add(link)

    def _remove_post_cat(self, link: post_cat):
      self.__set_post_links.discard(link)

    # INFO: UTILITIES
    def __hash__(self):
        return hash(self.__nome)

    def __eq__(self, other: object):
        if type(self) is not type(other):
            return False
        if hash(self) != hash(other):
            return False
        if type(other) == Categoria:
            return self.__nome == other.__nome
        return False

    def __repr__(self):
        return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self):
        return f"{self.get_nome()}"
