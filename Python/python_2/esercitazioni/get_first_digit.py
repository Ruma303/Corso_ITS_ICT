"""
Preso un numero, ritornare la cifra nella prima posizione
"""

from sys import exit
from num_digits import num_digits

def get_first_digit(number: int) -> int:
  temp = number
  len_digits = num_digits(number) - 1
  divider = 1 * (10 ** len_digits)
  result = temp // divider
  return result

def main() -> int:
    test = 27385
    print(get_first_digit(test))

    return 0

if __name__ == "__main__":
    exit(main())
