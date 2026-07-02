'''
prg085 – Escreva um programa que gere um jogo de 6 dezenas da megasena com números de
1 a 60. Aprimore o programa anterior não permitindo números repetidos.
'''

from random import randint

sorte = []

for i in range (6):
    num = randint(1,60)
    while num in sorte:
        print(f'Teve numero repetido!')
        num = randint(1,60)
    sorte.append(num)
    if i < 5:
        print(sorte[i], end = ' - ')
    else:
        print(sorte[i])