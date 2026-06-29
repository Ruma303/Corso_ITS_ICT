"""
Una stringa si dice "palindroma" se resta uguale sia se letta da
sinistra verso destra che da destra verso sinistra (ignorando spazi e
punteggiatura).

Ad esempio, la stringa seguente è palindroma:

Ed Irene se ne ride.

Scrivere un programma che, letta una stringa 'string' da tastiera,
verifichi se la stringa è palindroma, ignorando eventuali spazi e
caratteri di punteggiatura.

Organizzare il programma in opportune funzioni che effettuino il calcolo.
"""

from sys import exit

alfa = [chr(c) for c in range(65, 91)]


def check_palindrome(string: str) -> bool:

    if not string:
        raise ValueError("La stringa di confronto non può essere vuota")

    i = 0  # indice che parte all'inizio della stringa (Sinistra)
    j = len(string) - 1  # indice dalla fine della stringa (Destra)

    # Ci fermiamo quando gli indici si incontrano
    while i < j:
      
      # Se il carattere a sinitra non in alfa (ignoriamo caratteri speciali)
      if string[i].upper() not in alfa:
        i += 1  # incrementiamo indice altrimenti loop infinito
        continue

      if string[j].upper() not in alfa: 
        j -= 1  # decrementiamo j per lo stesso motivo
        continue

      print(f"{i = }: {string[i].upper() = } | {j = }: {string[j].upper() = }")
      # Verificare che entrambi siano lo stesso carattere (upper)
      if string[i].upper() != string[j].upper():
        return False

      # Se sono uguali, procediamo lo stesso
      i += 1
      j -= 1

    return True


def main() -> int:
    test1 = "Ed Irene se ne ride.".strip()
    test1_check = check_palindrome(test1)

    if test1_check:
        print(f"La frase'{test1}' è palindroma.")
    else:
        print(f"La frase'{test1}' NON è palindroma.")

    return 0


if __name__ == "__main__":
    exit(main())
