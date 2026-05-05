'''
List reverse

Scrivere un programma Python che prende in input una lista di interi e calcoli e
scriva a schermo la lista con gli stessi elementi in ordine inverso.

Ad esempio, ricevuta in input la lista [3, 7, 1], il programma deve
calcolare [1, 7, 3].

Si scriva il programma utilizzando solo i costrutti base del linguaggio,
senza l'ausilio di funzioni offerte da librerie.

Organizzare il programma in opportune funzioni.
'''

list1 = [3, 7, 1]

def reverse(list1):
  final_list = []

  for _ in range(len(list1)):
    last = list1.pop()
    final_list.append(last)

  return final_list

if __name__ == "__main__":
  print(reverse(list1))