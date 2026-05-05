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

import sys

list1 = [3, 7, 11, 18, 2, 4]

def stats(list1):
  now_min = list1[0]
  now_max = list1[0]
  sum_num = 0

  for num in list1:
    if num < now_min:
      now_min = num

    if num > now_max:
      now_max = num

    sum_num += num

  now_avg = sum_num / 2

  return now_min, now_max, now_avg


def main():
  print(stats(list1))
  return 0

if __name__ == "__main__":
  sys.exit(main())
