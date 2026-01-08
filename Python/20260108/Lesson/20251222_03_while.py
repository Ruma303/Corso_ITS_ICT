# # Esempio
# 3
#     - dispari!
#     - media=3
# 6
#     - pari!
#     - media = 4.5
# 8
#     - pari!
#     media = 8.5
# 2
# 3
# 3

# Inizializza la somma dei numeri a 0
# ogni numero che legge lo somma a questo totale
# Inizializza un contatore che conta quanti
# numeri sono stati letti. Mi serve per fare 
# totale/contatore = media
totale=0
contatore=0
while True:
    # leggo un numero
    n=int(input("Numero: "))
    if n % 2 == 0:
        print("Numero ", n, " è pari.")
    else:
        print("Numero ", n, " è dispari.")
    # Oltre all'operatore modulo (%) c'è anche l'operatore
    # "divisione intera" che si esprime con //
    # 9 / 2 => 4.5
    # 9 // 2 => 4
    
    # calcolo se pari o dispari
    # stampo se pari o dispari
    contatore = contatore + 1 #vado al prossimo valore
    totale = totale + n   # incremento il totale
    print("Media: ", totale/contatore)

    # calcolo la media con i valori precedenti
    # stampo la media

