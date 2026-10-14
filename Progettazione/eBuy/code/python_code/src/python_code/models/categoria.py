from typing import Self

from src.python_code.associations.post_cat import post_cat


class Categoria:
    __all_objects_by_nome: dict[str, Self] = dict()
    __set_all_post_cat: set[post_cat] = set()  # Set di associazioni post_cat

    # INFO: CLASSMETHODS

    @classmethod
    def get_all_post_cat(cls):
        return type(cls).__set_all_post_cat

    @classmethod
    def get_by_nome(cls, nome: str) -> Self | None:
        return cls.__all_objects_by_nome.get(nome)

    @classmethod
    def _clear_registry(cls) -> None:
        """Solo per i test."""
        cls.__all_objects_by_nome.clear()

    # INFO: GETTERS
    def get_nome(self) -> str | None:
        return self.__nome

    # INFO: SETTERS
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError(
                f"Il valore dev'essere di tipo str. Ora è '{type(nome).__name__}'"
            )
        nome = nome.strip()
        if not nome:
            raise ValueError("Il nome non può essere vuoto")
        if nome == self.__nome:
            return
        registry = type(self).__all_objects_by_nome
        if nome in registry:
            raise KeyError("Questa categoria già esiste")

        # Tutti i controlli sono passati: ora si può modificare lo stato
        if self.__nome is not None:
            del registry[self.__nome]
        self.__nome = nome
        registry[nome] = self

    # INFO: ASSOCIATIONS
    def _add_post_cat(self, link: post_cat): 
      if not link or not isinstance(link, post_cat):
        raise TypeError(f"Il link passato non è valido. Dev'essere un '{type(link).__name__}'")
      if link in self.__set_all_post_cat:
        raise KeyError(
            "Questa associazione già è presente"
        )
      if link in type(self).get_all_post_cat():
        raise KeyError(
            "Questa associazione già è presente"
        )
        # TODO: Cambiare in frozenset

      self.__set_all_post_cat.add(link) # [0..*] aggiunta al set dell'istanza
      type(self).__set_all_post_cat.add(link) # aggiunto al registro della classe

        
    def _remove_post_cat(self, link: post_cat):
      if not link or not isinstance(link, post_cat):
        raise TypeError(f"Il link passato non è valido. Dev'essere un '{type(link).__name__}'")
      # TODO: Cambiare in frozenset
      self.__set_all_post_cat = {l for l in self.__set_all_post_cat if l != link}
      

    # INFO: CONSTRUCTORS
    def __init__(self, nome: str):
        self.__nome: str | None = None
        self.set_nome(nome)
        self.__set_post_cat = frozenset() # Set di associazioni post_cat 0..*


    # INFO: UTILITIES
    def __hash__(self):
        return hash(self.__nome)

    def __eq__(self, other: object):
        if type(self) is not type(other):
            return False
        if hash(self) != hash(other):
          return False
        if type(other) == Categoria:
          return self.__nome == other.__nome
        return False

    def __repr__(self):
      return f"[{type(self).__name__}] nome: {self.get_nome()}"

    def __str__(self):
      return f"{self.get_nome()}"