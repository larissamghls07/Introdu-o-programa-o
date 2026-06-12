'''
prg064 – Escreva um programa que leia o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os próximos 24 meses. Escreva o total ganho com juros no
período:
'''

deposito_inical = float(input(f'Digite o seu depósito inicial: '))
taxa_juros = (float(input(f'Digite a taxa de juros: '))) / 100

deposito_final = deposito_inical * (1 + taxa_juros) ** 24 

print('O valor final deste depósito após 24 meses: R$%3.2f' % deposito_final)