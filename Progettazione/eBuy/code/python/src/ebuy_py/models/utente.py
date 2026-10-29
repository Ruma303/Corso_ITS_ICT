from __future__ import annotations

from abc import ABC, abstractmethod
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


# TODO: forse non sarà una classe astratta


class Utente:
    __all_objects_by_nome: dict[str, Self] = dict()
    __all_pubblica_links: set[pubblica] = (
        set()
    )  # insieme di post pubblicati tramite l'associazione "pubblica"

    # INFO: CLASSMETHODS
    @classmethod
    def get_all_objects(cls):
      return cls.__all_objects_by_nome

    @classmethod
    def get_set_name_objects(cls):
      return frozenset({l for l in cls.__all_objects_by_nome.values()})
    
    @classmethod
    def get_by_nome(cls, nome: str):
        return cls.__all_objects_by_nome.get(nome)

    @classmethod
    def get_all_pubblica_links(cls):
        return frozenset(cls.__all_pubblica_links)

    # INFO: CONSTRUCTORS
    # @abstractmethod
    def __init__(self, nomeutente: str, registrazione: datetime):
        self.__nome = None
        self.__registrazione = None
        self.__pubblica_links: set[pubblica] = set()
        self.__set_registrazione(registrazione)
        self.__set_nome(nomeutente)

    # INFO: SETTERS
    def __set_nome(self, nome: str):
        DataValidator._require_type(nome, str)
        nome = nome.strip()
        if not nome:
            raise ValueError("Il nome non può essere vuoto")
        if nome in type(self).__all_objects_by_nome:
            raise KeyError("Questo nome già esiste")
        self.__nome = nome
        type(self).__all_objects_by_nome[nome] = self

    def __set_registrazione(self, registrazione: datetime):
        DataValidator._require_type(registrazione, datetime)
        self.__registrazione = registrazione

    # INFO: GETTERS
    def get_nome(self):
        return self.__nome

    def get_registrazione(self):
        return self.__registrazione

    def get_post_pubblicati(self):
        return frozenset(l._get_post() for l in self.__pubblica_links)

    # INFO: ASSOCIATIONS

    def _add_pubblica_link(self, link: pubblica):
        if (
            not link
            or not isinstance(link, pubblica)
            or not link._get_is_valid()
            or link._get_utente() is not self
        ):
            raise InvalidLinkException("pubblica")
        if link._get_utente() is not self:
            raise NotSelfLinkException(link)
        if link in self.__pubblica_links:
            raise AlreadyExistingLinkException(
                "pubblica", "Questa associazione già è presente"
            )
        self.__pubblica_links.add(link)
        type(self).__all_pubblica_links.add(link)

    # INFO: USE-CASE
    # TODO: in futuro andranno spostati in un service layer

    def search_by_categoria(self, c: Categoria):
        DataValidator._require_type(c, Categoria)
        results = set()

        for link in self.__pubblica_links:
            post = link._get_post()
            if post.get_categoria() == c:
                results.add(post)

        return frozenset(results)

    @staticmethod
    def search(
        c: Categoria, inizio: Float_GEZ, fine: Float_GEZ, met_pag: MetodoPagamento, valuta: Valuta
    ):
        """
        Trova tutti i post da una categoria, in un certo range di prezzo, con un determinato metodo di pagamento

        param: c: Categoria
        param: inizio: Float_GEZ
        param: fine: Float_GEZ
        param: m: MetodoPagamento
        param: v: Valuta
        """
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
                and post.get_valuta() == met_pag
            ):
                results.add(post)
        return frozenset(results)

    # INFO: UTILITIES
    def __hash__(self):
        return hash(self.__nome)

    def __eq__(self, other: object):
        if not other or type(self) != type(other):
            return False
        if isinstance(other, Utente):
            return (self.__nome == other.__nome) and (
                self.__registrazione == other.__registrazione
            )
        return False

    def __repr__(self):
        return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self):
        return f"{self.get_nome()}"
