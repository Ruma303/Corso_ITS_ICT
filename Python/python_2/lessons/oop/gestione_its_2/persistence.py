import json
from uuid import UUID

from datatypes import CodiceFiscale
from classes import Citta, Nazione, Regione, AreaDisciplinare, Docente, Studente, Modulo, CorsoITS

datafile = "data.json"


def load_all():
    print(f"Loading data file '{datafile}':")
    try:
        fp = open(datafile, "rt")
        data: dict = json.load(fp)
        fp.close()

        print(" - Nazioni")
        try:
            for k, obj in data.get("Nazioni", {}).items():
                try:
                    Nazione.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error nazione {k}: {ex}")
        except Exception:
            pass

        print(" - Regioni")
        try:
            for k, obj in data.get("Regioni", {}).items():
                try:
                    Regione.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error regione {k}: {ex}")
        except Exception:
            pass

        print(" - Citta")
        try:
            for k, obj in data.get("Citta", {}).items():
                try:
                    Citta.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error citta {k}: {ex}")
        except Exception:
            pass

        print(" - Aree Disciplinari")
        try:
            for k, obj in data.get("AreaDisciplinare", {}).items():
                try:
                    AreaDisciplinare.create_from_dict(UUID(k), obj)
                except Exception as ex:
                    print(f"Error area disciplinare {k}: {ex}")
        except Exception:
            pass

        print(" - Docente")
        try:
            for k, obj in data.get("Docente", {}).items():
                try:
                    Docente.create_from_dict(CodiceFiscale(k), obj)
                except Exception as ex:
                    print(f"Error docente {k}: {ex}")
        except Exception:
            pass
            
        print(" - Studente")
        try:
            for k, obj in data.get("Studente", {}).items():
                try:
                    Studente.create_from_dict(CodiceFiscale(k), obj)
                except Exception as ex:
                    print(f"Error studente {k}: {ex}")
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
            "AreaDisciplinare": {},
        }
        for n in Nazione.all_objects_by_uuid():
            k, d = n.to_json()
            data["Nazioni"][k] = d
        for r in Regione.all_objects_by_uuid():
            k, d = r.to_json()
            data["Regioni"][k] = d
        for c in Citta.all_objects_by_uuid():
            k, d = c.to_json()
            data["Citta"][k] = d
        for c in AreaDisciplinare.all_objects_by_uuid():
            k, d = c.to_json()
            data["AreaDisciplinare"][k] = d
        for c in Docente.all_objects_by_cf():
            k, d = c.to_json()
            data["Docente"][k] = d
        for c in Studente.all_objects_by_cf():
            k, d = c.to_json()
            data["Studente"][k] = d
        
        fp = open(datafile, "wt")
        json.dump(data, fp, indent=4, sort_keys=True)
        fp.close()
    except Exception as ex:
        print(f"Error saving: {ex}")
