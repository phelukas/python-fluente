import pprint
from colorama import Fore, Back, Style, init

from collections import namedtuple

print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.GREEN)
init()
# Tuplas nomeadas
# # Definindo e usando um tupla nomeada

City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "jp", 36.933, (35.689772, 139.691667))

# print(tokyo)
# print(type(tokyo))
# for i in tokyo:
#     print(i)

# # Atributos e métodos de uma tupla nomeada

# print(City._fields)

LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.61, 77.208))
print("delhi_data")
print([i for i in delhi_data])
delhi = City._make(
    delhi_data
)  # make permite instanciar uma tupla nomeada a partir de um interavel City(*faria o mesmo)
latLongDict = delhi._asdict()

print(latLongDict)

for k, v in latLongDict.items():
    print(f"{k}:{v}")


print(Fore.GREEN)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
