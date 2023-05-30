from array import array
from random import random

floats = array("d", (random() for _ in range(10**7)))

with open("floats-10M-lines.txt", "w") as fp:
    for num in floats:
        fp.write(str(num) + "\n")

print("Gravação concluída.")
