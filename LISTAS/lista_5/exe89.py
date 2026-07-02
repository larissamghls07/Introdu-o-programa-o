'''
prg089 – Escreva um programa que gere 10 cartelas de bingo com 25 números não repetidos
entre 1 e 75. Imprima os números de cada cartela na tela.
'''

from random import randint

num = 0

for i in range(10):
    cartela = []
    
    
    for j in range(25):
        num = randint(1,75)
        while num in cartela:
            num = randint(1,75)
        cartela.append(num)
        
        
        
    print(cartela)
    print(' ')