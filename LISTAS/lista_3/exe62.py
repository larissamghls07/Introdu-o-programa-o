'''
Escreva um programa que leia um termo qualquer, verifique e informe se é ou não palíndromo.
'''

termo = str(input(f'Informe uma palavra: '))
invertido = termo[::-1]

if termo == invertido:
  print('É um palíndromo.')
else:
  print(f'Não é um palíndromo.')