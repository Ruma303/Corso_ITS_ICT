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


def applica(risultato, operatore, valore):
    """Applica l'operatore pendente tra risultato e valore."""
    match operatore:
        case '+': return risultato + valore
        case '-': return risultato - valore
        case '*': return risultato * valore
        case '/': return risultato / valore


def calc(inp):
    risultato = 0.0         # accumulatore
    corrente = ""           # numero che sto costruendo (stringa)
    operatore = '+'         # operatore pendente (+ iniziale così il primo numero viene sommato a 0)
    state = 0

    # Stati:
    #   0 = in attesa di un numero (stato iniziale, o appena ricevuto un operatore)
    #   1 = sto leggendo la parte intera di un numero
    #   2 = sto leggendo la parte decimale di un numero (dopo il '.')

    for char in inp:
        match state:

            case 0:  # In attesa — nessun numero in costruzione
                match char:
                    case char if char in ['0','1','2','3','4','5','6','7','8','9']:
                        corrente += char
                        state = 1
                    case char if char == '.':
                        corrente += char
                        state = 2
                    case char if char in ['+', '-', '*', '/']:
                        # Cambio operatore pendente (es. se premo * poi + poi -, vale -)
                        operatore = char
                        state = 0
                    case char if char == '=':
                        # Nessun nuovo numero inserito: restituisco il risultato attuale
                        return risultato

            case 1:  # Parte intera del numero
                match char:
                    case char if char in ['0','1','2','3','4','5','6','7','8','9']:
                        corrente += char
                        state = 1
                    case char if char == '.':
                        corrente += char
                        state = 2
                    case char if char in ['+', '-', '*', '/']:
                        # Ho un numero completo: eseguo il calcolo pendente
                        risultato = applica(risultato, operatore, float(corrente))
                        corrente = ""           # resetto il numero corrente
                        operatore = char        # salvo il nuovo operatore
                        state = 0
                    case char if char == '=':
                        risultato = applica(risultato, operatore, float(corrente))
                        return risultato

            case 2:  # Parte decimale del numero
                match char:
                    case char if char in ['0','1','2','3','4','5','6','7','8','9']:
                        corrente += char
                        state = 2
                    case char if char == '.':
                        # Punto duplicato: lo ignoro, resto nello stato 2
                        state = 2
                    case char if char in ['+', '-', '*', '/']:
                        risultato = applica(risultato, operatore, float(corrente))
                        corrente = ""
                        operatore = char
                        state = 0
                    case char if char == '=':
                        risultato = applica(risultato, operatore, float(corrente))
                        return risultato

    # Se l'input finisce senza '=', restituisco comunque il risultato
    return risultato


def main():
    ris1 = calc(input1)
    print(ris1)      # 359.0 * 0.45133 = 162.02747
    ris2 = calc(input2)
    print(ris2)      # (0 - 12) + 4.02 = -7.98
    ris3 = calc(input3)
    print(ris3)      # (12.0 - 3.0) poi * senza operando → 9.0
    return 0


if __name__ == "__main__":
    exit(main())