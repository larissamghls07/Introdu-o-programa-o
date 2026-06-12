'''
prg050 - Escreva um programa que leia o nome e a as três notas de 6 alunos. Seu programa
deve calcular e informar a média ponderada, onde as notas têm os pesos 2, 3 e 5
respectivamente. Seu programa também deve informar o grau do aluno, aprovado para notas
maiores ou iguais a 6 e em recuperação para as notas menores que 6.
'''


for i in range(6):
  nome = input(f'Digite o seu nome: ')
  n1 = float(input(f'Digite a 1ª nota: '))
  n2 = float(input(f'Digite a 2ª nota: '))
  n3 = float(input(f'Digite a 3ª nota: '))
  media = ((n1*2)+(n2*3)+(n3*5)) / 10
  print('Média: %3.1f' % media)
  if media>=6:
    print(f'Aprovado com média: {media}')
  else:
    print(f'Recuperação pela média: {media}')


#%3.1f a nota terá 3 dígitos, mas apenas 1 após a vírgula Ex: 10.0 ou 9.3