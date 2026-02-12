"""
Data una frase determinare se la frase è palindroma
"""

# Variante 1

frase_test_1 = "I topi non avevano nipoti"
frase_test_2 = "Amo Roma"
frase_test_3 = "Ai lati d'Italia"
frase_test_4 = "E la sete sale"

# frase_test =  input("Inserisci una frase di test: ").strip().lower()

def check_palindrome(phrase):
  # print(phrase)
  if phrase == phrase[::-1]:
    return True
  else:
    return False


# Versione 2
def check_palindrome_v2(phrase):
  n = len(phrase)
  for i in range(n // 2):
    # Verificare se il primo è diverso dall'ultimo
    # Il ciclo muove gli indici "verso l'interno" fino alla metà
    print("Verifica: ", phrase[i], phrase[n - i - 1])
    if phrase[i] != phrase[n - i - 1]:
      return False
  return True


frase_test_1_validated = frase_test_1.strip().lower().replace(" ", "").replace("'", "")
frase_test_2_validated = frase_test_2.strip().lower().replace(" ", "").replace("'", "")
frase_test_3_validated = frase_test_3.strip().lower().replace(" ", "").replace("'", "")
frase_test_4_validated = frase_test_4.strip().lower().replace(" ", "").replace("'", "")


# Test Versione 1: OK
t1v1 = check_palindrome(frase_test_1_validated)
if t1v1 == True: print(f"La frase {frase_test_1} è palindroma")
else: print(f"La frase {frase_test_1} non è palindroma")

t2v1 = check_palindrome(frase_test_2_validated)
if t2v1 == True: print(f"La frase {frase_test_2} è palindroma")
else: print(f"La frase {frase_test_2} non è palindroma")

t3v1 = check_palindrome(frase_test_3_validated)
if t3v1 == True: print(f"La frase {frase_test_3} è palindroma")
else: print(f"La frase {frase_test_3} non è palindroma")

t4v1 = check_palindrome(frase_test_4_validated)
if t4v1 == True: print(f"La frase {frase_test_4} è palindroma")
else: print(f"La frase {frase_test_4} non è palindroma")


# Test Versione 2: OK
t1v2 = check_palindrome_v2(frase_test_1_validated)
if t1v2 == True: print(f"La frase {frase_test_1} è palindroma")
else: print(f"La frase {frase_test_1} non è palindroma")

t2v2 = check_palindrome_v2(frase_test_2_validated)
if t2v2 == True: print(f"La frase {frase_test_2} è palindroma")
else: print(f"La frase {frase_test_2} non è palindroma")

t3v2 = check_palindrome_v2(frase_test_3_validated)
if t3v2 == True: print(f"La frase {frase_test_3} è palindroma")
else: print(f"La frase {frase_test_3} non è palindroma")

t4v2 = check_palindrome_v2(frase_test_4_validated)
if t4v2 == True: print(f"La frase {frase_test_4} è palindroma")
else: print(f"La frase {frase_test_4} non è palindroma")
