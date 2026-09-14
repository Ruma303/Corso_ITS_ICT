from sys import exit

from models.officina import Officina
from models.persona import Persona

def dirige_test():
    print("=== 1. Creazione base (1..1 obbligatoria) ===")
    o_roma = Officina("Officina Roma")
    o_milano = Officina("Officina Milano")
 
    mario = Persona("Mario", o_roma)
    print(f"{mario} -> officina: {mario.officina()}")
    print(f"{o_roma} -> persone: {o_roma.persone()}")
    assert mario.officina() is o_roma
    assert o_roma.persone() == {mario}
 
    print("\n=== 2. Molteplicita' 0..* lato Officina (piu' Persona) ===")
    luigi = Persona("Luigi", o_roma)
    print(f"{o_roma} -> persone: {o_roma.persone()}")
    assert o_roma.persone() == {mario, luigi}
 
    print("\n=== 3. Aggiornamento link (distruzione + ricreazione) ===")
    vecchio_link = mario._Persona__link  # accesso solo per test/verifica
    mario.crea_link(o_milano)
    print(f"{mario} -> officina: {mario.officina()}")
    print(f"{o_roma} -> persone: {o_roma.persone()}")
    print(f"{o_milano} -> persone: {o_milano.persone()}")
    print(f"vecchio link ancora valido? {vecchio_link.is_valid()}")
 
    assert mario.officina() is o_milano
    assert o_roma.persone() == {luigi}
    assert o_milano.persone() == {mario}
    assert vecchio_link.is_valid() is False
 
    print("\n=== 4. Officina senza nessuna Persona (0..* ammette 0) ===")
    o_vuota = Officina("Officina Torino")
    print(f"{o_vuota} -> persone: {o_vuota.persone()}")
    assert o_vuota.persone() == set()
 
    print("\nTutte le verifiche sono passate correttamente.")



def main() -> int:
    dirige_test()
    return 0


if __name__ == "__main__":
    exit(main())
