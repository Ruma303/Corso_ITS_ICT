"""
Data una frase da terminale determinare se la frase è palindroma
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

def check_palindrome_v2(phrase):
  phrase_list = list(phrase) # Trasformo in lista
  test = []
  is_palindrome = False

  for i, _ in enumerate(phrase):
    # Rimuovo ogni elemento dall'ultimo e lo inserisco in test
    ele = phrase_list[len(phrase) -1 - i] # Ultimo elemento
    # Oppure, usando il metodo pop()
    test.append(ele)

  # Verifico che ogni elemento corrisponde
  for i, _ in enumerate(phrase_list):
    for j, _ in enumerate(test):
      if phrase_list[i] == test[j]:
        is_palindrome = True
      else:
        is_palindrome = False

  if is_palindrome:
    return True
  else:
    return False

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


# Test Versione 2
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

