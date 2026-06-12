'''
Faça um programa que peça ao usuário a base e a altura de um
retângulo, calcule e informe o perímetro e a sua área.
'''

base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

p = (2 * base) + (2 * altura)
area = base * altura

print('O seu perímetro vale: ', p, '\nA sua área vale: ', area)