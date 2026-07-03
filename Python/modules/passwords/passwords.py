from sys import exit
from random import randint

"""
NOTA BENE: NESSUNA DI QUESTE FUNZIONI DEVE MAI ESSER UTILIZZATA PER GENERARE UNA PASSWORD REALE. 

QUESTE FUNZIONI NON UTILIZZANO DEGLI ALGORITMI DI HASHING / RANDOMIZZAZIONE ROBUSTI,
E LE PASSWORD VERREBBERO INDOVINATE CON UN PO' DI BRUTEFORCE.

QUESTO È SOLO UN MODULO DI ESERCITAZIONE.

Suggerimenti per gli esercizi:
- Tutti i caratteri devono trovarsi nell'alfabeto ASCII, definiti di seguito.
- Modularizzare il codice in opportune funzioni riutilizzabili.
- Modulo python suggerito: random. DA NON USARE MAI IN PRODUZIONE.
- In caso di violazioni dei requisiti, lanciare esclusivamente errori con raise, non assert.

- BONUS 1: definire una funzione get_password_composition che prende una stringa e ritorna un dizionario di carattere: numero occorrenze.
  - BONUS 1.1: Aggiungere un parametro ignore_case e contare i caratteri sia in case insensitive che sensitive.

- BONUS 1: definire delle classi di eccezioni personalizzate e lanciarle quando necessario.
- BONUS 3: Modularizzare il codice: definire le funzioni in questo file, le eccezioni in un altro, i test in un altro ancora.
"""

# Alfabeto senza accenti e numeri arabi
maiuscole = {chr(c) for c in range(65, 91)}    # A-Z
minuscole = {chr(c) for c in range(97, 123)}   # a-z
numeri    = {chr(c) for c in range(48, 58)}    # 0-9

# caratteri speciali "stampabili" divisi per blocco ASCII
speciali_1 = {chr(c) for c in range(33, 48)}   # ! " # $ % & ' ( ) * + , - . /
speciali_2 = {chr(c) for c in range(58, 65)}   # : ; < = > ? @
speciali_3 = {chr(c) for c in range(91, 97)}   # [ \ ] ^ _ `
speciali_4 = {chr(c) for c in range(123, 127)} # { | } ~


"""
1. Creare una funzione password_generator che generi una password randomica tra 8 e 16 caratteri.

Requisiti:
  - La password deve contenere caratteri minuscoli e maiuscoli.
  - Se presenti delle vocali, modificarle con dei numeri. 
      - Es: a = 4, e = 3, i = 1, o = 0, u = carattere a piacere. 
      - Non tutte le vocali devono essere modificate contemporaneamente. Randomizzarle.
  - Non utilizzare caratteri speciali, al momento.
  - Possono esistere al massimo due caratteri uguali di seguito, case-insensitive
"""

def check_password_len(pass_len: int, min_len=8, max_len=16) -> bool: 
    if min_len <= pass_len <= max_len:
      return True
    else: 
      return False
      

def generate_alphabet() -> set[str]:
  alfa = maiuscole | minuscole
  return alfa


def get_char_from_alphabet(pos: int) -> str:
  alfa = list(generate_alphabet())
  result = alfa[pos]
  return result


def password_generator() -> str:

  result = ""
  passw_len = 0
  # Ciclo scaramantico
  while True:
    passw_len = randint(8, 16)
    if check_password_len(passw_len):
      break

  # Cambiare condizione. Verificare fin quando la stringa non ha esattamente passwd_len 
  i = 0
  while len(result) < passw_len:
    # Prendere randomicamente un carattere dall'alfabeto
    pos = randint(0, len(generate_alphabet()) - 1)
    char = get_char_from_alphabet(pos)

    # Verifica dell'uguaglianza dei caratteri
    # saltiamo il primo ciclo perché non possiamo confrontare
    if len(result) == 1:
      result += char
      i += 1
    # Se compaiono tre caratteri uguali, scarta e ripeti
    elif len(result) > 2 and char.lower() == result[i-1].lower() == result[i-2].lower():
     continue 
    else:
      result += char
      i += 1  
      
  return result

def get_password_length(passwd: str) -> int:
  return len(passwd)

def get_password_composition(passwd: str, ignore_case: bool = False) -> dict[str, int]:
  """Data una password, ritorna un dizionario di caratteri:
    - key: il carattere presente
    - value: numero occorrenze di quel carattere
    - ignore_case = False: il confronto è case sensitive di default
  """
  result: dict[str, int] = dict()

  i = 0
  while i < get_password_length(passwd):
    if ignore_case:
      char = passwd[i].lower() if ignore_case else passwd[i]
      if char not in result:
        result[char] = 1
      else: 
        result[char] += 1

    i += 1
 
  return result

def sort_passwd_composition(passwd: dict[str, int]) -> dict[str, int]:
  ...

"""
2. Sulla base del password_generator precedente, creare una seconda funzione 
password_generator_kw utilizzando dei parametri (keyword arguments) per 
modificare opzioni come:

- Lunghezza minima non inferiore a 8 caratteri
- Lunghezza massima non superiore a 1024 caratteri
- Possibilità di passare diversi dizionari di caratteri tra cui scegliere
  - Per ogni dizionario si può scegliere un numero di caratteri, default = 0 (dizionario non scelto)
- Possibiltà di abilitare solo caratteri maiuscoli, minuscoli, o case-insensitive
- Possibilità di modificare le vocali con dei numeri. 
    - Es: a = 4, e = 3, i = 1, o = 0, u = carattere a piacere. 
    - Non tutte le vocali devono essere modificate contemporaneamente. Randomizzarle.
"""



"""
3. Creare una funzione passphrase_generator sempre con keyword arguments con i seguenti requisiti:

- Lunghezza minima delle parole: 5 caratteri
- Lunghezza massima delle parole: 12 caratteri
- Numero minimo di parole: 3
- Numero massimo di parole: 8
- Scelta del separatore tra un insieme ben preciso di caratteri
- Possibilità di modificare le vocali con dei numeri. 
    - Es: a = 4, e = 3, i = 1, o = 0, u = carattere a piacere. 
    - Non tutte le vocali devono essere modificate contemporaneamente. Randomizzarle.
"""



"""
4. Utilizzare il modulo secrets per generare una vera password robusta.
- Documentarsi sulla differenza tra random e secrets, e sul perché
  quest'ultimo sia adatto a scopi crittografici mentre random no.
- Creare una funzione che generi una password sicura usando 
  secrets.choice() su un alfabeto a scelta.
- Confrontare le prestazioni/usabilità con secrets.token_urlsafe() 
  e secrets.token_hex().
- BONUS: implementare un controllo di robustezza minima 
  (es. tramite secrets.compare_digest() per confronti sicuri, 
  utile a evitare timing attack in fase di verifica).
"""


def main() -> int:
    passwd1 = password_generator()
    print(f"Password generata = {passwd1} di {get_password_length(passwd1)} caratteri, composta così:")
    for k, v in get_password_composition(passwd1, True).items():
      print(f"\t- '{k}' appare {v} volte")


    return 0

if __name__ == "__main__":
    exit(main())
