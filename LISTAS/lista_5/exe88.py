'''
prg088 – Escreva um programa que preencha um vetor com os nomes fornecidos pelo usuário.
Ao final, quando o usuário digitar o usuário de nome ‘fim’, sorteie um nome que vencerá uma
rifa.
'''
from random import choice

nomes = []
nome = ''

while True:
    nome = str(input(f'Informe um nome: (\'fim\' para finalizar) '))
    if nome == "fim":
        break
    nomes.append(nome)
    
print(f'O vencedor da rifa: {choice(nomes)}')