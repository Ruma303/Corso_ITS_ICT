"""
Generazione di una password "semplice" tramite
l'unione di caratteri alfabetici casuali

BONUS: Uso di vincoli quali
1. Es massimo - min tot numeri
2. Non due caratteri successivi
3. Lunghezza complessiva non superiore o inferiore ad un intervallo
"""

from random import randint, shuffle, choice

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
    alfa,
    /,  # Tipo di alfabeto (es solo numeri, solo speciali etc.)
    min_len=8,
    max_len=8,  # Lunghezza min - max dell'intera password
    # Vincoli sui set di caratteri
    can_nums=True,
    can_chars_lower=True,
    can_chars_upper=True,
    can_specials=True,
    # Vincoli lunghezze set di caratteri
    min_nums=1,
    max_nums=1,  # Quantità min - max di numeri
    min_char_lower=1,
    max_char_lower=1,  # Quantità min - max di caratteri minuscoli
    min_char_upper=1,
    max_char_upper=1,  # Quantità min - max di caratteri maiuscoli
    min_special=1,
    max_special=1,  # Quantità min - max di caratteri speciali
):

    current_password_length = max_nums + max_char_lower + max_char_upper + max_special
    # print(f"Vincoli totali: {current_password_length}")

    if max_len < min_len:
        print(
            f"La lunghezza massima {max_len} non può essere inferiore alla lunghezza minima {min_len}"
        )
        max_len = min_len
        print(f"La password sarà lunga {max_len} caratteri")

    password_length = randint(min_len, max_len)
    print(f"Lunghezza casuale password: {password_length}")

    # Gestione delle eccezioni
    try:
        if password_length < 8 or min_len < 8:
            raise Exception(
                f"Per ragioni di sicurezza la lunghezza della password dev'essere di 8 o più caratteri"
            )

        if current_password_length > max_len:
            raise Exception(
                f"L'insieme dei vincoli inseriti {current_password_length} supera la lunghezza della password da generare {max_len}"
            )

        if min_len < current_password_length < max_len:
            raise Exception(
                f"L'insieme dei vincoli inseriti {current_password_length} dev'essere compreso tra {min_len} e {max_len}"
            )

    except Exception as e:
        print()
        print("=====================")
        print("Eccezione: ", e)
        print("=====================")
        print()

    # TODO Calcolare se e quanti caratteri per ogni set
    charset_nums = []
    charset_len = len(charset_nums)
    charset_list = []

    # Set dei numeri (se non False)
    if can_nums is not False:
        # Generazione di una lunghezza per la lista di questo set di caratteri
        charset_len = randint(min_nums, max_nums + 1)
        charset_nums.append(charset_len)
        print(f"\t- {charset_nums[0]} numeri;")

        count = 0
        while count <= charset_len:
            charset_list.append(choice(numbers))
            count += 1

    # Set dei caratteri minuscoli (se non False)
    if can_chars_lower is not False:
        charset_len = randint(min_char_lower, max_char_lower + 1)
        charset_nums.append(charset_len)
        print(f"\t- {charset_nums[1]} caratteri minuscoli;")

        count = 0
        while count <= charset_len:
            charset_list.append(choice(alfa_lower))
            count += 1

    # Set dei caratteri maiuscoli (se non False)
    if can_chars_upper is not False:
        charset_len = randint(min_char_upper, max_char_upper + 1)
        charset_nums.append(charset_len)
        print(f"\t- {charset_nums[2]} caratteri maiuscoli;")

        count = 0
        while count <= charset_len:
            charset_list.append(choice(alfa_upper))
            count += 1

    # Set dei speciali (se non False)
    if can_specials is not False:
        charset_len = randint(min_special, max_special + 1)
        charset_nums.append(charset_len)
        print(f"\t- {charset_nums[3]} speciali;")

        count = 0
        while count <= charset_len:
            charset_list.append(choice(special_chars))
            count += 1


    # Elenco di lunghezze finali per ogni set
    print(f"La password sarà lunga {charset_len} caratteri.")

    # Inserire tutti i caratteri in base ai vincoli in una lista
    print(f"Tutti i caratteri da mischiare {charset_list}")

    # Mischiare la lista dei caratteri
    shuffle(charset_list)

    # Unione e ritorno della password
    return "".join(charset_list)


pass1 = password_generator(numbers)
print(f"\t- Password 1 di {len(pass1)} numeri: {pass1}")

pass2 = password_generator(all_chars, min_len=10)
print(f"\t- Password 2 di {len(pass2)} caratteri: {pass2}")

pass3 = password_generator(all_chars, min_len=16, max_len=20)
print(f"\t- Password 3 di {len(pass3)} caratteri: {pass3}")

pass_err1 = password_generator(all_chars, min_len=7, max_len=20)
print(f"\t- Password 4 di {len(pass_err1)} caratteri: {pass_err1}")

pass_no_numbers = password_generator(all_chars, min_len=16, max_len=20, can_nums=False)
print(f"\t- Password di {len(pass_no_numbers)} caratteri senza numeri: {pass_no_numbers}")