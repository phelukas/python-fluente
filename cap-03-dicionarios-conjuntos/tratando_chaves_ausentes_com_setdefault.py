# index0.py utiliza dict.get para buscar e atualizar uma lista de ocorrencia de palavras a partir do indece (não é a melhor)
"""Criar um indice que mapeia palavra -> lista de ocorrencias"""
import sys
import re

WORD_RE = re.compile("\w+")

index = {}

with open(sys.argv[1], encoding="utf-8") as fp:
    for line_on, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            columun_on = match.start() + 1
            location = (line_on, columun_on)
            # isso não é elegante
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
# exibe em ordem alfabetica
for word in sorted(index, key=str.upper):
    print(word, index[word])
