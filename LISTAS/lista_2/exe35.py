'''
prg035 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do
aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os
inferiores ou iguais, de 15%.
'''

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    aumento = salario * 1.1
    print(f'Seu novo salário é de R${aumento} com aumento de 10%.')
if salario <= 1250:
    aumento = salario * 1.15
    print(f'Seu novo salário é de R${aumento} com aumento de 15%.')