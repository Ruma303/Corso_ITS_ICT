class InvalidLinkException(Exception): 
    """Sollevata quando l'istanza non corrisponde a un link valido."""
    def __init__(self, message: str = "L'istanza non è un link valido"):
        super().__init__(message)
