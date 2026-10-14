from __future__ import annotations

from typing import TYPE_CHECKING

from src.python_code.exceptions.exceptions import InvalidLinkException

if TYPE_CHECKING:  # solo type hint
    from src.python_code.models.categoria import Categoria
    from src.python_code.models.post import Post


class post_cat:
    """Crea un link immutabile Categoria 1..1 -- post_cat -- 0..* Post."""

    # INFO: CLASSMETHODS

    @classmethod
    def _create(cls, p: Post, c: Categoria):
        link = cls(p, c)
        p._set_post_cat(link)
        c._add_post_cat(link)
        return link

    @classmethod
    def _remove(cls, link: post_cat):
        if not link._get_is_valid():
            raise InvalidLinkException("post_cat")
        link._get_post()._remove_post_cat(link)
        link._get_categoria()._remove_post_cat(link)
        link.__post = None
        link.__categoria = None
        link.__is_valid = False

    # INFO: CONSTRUCTORS

    def __init__(self, p: Post, c: Categoria):
        self.__set_post(p)
        self.__set_categoria(c)
        self.__is_valid = True

    # INFO: UTILITIES

    def __hash__(self):
        return hash((self.__post, self.__categoria))

    def __eq__(self, other: object):
        if not other or type(self) != type(other):
            return False
        if hash(self) != hash(other):
            return False
        if type(other) == post_cat:
            return (self.__post == other.__post) and (
                self.__categoria == other.__categoria
            )
        return False

    # INFO: GETTERS

    def _get_post(self):
        return self.__post

    def _get_categoria(self):
        return self.__categoria

    def _get_is_valid(self):
        return self.__is_valid

    # INFO: SETTERS (opzionali)

    def __set_post(self, p: Post):
        self.__post = p

    def __set_categoria(self, c: Categoria):
        self.__categoria = c

    def __repr__(self):
        return f"[{type(self).__name__}] post: {self._get_post()} | categoria:  {self._get_categoria()}"

    def __str__(self):
        return f"{self._get_post()} | {self._get_categoria()}"
