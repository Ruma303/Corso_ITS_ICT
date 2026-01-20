"""
Carte italiane

40 carte suddivise in 4 semi (coppe, bastoni, denari, spade)
Valori di ogni gruppo di semi: da 1 a 10
Realizzare un programma che simula una smazzata a scopone scientifico (10 carte per ogni giocatore), 4 giocatori
"""
from random import shuffle

# Lista di 4 liste di semi, ogni lista interna ha 10 numeri

carte = [
  "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C",
  "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B",
  "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D",
  "1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S",
]
shuffle(carte)

def smazza():

  G1 = []
  G2 = []
  G3 = []
  G4 = []

  for i in range(0, 10):
    G1.append(carte[i])
  for i in range(10, 20):
    G2.append(carte[i])
  for i in range(20, 30):
    G3.append(carte[i])
  for i in range(30, 40):
    G4.append(carte[i])

  return G1, G2, G3, G4

G1, G2, G3, G4 = smazza()

print(f"Carte del giocatore G1 {G1}")
print(f"Carte del giocatore G2 {G2}")
print(f"Carte del giocatore G3 {G3}")
print(f"Carte del giocatore G4 {G4}")


# per ogni giocatore iterare sulle sue carte
def semi_per_giocatore(giocatore):
  coppe = []
  bastoni = []
  denari = []
  spade = []
  for carta in giocatore:

    # Troviamo quanti semi hanno i giocatori in una mano
    match carta:
      case carta if carta[1] == "C": coppe.append(carta)
      case carta if carta[1] == "B": bastoni.append(carta)
      case carta if carta[1] == "D": denari.append(carta)
      case carta if carta[1] == "S": spade.append(carta)

  return coppe, bastoni, denari, spade

print("\nTest liste di semi per giocatori\n")
print(semi_per_giocatore(G1))
print(semi_per_giocatore(G2))
print(semi_per_giocatore(G3))
print(semi_per_giocatore(G4))

"""
Contare punteggi del gioco = Bestia

Si deve prendere il massimo punteggio con tre carte dello stesso seme.

1 = 16
da 2-5 va aggiunto 10
6 = 18
7 = 21
8-9-10 (figure) = 10
"""

print("\nCalcolo bestia\n")

def calcola_bestia(semi):
  print("Liste di semi del giocatore X: ", semi)
  tripletta_migliore = []

  tripletta_coppe = []
  tripletta_bastoni = []
  tripletta_denari = []
  tripletta_spade = []

  triplette = [tripletta_coppe, tripletta_bastoni, tripletta_denari, tripletta_spade]

  for seme in semi:
    print("seme analizzato: ", seme)

    # Se ogni gruppo di semi contiene meno di 3 carte, ignora
    if len(seme) < 3:
      continue

    else:

      # TODO Devo iterare per ogni seme
      # for tipo in seme:

      for carta in seme:

        # Controllo valori
        # In base al valore della carta verrà automaticamente
        # preso quello con il valore più alto grazie al costrutto match case
        match carta:
          case carta if carta[0] == 7: 21
          case carta if carta[0] == 6: 18
          case carta if carta[0] == 1: 16
          case carta if carta[0] == 5: 15
          case carta if carta[0] == 4: 14
          case carta if carta[0] == 3: 13
          case carta if carta[0] == 2: 12
          case _: 10 # tutti gli altri

        # Aggiungo alla tripletta del seme in esame
        # tipo.append(carta)
        # print(tipo)

        # Prese tre carte, uscire dal loop e vedere il prossimo seme
      if len(seme) > 3: break


  # Valutare la tripletta migliore
  # for tripletta in triplette:

  return sum(tripletta_migliore), tripletta_migliore


p1_max, p1_tripletta = calcola_bestia(semi_per_giocatore(G1))
p2_max, p2_tripletta = calcola_bestia(semi_per_giocatore(G2))
p3_max, p3_tripletta = calcola_bestia(semi_per_giocatore(G3))
p4_max, p4_tripletta = calcola_bestia(semi_per_giocatore(G4))

p_vincitore = max(p1_max, p2_max, p3_max, p4_max)

print(f"Il punteggio più alto è {p_vincitore}")
