'''
prg031 - Escreva um programa que leia os valores da gasolina e do etanol de um determinado
posto de abastecimento de combustível. Seu programa deve verificar e informar qual
combustível é mais vantajoso para o cliente, considerando que o etanol rende 30% menos que
a gasolina.
'''

gasolina = float(input('Digite o valor da gasolina: '))
etanol = float(input('Digite o valor do etanol: '))

#Verificar o redimento, considerando 1L. 
'''
o etanol só vale se o preço dele for menor que 70% do preço da gasolina
'''

if etanol < 0.7 * gasolina:
    print(f'O mais vantagoso para abastecimento é o etanol, com valor de: {etanol}')
else:
    print(f'O mais vantagoso para abastecimento é a gasolina, com valor de: {gasolina}')