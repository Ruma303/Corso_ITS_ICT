from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Self

from src.ebuy_py.associations.pubblica import pubblica
from src.ebuy_py.datatypes.datatypes import Float_GEZ
from src.ebuy_py.datatypes.validators import DataValidator
from src.ebuy_py.exceptions.exceptions import (
    AlreadyExistingLinkException,
    InvalidLinkException,
    NotSelfLinkException,
)
from src.ebuy_py.models.categoria import Categoria
from src.ebuy_py.models.met_pag import MetodoPagamento
from src.ebuy_py.models.valuta import Valuta

if TYPE_CHECKING:
    from src.ebuy_py.models.post import Post


class Utente:
    __all_objects_by_nome: dict[str, Self] = dict()
    __all_pubblica_links: set[pubblica] = set()

    # INFO: CLASSMETHODS
    @classmethod
    def get_all_objects(cls) -> dict[str, Self]:
        return cls.__all_objects_by_nome

    @classmethod
    def get_set_name_objects(cls) -> frozenset[Self]:
        return frozenset(cls.__all_objects_by_nome.values())
    
    @classmethod
    def get_by_nome(cls, nome: str) -> Self | None:
        return cls.__all_objects_by_nome.get(nome)

    @classmethod
    def get_all_pubblica_links(cls) -> frozenset[pubblica]:
        return frozenset(cls.__all_pubblica_links)

    @classmethod
    def _clear_registry(cls) -> None:
        """Solo per i test."""
        cls.__all_objects_by_nome.clear()
        cls.__all_pubblica_links.clear()

    # INFO: CONSTRUCTORS
    def __init__(self, nomeutente: str, registrazione: datetime):
        self.__nome: str | None = None
        self.__registrazione: datetime | None = None
        self.__pubblica_links: set[pubblica] = set()
        self.__set_registrazione(registrazione)
        self.__set_nome(nomeutente)

    # INFO: SETTERS
    def __set_nome(self, nome: str) -> None:
        DataValidator._require_type(nome, str)
        nome = nome.strip()
        if not nome:
            raise ValueError("Il nome non può essere vuoto")
        if nome in type(self).__all_objects_by_nome:
            raise KeyError("Questo nome già esiste")
        self.__nome = nome
        type(self).__all_objects_by_nome[nome] = self

    def __set_registrazione(self, registrazione: datetime) -> None:
        DataValidator._require_type(registrazione, datetime)
        self.__registrazione = registrazione

    # INFO: GETTERS
    def get_nome(self) -> str | None:
        return self.__nome

    def get_registrazione(self) -> datetime | None:
        return self.__registrazione

    def get_post_pubblicati(self) -> frozenset[Post]:
        return frozenset(link._get_post() for link in self.__pubblica_links if link._get_is_valid())

    # INFO: ASSOCIATIONS

    def _add_pubblica_link(self, link: pubblica) -> None:
        DataValidator._require_valid_link(link, pubblica)
        if link._get_utente() is not self:
            raise NotSelfLinkException(link)
        if link in self.__pubblica_links:
            raise AlreadyExistingLinkException(
                "pubblica", "Questa associazione già è presente"
            )
        self.__pubblica_links.add(link)
        type(self).__all_pubblica_links.add(link)

    def _remove_pubblica_link(self, link: pubblica) -> None:
        self.__pubblica_links.discard(link)
        type(self).__all_pubblica_links.discard(link)

    # INFO: USE-CASE
    def search_by_categoria(self, c: Categoria) -> frozenset[Post]:
        DataValidator._require_type(c, Categoria)
        results = set()

        for link in self.__pubblica_links:
            if link._get_is_valid():
                post = link._get_post()
                if post.get_categoria() == c:
                    results.add(post)

        return frozenset(results)

    @staticmethod
    def search(
        c: Categoria, inizio: Float_GEZ, fine: Float_GEZ, met_pag: MetodoPagamento, valuta: Valuta
    ) -> frozenset[Post]:
        """Trova tutti i post da una categoria, in un certo range di prezzo, con un determinato metodo di pagamento."""
        from src.ebuy_py.models.post import Post  # import locale

        DataValidator._require_type(c, Categoria)
        DataValidator._require_type(inizio, Float_GEZ)
        DataValidator._require_type(fine, Float_GEZ)
        DataValidator._require_type(met_pag, MetodoPagamento)
        DataValidator._require_type(valuta, Valuta)

        if inizio > fine:
            raise ValueError("L'inizio del range non può superare la fine")

        results = set()

        for post in Post.get_all_posts():
            if (
                post.get_categoria() == c
                and inizio <= post.get_prezzo()
                and post.get_prezzo() <= fine
                and post.has_metodo_pagamento(met_pag)
                and post.get_valuta() == valuta
            ):
                results.add(post)
        return frozenset(results)

    # INFO: UTILITIES
    def __hash__(self) -> int:
        return hash(self.__nome)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Utente):
            return False
        return (self.__nome == other.__nome) and (
            self.__registrazione == other.__registrazione
        )

    def __repr__(self) -> str:
        return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self) -> str:
        return f"{self.get_nome()}"