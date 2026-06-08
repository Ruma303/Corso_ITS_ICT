def Stampa(n):
    a=10
    b=20
    return a+b

Stampa(10)
Stampa(20)

""" NB: quanto dico va applicato al linguaggio C non a PYTHON
Quando viene eseguita l'istruzione alla riga 6, nello stack ci va scritto 7 (che è l'indirizzo di ritorno)
Quando parte la funzione Stampa, essa sa che gli servono due variabili (a e b) e quindi nello stack ci mette lo spazio per
memorizzare il valore di a e il valore di b
Quando si esegue la return, allora
1) viene tolto dallo stack lo spazio riservato alle due variabili a e b
2) viene letto nello stack l'indirizzo di ritorno """

"""
Attacco buffer overflow
Supponiamo che la funzione chiama utilizzi una stringa per gestire l'input da tastiera
def Funzione():
    s = input("Inserire una stringa: ")
    ...
    return

Ovviamente lo spazio necessario a s (che in linguaggio C è 
necessariamente detifinito a priori. Es: 32 caratteri, 256 caratteri...)
viene allocato nello stack
Se ora l'utente inserisce una stringa più lunga di 32 caratteri (o di 256 caratteri) la parte finale non sarà tolta dalla funzione (che togli solo i 32 o i 256 caratteri definiti) e quindi i successivi 4 o 8 byte 
della stringa inserita diventano automaticamente l'indirizzo di dove tornare dallo stack.
"""


# Esempio di programma ricorsivo
# Il calcolo del fattoriale
# fattoriale di n è il prodotto dei valori da 1 a n

n=100
# scrivere il codice per calcolare il fattoriale di n
fatt=1
for i in range(2, n+1):
    fatt=fatt*i
print("Il fattoriale di ", n, " è: ", fatt)

# dato n pari a 10 calcolare la somma dei numeri da 1 a 10

N=1000000000
# somma=0
# for i in range(1, N+1):
#     somma=somma+i

print("La somma dei numeri da 1 a ", N, " è: ", N*(N+1)//2)

# Poi c'è la formulazione ricorsiva
N=10
def Fr(N):
    if N==1:
        return 1
    else:
        return N*Fr(N-1)

print("Il prodotto dei numeri da 1 a ", N, " è: ", Fr(N))

def Fibonacci(n):
    # f(n) = f(n-1) + f(n-2)
    # f(1) = 1
    # f(0) = 0
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

for i in range(1, 20):   
    print(Fibonacci(i))

#print(Fibonacci(100))

# Fibonacci iterativo
# NB: non calcola F(0)!
N=11
f1=0
f2=1
for i in range(2, N+1):
    f3=f1+f2
    f1=f2
    f2=f3

print(f2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

#Questa funziona MA non potete utilizzarla!!!
def Scambia(a, b):
    return b,a

a=10
b=20
a,b=Scambia(a, b)
print(a, b)

def BubbleSort(l):
 # l è una lista di numeri
 # il primo è l[0], l[1], l[2]...
 # len(l) è il totale dei numeri
    # quanti confronti fare?
    # numconf é il numero di confronti da fare
    for i in range(0, len(l)-1):
        # avrei potuto scrivere: for numconf in range(len(l), 1, -1)
        # ma sarebbe stato troppo oscuro da decifrare
        numconf = len(l)-1-i 
        # se len(l) fosse 6, la prima volta faccio 5
        # confronti, la seconda volta 4 ecc
        for j in range(0, numconf):
            if l[j] > l[j+1]:
                tmp=l[j]
                l[j]=l[j+1]
                l[j+1]=tmp
        # Ora in fondo c'è il valore più grande
    return l

print(BubbleSort([3,1,6,4,8,5,1,9,0,8,4,5,6]))

