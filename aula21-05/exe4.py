'''
Leia 100 números.
'''
maior, menor = 0,0
for i in range(100):
  num = int(input(f'Digite o número: '))
  if i == 0 or num>maior:
    maior = num
  if i == 0 or num<menor:
    menor = num