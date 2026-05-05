"""
Una persona pensa a un numero tra 1 e 1000.
Il suo collega fa delle domande:
  - è minore di N
  - è maggiore di N
fino a indovinare il numero pensato.

Vince chi ha fatto un minor numero di domande
"""

# Versione 1 con albero di ricerca binario: Versione iterativa
"""
def trova_numero():

    vmin = 1
    vmax = 1000
    tentativi = 0

    # Fin quando il numero non è lo stesso
    while (vmax - vmin) != 0:
        vmid = (vmin + vmax) // 2
        tentativi += 1
        res = input(f"Il valore è più grande di {vmid}? (Y/N): ").strip().upper()
        if res == "Y":
            vmin = vmid + 1
        else:
            vmax = vmid

    return vmin, tentativi

N = int(input("Inserisci il valore segreto da 1 a 1000: "))
numero, tent = trova_numero()
print(f"Hai trovato il numero {numero} dopo {tent} tentativi")
"""


""" # Versione 2: ricorsiva
def trova_numero():
    vmin = 1
    vmax = 1000
    tentativi = 0

    # Fin quando il numero non è lo stesso
    while (vmax - vmin) != 0:
        vmid = (vmin + vmax) // 2
        tentativi += 1
        res = input(f"Il valore è più grande di {vmid}? (Y/N): ").strip().upper()
        if res == "Y":
            vmin = vmid + 1
        else:
            vmax = vmid

    return vmin, tentativi


N = int(input("Inserisci il valore segreto da 1 a 1000: "))
numero, tent = trova_numero()
print(f"Hai trovato il numero {numero} dopo {tent} tentativi")
 """
# Gioco al contrario. L'utente fa i tentativi

from random import randint

minimo = 1
massimo = 1000
num = randint(minimo, massimo)
tentativi = 1

print("Numero corretto", num) # SOLO PER DEBUG

while True:
  scelta = int(input("Inserisci un numero: ").strip())

  if 1 < scelta > 1000:
    print(f"Il valore {scelta} non è corretto")
    print("Il numero segreto si trova tra 1 e 1000")
    continue

  if scelta == num:
    break

  elif scelta > num:
    massimo = scelta - 1
    tentativi += 1
    print(f"Il numero corretto è più piccolo di {scelta}")
    print(f"Nuovo range: {minimo}-{massimo}") # SOLO PER DEBUG

  else:
    minimo = scelta + 1
    tentativi += 1
    print(f"Il numero corretto è più grande di {scelta}")
    print(f"Nuovo range: {minimo}-{massimo}") # SOLO PER DEBUG

print(f"Complimenti, hai trovato il numero: {num} dopo {tentativi} tentativi")
