# Stampare la tabellina del 7

def tabellina(num):
  print("Tabellina del ", num, " da 1 a 10")
  for n in range(1, 11):
    print(f"\t{num} * {n} = ", num * n)
  print()

tabellina(1)
tabellina(2)
tabellina(3)
tabellina(4)
tabellina(5)
tabellina(6)
tabellina(7)
tabellina(8)
tabellina(9)
tabellina(10)


# prendere un numero in input e stampare su una riga la tabellina 20 iterazioni

num = int(input("Dammi un numero: "))
res = []

for i in range(1, 21):
  mul = i * num
  print(mul, end=" ")

 # Oppure appendendo in una lista

  # res.append(mul)

# print(f"Tabellina del {num} da 1 a 20 iterazioni: {res}")



