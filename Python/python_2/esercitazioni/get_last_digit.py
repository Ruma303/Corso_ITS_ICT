"""
Preso un numero, ritornare la cifra nell'ultima posizione
"""

from sys import exit

def get_last_digit(number: int) -> int:
  result = number
  result = result % 10
  return result

def main() -> int:
    test = 57385
    print(get_last_digit(test))

    return 0

if __name__ == "__main__":
    exit(main())
