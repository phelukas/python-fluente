from time import perf_counter as pc


def medir_tempo_execucao(codigo):
    t0 = pc()
    codigo()
    t1 = pc()
    tempo_decorrido = t1 - t0
    print("Tempo de execução:", tempo_decorrido, "segundos")


# Exemplo de uso da função:
def meu_codigo():
    # Código que você deseja medir o tempo de execução
    print("Meu código está sendo executado...")


# Chame a função para medir o tempo de execução do seu código
medir_tempo_execucao(meu_codigo)
