"""
Un numero primo è un numero intero maggiore di 1 che ha esattamente due divisori:
se stesso e 1
"""

import logging
from math import sqrt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s]: %(message)s",
    handlers={
        logging.FileHandler("./Python/20260203/logs/20260203_02_primes.log"),
        logging.StreamHandler(),
    },
)

num = int(input("Inserisci un numero: ").strip())

def is_prime(num):

    if num <= 1:
        logging.error(f"{num} non può essere un numero zero o negativo")
        print(f"{num} è 0 o negativo")
        return False

    if num == 2:
        print(f"{num} è 2, unico numero pari che è primo")
        return True

    if num % 2 == 0:
        print(f"{num} è pari e non può essere primo")
        return False

    rad = sqrt(num)
    for ele in range(2, int(rad) + 1):

      if num % ele == 0:
          return False
    return True

res = is_prime(num)

if res == True:
    logging.info(f"NUMERO PRIMO: {num}")
else:
    logging.error(f"NUMERO NON PRIMO: {num}")
