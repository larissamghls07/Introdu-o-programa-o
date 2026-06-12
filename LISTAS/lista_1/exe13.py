'''Escreva um programa que leia 2 pontos quaisquer no plano, P(x1, y1) e P(x2, y2), e
escreva a distância entre eles.'''

import math
x1 = float(input('Digite o x1: '))
x2 = float(input('Digite o x2: '))

y1 = float(input('Digite o y1: '))
y2 = float(input('Digite o y2: '))

# d = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'A distância é: {d}')