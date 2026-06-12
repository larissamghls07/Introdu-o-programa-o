'''
prg036 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer
em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km,
e R$ 0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distância que deseja percorrer: '))

if distancia > 200:
    preco = 0.45 * distancia
    print(f'O preço da sua passagem será de R${preco}')
else:
    preco = 0.5 * distancia
    print(f'O preço da sua passagem será de R${preco}')