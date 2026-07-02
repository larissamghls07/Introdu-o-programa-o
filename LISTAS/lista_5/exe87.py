'''
prg087 – Escreva um programa que preencha um vetor com números aleatórios até que o
número 1 seja sorteado. Ao final informe quantos números foram sorteados excetuando-se o 1.
'''
from random import randint

num, qtd = 0, 0

vet = []

while num != 1:
    num = randint(1,100)
    vet.append(num)
    qtd += 1
    
print(f'A quantidade de números sorteados foram: {len(vet)}')