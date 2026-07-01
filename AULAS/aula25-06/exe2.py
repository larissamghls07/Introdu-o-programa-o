'''
2 - Crie um programa que sorteie e exiba na tela 10 vezes um valor sorteado do seguinte vetor: 
copa = ['alemanha','argentina','italia','brasil','uruguai','frança','espanha']
'''

copa = ['alemanha','argentina','italia','brasil','uruguai','frança','espanha']

from random import choice

for i in range(10):
  print(f'O {i + 1}º escolhido foi: { choice(copa)}', end='\n')