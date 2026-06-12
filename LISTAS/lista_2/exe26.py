'''
prg026 - Escreva um programa para a leitura de duas notas de um aluno. O programa deve
calcular a média alcançada pelo aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
• A mensagem "Reprovado", se a média for menor do que seis;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 6 and media <=9:
  print('Aprovado!')
if media < 6:
  print('Reprovado!')
if media == 10:
  print('Aprovado com distinção!')

