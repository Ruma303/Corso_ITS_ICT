'''
Create a dictionary from a list

Scrivere un programma Python che prende in input una lista di stringhe 'list',
e produca un dizionario 'd' le cui chiavi sono le stringhe in 'list'.
Ogni chiave 'k' deve essere associata ad una lista di int che rappresentano
tutte le posizioni della stringa 'k' in 'list'.

Ad esempio, se
	list = ["ciao", "hello", "hola", "hello"]

il programma deve produrre il dizionario:

	d = {
		"ciao": [0]
		"hello": [1, 3],
		"hola": [2]
	}
'''
import sys

def create_dict(liste: list[str]) -> dict[str, list[int]]:
  result: dict[str, list[int]] = dict()
  pos = 0

  for ele in liste:
    # Se la parola è già presente nel dizionario
    if ele in result:
        # Aggiungiamo la posizione corrente alla lista esistente
        result[ele] += [pos]
    else:
        # Se non esiste, creiamo una nuova lista contenente la posizione
        result[ele] = [pos]

    pos += 1

  return result


def main() -> int:
  liste = ["uno", "due", "tre", "uno", "uno", "cinque", "venti", "tre"]
  result = create_dict(liste)
  print(result)
  return 0


if __name__ == "__main__":
  sys.exit(main())