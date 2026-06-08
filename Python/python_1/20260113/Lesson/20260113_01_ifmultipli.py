# Dato un voto in trentesimi, indicare se lo studente è stato bocciato, se è mediocre, se il voto è buono, oppure se il voto è ottimo

import random

from pacchetti import pacchetti

voto = int(input("Inserisci il voto: "))
if voto < 18:
    print("Bocciato")
else:
    if voto < 24:
        print("Mediocre")
    else:
        if voto < 28:
            print("Buono")
        else:
            print("Ottimo")

if voto < 18:
    print("Bocciato")
elif voto < 24:
    print("Mediocre")
elif voto < 28:
    print("Buono")
else:
    print("Ottimo")

match voto:
    case range(0, 18):
        print("Bocciato")
    case 18, 19, 20, 21, 22, 23:
        print("Mediocre")
    case 24, 25, 26, 27:
        print("Buono")
    case _:
        print("Ottimo")

"""
in altri linguaggi (c, c++, java, javascript, golang, ...)
switch (voto) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
    case 13:
    case 14:
    case 15:
    case 16:
    case 17:
        print("Bocciato");
        break;
    case 18:
    case 19:
    case 20:
    case 21:
    case 22:
    case 23:
        print("Mediocre");
        break;
    case 24:
    case 25:
    case 26:
    case 27:
        print("Buono");
        break;
    default: //significa tutti gli altri casi
        print("Ottimo");
}
"""


proto=[
    int("0800", 16),
    int("0801", 16),
    int("0802", 16),
    int("0803", 16),
    int("0804", 16),
    int("0805", 16),
    int("0806", 16),
    int("0807", 16),
    int("0808", 16),
    int("081C", 16)
]

# # Costruzione dei pacchetti di prova
# elenco=[]
# for i in range(0, 1000):
#     pacchetto=[]
#     for j in range(64, 512):
#         pacchetto.append(random.randint(0, 255))
#     pacchetto[12]=random.randint(0, 1000) if random.random() < 0.05 else proto[random.randint(0, 9)]
#     elenco.append(pacchetto)

# print(elenco)

# 0800 Internet IP (IPv4)
# 0801 X.75 Internet
# 0802 NBS Internet
# 0803 ECMA Internet
# 0804 Chaosnet
# 0805 X.25 Level 3
# 0806 ARP
# 0807 XNS Compatability
# 0808 Frame Relay ARP
# 081C Symbolics Private

# Soluzione 1
Internet_IP=0
X75_Internet=0
NBS_Internet=0
ECMA_Internet=0
Chaosnet=0
X25_Level_3=0
ARP=0
XNS_Compatability=0
Frame_Relay_ARP=0
Symbolics_Private=0
AltriPacchetti=0

for pacchetto in pacchetti:
    if pacchetto[12] == int("0800", 16):
        Internet_IP = Internet_IP + 1
    elif pacchetto[12] == int("0801", 16):
        X75_Internet = X75_Internet + 1
    elif pacchetto[12] == int("0802", 16):
        NBS_Internet = NBS_Internet + 1
    elif pacchetto[12] == int("0803", 16):
        ECMA_Internet = ECMA_Internet + 1
    elif pacchetto[12] == int("0804", 16):
        Chaosnet = Chaosnet + 1
    elif pacchetto[12] == int("0805", 16):
        X25_Level_3 = X25_Level_3 + 1
    elif pacchetto[12] == int("0806", 16):
        ARP = ARP + 1
    elif pacchetto[12] == int("0807", 16):
        XNS_Compatability = XNS_Compatability + 1
    elif pacchetto[12] == int("0808", 16):
        Frame_Relay_ARP = Frame_Relay_ARP + 1
    elif pacchetto[12] == int("081C", 16):
        Symbolics_Private = Symbolics_Private + 1
    else:
        AltriPacchetti = AltriPacchetti + 1

print("Internet IP: ", Internet_IP)
print("X.75 Internet: ", X75_Internet)
print("NBS Internet: ", NBS_Internet)
print("ECMA Internet: ", ECMA_Internet)
print("Chaosnet: ", Chaosnet)
print("X.25 Level 3: ", X25_Level_3)
print("ARP: ", ARP)
print("XNS Compatability: ", XNS_Compatability)
print("Frame Relay ARP: ", Frame_Relay_ARP)
print("Symbolics Private: ", Symbolics_Private)
print("Altri pacchetti: ", AltriPacchetti)

print("Totale: ", Internet_IP + X75_Internet + NBS_Internet + ECMA_Internet + Chaosnet + X25_Level_3 + ARP + XNS_Compatability + Frame_Relay_ARP + Symbolics_Private + AltriPacchetti)


# Soluzione 2
Internet_IP=0
X75_Internet=0
NBS_Internet=0
ECMA_Internet=0
Chaosnet=0
X25_Level_3=0
ARP=0
XNS_Compatability=0
Frame_Relay_ARP=0
Symbolics_Private=0
AltriPacchetti=0

for pacchetto in pacchetti:
    match pacchetto[12]:
        case 0x0800:
            Internet_IP = Internet_IP + 1
        case 0x0801:
            X75_Internet = X75_Internet + 1
        case 0x0802:
            NBS_Internet = NBS_Internet + 1
        case 0x0803:
            ECMA_Internet = ECMA_Internet + 1
        case 0x0804:
            Chaosnet = Chaosnet + 1
        case 0x0805:
            X25_Level_3 = X25_Level_3 + 1
        case 0x0806:
            ARP = ARP + 1
        case 0x0807:
            XNS_Compatability = XNS_Compatability + 1
        case 0x0808:
            Frame_Relay_ARP = Frame_Relay_ARP + 1
        case 0x081C:
            Symbolics_Private = Symbolics_Private + 1
        case _:
            AltriPacchetti = AltriPacchetti + 1

print("Internet IP: ", Internet_IP)
print("X.75 Internet: ", X75_Internet)
print("NBS Internet: ", NBS_Internet)
print("ECMA Internet: ", ECMA_Internet)
print("Chaosnet: ", Chaosnet)
print("X.25 Level 3: ", X25_Level_3)
print("ARP: ", ARP)
print("XNS Compatability: ", XNS_Compatability)
print("Frame Relay ARP: ", Frame_Relay_ARP)
print("Symbolics Private: ", Symbolics_Private)
print("Altri pacchetti: ", AltriPacchetti)

print("Totale: ", Internet_IP + X75_Internet + NBS_Internet + ECMA_Internet + Chaosnet + X25_Level_3 + ARP + XNS_Compatability + Frame_Relay_ARP + Symbolics_Private + AltriPacchetti)

# Soluzione 3
Internet_IP=0x0800
X75_Internet=0x0801
NBS_Internet=0x0802
ECMA_Internet=0x0803
Chaosnet=0x0804
X25_Level_3=0x0805
ARP=0x0806
XNS_Compatability=0x0807
Frame_Relay_ARP=0x0808
Symbolics_Private=0x081C
#AltriPacchetti=

# Faccio una lista di 65536 zeri (i codici dei protocolli non superano i 65536 essendo a 2 byte)
lista=[0]*65536

for pacchetto in pacchetti:
    lista[pacchetto[12]]=lista[pacchetto[12]]+1

print("Internet IP: ", lista[Internet_IP])
print("X.75 Internet: ", lista[X75_Internet])
print("NBS Internet: ", lista[NBS_Internet])
print("ECMA Internet: ", lista[ECMA_Internet])
print("Chaosnet: ", lista[Chaosnet])
print("X.25 Level 3: ", lista[X25_Level_3])
print("ARP: ", lista[ARP])
print("XNS Compatability: ", lista[XNS_Compatability])
print("Frame Relay ARP: ", lista[Frame_Relay_ARP])
print("Symbolics Private: ", lista[Symbolics_Private])

