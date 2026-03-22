'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
R$ 0,15 por km rodado.
'''

kms = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias: '))
tot = (60 * dias) + (0.15 * kms)

print(f'O total a pagar é R${tot}')

