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

atividades = [
    ("Inglês", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome, atividade in atividades:
    atividade_sala1 = []
    atividade_sala2 = []
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("Atividade ", nome)
    print("-" * 30)
    print("Sala 1")
    print(atividade_sala1)
    print("-" * 30)
    print("Sala 2")
    print(atividade_sala2)
    print()
    
            
    