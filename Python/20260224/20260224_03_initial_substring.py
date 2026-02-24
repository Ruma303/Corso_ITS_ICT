'''
Initial substring

Scrivere un programma Python che, date due stringhe, string e accept,
scriva a schermo la porzione iniziale più lunga di string che contiene
solo caratteri che occorrono in accept.
Ad esempio, con string = "ciao mondo" e accept = "moia oc",
il programma deve scrivere a schermo "ciao mo".

Successivamente, modificare il programma di modo che:
 - definisca una opportuna funzione
       initial_substring(string:str, accept:str)->str
   che effettua il calcolo e restituisce il risultato
 - prenda l'input dell'utente (i valori per string e accept) da tastiera,
   invochi la funzione e ne stampi il risultato a schermo.
'''

string = input("Inserisci una stringa: ").strip()
accept = input("Inserisci una sottostringa di ricerca: ").strip()

def find(string, accept):
  result = ""

  for idx, char in enumerate(accept):
    if char in string:
      result += accept[idx]

  return result, len(result)

str_res, str_len = find(string, accept)

print(f"Stringa più lunga trovata {str_res} di lunghezza {str_len}")
