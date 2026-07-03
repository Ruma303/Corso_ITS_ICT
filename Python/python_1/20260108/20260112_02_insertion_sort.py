"""
Versione iterativa

"""

array1 = [8, 4, 34, 6, 86, 4, 0]

# Si parte dall'indice 1 (secondo elemento)
for i in range(1, len(array1)): 
    value = array1[i]
    j = i - 1
    while j >= 0 and array1[j] > value:
        array1[j + 1] = array1[j]  # Shift a destra degli elementi maggiori
        j -= 1
    array1[j + 1] = value  # Inserimento dell'elemento nella posizione corretta

print(array1)

"""
Versione ricorsiva

"""
def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    value = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > value:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = value

array2 = [8, 4, 34, 6, 86, 4, 0]
insertion_sort_recursive(array2)
print(array2)
