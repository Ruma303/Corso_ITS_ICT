class TypeInvalidException(TypeError):
    def __init__(self, target: str, received: str | None = None):
        err = f"Il valore passato non è valido. Dev'essere di tipo '{target}'"
        if received:
            err += f". Ora è '{received}'"
        super().__init__(err)


class NoneTypeException(TypeError):
    def __init__(self, target: str):
        super().__init__(f"Il valore passato è nullo. Dev'essere di tipo '{target}'")


class ConstraintViolationException(ValueError):
    def __init__(self, target: str, message: str | None = None):
        err = (
            f"Vincolo [{target}] violato! {message}"
            if message
            else f"Vincolo [{target}] violato!"
        )
        super().__init__(err)


class LinkException(Exception):
    """Base delle eccezioni sulle associazioni: `except LinkException` le prende tutte."""


class InvalidLinkException(LinkException):
    def __init__(self, tipo_link: str):
        super().__init__(
            f"Il link passato non è valido. Dev'essere di tipo '{tipo_link}'"
        )


class NotSelfLinkException(LinkException):
    def __init__(self, link: object):
        super().__init__(f"Il link '{type(link).__name__}' non appartiene a self")


class NotExistingLinkException(LinkException):
    def __init__(self, target: str, message: str | None = None):
        err = f"L'associazione '{target}' non è presente!"
        super().__init__(f"{err} {message}" if message else err)


class AlreadyExistingLinkException(LinkException):
    def __init__(self, target: str, message: str | None = None):
        err = f"L'associazione '{target}' già è presente!"
        super().__init__(f"{err} {message}" if message else err)