from colorama import Fore, Back, Style, init
from collections import namedtuple


def cabecalho(valor):
    init()
    print(Fore.YELLOW + "*" * 200)
    print(Fore.YELLOW + "*" * 200)
    print(Fore.YELLOW + "*" * 200)
    print(Fore.GREEN)

    print(valor)

    print(Fore.GREEN)
    print(Fore.YELLOW + "*" * 200)
    print(Fore.YELLOW + "*" * 200)
    print(Fore.YELLOW + "*" * 200)
