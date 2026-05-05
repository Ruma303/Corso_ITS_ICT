
"""
Python consente di utilizzare variabili esterne alla funzione,
ma non è una pratica consigliata, perché 
"""
nome = "Mario"

def saluta():
  print(nome)



saluta()

def addMul(a, b, c):
  print(nome, a, b, c)

print("inizio")

addMul(1, 2, 3)