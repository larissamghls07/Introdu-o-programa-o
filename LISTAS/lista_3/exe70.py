'''
prg070 – Você é o responsável pela gerência de um posto de abastecimento de combustíveis.
Seu posto possui um tanque com 50.000 litros de combustível que é reabastecido somente ao
ficar vazio. Você deseja saber quantos automóveis foram abastecidos por um dado tanque.
Faça um programa que leia valores de abastecimento e imprima a quantidade de carros
abastecidos.
'''

qtd_carro = 0
tanque = 50000

while tanque != 0:
    gasolina_carro = float(input(f'Infome a quantidade de litros comparadas: '))
    tanque -= gasolina_carro
    if gasolina_carro > 0:
        qtd_carro += 1
    print(tanque)

print(f'Foram necessários {qtd_carro} abastecimentos para esvaziar o tanque.')