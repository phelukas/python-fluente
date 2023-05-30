from colorama import Fore, Back, Style, init
from collections import namedtuple
import bisect, sys

print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.GREEN)
init()


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


f = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(f)
print(Fore.GREEN)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
