"""
Utilizzando il meccanismo while True: per realizzare un ciclo infinito:
"""

"""
1. leggere in sequenza numeri digitati da tastiera: numero=int(input("Numero: "))
"""

# while True:
#   numero = int(input("Inserisci un numero: "))
#   print(f"Hai digitato {numero}")

"""
2. contare il totale dei numeri acquisiti finora e stamparlo per ogni nuovo numero acquisito
"""

# totale_numeri = 0
# while True:
#   numero = int(input("Inserisci un numero: "))
#   totale_numeri += 1
#   print(f"Hai digitato {totale_numeri} fino ad ora.")

"""
3. stampare la somma dei numeri inseriti finora, come nell'esercizio precedente
"""

# totale = 0
# while True:
#   numero = int(input("Inserisci un numero: "))
#   totale += numero
#   print(f"Il totale fino ad ora è {totale}")


"""
4. calcolare il massimo valore inserito finora
"""

# currentval = int(input("Inserisci un numero di partenza: "))
# maxval = currentval

# while True:
#   currentval = int(input("Inserisci un altro numero: "))
#   if currentval > maxval:
#     maxval = currentval
#   print(f"Il valore massimo che hai inserito fino ad ora è {maxval}")


"""
5. calcolare il minimo valore inserito finora
"""

# Versione 1
# currentval = int(input("Inserisci un numero: "))
# minval = currentval

# while True:
#   currentval = int(input("Inserisci un altro numero: "))
#   if currentval < minval:
#     minval = currentval
#   print(f"Il valore minimo che hai inserito fino ad ora è {minval}")

# Versione 2

# values = []
# minval = 0

# while True:
#   currentval = int(input("Inserisci un altro numero: "))
#   values.append(currentval)
#   print(values)

#   if len(values) > 1:
#     print("eccomi")
#     minval = min(values)

#   print(f"Il valore minimo che hai inserito fino ad ora è {minval}")

"""
6. contare quante volte il numero successivo è maggiore del numero precedente. Esempio (3 2 5 6 10 1 2 7 0): 5 volte
"""

# numvolte = 0
# numero = int(input("Inserisci un numero: "))

# while True:
#   numerosuccessivo = int(input("Inserisci un numero: "))
#   if numero > numerosuccessivo:
#     numvolte += 1
#   numero = numerosuccessivo

#   print(f"Numeri precedenti più grandi: {numvolte}")


"""
7. calcolare la lunghezza della più lunga sequenza di numeri crescenti. Esempio (3 2 5 6 10 1 2 7 0): 4 (2 5 6 10)
"""

# numero = int(input("Inserisci un numero: "))
# lun = 1
# max_lun = lun

# while True:
#   nuovonumero = int(input("Inserisci un numero: "))
#   if nuovonumero > numero:
#     lun += 1
#     numero = nuovonumero
#     if lun > max_lun:
#       max_lun = lun
#   else:
#     print("Riavvio della sequenza\n")
#     lun = 1
#     numero = nuovonumero

#   print(f"Lunghezza sequenza crescente più lunga: {max_lun}")

"""
8. Bonus: calcolare la lunghezza della più lunga sequenza di numeri
che si alternano: maggiore del precedente, minore del precedente,
Esempio: (3 2 5 6 10 1 2 7 0): 3 (3 2 5 poiché 3>2, 2<5, )
"""

# currentValue = int(input("Inserisci un numero: "))
# sequence = [currentValue]  # Inserimento primo valore nella sequenza
# lun = len(sequence)  # Sempre 1

# while True:
#     prevValue = currentValue
#     currentValue = int(input("Inserisci un altro numero: "))

#     if currentValue == prevValue:
#         print("\nIl confronto non può essere effettuato su due valori identici")
#         print(f"Il secondo valore {currentValue} verrà incrementato di 1\n")
#         currentValue += 1

#     sequence.append(currentValue)
#     lun += 1
#     print(f"Sequenza attuale: {sequence}")
#     print(f"Lunghezza sequenza attuale: {lun}\n")

#     # Verifica la direzione dell'alternanza
#     if len(sequence) < 3:
#         continue  # Servono almeno due valori per verificarla

#     else:
#         # Controllare l'ultimo, il penultimo e terzultimo valore
#         a, b, c = sequence[-3], sequence[-2], sequence[-1]

#         # Verifica alternanza
#         if (a < b > c) or (a > b < c):
#             # Alternanza rispettata, si continua
#             continue # Si esce dall'else e si reitera nel ciclo
#         else:
#             print("Alternanza violata")
#             sequence.pop()  # Rimuovere ultimo elemento errato
#             lun -= 1        # Riduzione lunghezza
#             print(f"Lunghezza sequenza alternata maggiore: {lun}, con sequenza {sequence}")
#             # Usciamo dall'else e si interrompe nel ciclo
#             # Potremmo anche resettare la sequenza se vogliamo ripartire da capo
#             break


"""
9. Double bonus: cercare se una specifica sottosequenza
data a priori (es: 1, 5, 3, 7)
è presente nella sequenza di numeri fornita da tastiera
"""

# seq = [1, 5, 3, 7]
# comparison = []

# while True:
#   number = int(input("Inserisci un numero: "))
#   comparison.append(number)
#   print(comparison)

#   if all(item in seq for item in comparison):
#     print(f"I numeri {comparison} appartengono alla sequenza iniziale {seq}")
#   else:
#     print(f"{number} non fa parte della sequenza")
#     comparison.pop()
#     # del comparison[len(comparison) - 1]
#     print(f"Tutti gli elementi trovati fino ad ora {comparison}")
#     break
