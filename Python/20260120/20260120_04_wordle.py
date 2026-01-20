"""
Indovinare la parola segreta entro un certo numero di tentativi.

STRIKE = verdi = lettera giusta in posizione corretta = 2 punti
BALL = gialli = lettera giusta in posizione sbagliata = 1 punto
GRAY = grigi = lettera provata ma errata              = 0 punti
BLACK = neri = lettera non ancora provata

"""


"""
Un’operazione che in Wordle può essere considerata fondamentale è quella di calcolare, date 2 parole (quella nascosta e quella che coorrisponde al tentativo del giocatore),
Il numero di strike, quante lettere sono presente nel posto corretto
Il numero di ball, quante lettere ci sono ma nel posto sbagliato
NB: per semplicità viene pubblicato la lunghezza della parola corretta
Esempio
                     paralipomeni (parola segreta)
Prova 1              parallelette 5 strike, 1 ball
Prova 2              paralpineini 7 strike, 2 ball
Quindi dovere realizzare la funzione
Calcola(segreta, prova) => (strike, ball)
Suggerimento gli Strike sono più importanti dei Ball

"""

# num_tentativi = 10

parola = "paralipomeni"
word_len = len(parola)

print(f"La parola segreta ha {word_len} caratteri")
# scelta = input("Inserire una parola: ").strip()

def calcola(segreta, prova):
  strikes, balls, grey, blacks = 0, 0, 0, 0

  copia_segreta = list(segreta)
  copia_scelta = list(prova)

  coppie = zip(copia_segreta, copia_scelta)

  """
  if prova not in segreta:
    print("Nessuna lettera si trova nella parola segreta")
    return
  """

  # Iterare sulla parola segreta
  for (primo, secondo) in coppie:

    # IF Se c'è un match per posizione, allora è uno strike
    if primo == secondo:
      strikes += 1
      print("strikes: ", primo, secondo)

    # ELIF Se una lettera si trova nella parola segreta, allora è un ball
    elif secondo in copia_segreta:
      balls += 1
      print("ball: ", primo, secondo)

    # ELSE grigio: lettera non combacia
    elif secondo not in copia_segreta:
      grey += 1
      print("gray: ", primo, secondo)

    # Lettera non usata
    else:
      blacks += 1
      print("black: ", primo, secondo)

  print(f"Hai trovato {strikes} strikes, {balls} balls, {grey} grigi e {blacks} neri")


calcola(parola, "paralipomeni") # Corrispondenza completa
calcola(parola, "parailpomeni") # Corrispondenza parziale
calcola(parola, "03423") # Nessun match


calcola("abcabcabc", "cabcbacab") # Nessun match