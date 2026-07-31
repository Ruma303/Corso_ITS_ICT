import re


class CAP(str):

    def __new__(cls, cap: str):

        if cap is None or cap == "":
            raise ValueError("Il cap non può essere vuoto.")

        str_cap = str(cap)
        if not re.fullmatch(r"[0-9]{5}", str_cap):
            raise ValueError(f"Il cap '{cap}' inserito non è valido.")

        return super().__new__(cls, str_cap)

    def __str__(self):
        return self

    def __repr__(self):
        return f"CAP('{self}')"
