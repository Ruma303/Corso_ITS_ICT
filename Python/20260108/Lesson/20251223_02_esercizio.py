def max_alternating_fsm():

    # Definizione degli stati
    INIZIO = "INIZIO"
    VERSO_ALTO = "VERSO_ALTO"
    VERSO_BASSO = "VERSO_BASSO"

    stato = INIZIO
    current_len = 1
    max_len = 1

    a=int(input("Inserisci un numero: "))
    while True:
        b = int(input("Inserisci un numero: "))

        if stato == INIZIO:
            if b > a:
                stato = VERSO_BASSO
                current_len = 2
            elif b < a:
                stato = VERSO_ALTO
                current_len = 2
            else:
                current_len = 1 # Numeri uguali, restiamo in START

        elif stato == VERSO_ALTO:
            if b > a:
                stato = VERSO_BASSO
                current_len += 1
            elif b < a:
                current_len = 2 
            else:
                stato = INIZIO
                current_len = 1

        elif stato == VERSO_BASSO:
            if b < a:
                stato = VERSO_ALTO
                current_len += 1
            elif b > a:
                # Due salite di fila: reset del conteggio a 2 (la nuova salita).
                current_len = 2
            else:
                stato = INIZIO
                current_len = 1

        # Aggiorniamo il massimo globale a ogni passo
        max_len = max(max_len, current_len)
        print("Per ora max_lunghezza: ", max_len)
        a=b

print("Inserisci i numeri della sequenza, uno per riga")
risultato = max_alternating_fsm()
