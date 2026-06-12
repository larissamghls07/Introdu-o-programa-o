'''
Exemplos de manipulação de vetor com o for.
'''
from random import randint, choice

#randint sorteia um número de um intervalo 
#choice é uma escolha de algo  

nome = input(f'Digite o seu nome: ')
num = [10,20,30,40,50] #um vetor com cinco posições 
frutas = ['uva','maça','abacaxi','banana']

'''
for i in range(7):
  print(nome[i])

for i in range(5):
  print(f'posição do vetor {i}:',num[i])

  index out of range significa que pediu para imprimir um índice que não tem no vetor utilizado
for i in range(4):
  print(f'Fruta no índice {i}:', frutas[i])  
'''

'''
a bolinha vermelha serve para debugar erro, parar num exato ponto e examinar esse pedaço do código
'''
#Situação em não é possível saber o tamanho do vetor 
#a função len contabiliza a quantidade de algo

for i in range(len(nome)):
  print(nome[i], end=' ')

print(randint(1,100))

print(choice(frutas))
