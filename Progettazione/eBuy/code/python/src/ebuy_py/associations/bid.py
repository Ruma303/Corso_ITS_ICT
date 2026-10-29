from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from src.ebuy_py.exceptions.exceptions import InvalidLinkException

if TYPE_CHECKING:
    from src.ebuy_py.models.post import Post
    from src.ebuy_py.models.utente import Utente


class bid:
    """Crea un link immutabile Venditore 1..1 -- bid -- 0..* Asta."""

    @classmethod
    def _create(cls, p: Post, c: Utente):
        link = cls(p, c)
        p._set_bid(link)
        c._add_bid(link)
        return link

    @classmethod
    def _remove(cls, link: bid):
        if not link._get_is_valid():
            raise InvalidLinkException("bid")
        link._get_post()._remove_bid(link)
        link._get_bid()._remove_bid(link)
        link.__post = None
        link.__bid = None
        link.__is_valid = False

    # INFO: CONSTRUCTORS

    def __init__(self, p: Post, c: Utente):
        self.__set_post(p)
        self.__set_bid(c)
        self.__istante_pubbl = datetime.now() # Certamente Noto alla nascita <N.a.n>
        self.__is_valid = True

    # INFO: UTILITIES

    def __hash__(self):
        return hash((self.__post, self.__bid))

    def __eq__(self, other: object):
        if not other or type(self) != type(other):
            return False
        if hash(self) != hash(other):
            return False
        if type(other) == bid:
            return (self.__post == other.__post) and (self.__bid == other.__bid)
        return False

    # INFO: GETTERS

    def _get_post(self):
        return self.__post

    def _get_bid(self):
        return self.__bid

    def _get_is_valid(self):
        return self.__is_valid

    # INFO: SETTERS (opzionali)

    def __set_post(self, p: Post):
        self.__post = p

    def __set_bid(self, c: Utente):
        self.__bid = c

    def __repr__(self):
        return f"[{type(self).__name__}] post: {self._get_post()} | bid:  {self._get_bid()}"

    def __str__(self):
        return f"{self._get_post()} | {self._get_bid()}"
