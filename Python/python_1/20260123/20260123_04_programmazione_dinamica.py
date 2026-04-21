"""
Problema dei cammini

Sia data una matrice rettangolare di R righe e C colonne
Un viaggiatore è posizionato nello spigolo in alto a sinistra della matrice
Quanti percorsi diversi esistono che lo portano allo spigolo in basso a destra?
Il viaggiatore può andare esclusivamente nella casella sotto o nella casella a destra

Regole spostamenti: Soltanto + 1 per coordinata
Ovvero spostamento a destra (asse X) e sotto (asse Y)
"""

# Funzione opzionale per creare una matrice
def create_matrix(rows, columns):
    """
    Genera una lista di tuple, ovvero coordinate: (X riga, Y colonna)
    """
    matrix = []

    # Loop creazione righe
    for row in range(1, rows + 1):

        # Loop per creazione coordinate in una singola riga
        for j in range(1, columns + 1):
            # Tuple coordinate contenente riga e colonna
            coo = (row, j)
            matrix.append(coo)

    return matrix

m1 = create_matrix(8, 16)
# print(m1)


# È possibile eseguire questa funzione senza una matrice,
# passando direttamente il numero di righe e colonne
"""
def recursive_find_paths(rows, cols):
    all_paths = [] # Insieme dei percorsi noti

    start = (1, 1)
    target = (rows, cols)
    print(f"Coordinata di partenza: {start}", f"Coordinata di arrivo: {target}", sep="\n")

    # Calcolo ricorsivo con percorsi
    def backtrack(path, r, c):

      # Se siamo arrivati al target
      if (r, c) == target:
        # Aggiungiamo il percorso trovato
        all_paths.append(path[:])
        return

      # Altrimenti, spostamento a destra
      if r < rows:
        # Ricorsione con nuova coordinata
        backtrack(path + [(r + 1, c)], r + 1, c)

      # Altrimenti, spostamento in basso
      if c < cols:
        # Ricorsione con nuova coordinata
        backtrack(path + [(r, c + 1)], r, c + 1)

    backtrack([start], 1, 1)
    return len(all_paths), all_paths


rows = m1[len(m1) - 1][0]
cols = m1[len(m1) - 1][1]

num1, paths1 = recursive_find_paths(rows, cols)

for i, p in enumerate(paths1, 1):
  print(f"Percorso {i}: {p}")

print(f"Numero percorsi trovati: {num1}")
"""


def find_all_paths(rows, cols):
    start = (1, 1)
    target = (rows, cols)
    all_paths = []

    # Lo stack contiene il percorso attuale da valutare
    # Contiene tuple: (posizione_attuale, percorso_finora)
    stack = []
    stack.append((start, [start]))

    while stack:
        current, path = stack.pop()  # Estrae l'ultimo elemento (LIFO)
        x, y = current # Estrae singole coordinate

        # Se siamo arrivati alla fine
        if current == target:
            # Aggiungere il percorso
            all_paths.append(path)
            continue

        # Spostamento "verso destra": incremento coordinata x
        if x < rows:
            stack.append(((x + 1, y), path + [(x + 1, y)]))

        # Spostamento "verso il basso": incremento coordinata y
        if y < cols:
            stack.append(((x, y + 1), path + [(x, y + 1)]))

    return len(all_paths), all_paths

rows = m1[len(m1) - 1][0]
cols = m1[len(m1) - 1][1]

num2, paths2 = find_all_paths(rows, cols)

for i, p in enumerate(paths2, 1):
  print(f"Percorso {i}: {p}")

print(f"Numero percorsi trovati: {num2}")
