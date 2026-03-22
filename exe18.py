'''
prg018 - Escreva um programa que receba o salário fixo de um funcionário e o valor de suas
vendas, calcule e mostre a comissão e o salário final do funcionário. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
'''

salario = float(input('Digite o seu salário: '))
vendas = float(input('Digite o valor das vendas: '))

comissao = 0.04 * vendas
salario_final = salario + comissao

print(f'O valor da comissão é {comissao}, o salário fixo é {salario} enquanto com o salário atual é {salario_final}')
