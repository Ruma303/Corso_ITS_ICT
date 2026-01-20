"""
Generazione di una password "semplice" tramite
l'unione di caratteri alfabetici casuali

BONUS: Uso di vincoli quali
1. Es massimo - min tot numeri
2. Non due caratteri successivi
3. Lunghezza complessiva non superiore o inferiore ad un intervallo
4. Altri vincoli a piacere
"""

from random import randint, shuffle, choice

# Alfabeti
numbers = "0123456789"
idx = randint(0, len(numbers))

alfa_lower = "abcdefghijklmnopqrstuvwxyz"
idx = randint(0, len(alfa_lower))

alfa_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
idx = randint(0, len(alfa_upper))

special_chars = "!@#$%&*,;.:-_+/\\|\"'?^§[](){}"
idx = randint(0, len(special_chars))

# Tutti i caratteri (insieme di tutti gli alfabeti)
all_chars = alfa_upper + alfa_lower + numbers + special_chars


# Numero casuale da un alfabeto
def rand_char(alfa):
    return alfa[randint(0, len(alfa) - 1)]


def password_generator(
    # Tipo di alfabeto (es solo numeri, solo speciali etc.)
    min_len=8,
    max_len=8,  # Lunghezza min - max dell'intera password
    # Vincoli lunghezze set di caratteri
    min_nums=1,
    max_nums=1,  # Quantità min - max di numeri
    min_char_lower=1,
    max_char_lower=1,  # Quantità min - max di caratteri minuscoli
    min_char_upper=1,
    max_char_upper=1,  # Quantità min - max di caratteri maiuscoli
    min_special=1,
    max_special=1,  # Quantità min - max di caratteri speciali
    # Numero di shuffle
    shuffle_nums=1,
):
    # Quantità di vincoli, oltre la password stessa
    constraints_length = max_nums + max_char_lower + max_char_upper + max_special
    print(f"Vincoli totali: {constraints_length}")

    # Controllo lunghezza password
    if min_len > 128 or max_len > 128:
        print(f"Lunghezza massima della password consentita: 128")
        min_len = 128

    if max_len < min_len:
        print(f"La lunghezza massima {max_len} non può essere inferiore alla lunghezza minima {min_len}")
        max_len = min_len
        print(f"La password sarà lunga {max_len} caratteri")

    # Altri controlli simili
    if max_nums < min_nums:
        max_nums = min_nums

    if max_char_lower < min_char_lower:
        max_char_lower = min_char_lower

    if max_char_upper < min_char_upper:
        max_char_upper = min_char_upper

    if max_special < min_special:
        max_special = min_special

    password_length = randint(min_len, max_len)
    print(f"Lunghezza finale password: {password_length}")

    # Gestione delle eccezioni
    try:
        if password_length < 8 or min_len < 8:
            raise Exception(
                f"Per ragioni di sicurezza la lunghezza della password dev'essere di 8 o più caratteri"
            )

        if constraints_length > max_len:
            raise Exception(
                f"L'insieme dei vincoli inseriti {constraints_length} supera la lunghezza della password da generare {max_len}"
            )

        if not (min_len < constraints_length < max_len):
            raise Exception(
                f"La lunghezza della password {constraints_length} dev'essere compresa tra 8 e 128 caratteri"
            )

    except Exception as e:
        print()
        print("=====================")
        print("Eccezione: ", e)
        print("=====================")
        print()

    # Calcolare quanti caratteri per ogni set
    charset_nums = []  # Lista contenente il numero per ogni set di caratteri
    charset_len = len(charset_nums)
    charset_list = []  # Lista di caratteri completa

    # TODO rilevare quali sono i set di caratteri utilizzabili
    # Eseguire primo round di set obbligatori

    # Set dei numeri
    if max_nums > 0:
        # Generazione di una lunghezza per la lista di questo set di caratteri
        charset_len = randint(min_nums, max_nums + 1)
        charset_nums.append(charset_len)

        for _ in range(charset_len):
            charset_list.append(choice(numbers))

    # Set dei caratteri minuscoli
    if max_char_lower > 0:
        charset_len = randint(min_char_lower, max_char_lower + 1)
        charset_nums.append(charset_len)

        for _ in range(charset_len):
            charset_list.append(choice(alfa_lower))

    # Set dei caratteri maiuscoli
    if max_char_upper > 0:
        charset_len = randint(min_char_upper, max_char_upper + 1)
        charset_nums.append(charset_len)

        for _ in range(charset_len):
            charset_list.append(choice(alfa_upper))

    # Set dei speciali
    if  max_special > 0:
        charset_len = randint(min_special, max_special + 1)
        charset_nums.append(charset_len)

        for _ in range(charset_len):
            charset_list.append(choice(special_chars))

    # Secondo round, riempire i rimanenti caratteri con i set consentiti

    # password_length


    # Inserire tutti i caratteri in base ai vincoli in una lista
    print(f"Tutti i caratteri da mischiare {charset_list}")

    # Mischiare la lista dei caratteri
    if shuffle_nums > 15:
        shuffle_nums = 15
        print(f"Massimo numero di shuffle = 15")
    elif shuffle_nums < 10:
        shuffle_nums = 10
        print(f"Minimo numero di shuffle = 10")
    else:
        shuffle(charset_list)

    for _ in range(shuffle_nums + 1):
        shuffle(charset_list)

    # Unione e ritorno della password sottoforma di stringa
    return "".join(charset_list)


pass1 = password_generator()
print(f"\t- Password 1 di {len(pass1)} numeri: {pass1}\v")

pass2 = password_generator(min_len=10)
print(f"\t- Password 2 di {len(pass2)} caratteri: {pass2}\v")

pass3 = password_generator(min_len=16, max_len=20)
print(f"\t- Password 3 di {len(pass3)} caratteri: {pass3}\v")

pass_err1 = password_generator(min_len=7, max_len=20)
print(f"\t- Password 4 di {len(pass_err1)} caratteri: {pass_err1}\v")

pass_no_numbers = password_generator(min_len=16, max_len=20, max_nums=0)
print(f"\t- Password di {len(pass_no_numbers)} caratteri senza numeri: {pass_no_numbers}\v")

pass_4 = password_generator(min_len=16, max_len=20, max_char_lower=4, min_special=3, shuffle_nums=20)
print(f"\t- Password di {len(pass_4)} caratteri generici: {pass_4}\v")

pass_5 = password_generator(min_len=700, max_char_lower=4, min_special=3, shuffle_nums=3)
print(f"\t- Password di {len(pass_5)} caratteri generici: {pass_5}\v")
