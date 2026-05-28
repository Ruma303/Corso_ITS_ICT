"""
gestione_its_1.py

Prerequisiti:
Aver svolto l'Esercitazione "Gestione ITS 1" (modulo "Progettazione").


Si consideri lo schema concettuale prodotto dagli analisti 
per il progetto "Gestione ITS 1".

Si scriva un programma Python orientato agli oggetti che implementi
lo schema concettuale per l'applicazione, con le seguenti
semplificazioni necessarie per permettere l'implementazione Python
con i costrutti che conosciamo già:
	- ammettiamo la navigazione delle associazioni in una unica direzione.

In particolare, l'applicazione deve:

1) permettere di rappresentare gli oggetti di ogni classe del diagramma 
UML concettuale delle classi

2) implementare le associazioni esclusivamente nei seguenti versi:
	- reg_naz:  Regione -> Nazione
	- citta_reg: Citta -> Regione
	- stud_citta_nasc: Studente -> Citta
	- docente_citta_nasc: Docente -> Citta
	- studente_supera_modulo: Studente -> Modulo
	- studente_corso: Studente -> CorsoITS
	- corso_area: CorsoITS -> AreaDisciplinare
	- modulo_in_corso: CorsoITS -> Modulo
	- doc_insegna_modulo: Modulo -> Docente


3) gestire la persistenza dei dati tramite un file JSON.	
"""


import sys


# Class di interesse per il programma




# Funzioni di interfaccia ("ui": "User interface")

def ui_ask_what_to_do():
	while True:
		print(  "\n\n\n----------\n\nChoose an action:\n" + \
				" - add ...: Add a new ...\n" + \
				" - exit: Exit"
		)
		
		choice = input("Action? ")

		if choice == 'add ...':			
			pass
			#ui_add_...()
		elif choice == 'exit':
			print("Arrivederci!")
			break
		else:
			print(f"{choice}? mmm, unknown command...")


# Costante globale: nome del file che mantiene i dati
datafile = "data.json"

def load_all():
	print(f"Loading data file '{datafile}':")
	# Implementala tu!

def save_all():
	print(f"Saving data to file '{datafile}' (nothing done, really)")
	# Implementala tu!

def main():
	
	load_all()
	ui_ask_what_to_do()	
	save_all()

	return 0

if __name__ == '__main__':
	sys.exit( main() )
