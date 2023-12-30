#!usr/bin/env python 

"""Imprimindo a tabuada do 1 ao 10."""

__version_ = "0.1.1"
__author__ = "Diego Amorim"

template_base = """
---Tabuada do 1---

    {operacoes}

#################
"""


#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,255))

# print(numeros)
for n1 in numeros:
    for n2 in numeros:
        operacao = f"{n1}x{n2} = {n1 * n2}"
        print(operacao)
    #print(template_base.format(
    #    operacoes=operacoes
    #))