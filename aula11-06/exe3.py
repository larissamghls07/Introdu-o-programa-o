'''
Crie um programa que gere uma cartela de bingo com 25 números entre 1 e 99. 
Armezene-a em um vetor e imprima a cartela ao final. 
'''
from random import randint
cartela = []

for i in range(25):
  cartela.append(randint(1,99))


print(cartela, end=' ')