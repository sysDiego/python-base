#!/usr/bin/env python
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequen tam cada uma das atividades.
"""
__version__ = "0.0.1"

#Dados
sala1 = ["Erik", "João", "Marcia", "Pedro", "Marcelo", "Sophia"]
sala2 = ["Diego", "Sarah", "Luana", "Victor", "Velma"]

aula_ingles = ["Diego", "Velma", "Pedro", "João"]
aula_musica = ["Diego", "Sarah", "Erik", "Sophia"]
aula_danca = ["Sarah", "Marcia", "João", "Luana"]

# Listar alunos em cada atividade por sala
aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)
        
print("Inglês sala 1", aula_ingles_sala1)
print("Inglês sala 2", aula_ingles_sala2)