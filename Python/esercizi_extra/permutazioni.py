"""
Stampare tutte le permutazioni di una stringa
"""

def permutazioni(parola, risposta="", risultati=None):
    if risultati is None:
        risultati = []

    # Caso base: stringa vuota significa che abbiamo finito di costruire una permutazione
    if len(parola) == 0:
        risultati.append(risposta)

    else:
        # Caso ricorsivo: per ogni carattere, ricorriamo con il resto della stringa
        for i in range(len(parola)):
            nuova = parola[:i] + parola[i+1:]
            # Debug
            # print(risposta + parola[i], parola[:i], parola[i+1:], sep=" | ")
            permutazioni(nuova, risposta + parola[i], risultati)

    return risultati

parola1 = "Ciao"
parola2 = "Almanacco"
parola3 = "Python"

p1 = permutazioni(parola1)
p2 = permutazioni(parola2)
p3 = permutazioni(parola3)

print(f"Tutte le permutazioni di: {parola1}", p1)
print(f"Tutte le permutazioni di: {parola2}", p2)
print(f"Tutte le permutazioni di: {parola3}", p3)