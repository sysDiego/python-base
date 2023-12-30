#!usr/bin/env python 

"""Imprimindo a tabuada do 1 ao 10."""

__version_ = "0.0.1"
__author__ = "Diego Amorim"


#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,255))

# print(numeros)
for numero in numeros:
    print("Tabuada do :", numero)
    for key in numeros:
        print(key, "x", numero, ":", (key * numero) )
print("===========================")
