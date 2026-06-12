'''
prg061 – Escreva um programa que leia um número e verifique e informe se ele é ou não
primo:
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