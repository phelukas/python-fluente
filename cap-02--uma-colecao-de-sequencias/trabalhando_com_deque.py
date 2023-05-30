from time import perf_counter as pc


def medir_tempo_execucao(codigo):
    t0 = pc()
    codigo()
    t1 = pc()
    tempo_decorrido = t1 - t0
    print("Tempo de execução:", tempo_decorrido, "segundos")


# Exemplo de uso da função:
def meu_codigo():
    print("Meu código está sendo executado...")
    from collections import deque

    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)


# Chame a função para medir o tempo de execução do seu código
medir_tempo_execucao(meu_codigo)
