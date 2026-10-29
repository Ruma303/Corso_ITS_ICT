from __future__ import annotations

from typing import TYPE_CHECKING

from src.ebuy_py.exceptions.exceptions import InvalidLinkException

if TYPE_CHECKING:  # evita l'import circolare a runtime
    from src.ebuy_py.models.post import Post
    from src.ebuy_py.models.utente import Utente


class pubblica:
    """Crea un link immutabile Utente 1..1 -- pubblica -- 0..* Post, o meglio, le sue sottoclassi."""

    # INFO: CLASSMETHODS
    @classmethod
    def _create(cls, u: Utente, p: Post) -> pubblica:
        link = cls(u, p)
        p._set_pubblica_link(link)
        u._add_pubblica_link(link)
        return link

    @classmethod
    def _remove(cls, link: pubblica) -> None:
        if not link._get_is_valid():
            raise InvalidLinkException("pubblica")
        # link._get_utente()._remove_pubblica_link(link)
        # link._get_post()._remove_pubblica_link(link) # rimuovere perchè 1..1
        link.__is_valid = False
        link.__utente = None
        link.__post = None

    # INFO: GETTERS
    def _get_utente(self) -> Utente:
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return self.__utente

    def _get_post(self) -> Post:
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return self.__post

    def _get_is_valid(self) -> bool:
        return self.__is_valid

    # INFO: CONSTRUCTORS
    def __init__(self, u: Utente, p: Post):
        self.__utente = u
        self.__post = p
        self.__is_valid = True # Da utilizzare in tutti i metodi di istanza
    
    def __hash__(self):
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return hash((self.__utente, self.__post))

    def __eq__(self, other: object):
        if not isinstance(other, pubblica):
            return False
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return self.__utente == other.__utente and self.__post == other.__post

    def __repr__(self):
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return f"[{type(self).__name__}] post: {self._get_post()} | utente :  {self._get_utente()}"

    def __str__(self):
        if not self._get_is_valid():
            raise InvalidLinkException("pubblica")
        return f"{self._get_post()} | {self._get_utente()}"
