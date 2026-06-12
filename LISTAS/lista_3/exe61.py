'''
prg061 – Escreva um programa que leia um número e verifique e informe se ele é ou não
primo:

Resolução em sala do professor 

num = int(input(f'Informe um número: '))
contador = 0 

for i in range(1, (num+1)/2):
  if (num % i) == 0:
    contador += 1

if contador < 3:
  print(f'É um número primo.')
else:
  print(f'Não é um número primo. ')
'''

numero = int(input(f'Digite um número: '))
qtd = 0

for i in range(1, numero+1):
    if numero > 1 and ((numero%i) == 0) and ((numero%numero) == 0):
        qtd += 1
if qtd == 2:
    print(f'O {numero} é um número primo.')
else:
    print(f'O número {numero} não é um número primo.')