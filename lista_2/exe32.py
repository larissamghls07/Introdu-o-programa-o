'''
prg032 - Escreva um programa que receba o custo diário de transporte, o salário por dia de um funcionário e a quantidade de dias que este trabalhou no mês. Seu programa deve calcular o desconto do vale transporte considerando que este desconto seja o menor valor entre 6% do seu salário ou o valor do vale transporte. Dica: Calcule o custo de transporte e o salário mensal do funcionário para efetuar os cálculos do desconto do vale transporte.
'''

custo_diario = float(input('Digite o custo diário com transporte: '))
qtd_dia = int(input('Digite a quantidade de dias de trabalho: '))
salario_dia = float(input('Digite o seu salário por dia: '))

teto_6 = (salario_dia * qtd_dia) * 0.06

if (custo_diario * qtd_dia)  < teto_6:
    print(f'O desconto continua sendo o custo real no valor de {custo_diario * qtd_dia}')
else: #Se o custo diário passa o teto de 6%, o desconto será de 6%.
    print(f'O desconto será de 6%, visto que o valor do custo real ultrapassa o teto e, por lei, o empregador não poderá descontar acima de 6% do salário do empregado. Sendo assim, o desconto será de {teto_6} ')
