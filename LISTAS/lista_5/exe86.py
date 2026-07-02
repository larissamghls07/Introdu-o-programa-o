'''
prg086 – Escreva um programa que preencha um vetor de tamanho 10 com números inteiros
aleatórios entre 1 e 99. Por fim exiba uma lista com os números que não foram sorteados.
'''
from random import randint

escolhido = [] #tem 10 espaços 
naoescolhido = [] #é o restante, 99 - 10(os que ja foram escolhidos) = 89
for i in range(10):
    num = randint(1,99)
    escolhido.append(num)
    
for j in range(89):
    num2 = randint(1,99)
    while num2 in escolhido:
        num2 = randint(1,99)
    naoescolhido.append(num2)
    
print(escolhido)
print(naoescolhido)