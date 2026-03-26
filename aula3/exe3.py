'''
Faça um programa que leia a idade de uma pessoa e a enquadre de acordo com a tabela a seguir: 

0 a 12 anos - criança 
13 a 17 anos - adolescente 
18 a 64 anos - adulto 
65 além - idoso
'''


idade = int(input('Digite a sua idade: '))

if 0 <= idade <= 12:
  print(f'Você é uma criança porque tem {idade} anos.')
else:
  if 13 <= idade <= 17:
    print(f'Você é um adolescente porque tem {idade} anos!')
  else:
    if 18 <= idade <= 64:
      print(f'Você é um adulto porque tem {idade} anos!')
    else:
      print(f'Você é um idoso porque tem {idade} anos!')
