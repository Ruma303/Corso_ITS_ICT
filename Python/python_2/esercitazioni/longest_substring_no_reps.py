'''
Scrivere un programma che, letta una stringa 'string' da tastiera,
restituisca tutte le più lunghe sottostringhe (diverse) di 'string' che
non hanno caratteri ripetuti.

Ad esempio, se string = "abcabcbdbbc"
il programma deve restituire:

abc
bca
cab
cbd

Organizzare il programma in opportune funzioni che effettuino il calcolo.

'''
from sys import exit


def find_longest_substrings(string: str) -> list[str]:
    if not string:
        raise ValueError("La stringa non può essere vuota.")

    n = len(string)
    max_len = 0
    substrings = set() # insieme di sottostringhe più lunghe trovate
    
    # Scorriamo ogni possibile punto di inizio
    for i in range(n):
        seen = set()
        current_sub = ""
        
        # Cerchiamo la sottostringa più lunga che parte da i
        for j in range(i, n):
            if string[j] in seen:
                break
            seen.add(string[j])
            current_sub += string[j]
        
        # Aggiorniamo la lista delle stringhe massime trovate
        if len(current_sub) >= max_len:
            if len(current_sub) > max_len:
                max_len = len(current_sub)
                substrings = {current_sub} # Reset del set con la nuova lunghezza
            else:
                substrings.add(current_sub) # Aggiunta di sottostringa di pari lunghezza
                
    return sorted(list(substrings))



def main() -> int:
  string1 = "abcabcbdbbc"
  result1 = find_longest_substrings(string1)

  if result1 is not None:
    for r in result1:
      print(r, sep="\n")

  return 0


if __name__ == "__main__":
  exit(main())
