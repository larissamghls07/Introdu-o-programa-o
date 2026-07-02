'''
prg083 – Escreva um programa que simule o sorteio de dois dados 15 vezes. Ao final imprima a lista de números sorteados.
'''

from random import randint

dado = []
dado2 = []

for i in range(15):
    dado.append(randint(1,6))
    dado2.append(randint(1,6))


print(f"Resultados do dado 1: {dado}")
print(f"Resultado do dado 2: {dado2}")    

