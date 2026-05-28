'''
prg060 – Escreva um programa que leia um número e informe a tabuada deste número no
seguinte formato: 2 x 1 = 2 e etc.
'''

num = int(input(f'Digite um número: '))

for i in range(11):
  print(f'{num} x {i}: {num * i}')