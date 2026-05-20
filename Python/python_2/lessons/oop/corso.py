class Corso:
    voto_max = 30

    def voto_medio(self, voti) -> float:
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


class MyClass:
	message: str

	def __init__(self, message):
		self.message = message

	def print_message(self):
		print(self.message)

	def instance_to_str(this):
		print(this)

myClass = MyClass("Hello")
myClass.print_message()
myClass.instance_to_str()
