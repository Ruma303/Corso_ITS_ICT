"""
Preso un nome, salutare in base al sesso
"""

nome = input("Inserisci un nome: ").strip()

def saluta(nome):
  ultimo_carattere = nome[-1]
  match ultimo_carattere:
    case ultimo_carattere if ultimo_carattere in ["a"]:
      print(f"Ciao cara {nome}")
    case ultimo_carattere if ultimo_carattere in ["o", "e"]:
      print(f"Ciao caro {nome}")

# Input dinamico
saluta(nome)

# Input statico
saluta("Michele")
saluta("Anna")
saluta("Giorgio")
saluta("Andrea") 
saluta("Ugo")