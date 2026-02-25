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

 - Prenda l'input dell'utente (i valori per list1 e list2) da tastiera,
   invochi la funzione e ne stampi il risultato a schermo.
   Per leggere una lista (ordinata) da tastiera, il programma dovrà
   chiedere all'utente un intero alla volta; l'utente segnalerà la
   terminazione di ogni lista inserendo un valore minore del precedente.
   Ad esempio, se l'utente inserisce, nell'ordine: 1, 3, 53, 4, la lista
   memorizzata sarà [1, 3, 53].
'''

list1 = [3, 5, 6, 6, 8]
list2 = [1, 4, 6]

def sorted_lists_1(list1: list[int], list2: list[int]) -> list[int]:

  list3 = list1 + list2

  # Es: Ordinamento con Bubble Sort
  for i in range(len(list3)):
    for j in range(0, len(list3) - i - 1):

      # Se numero attuale minore è maggiore del successivo
      if list3[j] > list3[j + 1]:

        # Scambio posti
        temp = list3[j]
        list3[j] = list3[j + 1]
        list3[j + 1] = temp

  return list3

print(sorted_lists_1(list1, list2))

def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]: ...

def get_num():

  prev = int(input("Inserisci un numero: ").strip())
  numbers = []
  numbers.append(prev)

  while True:
    num = int(input("Inserisci un numero: ").strip())

    if num >= prev:
      numbers.append(num)
      prev = num

    else:
      return numbers

print(get_num())