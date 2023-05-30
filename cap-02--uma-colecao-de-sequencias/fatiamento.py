from colorama import Fore, Back, Style, init
from collections import namedtuple

print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.GREEN)
init()

"""
O slice `[a:b:c]` no Python é usado para obter uma parte de uma sequência (como uma lista, tupla, string, etc.) com base em um intervalo específico.

Aqui está o significado de cada componente no slice `[a:b:c]`:

- `a` (opcional, padrão: início): É o índice onde o slice começa. Ele representa o primeiro elemento incluído no slice. 
Se `a` for omitido, o slice começará do início da sequência.

- `b` (opcional, padrão: fim): É o índice onde o slice termina. Ele representa o primeiro elemento que não está incluído no slice. 
Se `b` for omitido, o slice irá até o final da sequência.

- `c` (opcional, padrão: 1): É o passo ou intervalo entre os elementos do slice. O valor `c` especifica quantos elementos devem 
ser pulados a cada iteração. 
Se `c` for omitido, o valor padrão é 1, o que significa que todos os elementos entre `a` e `b` serão incluídos no slice.

Aqui estão alguns exemplos para ilustrar o uso do slice:


sequencia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obter todos os elementos da sequência
print(sequencia[:])  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obter os elementos do índice 2 até o índice 6 (exclusivo)
print(sequencia[2:6])  # Saída: [2, 3, 4, 5]

# Obter todos os elementos começando do índice 3
print(sequencia[3:])  # Saída: [3, 4, 5, 6, 7, 8, 9]

# Obter todos os elementos até o índice 5 (exclusivo)
print(sequencia[:5])  # Saída: [0, 1, 2, 3, 4]

# Obter todos os elementos com intervalo de 2
print(sequencia[::2])  # Saída: [0, 2, 4, 6, 8]

# Obter todos os elementos com intervalo de -1 (inversão da sequência)
print(sequencia[::-1])  # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


Lembre-se de que o slice `[a:b:c]` retorna uma nova sequência contendo os elementos selecionados.
 A sequência original não é modificada. O slice pode ser usado em diferentes tipos de sequências, como listas, tuplas, strings e outras.
"""


invoice = """
... 0......6................................40........52...55........
... 1909      Pinoroni PiBrella                 $17.50    3    $52.50
... 1489      6m Tactile Switch x20             $4.95     2    $9.90
... 1510      Panavise 3r. - PV-201             $28.00    1    $28.00
... 1601      PiTFT Mini Kit 320x240            $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split("\n")[2:]

# for indice, letra in enumerate(line_items[0]):
#     print(f"A letra '{letra}' está no índice {indice}")


for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

print(Fore.GREEN)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
