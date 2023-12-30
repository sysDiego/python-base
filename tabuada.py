#!usr/bin/env python 

"""Imprimindo a tabuada do 1 ao 10."""

__version_ = "0.1.1"
__author__ = "Diego Amorim"

template_base = """
-----

    {operacoes}

#################
"""


#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# print(numeros)
for n1 in numeros:
    print(
        "{:-^18}".format(f" Tabuada do {n1} ")
    )
    print()
    for n2 in numeros:
        print("{:^18}".format( f"{n1}x{n2} = {n1 * n2}"))
    