from typing import Callable


def input_validated(message: str, converter: Callable[[str], object]) -> str:
    """
    Chiede un valore e prova a convertirlo in un oggetto corrispondente.

    param: message: messaggio di richiesta di input
    param: converter: è una funzione che riceve una str e restituisce un oggetto.
    """

    while True:
        value = input(message).strip()

        try:
            converter(value)
            return value

        except (ValueError, TypeError) as e:
            print(f"Valore non valido: {e}")
