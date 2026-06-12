'''
prg029 - Escreva um programa que 3 números inteiros quaisquer. Seu programa deve informar
estes números em ordem crescente.
'''

n1 = int(input('Digite um n1: '))
n2 = int(input('Digite o n2: '))
n3 = int(input('Digite o n3: '))

if n1 > n2:
    n1, n2 = n2, n1
    # teste = n1
    # n1 = n2
    # n2 = teste
if n1>n3:
    n1, n3 = n3, n1
if n2>n3:
    n2, n3 = n3, n2

print(n1, n2, n3)