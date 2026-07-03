"""
Data una stringa, trovare la sottostringa palindroma più lunga
"""

from sys import exit

alfa = [chr(c) for c in range(65, 91)]

def normalize(string: str) -> str:
    string = string.strip().upper()
    result = ""
    if not string:
        raise ValueError("La stringa di confronto non può essere vuota")
    result = "".join(char for char in string if "A" <= char <= "Z")
    return result


def is_char_palindrome(string: str, start, end) -> bool:
    # invariante la stringa in esame è normalizzata e ha solo caratteri validi
    # Verifico esclusivamente se i singoli caratteri sono uguali
    if string[start] == string[end]:
      return True

    return False


def get_all_palindrome_substring(string: str) -> set[str]:
  # Invariante: la stringa è normalizzata e contiene solo caratteri alfa
  norm_string = normalize(string)

  set_longest_substr = set()

  # INFO: In gergo la strategia si chiama Expand Around Center
  # A partire da un carattere alla volta e spostare i puntatori
  # verso all'esterno, verificando la palindromicità dei caratteri.
  for char_pos in range(len(norm_string)):

    # INFO: i due cicli vengono effettuati sempre.
    # Per ogni posizione della stringa vengono fatti due tentativi:
    # - cercare un palindromo dispari
    # - cercare un palindromo pari
    # Quindi, cambia solo la definizione di 'centro'

    # CASO 1: Palindromi di lunghezza DISPARI (es. "ABA", centro su norm_string[char_pos])
    i = char_pos - 1
    j = char_pos + 1
    curr_substr = norm_string[char_pos] # Partiamo dal singolo carattere centrale.

    while i >= 0 and j < len(norm_string) and is_char_palindrome(norm_string, i, j):

        # Per aggiungere il carattere precedente, ricreare la stringa. 1) Partiamo dal primo carattere palindromo, 2) la sottostringa corrente più lunga, 3) l'ultimo carattere più lungo trovato
        curr_substr = norm_string[i] + curr_substr + norm_string[j]
        
        # muovere gli indici verso l'esterno
        i -= 1
        j += 1

    # Salvataggio solo se la sottostringa ha almeno 2 caratteri
    if len(curr_substr) >= 2:
        set_longest_substr.add(curr_substr)


    # CASO 2: Palindromi di lunghezza PARI (es. "ABBA", centro tra char_pos e char_pos+1)
    i = char_pos
    j = char_pos + 1
    curr_substr = "" # Non vi è un centro. Verranno confrontati e forse aggiunti i caratteri 
    # verificando le loro posizioni i e j.

    while i >= 0 and j < len(norm_string) and is_char_palindrome(norm_string, i, j):
        curr_substr = norm_string[i] + curr_substr + norm_string[j]
        i -= 1
        j += 1

    # Salvataggio solo se la sottostringa ha almeno 2 caratteri
    if len(curr_substr) >= 2:
        set_longest_substr.add(curr_substr)
        
  return set_longest_substr


def find_longest_substrings(set_substrs: set[str]) -> set[str]:
    max_len = 0
    longest_set = set()

    # Trova prima qual è la lunghezza massima presente nel set
    for string in set_substrs:
        if len(string) > max_len:
            max_len = len(string)
            # Resetta il set delle sottostringhe più lunghe
            longest_set = { string }
        elif len(string) == max_len:
            # Aggiunge la sottostringa al set
            longest_set.add(string)

    return longest_set


def main() -> int:
    # test1 = "Ed Irene se ne ride.".strip()
    tests = {"Ed Irene se ne ride.", "Ed Irene se ne", "banANA", "rAdaRAd"}

    for test in tests:

      test_set = get_all_palindrome_substring(test)
      test_longest_substr = find_longest_substrings(test_set)
  
      if test_longest_substr:
          print(f"\nL'insieme delle sottostringhe più lunghe di '{test}' sono : ", {s for s in test_longest_substr})
      else:
          print(f"\nLa frase '{test_longest_substr}' NON è palindroma.")

    return 0


if __name__ == "__main__":
    exit(main())
