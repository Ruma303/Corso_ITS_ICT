class InvalidLinkException(Exception): 
    """Sollevata quando l'istanza non corrisponde a un link valido."""
    def __init__(self, message: str = "L'istanza non è un link valido"):
        super().__init__(message)

class InvalidLinkOwnerException(Exception):
  """Sollevata quando il link non appartiene alla stessa istanza."""
  def __init__(self, message: str = "Il link non appartiene a questa istanza"):
      super().__init__(message)