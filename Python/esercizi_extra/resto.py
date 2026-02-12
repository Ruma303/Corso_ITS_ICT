"""
Ritornare il minor numero di monete possibili
Calcolare quante monete da restituire
Indicare quante monete per tipo

Consiglio: implementare un algoritmo greedy
"""

def calculate_rest(amount, cost):
    """
    Calcola il resto restituendo la differenza amount-cost se sufficiente.
    Lavora in centesimi per precisione.
    """
    if amount < cost:
        raise ValueError(f"Il prodotto costa {cost} ma hai solo {amount}.")
    rest = round((amount - cost) + 1e-9, 2)
    return rest


def get_rest(rest, coins):
    """
    Algoritmo greedy che restituisce la composizione del resto in monete,
    minimizzando il numero totale di monete.
    - rest: il resto (float, es. 7.37)
    - coins: dict {nome_moneta: valore_float}
    - return: (int: conta totale, dict: nome_moneta -> quantità)
    """

    # Conversione in centesimi/interi per precisione
    rest_cent = int(round(rest * 100))

    # Costruire lista ordinata di tuple (nome moneta, valore_cent) decrescente
    # iterando sul set di monete (coins) passate in input
    ordered_coins = sorted( # sorted ritorna una lista ordinata
        ((name, int(round(value * 100))) for name, value in coins.items()),
        key=lambda x: -x[1] # key è un parametro che indica a sorted() per quale indice ordinare
        # Che in questo caso è il valore in centesimi cambiato di segno
    )

    # Dizionario per la risposta composta da nome moneta : quantità
    coins_type = {name: 0 for name in coins}

    for name, value in ordered_coins:
        if value == 0:
            continue
        n = rest_cent // value
        coins_type[name] = n
        rest_cent -= n * value

    if rest_cent > 0:
        # Nel caso non sia possibile rendere tutto il resto,
        # segnalare la quantità non convertita (rarissimo con set completi)
        raise ValueError(f"Resto non completamente convertibile: avanzano {rest_cent} centesimi.")

    coins_qty = sum(coins_type.values())
    return coins_qty, coins_type


# Set di valute con tagli differenti per moneta
euro = {
    "1 centesimo" : 0.01,
    "2 centesimi" : 0.02,
    "5 centesimi" : 0.05,
    "10 centesimi" : 0.10,
    "20 centesimi" : 0.20,
    "50 centesimi" : 0.50,
    "1 euro" : 1.00,
    "2 euro" : 2.00,
  }

# Tests (da pagare, pagato)
tests = [
    (20, 10),
    (20, 17.67),
    (10, 20),   # Questo solleva errore
    (200, 42.81),
]

for a, c in tests:
    try:
        rest = calculate_rest(a, c)
        num, breakdown = get_rest(rest, euro)
        print(f"\nRestituisco {rest:.2f} euro con {num} monete: {breakdown}")
    except ValueError as e:
        print(f"Errore: {e}")
