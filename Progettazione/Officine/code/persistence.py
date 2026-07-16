import json
from uuid import UUID

from datatypes import CodiceFiscale
from classes import Citta, Nazione, Regione
datafile = "data.json"


def load_all():
    print(f"Loading data file '{datafile}':")
    try:
        fp = open(datafile, "rt")
        data: dict = json.load(fp)
        fp.close()

        
        try:
            for k, obj in data.get("Nazioni", {}).items():
                try:
                    Nazione.create_from_dict(k, obj)
                except Exception as ex:
                    print(f"Error nazione {k}: {ex}")
            print(" - Nazioni loaded")
        except Exception:
            pass

        try:
            for k, obj in data.get("Regioni", {}).items():
                try:
                    Regione.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error regione {k}: {ex}")
            print(" - Regioni loaded")
        except Exception:
            pass

        try:
            for k, obj in data.get("Citta", {}).items():
                try:
                    Citta.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error citta {k}: {ex}")
            print(" - Città loaded")
        except Exception:
            pass

      
            
    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(f"Error: {ex}")


def save_all():
    print(f"Saving data file '{datafile}':")
    try:
        data = {
            "Nazioni": {},
            "Regioni": {},
            "Citta": {},
        }
        for n in Nazione.all_objects_by_nome():
            k, d = n.to_json()
            data["Nazioni"][k] = d
        for r in Regione.all_objects_by_uuid():
            k, d = r.to_json()
            data["Regioni"][k] = d
        for c in Citta.all_objects_by_uuid():
            k, d = c.to_json()
            data["Citta"][k] = d

        fp = open(datafile, "wt")
        json.dump(data, fp, indent=2, sort_keys=True)
        fp.close()
    except Exception as ex:
        print(f"Error saving: {ex}")
