'''
Escreva um programa que leia 2 numeros e imprima todos os números entre eles. 

n1 = int(input(f'Digite n1: '))
n2 = int(input(f'Digite n2: '))

if n1>n2:
  n1, n2 = n2,n1
for i in range(n1+1,n2):
  print(i)

'''

''' inclusive os numeros digitados
n1 = int(input(f'Digite n1: '))
n2 = int(input(f'Digite n2: '))

if n1>n2:
  n1, n2 = n2,n1
for i in range(n1,n2+1):
  print(i)
'''

n1 = int(input(f'Digite n1: '))
n2 = int(input(f'Digite n2: '))

n1 += 1
while n1<n2:
  print(n1)
  n1 += 1
