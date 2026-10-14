from __future__ import annotations

from typing import TYPE_CHECKING

from src.python_code.exceptions.exceptions import InvalidLinkException

if TYPE_CHECKING:  # evita l'import circolare a runtime
    from python_code.models.post import Post
    from python_code.models.utente import Utente


class pubblica:
    """Crea un link immutabile Utente 1..1 -- pubblica -- 0..* Post."""

    # INFO: CLASSMETHODS
    @classmethod
    def _create(cls, u: Utente, p: Post) -> pubblica:
        link = cls(u, p)
        u._add_pubblica(link)
        p._set_pubblica(link)
        return link

    @classmethod
    def _remove(cls, link: pubblica) -> None:
        if not link._get_is_valid():
            raise InvalidLinkException("pubblica")
        link._get_utente()._remove_pubblica(link)
        link._get_post()._remove_pubblica(link)
        link.__is_valid = False
        link.__utente = None
        link.__post = None

    # INFO: GETTERS
    def _get_utente(self) -> Utente:
        return self.__utente

    def _get_post(self) -> Post:
        return self.__post

    def _get_is_valid(self) -> bool:
        return self.__is_valid

    # INFO: CONSTRUCTORS
    def __init__(self, u: Utente, p: Post):
        self.__utente = u
        self.__post = p
        self.__is_valid = True

    # INFO: UTILITIES
    def __hash__(self):
        return hash((self.__utente, self.__post))

    def __eq__(self, other: object):
        if not isinstance(other, pubblica):
            return False
        return self.__utente == other.__utente and self.__post == other.__post

    def __repr__(self):
        return f"[{type(self).__name__}] post: {self._get_post()} | utente :  {self._get_utente()}"

    def __str__(self):
        return f"{self._get_post()} | {self._get_utente()}"
