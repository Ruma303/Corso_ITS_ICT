"""
Il crivello di Eratostene è un antico ed efficiente algoritmo greco (circa 200 a.C.) per trovare tutti i numeri primi fino a un numero prefissato n. Funziona "setacciando" i numeri: si elencano i numeri da 2 a n, si elimina il 2 e tutti i suoi multipli, poi il 3 e i suoi, procedendo con i primi successivi.
"""

def get_crivello(max_ele):
  # Serve max_ele+1 perché massimo incluso
  primi = [True] * (max_ele + 1)
  # Impostiamo i primi due numeri come numeri primi
  primi[0] = primi[1] = False

  # Solo fino a sqrt(max_ele), poi i multipli più piccoli sono già stati segnati
  p = 2 # Posizione di partenza
  while p * p <= max_ele:
    if primi[p]: # Se è True
      # Setaccia tutti i multipli di p da p*p fino a max_ele incluso
      # Salta di p (multipli)
      for n in range(p * p, max_ele + 1, p):
        primi[n] = False
    p += 1

  for i in range(2, max_ele):
    if primi[i]:

      print(i)


max_ele = 1_000_000
# max_ele = int(input("Inserisci un massimo: ").strip())
get_crivello(max_ele)