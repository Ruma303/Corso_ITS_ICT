class Contact:
    nome = ""
    cognome = ""
    numero_casa = ""
    numero_ufficio = ""
    numero_mobile = ""
    email = ""

    # def add_contact(self): ...
    # def add_contact(self, nome="ugo"): ...


class Corso:
    voto_max = 30

    def voto_medio(self, voti):
        somma = 0
        esami = 0
        for voto in voti:
            if voto >= 18 and voto <= self.voto_max:
                somma = somma + voto
                esami += 1

        return somma / esami


corso_di_Python = Corso()
media = corso_di_Python.voto_medio([18, 20, 30])
print(f"Media: {media}")
print(corso_di_Python.voto_max)
