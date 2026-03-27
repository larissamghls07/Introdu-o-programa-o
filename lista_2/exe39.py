'''
prg039 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a
pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da
prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
'''
valor_casa = float(input(f'Qual o valor da casa a comprar: '))
salario = float(input(f'Digite o seu salário: '))
qtd_anos = float(input(f'Digite a quantidade de a pagar: '))

teto_30 = 0.30 * salario
meses = qtd_anos * 12

if (valor_casa/meses) > teto_30:
  print(f'A prestação vale: R${valor_casa/meses}.')
else:
  print(f'O valor da prestação superou ')
