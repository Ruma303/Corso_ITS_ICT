from abc import ABC
from datetime import datetime
from typing import TYPE_CHECKING, Self

from src.python_code.exceptions.exceptions import InvalidLinkException

if TYPE_CHECKING:
    from python_code.models.categoria import Categoria
    from python_code.models.datatypes import Condizione, Float_GEZ, StatoPost
    from src.python_code.associations.post_cat import post_cat
    from src.python_code.associations.pubblica import pubblica
    from src.python_code.models.met_pag import MetodoPagamento
    from src.python_code.models.utente import Utente
    from src.python_code.models.valuta import Valuta


# TODO: questa è una classe astratta. Alcuni metodi vanno resi astratti (anche quelli statici)


class Post(ABC):
    # TODO: come si identificano i post?
    __all_objects_by_TODO: dict = dict()  # come li identifico?
    __set_objects: set[Self] = set()
    __all_post_cat_links: set[post_cat] = set()  # Set di associazioni post_cat
    __all_pubblica_links: set[pubblica] = set()  # Set di associazioni pubblica

    # INFO: CLASSMETHODS
    @classmethod
    def get_all_posts(cls):
        return cls.__set_objects

    @classmethod
    def get_pubblica_links(cls):
        return frozenset(cls.__all_pubblica_links)

    # INFO: SETTERS
    def __set_istante_pubbl(self, istante_pubbl: datetime):
        if not datetime:
            raise ValueError("L'istante di pubblicazione non può essere vuoto")
        if not isinstance(istante_pubbl, datetime):
            raise TypeError(
                f"Il valore dev'essere di tipo datetime. Ora è '{type(istante_pubbl).__name__}'"
            )
        self.__istante_pubbl = istante_pubbl

    def __set_prezzo(self, prezzo: Float_GEZ):
        if not prezzo:
            raise ValueError("Il prezzo non può essere vuoto")
        if not isinstance(prezzo, Float_GEZ):
            raise TypeError(
                f"Il valore dev'essere di tipo Float_GEZ. Ora è '{type(prezzo).__name__}'"
            )
        self.__prezzo = prezzo

    # pubblico per consentire la modifica in quanto non  <<imm>>
    def set_descrizione(self, desc: str):
        if not desc:
            raise ValueError("La descrizione non può essere vuota")
        if not isinstance(desc, str):
            raise TypeError(
                f"Il valore dev'essere di tipo str. Ora è '{type(desc).__name__}'"
            )
        self.__descrizione = desc

    # Aggiunge un insieme (set) di metodi di pagamento
    def add_metodi_pagamento(self, met_pags: set[MetodoPagamento]):
        if not met_pags:
            raise ValueError(
                "I metodi di pagamento da aggiungere non possono essere vuoti"
            )
        for met in met_pags:
            if not met:
                raise ValueError("Il metodo di pagamento non può essere vuoto")
            if not isinstance(met, MetodoPagamento):
                raise TypeError(
                    f"Il valore dev'essere di tipo MetodoPagamento. Ora è '{type(met_pags).__name__}'"
                )
            if met in self.get_metodi_pagamento():
                print(f"Il metodo di pagamento '{met}' già è presente. Verrà ignorato")

            self.__metodi_pagamento.add(met)

    # Rimuove un singolo metodo di pagamento
    def remove_metodo_pagamento(self, met_pag: MetodoPagamento):
        if not met_pag or type(met_pag) != MetodoPagamento:
            raise TypeError(
                f"Il valore dev'essere di tipo MetodoPagamento. Ora è '{type(met_pag).__name__}'"
            )
        # IMPORTANT: vincolo 1..*
        if len(self.__metodi_pagamento) <= 1:
            raise ValueError("Almeno un metodo di pagamento richiesto")

        self.__metodi_pagamento = {m for m in self.__metodi_pagamento if m != met_pag}

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

    def get_valuta(self):
        return self.__valuta

    def get_metodi_pagamento(self):
        return self.__metodi_pagamento

    def get_pubblica_link(self):
        return self.__set_pubblica_links

    def get_pubblicato_da(self):
        return self.__pubblicato_da

    def get_post_cat_links(self):
        return self.__all_post_cat_links

    # INFO: ASSOCIATIONS
    # IMPORTANT: INTERFACCIA PUBBLICA
    def create_post_cat(self, categoria: Categoria):
        if not categoria or not isinstance(categoria, Categoria):
            raise TypeError("Il valore passato non è una Categoria")
        link = post_cat._create(self, categoria)
        if link in self.get_post_cat_links():
            post_cat._remove(link)  # Rimozione SINGOLA associazione pre-esistente
        post_cat._create(self, categoria)  # Aggiunta SINGOLA associazione

    def _set_post_cat(self, link: post_cat):
        if not link or not link._get_is_valid() or not isinstance(link, post_cat):
            raise InvalidLinkException("post_cat")
        if link in self.get_post_cat_links():
            raise KeyError(
                f"Questa associazione '{type(link).__name__}' già è presente"
            )  # Eliminare o lanciare eccezione?
        # Aggiunta al set di post_cat dell'intera classe
        type(self).__all_post_cat_links.add(link)
        self.__categoria = (
            link._get_categoria()
        )  # Assegna la categoria prendendola dall'associazione

    def _remove_post_cat(self, link: post_cat):
        if not link or not link._get_is_valid() or not isinstance(link, post_cat):
            raise InvalidLinkException("post_cat")
        if link in self.get_post_cat_links():
            # Eliminare l'associazione ricreando il set senza il link
            type(self).__all_post_cat_links = {
                x for x in self.get_post_cat_links() if x != link
            }
            self.__categoria = None
        else:
            raise KeyError(
                f"Questa associazione '{type(link).__name__}' non è presente"
            )

    def create_pubblica(self, utente: Utente):
        if not utente or not isinstance(utente, Utente):
            raise TypeError("Il valore passato non è una Utente")
        if self.__pubblica_link is not None:
            pubblica._remove(self.__pubblica_link)
        pubblica._create(utente, self)

    def _set_pubblica(self, link: pubblica):
        if not link or not link._get_is_valid() or not isinstance(link, pubblica):
            raise InvalidLinkException("pubblica")
        if self.__pubblica_link is not None:
            raise KeyError("Il post ha già un autore: rimuovere prima il vecchio link")
        Post.__all_pubblica_links.add(link)
        self.__pubblica_link = link  # assegna l'associazione
        self.__pubblicato_da = link._get_utente()  # ottiene l'autore

    def _remove_pubblica(self, link: pubblica):
        if not link or not link._get_is_valid() or not isinstance(link, pubblica):
            raise InvalidLinkException("pubblica")
        if link != self.__pubblica_link:
            raise KeyError("Questa associazione non è presente")
        Post.__all_pubblica_links.discard(link)
        self.__pubblica_link = None  # rimuove l'associazione
        self.__pubblicato_da = None  # rimuove direttamente l'autore

    # INFO: CONSTRUCTORS
    # IMPORTANT: Al momento non ho un campo univoco {id}.
    # Ignorare le operazioni che lo richiedono
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
        # condizione: Condizione | None
    ):
        self.__istante_pubbl = None
        self.__descrizione = None
        self.__prezzo = None
        self.__stato = stato
        # self.__categoria = categoria # Aggiungere l'associazione post_cat invece
        self.__valuta = valuta
        self.__metodi_pagamento = set()  # set privato di metodi di pagamento
        self.add_metodi_pagamento(metodi_pagamento)  # aggiunta obbligatoria 1..*

        self.__set_pubblica_links = set()
        self.__pubblica_link = None
        self.__pubblicato_da = None
        self.create_pubblica(venditore)  # 1..1

    # INFO: UTILITIES
    # IMPORTANT: al momento non è ancora stato definito come identificare univocamente i Post
    # def __hash__(self):
    #   return hash((self._get_utente(), self._get_post()))

    # def __eq__(self, other: object):
    #   if other is None or type(self) != type(other):
    #     return False
    #   if hash(self) != hash(other):
    #     return False
    #   return (self._post == other._post) and (self._utente == other._utente)

    def __repr__(self):
        return f"[{type(self).__name__}] pubblicato: {self.get_istante_pubbl()} | prezzo:  {self.get_prezzo()}\ndescrizione: {self.get_descrizione()} "

    def __str__(self):
        return f"{self.get_istante_pubbl()} | {self.get_prezzo()} | {self.get_descrizione()}"
