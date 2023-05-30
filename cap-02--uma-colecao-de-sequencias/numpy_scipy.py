from time import perf_counter as pc
import numpy

t0 = pc()

print("*" * 50)

floats = numpy.loadtxt("floats-10M-lines.txt")
print(floats[-3:])
floats *= 0.5
print(floats[-3:])

t1 = pc()

print("Tempo decorrido até aqui:", (t1 - t0) / 60, "minutos")

floats /= 3

t2 = pc()

print("Tempo decorrido após a divisão:", (t2 - t1) / 60, "minutos")

numpy.save("floats-10M", floats)
floats2 = numpy.load("floats-10M.npy", "r+")
floats2 *= 6
print(floats2[-3:])

t3 = pc()

print("Tempo decorrido total:", (t3 - t0) / 60, "minutos")
