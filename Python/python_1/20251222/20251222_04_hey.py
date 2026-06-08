"""
Stampare un banner (caratteri molto grandi) che contiene la parola: Hey
NB: Utilizzare i caratteri X o simili per le parti scure dei caratteri grandi.
"""

print("""
HHH   HHH   EEEEEEE   YYY   YYY
HHH   HHH   EEEEEEE    YYY YYY
HHH   HHH   EEE         YYYYY
HHHHHHHHH   EEEEEEE      YYY
HHHHHHHHH   EEEEEEE      YYY
HHHHHHHHH   EEEEEEE      YYY
HHH   HHH   EEE          YYY
HHH   HHH   EEEEEEE      YYY
HHH   HHH   EEEEEEE      YYY
""")

import pyfiglet
from termcolor import colored

def banner_personalizzato(afont):
    testo = "Hey"

    # 'slant' è uno dei font più popolari, ma ce ne sono centinaia
    ascii_art = pyfiglet.figlet_format(testo, font=afont)

    # Stampa il banner in blu
    banner_colorato = colored(ascii_art, "blue")

    print(banner_colorato)

banner_personalizzato("slant")
banner_personalizzato("block")
banner_personalizzato("bubble")
banner_personalizzato("digital")
banner_personalizzato("isometric1")
banner_personalizzato("banner")
banner_personalizzato("banner3")
banner_personalizzato("starwars")
# print(pyfiglet.FigletFont.getFonts())
