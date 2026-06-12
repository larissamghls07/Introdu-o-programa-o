'''
Crie um programa que gere uma cartela de bingo com 25 números entre 1 e 99. 
Armezene-a em um vetor e imprima a cartela ao final. 
'''
from random import randint
cartela = []

for i in range(25):
  num = randint(1,99)
  while num in cartela: #um teste lógico que verifica se o número está no vetor
    print(f'Número repetido descartado: ', num)
    num = randint(1,99)
  cartela.append(num)


#print(cartela, end=' ')
print(f'Cartela: ')
for y in range(25):
  if y in [4,9,14,19]:
    print(cartela[y])
  else:
    print(cartela[y], end=' ')