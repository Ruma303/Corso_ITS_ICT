parola = "Precipitevolissimevolmente"

# Indexing: prende un singolo elemento di un insieme
# Ricordarsi che gli indici partono da 0
print("Indexing:")
primo = parola[0]
terzo = parola[2]
penultimo = parola[-2]
ultimo1 = parola[-1]
ultimo2 = parola[len(parola) - 1]

print(f"{primo = }, {terzo = }, {penultimo = } {ultimo1 = }, {ultimo2 = }", sep=", ")


# Slicing: prende una porzione di un insieme
print("\nSlicing:")

# Slice [start:stop:step] (ultimi due opzionali)
print(parola[5:9]) # pite

# Ultime 7 lettere
print(parola[-7:]) # olmente

# Parola al contrario
print(parola[::-1]) # etnemlovemissilovetipicerP

