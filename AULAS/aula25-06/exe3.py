'''
3 - Crie um programa que sorteie 6 números entre 1 e 60. Seu programa deve exibir na tela 100 jogos como estes. 
'''
from random import randint

for i in range(100):
  jogo = []
  for j in range(6):
    jogo.append(randint(1,60))
  print(f'Os números escolhidos na rodada {i+1}: {jogo}', end='\n')


'''
Versão professor 

from randon import randint 
for j in range(100):
  for i in range(6):
    if i == 5:
      print(randint(1,60))
    else:
      print(randint(1,60), end='-')
'''