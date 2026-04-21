# Disegnare una piramide specificando altezza e carattere da stampare

def draw_pyramid(height, symbol):
    for i in range(height):
        spaces = height - i - 1
        symbols = 2 * i + 1
        print(" " * spaces + symbol * symbols)


if __name__ == "__main__":
  height = int(input("Indica l'altezza della piramide: ").strip())
  symbol = input("Inserisci un simbolo che vuoi ripetere: ").strip()

  draw_pyramid(height, symbol)