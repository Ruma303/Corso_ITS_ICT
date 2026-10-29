from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Self

# from src.ebuy_py.associations.post_cat import post_cat
from src.ebuy_py.associations.post_cat import post_cat
from src.ebuy_py.associations.pubblica import pubblica
from src.ebuy_py.datatypes.datatypes import Condizione, Float_GEZ, StatoPost
from src.ebuy_py.datatypes.validators import DataValidator
from src.ebuy_py.exceptions.exceptions import (
    AlreadyExistingLinkException,
    ConstraintViolationException,
    InvalidLinkException,
)
from src.ebuy_py.models import met_pag
from src.ebuy_py.models.categoria import Categoria
from src.ebuy_py.models.met_pag import MetodoPagamento
from src.ebuy_py.models.utente import Utente
from src.ebuy_py.models.valuta import Valuta

"""
I post non hanno un identificatore. Possono avere esattamente gli stessi valori negli attributi, ma tramite l'uso di "is" oppure "==", lasciamo l'implementazione di default che verifica l'indirizzo di memoria per capire se due post identici, sono in realtà oggetti diversi con locazioni differenti.
"""


class Post(ABC):
    __set_objects: set[Self] = set()

    # INFO: CLASSMETHODS
    @classmethod
    def get_all_posts(cls):
        return frozenset(cls.__set_objects)

    # INFO: CONSTRUCTORS
    @abstractmethod
    def __init__(
        self,
        istante_pubbl: datetime,
        descrizione: str,
        prezzo: Float_GEZ,
        stato: StatoPost,
        categoria: Categoria,  # 1..1
        valuta: Valuta,  # 1..1
        # NB: Si potrebbe anche inserire un singolo met_pag e aggiungerli manualmente
        metodi_pagamento: set[MetodoPagamento],  # 1..*
        venditore: Utente,  # 1..1
        condizione: Condizione | None = None,  # 0..1
    ):
        self.__set_istante_pubbl(istante_pubbl)
        self.set_descrizione(descrizione)  # pubblico
        self.__set_prezzo(prezzo)
        self.__set_stato(stato)

        # Aggregazioni
        if self.get_stato() == StatoPost.USATO and condizione is not None:
            self.__set_condizione(condizione)
        self.__set_valuta(valuta)
        self.__metodi_pagamento: set[MetodoPagamento] = (
            set()
        )  # set privato di metodi di pagamento
        self.add_metodi_pagamento(metodi_pagamento)  # 1..*
        post_cat._create(self, categoria)  # 1..1 <imm>

        # Inizializzazione Riferimenti Associazioni Doppie
        self.__post_cat_link: post_cat | None = None
        self.__categoria: Categoria | None = None
        self.__pubblica_link: pubblica | None = None
        self.__pubblicato_da: Utente | None = None

        # Creazione Link Immutabile post_cat (1..1)
        post_cat._create(self, categoria)

        # Creazione Link Immutabile pubblica (1..1)
        pubblica._create(venditore, self)

        # Registrazione dell'istanza
        type(self).__set_objects.add(self)

    # INFO: SETTERS
    def __set_istante_pubbl(self, istante_pubbl: datetime):
        if not istante_pubbl:
            raise ValueError("L'istante di pubblicazione non può essere vuoto")
        if not isinstance(istante_pubbl, datetime):
            raise TypeError(
                f"Il valore dev'essere di tipo datetime. Ora è '{type(istante_pubbl).__name__}'"
            )
        self.__istante_pubbl = istante_pubbl

    def __set_prezzo(self, prezzo: Float_GEZ):
        if prezzo is None:
            raise ValueError("Il prezzo non può essere vuoto")
        if not isinstance(prezzo, Float_GEZ):
            raise TypeError(
                f"Il valore dev'essere di tipo Float_GEZ. Ora è '{type(prezzo).__name__}'"
            )
        self.__prezzo = prezzo

    # pubblico per consentire la modifica in quanto non <<imm>>
    def set_descrizione(self, desc: str):
        if not desc:
            raise ValueError("La descrizione non può essere vuota")
        if not isinstance(desc, str):
            raise TypeError(
                f"Il valore dev'essere di tipo str. Ora è '{type(desc).__name__}'"
            )
        self.__descrizione = desc

    def __set_stato(self, stato: StatoPost):
        DataValidator._require_type(stato, StatoPost)
        self.__stato = stato

    def __set_condizione(self, condizione: Condizione):
        if self.__stato == StatoPost.USATO:
            if condizione is None:
                raise ValueError("Per un oggetto usato la condizione è obbligatoria")
            DataValidator._require_type(condizione, Condizione)
        elif condizione is not None:
            raise ValueError("Solo gli oggetti usati hanno una condizone")
        self.__condizione = condizione

    def __set_valuta(self, valuta: Valuta):
        DataValidator._require_type(valuta, Valuta)
        self.__valuta = valuta

    # Usato in aggregazione
    # def __set_categoria(self, categoria: Categoria):
    #     DataValidator._require_type(categoria, Categoria)
    #     self.__categoria = categoria

    # INFO: GETTERS
    def get_istante_pubbl(self):
        return self.__istante_pubbl

    def get_descrizione(self):
        return self.__descrizione

    def get_prezzo(self):
        return self.__prezzo

    def get_stato(self):
        return self.__stato

    def get_categoria(self):
        return self.__categoria

    def get_condizione(self):
        return self.__condizione

    def get_valuta(self):
        return self.__valuta

    def get_metodi_pagamento(self):
        return frozenset(self.__metodi_pagamento)

    def has_metodo_pagamento(self, m: MetodoPagamento) -> bool:
        return m in self.get_metodi_pagamento()

    def get_pubblicato_da(self):
        return self.__pubblicato_da

    # INFO: AGGREGAZIONI
    def add_metodi_pagamento(self, met_pags: set[MetodoPagamento]):
        DataValidator._require_type(met_pag, (set, frozenset))
        if not met_pags:
            raise ValueError(
                "I metodi di pagamento da aggiungere non possono essere vuoti"
            )
        for met in met_pags:
            DataValidator._require_type(met, MetodoPagamento)
        # Aggiunta / aggiornamento dei set
        self.__metodi_pagamento |= set(met_pags)

    def remove_metodo_pagamento(self, met_pag: MetodoPagamento):
        DataValidator._require_type(met_pag, MetodoPagamento)
        if met_pag not in self.__metodi_pagamento:
            raise KeyError("Il metodo di pagamento non è presente")
        # IMPORTANT: vincolo 1..*
        if len(self.__metodi_pagamento) <= 1:
            raise ConstraintViolationException(
                "1..*", "Almeno un metodo di pagamento richiesto"
            )
        self.__metodi_pagamento.remove(met_pag)

    # INFO: ASSOCIAZIONI DOPPIE

    # Post -- pubblica -- 1..1 Utente
    def _set_pubblica_link(self, link: pubblica):
        if (
            not isinstance(link, pubblica)
            or not link._get_is_valid()
            or link._get_post() is not self
        ):
            raise InvalidLinkException("pubblica")
        if self.__pubblica_link is not None:
            raise AlreadyExistingLinkException("pubblica", "Il post ha già un autore")
        self.__pubblica_link = link  # assegna l'associazione
        self.__pubblicato_da = link._get_utente()  # ottiene l'autore

    def _set_post_cat(self, link: post_cat):
        DataValidator._require_valid_link(link, post_cat)
        if (
            not isinstance(link, post_cat)
            or not link._get_is_valid()
            or link._get_post() is not self
        ):
            raise InvalidLinkException("post_cat")
        self.__post_cat_link = link
        self.__categoria = link._get_categoria()  # La categoria 1..1

    def _remove_post_cat(self, link: post_cat):
        if self.__post_cat_link is link:
            self.__post_cat_link = None
            self.__categoria = None

    # INFO: UTILITIES
    def __repr__(self):
        desc = (
            self.get_descrizione()[:10] + "..."
            if len(self.get_descrizione()) > 10
            else self.get_descrizione()
        )

        return f"[{type(self).__name__}] pubblicato: {self.get_istante_pubbl()} | prezzo:  {self.get_prezzo()}€\ndescrizione: {desc} "

    def __str__(self):
        desc = (
            self.get_descrizione()[:10] + "..."
            if len(self.get_descrizione()) > 10
            else self.get_descrizione()
        )
        return f"{self.get_istante_pubbl()} | {self.get_prezzo()}€ | {desc}"
