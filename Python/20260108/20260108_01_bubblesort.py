
#, Numeri da input
# numbers = [int(input("Quanti numeri vuoi inserire? "))]

# for _ in range(0, len(numbers)):
#   num = int(input("Inserisci un numero: "))
#   numbers.append(num)

# print(numbers)


#, Bubble classico
numbers = [3, 4, 2, 5, 1, 7]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Scambio tradizionale a tre variabili
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

            # Oppure, scambio degli elementi in stile Python
            # numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)


#, Bubble ottimizzato con flag
# numbers = [3, 4, 2, 5, 1, 7]

# for i in range(len(numbers)):
#     swapped = False
#     for j in range(0, len(numbers) - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#     if not swapped:
#         break

# print(numbers)