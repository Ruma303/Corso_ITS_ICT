import json
from uuid import UUID

from classes import Citta, Nazione, Regione

datafile = "data.json"


def load_all():
    print(f"Loading data file '{datafile}':")
    try:
        fp = open(datafile, "rt")
        data: dict = json.load(fp)
        fp.close()

        print(f" - Nazione")
        try:
            for k, obj in data.get("Nazione", {}).items():
                try:
                    n = Nazione.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error nazione {k}: {ex}")
        except Exception:
            pass

        print(f" - Regione")
        try:
            for k, obj in data.get("Regione", {}).items():
                try:
                    r = Regione.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error regione {k}: {ex}")
        except Exception:
            pass

        print(f" - Citta")
        try:
            for k, obj in data.get("Citta", {}).items():
                try:
                    c = Citta.create_from_dict(int(k), obj)
                except Exception as ex:
                    print(f"Error citta {k}: {ex}")
        except Exception:
            pass
    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(f"Error: {ex}")


def save_all():
    print(f"Saving data file '{datafile}':")
    try:
        data = {"Nazione": {}, "Regione": {}, "Citta": {}}
        for n in Nazione.all_objects():
            k, d = n.to_json()
            data["Nazione"][k] = d
        for r in Regione.all_objects():
            k, d = r.to_json()
            data["Regione"][k] = d
        for c in Citta.all_objects():
            k, d = c.to_json()
            data["Citta"][k] = d
        fp = open(datafile, "wt")
        json.dump(data, fp, indent=4, sort_keys=True)
        fp.close()
    except Exception as ex:
        print(f"Error saving: {ex}")
