def get_inputs():
  strings = ""
  row = input("Inserisci una frase: ")
  while True:
    if row == "":
      break

    row = input()
    strings += row + "\n"

  return strings
