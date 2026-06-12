'''
prg027 - Escreva um programa baseado no prg026, mas inclua na leitura o percentual de
frequência do aluno. Se o aluno obtiver um percentual menor que 75, estará reprovado não
importando a sua média.
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
freq = float(input('Digite o percentual de frequência: '))

media = (n1 + n2) / 2

if media >= 6 and media <=9.9 and freq >= 75:
  print('Aprovado!')
if media < 6 or freq < 75:
  print('Reprovado!')
if media == 10 and freq >= 75:
  print('Aprovado com distinção!')