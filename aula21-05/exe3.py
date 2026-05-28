'''
Escreva um programa que leia números até que um número negativo seja digitado. 
No final, informe o maior e o menor número. 
'''
maior = 0
menor = 999999999
num = float(input(f'Digite um número: '))
while num >= 1:
  if num > maior:
    maior = num
  if num < menor:
    menor = num
  num = float(input(f'Digite um número: '))
  if num < 0:
    exit
print(f'Maior:{maior}\nMenor: {menor}')