from colorama import Fore, Back, Style, init
from collections import namedtuple

print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.GREEN)
init()

board = [["_"] * 3 for i in range(3)]
print(board)
print(board[1])
board[1][2] = "X"
print(board)

print(Back.YELLOW)

weird_board = [["_"] * 3] * 3
print(weird_board)
weird_board[1][2] = "0"
print(weird_board)


print(Fore.GREEN)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)
print(Fore.YELLOW + "*" * 200)

"""
Embora as duas listas tenham a mesma aparência inicialmente, elas têm um comportamento diferente devido à forma como foram criadas.

A lista `board` foi criada usando uma compreensão de lista aninhada. Cada elemento da lista externa é uma nova lista, 
preenchida com o caractere "_" repetido três vezes. 
Isso garante que cada lista interna seja independente e referencie objetos separados na memória.

A lista `weird_board`, por outro lado, foi criada multiplicando uma lista `[["_"] * 3]` por 3. 
Nesse caso, apenas uma lista interna é criada e é referenciada três vezes na lista externa. Isso significa que todas as três listas internas são, 
na verdade, a mesma lista na memória.

A diferença fundamental ocorre quando você modifica uma das listas. Vamos ver um exemplo:

```python
board[0][0] = "X"
weird_board[0][0] = "X"
print(board)
print(weird_board)
```

A saída será:

```
[["X", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
[["X", "_", "_"], ["X", "_", "_"], ["X", "_", "_"]]
```

Observe que, ao modificar `board[0][0]`, apenas o primeiro elemento da primeira lista interna é atualizado. 
No entanto, ao modificar `weird_board[0][0]`, todos os elementos correspondentes das três listas internas são atualizados, 
porque todas as três listas são a mesma.

Portanto, embora as duas listas pareçam iguais inicialmente, o comportamento ao modificar os elementos é diferente. 
Se você deseja criar uma matriz de forma segura, onde cada elemento é independente, é recomendado usar a abordagem 
da lista `board` usando uma compreensão de lista aninhada.
"""
