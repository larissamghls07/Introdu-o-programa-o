'''
prg090 – Escreva um programa que leia 3 números inteiros N, I e F. Sendo N, a quantidade de
números a serem sorteados, e I e F o intervalo de números do sorteio. Por fim exiba os números
sorteados.
'''
from random import choice

sorteados = []
n, i, f = 0, 0, 0
numeros = []

n = int(input(f'Informe a quantidade de números que serão sorteados: '))
i = int(input(f'Informe o primeiro número do intervalo: '))
f = int(input(f'Informe o último número do intervalo: '))

if i > f:
    f = i
    i = f
    
for j in range(i,f+1):
    numeros.append(j)
    
for i in range(n):
    escolhido = choice(numeros)
    sorteados.append(escolhido)
    
print(sorteados)