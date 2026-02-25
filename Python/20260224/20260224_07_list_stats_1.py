'''
List stats 1

Scrivere un programma Python che, data una lista di interi, calcoli e
scriva a schermo:
 - il valore minimo (ovvero l'intero più piccolo nella lista)
 - il valore massimo
 - il valore medio

Si scriva il programma di modo che:
- non utilizzi alcuna funzione di calcolo di statistiche offerta
  da librerie esterne

- scandisca la lista esattamente una volta.

Organizzare il programma in opportune funzioni.
'''

list1 = [3, 7, 11, 18, 2, 4]

def get_min(list1):
  now_min = list1[0]

  for num in list1:
    if num < now_min:
      now_min = num

  return now_min

def get_max(list1):
  now_max = list1[0]

  for num in list1:
    if num > now_max:
      now_max = num

  return now_max

def get_avg(list1):
    now_min = get_min(list1)
    now_max = get_max(list1)

    return (now_min + now_max ) // 2


if __name__ == "__main__":
  print(get_min(list1))
  print(get_max(list1))
  print(get_avg(list1))