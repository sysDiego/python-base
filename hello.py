#!usr/bin/env python 

"""Hello World Multi Linguas.

Dependendo da lingua utilizada pelo almbiente o programa
exibe a mensagem correspondente

Modo de uso: 

Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR
    
Execução: 

    python3 hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Diego Amorim"
__license__ = "Unlicense"
#  Dunder

import os

current_language = os.getenv("LANG", 'en_US')[:5]

msg = "Hello World"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"


print(msg)