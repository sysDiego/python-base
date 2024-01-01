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
__version__ = "0.1.1"
__author__ = "Diego Amorim"
 #  Dunder

import os

current_language = os.getenv("LANG", 'en_US')[:5]

obj = {
    "pt_BR": "Olá Mundo",
    "en_US": "Hello World",
    "it_IT": "Ciao, Mundo"
}

print(obj[current_language])