"""
Tramite uno sniffer, sono stati acquisiti 100 pacchetti di dati di rete e archiviati in una lista di liste di numeri

Sapendo che in un pacchetto di rete, al posto 12 c’è un numero(esadecimale) che rappresenta il protocollo di comunicazione trasportato dal protocollo Ethernet, contare per ogni protocollo di seguito listato, quante occorrenze sono state individuate nei 100 pacchetti

Iterare per ogni lista alla posizione 12

hex  protocollo
0800 Internet IP (IPv4)
0801 X.75 Internet
0802 NBS Internet
0803 ECMA Internet
0804 Chaosnet
0805 X.25 Level 3
0806 ARP
0807 XNS Compatability
0808 Frame Relay ARP
081C Symbolics Private
"""
from pacchetti import pacchetti

num_proto = []

num_0800 = []
num_0801 = []
num_0802 = []
num_0803 = []
num_0804 = []
num_0805 = []
num_0806 = []
num_0807 = []
num_0808 = []
num_081C = []
num_null = []

for i, lista in enumerate(pacchetti):

  if len(lista) > 12:
    proto = lista[12]
    num_proto.append(proto)
    print(f"Lista {i}, Pacchetto analizzato: {proto}")

    match proto:
        case proto if int("0800", 16) == proto:
            num_0800.append(proto)
            print("Internet IP (IPv4)")
        case proto if int("0801", 16) == proto:
            num_0801.append(proto)
            print("X.75 Internet")
        case proto if int("0802", 16) == proto:
            num_0802.append(proto)
            print("NBS Internet")
        case proto if int("0803", 16) == proto:
            num_0803.append(proto)
            print("ECMA Internet")
        case proto if int("0804", 16) == proto:
            num_0804.append(proto)
            print("Chaosnet")
        case proto if int("0805", 16) == proto:
            num_0805.append(proto)
            print("X.25 Level 3")
        case proto if int("0806", 16) == proto:
            num_0806.append(proto)
            print("ARP")
        case proto if int("0807", 16) == proto:
            num_0807.append(proto)
            print("XNS Compatibility")
        case proto if int("0808", 16) == proto:
            num_0808.append(proto)
            print("Frame Relay ARP")
        case proto if int("081C", 16) == proto:
            num_081C.append(proto)
            print("Symbolics Private")
        case _:
            num_null.append(proto)
            print("No protocol")

print(f"Trovati {len(num_proto)} protocolli: {num_proto}")

print(f"\t- Trovati {len(num_0800)} protocolli Internet IP (IPv4)")
print(f"\t- Trovati {len(num_0801)} protocolli X.75 Internet")
print(f"\t- Trovati {len(num_0802)} protocolli NBS Internet")
print(f"\t- Trovati {len(num_0803)} protocolli ECMA Internet")
print(f"\t- Trovati {len(num_0804)} protocolli Chaosnet")
print(f"\t- Trovati {len(num_0805)} protocolli X.25 Level 3")
print(f"\t- Trovati {len(num_0806)} protocolli ARP")
print(f"\t- Trovati {len(num_0807)} protocolli XNS Compatibility")
print(f"\t- Trovati {len(num_0808)} protocolli Frame Relay ARP")
print(f"\t- Trovati {len(num_081C)} protocolli Symbolics Private")
print(f"\t- Trovati {len(num_null)} protocolli nulli: {num_null}")