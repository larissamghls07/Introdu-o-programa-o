'''
Escreva um programa que receba o valor dos catetos de um triângulo, calcule e mostre
o valor da hipotenusa.
'''

cat1 = float(input('Digite o cateto 1: '))
cat2 = float(input('Digite o cateto 2: '))

hip = ((cat1) **2 + (cat2) ** 2) ** 0.5 

print(f'A hipotenusa vale: {hip}')