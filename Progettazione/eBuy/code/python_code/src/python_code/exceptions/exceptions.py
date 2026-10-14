class InvalidLinkException(Exception):
    def __init__(self, tipo_link: str):
        super().__init__(
            f"Il link passato non è valido. Dev'essere di tipo '{tipo_link}'"
        )


class TypeInvalidException(Exception):
    def __init__(self, target: str):
        super().__init__(
            f"Il valore passato non è valido. Dev'essere di tipo '{target}'"
        )
