'''
Merge sorted lists

Scrivere un programma Python che, date due liste di interi
list1 e list2 che sono garantite (ovvero possiamo assumere)
essere ordinate (dal più piccolo al più grande, ma con possibili
elementi duplicati), produca e stampi a schermo una nuova lista
list3 che contenga tutti gli elementi di list1 e tutti gli elementi
di list2 ordinati (ancora, dal più piccolo al più grande).

Ad esempio, se
 - list1 = [3, 5, 6, 6, 8] e
 - list2 = [1, 4, 6],
allora il programma deve produrre la lista
   list3 = [1, 3, 4, 5, 6, 6, 6, 8]
e stamparla a schermo.

Successivamente, modificare il programma di modo che:

 - Definisca una opportuna funzione
      merge_sorted_lists(list1:list[int], list2:list[int])->list[int]
   che effettua il calcolo e restituisce il risultato.


Prenda l'input dell'utente (i valori per list1 e list2) da tastiera,
    invochi la funzione e ne stampi il risultato a schermo.
    Per leggere una lista (ordinata) da tastiera, il programma dovrà
    chiedere all'utente un intero alla volta; l'utente segnalerà la
    terminazione di ogni lista inserendo un valore minore del precedente.
    Ad esempio, se l'utente inserisce, nell'ordine: 1, 3, 53, 4, la lista
    memorizzata sarà [1, 3, 53].
'''

def get_list():

  print("""
        \r==============================
        \rInserimento valori nella lista.
        \rInserire un numero minore del
        \rprecedente per passare alla
        \rprossima lista
        \r==============================
        """)

  prev = int(input("Inserire un numero: ").strip())
  lists = [prev] # Creazione e inserimento del primo numero nella lista per iniziare i confronti

  while True:
    # Acquisizione altri numeri per confronti
    num = int(input("Inserire un numero: ").strip())

    if num >= prev:
      lists.append(num)
      prev = num

    else:
      break

  return lists


def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
  i = 0 # Indice per accedere a list1
  j = 0 # Indice per accedere a list2
  result = []

  # Se ci sono elementi in entrambe le liste, confrontarli
  while i < len(list1) and j < len(list2):

    # Confrontare gli elementi di entrambe le liste
    # Inserire prima l'elemento più piccolo: lista 1
    if list1[i] < list2[j]:
      result.append(list1[i])
      i += 1

    # Oppure dalla lista 2
    elif list1[i] > list2[j]:
      result.append(list2[j])
      j += 1

    # Se sono uguali, inserirli entrambi
    else:
      result.append(list1[i])
      result.append(list2[j])
      i += 1
      j += 1

  # Se non esistono elementi in una delle due liste,
  # caricare gli ultimi elementi già ordinati della lista rimanente
  if i < len(list1):
    while i < len(list1):
      result.append(list1[i])
      i += 1

  if j < len(list2):
    while j < len(list2):
      result.append(list2[j])
      j += 1

  return result


if __name__ == "__main__":
  # Liste di test
  # list1 = [3, 5, 6, 6, 8]
  # list2 = [1, 4, 6]

  lists = []
  for i in range(2):
    new_list = get_list()
    lists.append(new_list)

  merged_list = merge_sorted_lists(lists[0], lists[1])
  print(f"{merged_list}")
