'''
prg034 - Escreva um programa que leia três números e que imprima o maior e o menor.
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    n1, n2 = n2, n1 #se n1 for maior que n2, n2 receberá o maior número
if n1 > n3:
    n1, n3 = n3, n1 #se n1 for maior que n3, o n3 receberá o maior valor
if n2 > n3:
    n2, n3 = n3, n2 #ultima comparação, se n2 testato lá em cima for maior que o n3, o n3 receberá o valor atribuido a n2, assim o maior número sempre ficará na variável n3

print(f'O menor número é {n1} e o maior é {n3}.')