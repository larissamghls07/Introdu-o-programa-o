'''
prg054 – Escreva um programa que leia a quantidade de votos a serem lidos. Para cada voto o
usuário digita 0 para branco, 1 para o candidato Bráulio e 2 para a candidata Theresa. Se
digitar qualquer número diferente deve computar como nulo. Seu programa deve informar ao
final a quantidade de votos e o percentual de cada um. (Branco, Nulos, Bráulio e Thereza)
'''
branco, braulio, theresa, nulo = 0,0,0,0 

qtd_voto = int(input(f'Digite a quantidade de voto: '))
for i in range(qtd_voto):
  print('0 - branco\n1 - Braúlio\n2 - Theresa')
  voto = int(input(f'Digite o seu voto: '))
  if voto == 0:
    branco += 1
  else:
    if voto == 1:
      braulio += 1
    else:
      if voto == 2:
        theresa += 1
      else:
        nulo += 1
print(f'Branco: {branco} com percentual de {100*(branco/qtd_voto)}%\nBraúlio: {braulio} com percentual de {100*(braulio/qtd_voto)}%\nTheresa: {theresa} com percentual de {100*(theresa/qtd_voto)}%\nNulo: {nulo} com percentual de {100*(nulo/qtd_voto)}%.')