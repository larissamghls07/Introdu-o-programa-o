'''
Crie um programa que leia a quantidade de dias trabalhados e o valor do salário por dia. 
Seu programa deve calcular o salário mensal. 

Em seguida calcule o valor da comissão baseado na quantidade de dias trabalhados, conforme a tabela
a seguir: 

0 - 10 -> 12%
11 - 18 -> 14%
19 - 25 -> 16%
Acima de 26 -> 18%
'''

dias_trab = int(input('Digite os dias trabalhados: '))
valor_salariodia = float(input('Digite o valor do salário diário: '))

salariomensal = float(dias_trab * valor_salariodia)

if dias_trab <= 10:
  comissao = 0.12 * salariomensal
else:
  if dias_trab <= 18:
    comissao = 0.14 * salariomensal
  else:
    if dias_trab <= 25:
      comissao = 0.16 * salariomensal
    else:
      comissao = 0.18 * salariomensal

salariomensal += comissao
print(f'O seu novo salário é de R${salariomensal} e a sua comissão vale R${comissao}')
