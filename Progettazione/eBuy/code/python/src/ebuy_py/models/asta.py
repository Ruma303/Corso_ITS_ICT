from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from src.ebuy_py.associations.bid import bid
from src.ebuy_py.datatypes.datatypes import Float_GZ, TimeDelta_GZ
from src.ebuy_py.exceptions.exceptions import (
    ConstraintViolationException,
    NoneTypeException,
    TypeInvalidException,
)
from src.ebuy_py.models.post import Post

if TYPE_CHECKING:
    from src.ebuy_py.datatypes.datatypes import Condizione, Float_GEZ, StatoPost
    from src.ebuy_py.models.categoria import Categoria
    from src.ebuy_py.models.met_pag import MetodoPagamento
    from src.ebuy_py.models.utente import Utente
    from src.ebuy_py.models.valuta import Valuta


class Asta(Post):
    """Crea un Post di tipo Asta"""  
  
    # INFO: CLASSMETHODS

    # INFO: CONSTRUCTORS
    # INFO: Implementa il costruttore astratto Post
    def __init__(
        self,
        istante_pubbl: datetime,
        descrizione: str,
        prezzo: Float_GEZ,  # prezzo iniziale d'asta
        stato: StatoPost,
        categoria: Categoria,  # 1..1
        valuta: Valuta,  # 1..1
        metodi_pagamento: set[MetodoPagamento],  # 1..*
        venditore: Utente,
        rialzo: Float_GZ,
        durata: TimeDelta_GZ,
        condizione: Condizione | None = None,
    ):
        # Prima gli attributi propri per evitare link fantasma
        self.__set_rialzo(rialzo)
        self.__set_durata(durata)

        self.__set_bid_links: set[bid] = set()

        # Poi attributi generici di Post e creazione associazioni
        # Così si evitano link fantasma
        super().__init__(
            istante_pubbl,
            descrizione,
            prezzo,
            stato,
            categoria,
            valuta,
            metodi_pagamento,
            venditore,
            condizione,
        )

    # INFO: SETTERS
    def __set_rialzo(self, rialzo: Float_GZ):
        if not rialzo:
            raise NoneTypeException("Float_GZ")
        if not isinstance(rialzo, Float_GZ):
            raise TypeInvalidException("Float_GZ")
        self.__rialzo = rialzo

    def __set_durata(self, durata: TimeDelta_GZ):
        if not durata:
            raise NoneTypeException("TimeDelta_GZ")
        if not isinstance(durata, TimeDelta_GZ):
            raise TypeInvalidException("TimeDelta_GZ")
        self.__durata = durata

    # INFO: GETTERS
    def get_rialzo(self):
        return self.__rialzo

    def get_durata(self):
        return self.__durata

    def get_numero_rialzi(self):
        return len(self.__set_bid_links)

    # INFO: ASSOCIATIONS
    # TODO: attendere il prof prima di implementare
    def create_bid(self, acquirente: Utente): ...

    # INFO: OPERATIONS
    def _scadenza(self) -> datetime:
        return self.get_istante_pubbl() + self.__durata

    def _prezzo_finale(self):
        """Prezzo del bid aggiudicatario; None se l'asta si chiude senza bid.

        pre: l'asta è conclusa (now >= scadenza).
        Query pura: non modifica nulla.
        """
        if type(self) != Asta:
            raise TypeError("L'istanza dev'essere obbligatoriamente un'Asta")
        if datetime.now() < self._scadenza():
            raise ValueError("L'asta non è ancora conclusa")
        if self.__prezzo < 0:
            raise ValueError("Il prezzo non può essere negativo")
        if self.__rialzo < 0:
            raise ValueError("Il rialzo non può essere negativo")
        if self.get_numero_rialzi() == 0:
            return None

        return Float_GEZ(self.get_prezzo() + self.__rialzo * self.get_numero_rialzi())

    # INFO: UTILITIES

    def __repr__(self):
        return (
            super().__repr__()
            + f"rialzo: {self.get_rialzo()} | "
            + f"durata: {self.get_durata()}"
        )

    def __str__(self):
        return super().__str__() + f" | {self.get_rialzo()} | {self.get_durata()}"
