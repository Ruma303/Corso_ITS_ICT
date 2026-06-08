# Anche per i dizionari, come per i set, l'ordine è efficientato.
# L'univocità questa volta è garantito dalle chiavi di accesso (che sono hashate tramite un algoritmo di hashing)

d1 = { "uno": 1, "due": 2, "tre": 3, "quattro": 4, "uno": 20 }

print(d1) # {'uno': 20, 'due': 2, 'tre': 3, 'quattro': 4}
# Anche i dizionari non accettano doppioni come chiavi
# Verrà creata una chiave ma il valore verrà sovrascritto con quello l'ultima chiave

d2 = d1 | {
  "name": [1, True, "Java", (23, 41)],
  "age": 30,
  "birthday": 19850230,
  4: "Quattro", # Le chiavi non sono necessariamente stringhe
  "uno": "hallo"
}
print(d2.keys())


d2["zero"] = 0
print(d2.keys())

d3 = {
  "d1": d1,
  "d2": d2
}

print()
print(d3.items())
print(d3.keys())
print(d3.values())