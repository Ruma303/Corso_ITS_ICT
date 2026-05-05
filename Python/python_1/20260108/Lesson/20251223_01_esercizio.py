# calcolare la lunghezza della più lunga sequenza di numeri che si alternano: maggiore del precedente, minore del precedente, .... Esempio: (3 2 5 6 10 1 2 7 0): 3 (3 2 5 poiché 3>2, 2<5, )

def calcola_sequenza_alternata():
    max_lunghezza = 1
    corrente_lunghezza = 1
    precedente=int(input("Inserisci un numero: "))
    # Stato della relazione precedente: 
    # 1 se il precedente era 'maggiore di', -1 se 'minore di', 0 all'inizio
    last_relation = 0 
    
    while True:
        corrente=int(input("Inserisci un numero: "))
        if corrente > precedente:
            new_relation = 1  # Crescente
        elif precedente > corrente:
            new_relation = -1 # Decrescente
        else:
            new_relation = 0  # Numeri uguali (rompono l'alternanza)

        # Se la relazione è diversa dalla precedente e non è un numero uguale
        if new_relation != 0 and new_relation != last_relation:
            if corrente_lunghezza == 1:
                corrente_lunghezza = 2
            else:
                corrente_lunghezza += 1
            last_relation = new_relation
        else:
            # Se l'alternanza si rompe, ricominciamo
            # Se i due numeri sono diversi, la nuova sequenza parte da 2
            if new_relation != 0:
                corrente_lunghezza = 2
                last_relation = new_relation
            else:
                corrente_lunghezza = 1
                last_relation = 0
        max_lunghezza = max(max_lunghezza, corrente_lunghezza)
        print("Per ora max_lunghezza: ", max_lunghezza)
        precedente=corrente



# Input della sequenza principale
print("Inserisci i numeri della sequenza, uno per riga")
calcola_sequenza_alternata()
