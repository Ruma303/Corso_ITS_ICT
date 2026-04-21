"""
Dato un voto in 30imi indicare se lo studente è stato bocciato,
mediocre oppure ottimo
"""

voto = int(input("Inserisci un voto: ").strip())

# Sufficiente
if voto >= 18:
  if voto == 18:
    print("Voto appena sufficiente: ", voto)
    if voto < 24:
      print("Voto mediocre: ", voto)
    else:
      print("Voto ottimo", voto)
else:
  print("Prestazione insufficiente. Voto: ", voto)

# Uso di elif

# Match case
match voto:
  case 18:
    print("Voto appena sufficiente: ", voto)
  case voto if voto > 18 and voto <= 24:
    print("Voto mediocre: ", voto)
  case voto if voto > 24 and voto <= 30:
    print("Voto ottimo", voto)
  case _:
    print("Prestazione insufficiente. Voto: ", voto)