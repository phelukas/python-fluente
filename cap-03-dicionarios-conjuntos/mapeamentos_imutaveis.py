"""MappingProxyType cria uma instância DE mappingproxy somente para leitura a partir de um dict"""
from types import MappingProxyType

d = {1: "A"}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = "x"
d[2] = "B"
print(d_proxy)
print(d_proxy[2])
