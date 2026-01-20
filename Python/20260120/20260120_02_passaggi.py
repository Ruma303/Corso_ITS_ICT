"""
Passaggio per valore: copia del valore
Durante il passaggio di valori primitivi / scalari come interi, booleani
"""

num = 100

def cambia_num(num):
  num *= num
  return num

cambia_num(num)
print(num)


"""
Passaggio per riferimento
Durante il passaggio di valori complessi come liste, tuple, dizionari etc.
"""

num_ref = [100]

def cambia_num_ref(num):
  num[0] *= num[0]
  return num

cambia_num_ref(num_ref)
print(num_ref)

