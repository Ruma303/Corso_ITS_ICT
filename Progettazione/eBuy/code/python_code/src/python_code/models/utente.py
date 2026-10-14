from abc import ABC
from datetime import datetime
from typing import TYPE_CHECKING, Self

from src.python_code.models.exceptions import InvalidLinkException, TypeInvalidException

if TYPE_CHECKING:
    from src.python_code.associations.pubblica import pubblica
    from src.python_code.models.post import Post


class Utente(ABC):
    __all_objects_by_nome: dict[str, Self] = dict()
    __all_pubblica_links: set[pubblica] = set()

    # INFO: CLASSMETHODS
    @classmethod
    def get_by_nome(cls, nome: str):
        return cls.__all_objects_by_nome.get(nome)

    @classmethod
    def get_all_pubblica(cls):
        return cls.__all_pubblica_links

    # INFO: SETTERS
    def __set_nome(self, nome: str):
        if not nome:
            raise ValueError("Il nome non può essere vuoto")
        if not isinstance(nome, str):
            raise TypeError(
                f"Il valore dev'essere di tipo str. Ora è '{type(nome).__name__}'"
            )
        nome = nome.strip()
        if nome == self.__nome:
            return

        registry = type(self).__all_objects_by_nome
        if nome in registry:
            raise KeyError("Questo nome già esiste")

        if self.__nome is not None:
            del registry[self.__nome]
        self.__nome = nome
        registry[nome] = self

    def __set_registrazione(self, registrazione: datetime):
        if not isinstance(registrazione, datetime):
            raise TypeError(
                f"Il valore dev'essere di tipo datetime. Ora è '{type(registrazione).__name__}'"
            )
        if not registrazione:
            raise ValueError("La data di registrazione non può essere vuota")

        self.__registrazione = registrazione

    # INFO: GETTERS
    def get_nome(self):
        return self.__nome

    def get_registrazione(self):
        return self.__registrazione

    def get_post_pubblicati(self):
        return frozenset(l._get_post() for l in self.__pubblica_links)

    # INFO: ASSOCIATIONS

    def create_pubblica(self, p: Post):
        """L'interfaccia pubblica per creare l'associazione 'pubblica'
        si trova in Post. Questo è un metodo che richiama quell'interfaccia
        """
        if not p or not isinstance(p, Post):
            raise TypeInvalidException('Post')
        p.create_pubblica(self)

    def _add_pubblica(self, link: pubblica):
        if not link or not isinstance(link, pubblica) or not link.__is_valid:
            raise InvalidLinkException('pubblica')
        if link in self.__pubblica_links:
            raise KeyError(
                "Questa associazione già è presente"
            )
        type(self).__all_pubblica_links.add(link)
        self.__pubblica_links.add(link)

    def _remove_pubblica(self, link: pubblica):
        if not link or not isinstance(link, pubblica) or not link.__is_valid:
            raise InvalidLinkException('pubblica')
        if link not in self.__pubblica_links:
          raise KeyError("Questa associazione non è presente")
        self.__pubblica_links.discard(link)
        type(self).__all_pubblica_links.add(link)

    # INFO: CONSTRUCTORS
    def __init__(self, nome: str, registrazione: datetime):
        self.__nome = None
        self.__registrazione = None
        self.__set_nome(nome)
        self.__set_registrazione(registrazione)
        self.__pubblica_links = set()

    # INFO: UTILITIES
    def __hash__(self):
        return hash(self.__nome)

    def __eq__(self, other: object):
        if not other or type(self) != type(other):
            return False
        if isinstance(other, Utente):
          return (self.__nome == other.__nome) and (
            self.__registrazione == other.__registrazione)
        return False

    def __repr__(self):
        return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self):
        return f"{self.get_nome()}"
