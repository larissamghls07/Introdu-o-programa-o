'''
prg022 - Escreva um programa que peça um valor e mostre na tela se o valor é positivo ou
negativo.
'''

valor = int(input('Digite um valor: '))

if valor > 0: 
    print(f'O número {valor} é positivo.')
if valor == 0: 
    print('O número é o zero.')
if valor < 0:
    print(f'O número {valor} é negativo.') 
