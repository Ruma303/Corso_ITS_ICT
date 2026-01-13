"""
hex1 = "0xFF"

print(int(hex1, 16))

bin1 = "0b1001"

print(int(bin1, 2))

ott1 = "0o3677"

print(int(ott1, 8))
"""

"""
Python può gestire direttamente valori numerici differenti dalla base 10 (base decimale)
All’interno di un programma a una variabile numerica posso assegnare:
Numero = 100 #assegno il numero 100 decimale
Numero = 0xA20 # Assegno il valore A20 esadecimale
Numero = 0o654 # Assegno il valore 654 in ottale
Numero = 0b10110101 # Assegno il valore 10110101 in binario
Eseguire le assegnazioni e stampare il valore assunto da Numero nei quattro casi
Inoltre Python ha due funzioni di conversione
Int (stringa, base numerica): converte un numero espresso nella base numerica data in numero decimale

Scrivere un programma che
Legge una stringa
Legge una base numerica
Stampa il numero decimale corrispondente alla stringa nella base numerica scelta
str(numero, base numerica) converte un numero intero in una stringa che è scritta nella base numerica indicata

Scrivere un programma che
Legge un numero
Legge una base numerica
Stampa il numero nella base numerica scelta
"""

Numero = 100 #assegno il numero 100 decimale
print(Numero)
Numero = '0xA20' # Assegno il valore A20 esadecimale
print(int(Numero, 16))
Numero = '0o654' # Assegno il valore 654 in ottale
print(int(Numero, 8))
Numero = '0b10110101' # Assegno il valore 10110101 in binario
print(int(Numero, 2))

"""
num = input("Inserisci un numero: ")
base = int(input("Inserisci una base: "))
conv = int(num, base)
print(f"{num} in base {base} vale: {str(conv)}")
"""

def to_base(num, base):
    """
    Converte un intero positivo num (in base 10) in una stringa rappresentante
    il numero nella base 'base' (2 <= base <= 36).
    """
    if base < 2 or base > 36:
        raise ValueError("La base deve essere compresa tra 2 e 36.")
    if num == 0:
        return '0'
    digits = []
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        print(num % base)
        digits.append(chars[num % base])
        num //= base
    return ''.join(reversed(digits))

num = int(input("Inserisci un numero: "))
base = int(input("Inserisci una base: "))
conv = to_base(num, base)
print(f"Conversione {num} in base {base}: {conv}")