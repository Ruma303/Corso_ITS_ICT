list1 = [3, 5, 6, 6, 8]
list2 = [1, 4, 6]

list3 = list1 + list2

def merge_sort(list3, p, q):
  if p < q:
    m = (p + q) // 2
    merge_sort(list3, p, m)
    merge_sort(list3, m+1, q)
    merge(list3, p, m, q)

def merge(list3, p, m, q):
  L = list3[p:m]
  R = list3[m+1:q]

  final_list = []

  # i = indice dell'array di sinistra L
  # j = indice dell'array di destra R
  # k = indice dell'array finale final_list
  i, j, k = 0, 0, 0

  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      final_list[k] = L[i]
      i = i + 1

  # Copia eventuali elementi rimasti in L e R
  while i < len(L):
    final_list[k] = L[i]
    i = i + 1
    k = k + 1

  while j < len(R):
    final_list[k] = R[j]
    j = j + 1
    k = k + 1

print(merge_sort(list3, 0, len(list3)))