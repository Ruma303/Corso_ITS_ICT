"""
Algoritmo Insertion Sort iterativo

PSEUDOCODICE

function insertionSortIterativo(array A)
    for i ← 1 to length[A] do
      value ← A[i]
      j ← i-1
      while j >= 0 and A[j] > value do
            A[j + 1] ← A[j]
            j ← j-1
      A[j+1] ← value;
"""

array1 = [8, 4, 34, 6, 86, 4, 0]

for i in range(0, len(array1)):
  value = array1[i]
  j = value - 1
  while j >= 0 and array1[j] > value:
    array1[j + 1] = array1[j]
    j = j + 1
  array1[j + 1] = value

print(array1)



"""
Algoritmo Insertion Sort ricorsivo

PSEUDOCODICE

function insertionSortRicorsivo(array A, int n)
    if n>1
      insertionSortRicorsivo(A,n-1)
      value ← A[n-1]
      j ← n-2
      while j >= 0 and A[j] > value
        do A[j + 1] ← A[j]
          j ← j-1
      A[j+1] ← value
"""