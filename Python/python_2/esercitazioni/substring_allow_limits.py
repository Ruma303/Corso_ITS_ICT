'''
Scrivere una funzione Python che, data:
- una stringa string
- un dizionario max_occurrences le cui entry sono della forma:
    character -> int >= 0

restituisca la porzione più lunga di string che soddisfa la seguente condizione:
se un carattere 'c' della porzione di string in esame è in max_occurrences,
allora il suo numero di occorrenze (nella porzione) è al massimo max_occurrences['c'].

Ad esempio, se:
- stringa = "ciao mondo"
- max_occurrences = {
    'i': 0,
    'o': 2
}

la funzione restituirà la porzione di 'stringa' più lunga che non contiene
occorrenze di 'i' e contiene al massimo 2 occorrenze di 'o', ovvero:
"ao mond"

Attenzione: si chiede esplicitamente di implementare da zero tutte le eventuali
funzioni ausiliarie necessarie, e di non utilizzare le funzionalità avanzate
offerte dal tipo str di Python (se non gli operatori 'in', '[]', e la funzione
len()).

Organizzare il programma di modo che:
 - definisca una opportuna funzione
       substring_allow_limits(string:str, max_occurrences:dict[str,int])->str
   che effettua il calcolo e restituisca il risultato
 - prenda l'input dell'utente da tastiera,
   invochi la funzione e ne stampi il risultato a schermo.
'''
from sys import exit

stringa = "ciao mondo"
max_occurrences = {
  'i': 0,
  'o': 2
}

def substring_allow_limits(string: str, max_occurrences: dict[str, int]) -> str:
    best_result: str = ""

    # 1. Ciclo esterno: proviamo a far partire la sottostringa da ogni indice
    for start in range(len(string)):
        current_result: str = ""

        # Dizionario di appoggio per contare le occorrenze di questa specifica prova
        current_counts = {}

        # 2. Ciclo interno: costruiamo la stringa partendo dall'indice 'start'
        for j in range(start, len(string)):
            c = string[j]

            # Verifichiamo se il carattere ha una limitazione imposta dal dizionario
            if c in max_occurrences:

                # Inizializziamo il conteggio se è la prima volta che incontriamo 'c'
                if c not in current_counts:
                    current_counts[c] = 0

                current_counts[c] += 1

                # Se superiamo il limite per questo carattere, questa sottostringa non può più crescere
                if current_counts[c] > max_occurrences[c]:
                    break # Usciamo dal ciclo interno, esattamente come facevi tu!

            # Se il limite non è superato, aggiungiamo il carattere
            current_result += c

        # 3. Controllo finale: se questa prova ha generato una stringa più lunga, la salviamo
        if len(current_result) > len(best_result):
            best_result = current_result

    return best_result


def main() -> int:
  test_dict_1 = {
    'l' : 2,
    'p': 2,
    'e': 3
  }
  test_string_1 = "parallelepipedo"
  test_substring_1 = substring_allow_limits(test_string_1, test_dict_1)
  print(test_substring_1)

  """ test: str = input("Inserisci una stringa: ").lower().strip()
  substring = substring_allow_limits(test, max_occurrences)
  print(substring) """

  return 0


if __name__ == "__main__":
  exit(main())
