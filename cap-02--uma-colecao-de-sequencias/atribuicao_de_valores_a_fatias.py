from colorama import Fore, Back, Style, init
from collections import namedtuple

print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.GREEN)
init()

l = list(range(10))
print(l)
print(l[2:5])
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)


print(Fore.GREEN)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
