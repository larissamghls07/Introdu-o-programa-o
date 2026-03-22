'''
Escreva um programa que leia o radio de uma esfera e informe o seu volume. Considere para seu cálculo o valor de π = 3,14159

'''

raio = float(input('Informe o raio: '))
pi = 3.14159

volume = 4/3 * pi * (raio ** 3)
print('O seu volume é: ', volume)