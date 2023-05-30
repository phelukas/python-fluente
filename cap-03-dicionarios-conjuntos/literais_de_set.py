"""Chamar um set assim: {1,2,3} é mais rapido do que chamalo assim set([1,2,3]) por que o python executa um bytecode"""
from dis import dis

dis("{1}")
print("")
dis("set([1])")
