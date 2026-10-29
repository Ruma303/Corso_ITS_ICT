from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from src.ebuy_py.models.post import Post

if TYPE_CHECKING:
    from src.ebuy_py.datatypes.datatypes import Condizione, Float_GEZ, StatoPost
    from src.ebuy_py.models.categoria import Categoria
    from src.ebuy_py.models.met_pag import MetodoPagamento
    from src.ebuy_py.models.utente import Utente
    from src.ebuy_py.models.valuta import Valuta


class CompraloSubito(Post):
    """Crea un Post di tipo CompraloSubito"""  

    # INFO: CLASSMETHODS

    # INFO: CONSTRUCTORS
    # INFO: Implementa il costruttore astratto Post
    def __init__(
        self,
        istante_pubbl: datetime,
        descrizione: str,
        prezzo: Float_GEZ,
        stato: StatoPost,
        categoria: Categoria,  # 1..1
        valuta: Valuta,  # 1..1
        metodi_pagamento: set[MetodoPagamento],  # 1..*
        venditore: Utente,
        condizione: Condizione | None = None,
    ):
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
