#!/usr/bin/env python
"""Cadastro de Produto"""
__version__ = "0.0.1"
__author__ = "Diego Amorim"
import pprint
produto = { "nome": "Caneta", "cores": ["azul", "vermelha"], "preco": 3.23, "codigo": 45678, "Estoque": True, "codebar": None}
cliente = {
    "nome": "Diego",
    "saldo": 20.59,
    "ativo": True,
}
compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}
pprint.pprint(compra)
total_da_compra = compra["quantidade"] * compra["produto"]["preco"]

pprint.pprint(f"O cliente {compra['cliente']['nome']} comprou {produto['nome']} e pagou o total de {total_da_compra}")