from generator import generat_pass
from validator import validator

def show_banner():
    banner = [
        "###############################",
        "#                             #",
        "#         SECURSEPASS         #",
        "#                             #",
        "###############################",
    ]

    for line in banner:
        print(line, end="\n")

show_banner()

def show_menu():
    pass