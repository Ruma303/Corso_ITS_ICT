"""
Data una stringa, trovare la sottostringa palindroma più lunga
"""

from sys import exit

alfa = [chr(c) for c in range(65, 91)]

def normalize(string: str) -> str:
    string = string.upper()
    result = ""
    if not string:
        raise ValueError("La stringa di confronto non può essere vuota")
    result = "".join(char for char in string if "A" <= char <= "Z")
    return result


def find_longest_substring(string: str) -> str:
  # Invariante: la stringa è normalizzata e contiene solo caratteri alfa
  norm_string = normalize(string)
  print(norm_string)

  # Calcolare la sottostringa da analizzare
  i = 0
  j = len(norm_string) -1
  substr = ""
  curr_substr = ""

  # FIXME: la sotto_stringa qui non viene modificata
  while i < j:
    palyndrome_substr = is_char_palyndrome(norm_string, i, j)
    print(palyndrome_substr, norm_string, norm_string[i], norm_string[j])
    if palyndrome_substr:
      # Se i due caratteri sono palindromi, creo la stringa a partire
      # dai lati opposti (posizione i-esima e j-esima)
      curr_substr += norm_string[i]
      curr_substr += norm_string[j]
     
      # decrementare l'indice J
      j -= 1

      # TODO: controllare fin quando tutti i caratteri sono uguali
      # Avanzando gli indici sia da sx che da dx
      curr_i = i # Non so se serve un indice temporaneo per la sottostringa
      # che avanzi fin quando i caratteri sono uguali.

      
    else:
      # Altrimenti, reset
      curr_substr = ""
      # Partire dal prossimo indice i
      i += 1
      
    print(f"\nSubstr: ", (norm_string, i, j), "Palindroma" if palyndrome_substr else "Non palindroma")

    if len(curr_substr) > len(substr):
      substr = curr_substr

  return substr


def is_char_palyndrome(string: str, start, end) -> bool:
    # invariante la stringa in esame è normalizzata e ha solo caratteri validi
    # Verifico esclusivamente se i singoli caratteri sono uguali
    print(f"\ndentro while in is_char_palyndrome {string[start] = }, {string[end] = }")
    if string[start] == string[end]:
      return True

    return False


def main() -> int:
    # test1 = "Ed Irene se ne ride.".strip()
    test1 = "Ed Irene se ne".strip()
    test1_check = find_longest_substring(normalize(test1))

    if test1_check:
        print(f"\nLa sottostringa più lunga è '{test1}'.")
    else:
        print(f"\nLa frase'{test1}' NON è palindroma.")

    return 0


if __name__ == "__main__":
    exit(main())
