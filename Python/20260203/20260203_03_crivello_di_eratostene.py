"""
Il crivello di Eratostene è un antico ed efficiente algoritmo greco (circa 200 a.C.) per trovare tutti i numeri primi fino a un numero prefissato n. Funziona "setacciando" i numeri: si elencano i numeri da 2 a n, si elimina il 2 e tutti i suoi multipli, poi il 3 e i suoi, procedendo con i primi successivi. 
"""

def get_crivello():
  # max_ele = int(input("Inserisci un massimo: ").strip())
  max_ele = 1_000_000
  primi = [True] * max_ele

  for i in range(2, max_ele + 1, i):
    if primi[i] == True:
      primi[i] = False

  for i in range(2, max_ele):
    if primi[i]:
      print(primi[i])

get_crivello()