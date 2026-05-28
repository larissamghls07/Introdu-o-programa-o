'''
prg048 - Escreva um programa que leia dois números e imprima todos os números entre eles.
'''

num1 = int(input(f'Digite o primeiro número: '))
num2 = int(input(f'Digite o segundo número: '))

if num2>num1:
  num1, num2 = num2, num1

for i in range(num1+1, num2):
  print(i)