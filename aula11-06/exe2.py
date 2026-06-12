'''
Crie um programa que sorteie 6 dezenas para um jogo na megasena. Armazene em um vetor. 
Ao final, imprima o vetor.
'''

from random import randint

jogo = [] #um vetor vazio é uma estrutura sem nada, o tamanho pode ser manipulado ao longo do código


for i in range(6):
  jogo.append(randint(1,60))

print(jogo)