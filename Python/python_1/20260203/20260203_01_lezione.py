"""
Cosa fa questa funzione?
"""

"""
def trova(stringa, carattere):
  indice = 0
  while indice < len(stringa):
    if stringa[indice] == carattere:
      return indice
    indice = indice + 1

  return -1

res = trova("ippopotamo", "a")
print(res)
"""

"""
La funzione trova l'indice del carattere in una stringa, altrimenti ritorna -1
"""

"""
Divisione, gestire i casi estremi
"""

"""
Logging
"""
import logging

logging.basicConfig(
  level = logging.INFO,
  format = f"Log %(asctime)s: [%(levelname)s] - %(message)s",
  handlers = {
    logging.FileHandler("./Python/20260203/logs/20260203_01_logging.log"),
    logging.StreamHandler()
  }
)

numeratore = float(input("Numeratore: ").strip())
denominatore = float(input("Denominatore: ").strip())

def get_division(numeratore, denominatore):
  while True:
    divisione = 0

    try:
      divisione = numeratore / denominatore

    except ZeroDivisionError as e:
      print("Errore di tipo: ", e.__class__.__name__)
      divisione = None

    except ValueError as v:
      print("Errore di tipo: ", v.__class__.__name__)
      divisione = None

    else:
      print(f"Divisone: {divisione}")

    finally:
      print("Terminazione")

    return divisione

logging.info(get_division(numeratore, denominatore))