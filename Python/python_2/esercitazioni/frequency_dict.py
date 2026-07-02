"""
1. Scrivere una funzione frequency_dict che prende una stringa e ritorna un dizionario di frequenze per carattere.

2. Bonus: Creare una funzione get_chars_with_max_freq che ritorna un set di caratteri più frequenti nella stringa
"""

from sys import exit

# Set di caratteri alfabetici validi (ASCII)
alfa = {chr(a) for a in range(65, 91)}

def normalize(string: str, alfa: set) -> str:
  """Funzione di supporto che ritorna una stringa di soli caratteri alfabetici validi"""
  temp = string.strip().upper()
  result = ""

  # Costruisco la stringa di soli caratteri validi
  for c in temp:
    if c in alfa:
      result += c

  return result
  

def frequency_dict(string: str) -> dict[str, int]:
  """
    A partire da una stringa, costruisce un dizionario con 
      - str: un singolo carattere della stringa 
      - int: la frequenza di apparizione di questo carattere
  """
  result = dict()

  for char in string:
    # Verifico se il carattere già esiste
    if char in result:
      # Aggiorno il contatore
      result[char] += 1
    # Altrimenti, aggiungo il carattere nel dizionario con freq: 1
    else:
      result[char] = 1

  return result


def get_chars_with_max_freq(frequencies: dict) -> set[tuple[str, int]]:
  """Ritorna un set di caratteri con frequenza più alta"""
  freqs = frequencies.copy() # Lavoriamo sempre su una copia

  result: set[tuple] = set() # set di tuple con freq. maggiore
  max_char_freq = () # tupla con carattere, frequenza
  max_freq = 0

  for ch, fr in freqs.items():
    if fr == max_freq:
      max_char_freq = (ch, fr)
      result.add(max_char_freq)
    if fr > max_freq:
      max_char_freq = (ch, fr)
      result = { max_char_freq }
      max_freq = fr

  print(result) 
  return result
  

def main() -> int:
    test1 = "Hello Worldo"
    test1_norm = normalize(test1, alfa)
    
    print(f"\nStringa normalizzata: {test1_norm}")
    test1_freq = frequency_dict(test1_norm)

    print(f"\nNella stringa '{test1}' le frequenze dei caratteri sono:")
    for k,v in test1_freq.items():
      print(f"\t- '{k}' : '{v}'")

    test1_max = get_chars_with_max_freq(test1_freq)
    print(f"\nNella stringa '{test1}' i caratteri con maggior frequenza sono:")
    for k,v in test1_max:
      print(f"\t- '{k}' : '{v}'")

    return 0

if __name__ == "__main__":
    exit(main())

"""
Test1: 
Stringa normalizzata: HELLOWORLDO

Nella stringa 'Hello Worldo' le frequenze dei caratteri sono:
	- 'H' : '1'
	- 'E' : '1'
	- 'L' : '3'
	- 'O' : '3'
	- 'W' : '1'
	- 'R' : '1'
	- 'D' : '1'
{('L', 3), ('O', 3)}

Nella stringa 'Hello Worldo' i caratteri con maggior frequenza sono:
	- 'L' : '3'
	- 'O' : '3'
"""