'''
Faça um programa que leia a idade de 20 pessoas e ao final informe quantos são menores de idade.
'''
j = 0
for i in range(20):
  idade = int(input(f'Digite a sua idade: '))
  if idade<18:
    j += 1
print(f'A quantidade de menores de idade: ', j)