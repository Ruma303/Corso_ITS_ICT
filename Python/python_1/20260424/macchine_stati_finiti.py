"""
1. Scrivere una funzione python calc alla quale viene passato un carattere alla volta
e la funzione verifica riconoscere una semplice operazione aritmetica (+, x, /, -, =)
e quando arriva a = deve fornire il risultato

2. La funzione deve avere un comportamento simile alle usuali calcolatrice elettroniche.
"""

from sys import exit
input1 = ['0', '3', '5', '9', '.', '*', '.', '4', '5', '1', '3', '3', '=']
input2 = ['-', '1', '2', '+', '4', '.', '0', '2', '=']
input3 = ['1', '2', '.', '.', '.', '*', '+', '-', '3', '*', '=']

def calc(inp):
  op1 = ""
  op2 = ""
  state = 0

  #TODO: Definire tutti gli stati della FSM

  for char in inp:
    match state:
      case 0:
        match char:
          case char if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            op1 += char
            state = 1
          case char if char == ".":
            op1 += char
            state = 2
          case char if char in ['+', '-', '*', '/']:
            state = 0
      case 1:
        match char:
          case char if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            op1 += char
            state = 1
          case char if char == ".":
            op1 += char
            state = 2
          case char if char in ['+', '-', '*', '/']:
            state = 0


# d.c = don't care - Non è consigliato metterlo in una macchina a stati finiti ma
# riduce le dimensioni della macchina

def main():
  ris1 = calc(input1)
  print(ris1)
  ris2 = calc(input2)
  print(ris2)
  ris3 = calc(input3)
  print(ris3)
  return 0


if __name__ == "__main__":
  exit(main())