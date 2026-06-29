'''
Insert in list

Si scriva un programma che legga da tastiera:
- una lista 'list' di stringhe
- una posizione 'p'
- una stringa 's'

e modifichi 'list' inserendo la stringa 's' in posizione 'p'.

Ad esempio, se l'utente inserisce:
	list = ["ciao", "hello", "hola"]
	p = 1
	s = 'xxx'

l'algoritmo modifica 'list'	nel modo seguente:

	list = ["ciao", "xxx", "hello", "hola"]
'''

from sys import exit

def get_strings():
  strings = []
  row = input("Inserisci una frase: ")
  strings.append(row)

  while True:
    row = input()
    if row == "":
      break

    strings.append(row)

  return strings


def insert_in_strings(strings: list[str], pos: int, new: str, substitute: bool = False) -> list[str]:

  try:
    if pos < 0 or pos > len(strings):
      raise IndexError(f"Non è possibile accedere alla posizione {pos}. La lunghezza della lista è di {len(strings)}! Nessun inserimento eseguito.")

    if substitute:
        # Espandiamo la lista di 1 copiando dal fondo verso pos
        strings.append("")  # placeholder per fare spazio
        i = len(strings) - 1
        while i > pos:
            #debug
            print(f"{i = }, al posto di: '", strings[i], "' assegno '", strings[i -1], "' ", strings, sep="")
            strings[i] = strings[i - 1]  # shifta a destra
            i = i - 1
        strings[pos] = new
        return strings

    else:
        result = []
        i = 0
        while i < len(strings):
            if i == pos:
                result.append(new)
            result.append(strings[i])
            i = i + 1
        return result

  except IndexError as err:
    print(f"""
          \r======================================
          \r{err.__class__.__name__}: {err}
          \r======================================
          """)
    return strings


def main():
  """  strings = get_strings()
  print(f"Lista di stringhe originale: {strings = }")

  pos = int(input("Inserisci una posizione numerica: ").strip())
  new = input("Inserisci una stringa da inserire: ").strip()
  """
  strings = ["ciao", "hello", "hola"]
  pos = 1
  new = 'xxx'
  new_list = insert_in_strings(strings, pos, new)
  print(f"\nProva con nuova lista: {new_list = }")

  print()

  substituted_list = insert_in_strings(strings, pos, new, substitute=True)
  print(f"Prova con sostituzione, nuova lista: {substituted_list = }\n\nLista originale: {new_list = }")

  return 0

if __name__ == "__main__":
  exit(main())
