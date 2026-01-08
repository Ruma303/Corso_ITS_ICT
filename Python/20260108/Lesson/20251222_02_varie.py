# a=[1, "Ciao", 45, [1,2,3], ["aaa", "bbb"]]
# print(a)
# ilContatorePerContareQuanteVolteaèMaggioreDib = 0
# il_contatore_per_contare=20
# print(a[1])

# Versione ottimizzata
elementoPiùGrande = int(input("dammi un numero: "))

elementoCorrente =  int(input("dammi un numero: "))
elementoPiùGrande=max(elementoPiùGrande, elementoCorrente)

elementoCorrente =  int(input("dammi un numero: "))
elementoPiùGrande=max(elementoPiùGrande, elementoCorrente)

elementoCorrente =  int(input("dammi un numero: "))
elementoPiùGrande=max(elementoPiùGrande, elementoCorrente)

print("Il più grande è: ", elementoPiùGrande)


#Versione con if
elementoPiùGrande = int(input("dammi un numero: "))
elementoCorrente =  int(input("dammi un numero: "))
if elementoCorrente > elementoPiùGrande:
    elementoPiùGrande = elementoCorrente

elementoCorrente =  int(input("dammi un numero: "))
if elementoCorrente > elementoPiùGrande:
    elementoPiùGrande = elementoCorrente

elementoCorrente =  int(input("dammi un numero: "))
if elementoCorrente > elementoPiùGrande:
    elementoPiùGrande = elementoCorrente

elementoCorrente =  int(input("dammi un numero: "))
if elementoCorrente > elementoPiùGrande:
    elementoPiùGrande = elementoCorrente

print("Il più grande è: ", elementoPiùGrande)
