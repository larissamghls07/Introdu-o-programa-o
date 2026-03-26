'''
Testar o desconto para imposto de renda de acordo com o salário 
'''

salario = float(input(f'Digite o seu salário: '))

if salario <= 2428.80:
  desconto = 0
  print(f'Não há desconto!')
else:
  if salario <= 2826.65:
    desconto = 0.075 * salario 
    print(f'O desconto será de {desconto}')
  else:
    if salario <= 3751.05:
      desconto = 0.15 * salario
      print(f'O desconto será de {desconto}')
    else:
      if salario <= 4664.88:
        desconto = 0.225 * salario
        print(f'O desconto será de {desconto}')
      else:
        desconto = 0.275 * salario
        print(f'O desconto será de {desconto}')