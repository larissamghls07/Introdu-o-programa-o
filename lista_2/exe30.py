'''
prg030 - Escreva um programa que leia o nome e o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

prod1 = input('Nome do produto 1: ')
preco1 = float(input('Preço do produto1: ')) 

prod2 = input('Nome do produto 2: ')
preco2 = float(input('Preço do produto2: ')) 

prod3 = input('Nome do produto 3: ')
preco3 = float(input('Preço do produto3: '))

if preco1 > preco2: #Se preço 1 for maior que o 2, eu já coloco o menor no preco1
    preco1, preco2 = preco2, preco1 
    prod1, prod2 = prod2, prod1
if preco1 > preco3:
    preco1, preco3 = preco3, preco1
    prod1, prod3 = prod3, prod1
    #Se preco1 for maior que o 3, preco3 recebe o maior valor enquanto o 1 recebe sempre o menor 
if preco2 > preco3:
    preco2, preco3 = preco3, preco2
    prod2, prod3 = prod3, prod2
    #Se o 2 for maior que o 3, o 3 (ultimo) já recebe o maior valor enquanto o 2 recebe o menor. 

print(f'Você deve comprar o produto {prod1} com preço {preco1}.')
