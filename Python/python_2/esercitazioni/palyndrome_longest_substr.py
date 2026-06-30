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
    print(result)
    return result


def find_longest_substring(string: str) -> str:
  string = normalize(string)
  # Calcolare la sottostringa da analizzare
  i = 0
  j = len(string) -1
  substr = ""
  curr_substr = ""

  while i < j:
    check_substr = check_palindrome(string, i, j)
    if check_substr:
      curr_substr += string[i]
      curr_substr += string[j]
    else:
      curr_substr = ""

    print(f"Substr: ", (string, i, j), (curr_substr, string[i], string[j]), "Palindroma" if check_substr else "Non palindroma")
    i += 1
    j -= 1

    if len(curr_substr) > len(substr):
      substr = curr_substr

  return substr


def check_palindrome(string: str, start, end) -> bool:
    # invariante la stringa in esame è normalizzata e ha solo caratteri validi

    i = start  # indice che parte all'inizio della stringa (Sinistra)
    j = end  # indice dalla fine della stringa (Destra)

    # Ci fermiamo quando gli indici si incontrano
    # invariante: i sarà sempre minore di j
    while i < j:
        if string[i] != string[j]:
          return False

        i += 1
        j -= 1

    return True


def main() -> int:
    # test1 = "Ed Irene se ne ride.".strip()
    test1 = "Ed Irene se ne".strip()
    test1_check = find_longest_substring(normalize(test1))

    if test1_check:
        print(f"La sottostringa più lunga è '{test1}'.")
    else:
        print(f"La frase'{test1}' NON è palindroma.")

    return 0


if __name__ == "__main__":
    exit(main())
