"""
Leggere quattro numeri da tastiera, uno per volta, e stampare il più grande di essi.
"""

num1 = int(input("Inserire numero 1: "))
num2 = int(input("Inserire numero 2: "))
num3 = int(input("Inserire numero 3: "))
num4 = int(input("Inserire numero 4: "))

"""
Variante 1
"""

"""
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"Il numero 1 più grande è {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"Il numero 2 più grande è {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"Il numero 3 più grande è {num3}")
else:
    print(f"Il numero 4 più grande è {num4}")
"""

"""
Variante 2
"""

maxnum = 0
if num1 > num2:
    maxnum = num1
    print(f"num1 è più grande e vale {num1}")
else:
    if num2 > num3:
        maxnum = num3
        print(f"num2 è più grande e vale {num2}")
    else:
        if num3 > num4:
            maxnum = num3
            print(f"num3 è più grande e vale {num3}")
        else:
            maxnum = num4
            print(f"num4 è più grande e vale {num4}")
