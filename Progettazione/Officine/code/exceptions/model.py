class IsNotValidPersonaException(Exception):
    """Eccezione base per le violazioni dei vincoli legati alle persone."""
    def __init__(self, message: str = "La persona non rispetta i criteri di validazione. Dev'essere obbligatoriamente avere un ruolo 'cliente' e/o 'dipendente' e/o 'direttore'"):
        self.message = message
        super().__init__(self.message)


class IsNotClienteException(IsNotValidPersonaException):
    """Sollevata quando l'entità non possiede i requisiti di un cliente."""
    def __init__(self, message: str = "L'istanza non è un cliente valido"):
        super().__init__(message)


class IsNotDipendenteException(IsNotValidPersonaException):
    """Sollevata quando l'istanza non corrisponde al ruolo di dipendente."""
    def __init__(self, message: str = "L'istanza non è un dipendente valido"):
        super().__init__(message)


class IsNotDirettoreException(IsNotDipendenteException):
    """Sollevata quando le autorizzazioni dell'istanza non corrispondono a quelle di un direttore."""
    def __init__(self, message: str = "L'istanza non è un direttore valido"):
        super().__init__(message)