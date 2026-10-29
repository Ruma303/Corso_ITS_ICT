from src.ebuy_py.exceptions.exceptions import (
    InvalidLinkException,
    NoneTypeException,
    TypeInvalidException,
)


class DataValidator:
    @staticmethod
    def _require_type(value: object, expected: type | tuple[type, ...]) -> None:
        """Lancia NoneTypeException / TypeInvalidException (entrambe TypeError).

        `expected` può essere una tupla di tipi, come in isinstance().
        """
        tipi = expected if isinstance(expected, tuple) else (expected,)
        nomi = " o ".join(t.__name__ for t in tipi)
        if value is None:
            raise NoneTypeException(nomi)
        if not isinstance(value, expected):
            raise TypeInvalidException(nomi, type(value).__name__)

    @staticmethod
    def _require_valid_link(link: object, expected: type) -> None:
        """Il controllo ripetuto in ogni _set/_add: tipo giusto e link ancora valido.

        Sta qui e non in un'eccezione: un'eccezione descrive un errore, non lo cerca.

        CONVENZIONE: nelle classi associative a responsabilità doppia creare un getter chiamato esclusivamente _get_is_valid() che ritorna self.__is_valid: bool
        """
        if not isinstance(link, expected) or not link._get_is_valid():
            raise InvalidLinkException(expected.__name__)