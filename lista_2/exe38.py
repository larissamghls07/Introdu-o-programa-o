'''
prg038 - Escreva um programa que leia uma idade (número inteiro) e se é brasileiro (True ou
False). Ao final deve informar:
• Idade de 18 a 70 anos e brasileiro ........................................... : Voto obrigatório
• Idade de 16 a 17 ou acima de 70 anos e brasileiro.................. : Voto não obrigatório
• Abaixo de 16 anos ou não brasileira ........................................ : Voto não permitido
'''

idade = int(input('Digite uma idade: ')) 
nacionalidade = str(input('Você é brasileiro: '))

if nacionalidade == 'Sim' or nacionalidade == 'sim':
  nacionalidade = True
else:
  nacionalidade = False


if 18 <= idade <= 70 and nacionalidade == True:
  print(f'Voto obrigatório.')
else:
  if 16 <= idade <= 17 and idade >= 70 and nacionalidade == True:
    print(f'Voto não obrigatório!')
  else:
    print(f'Voto não permitido!')