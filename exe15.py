'''
prg015 - Escreva um programa que leia um número inteiro qualquer com 3 algarismos e o
informe de traz pra frente.
'''

num = int(input('Digite um número: '))

d1 = num // 100
d2 = num % 100 // 10
d3 = num % 100 % 10
print('Os algarismo de tras pra frente são:', d3,d2,d1)