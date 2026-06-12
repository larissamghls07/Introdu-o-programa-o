'''
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
'''

salario_atual = float(input('Digite seu atual salário: '))
porcentagem_aumento = float(input('Digite qual será a porcentagem de aumento: '))

novo_salario = (1 + porcentagem_aumento/100) * salario_atual
print('O seu novo salário é: ', novo_salario)



