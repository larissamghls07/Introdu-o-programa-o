'''
5 - Crie um programa que sorteie um jogo de 6 dezenas entre 1 e 60. Em seguida leia 6 números informados pelo usuário e informe quantos ele acertou. 
'''
qtd = 0
from random import randint


jogo = []
for j in range(6):
  numero = randint(1,60)
  if numero in jogo:
    numero = randint(1,60)
  else:
    jogo.append(numero)

usuario = []
for i in range(6):
  usuario.append(int(input(f'Infome o {i+1}º número: ')))

for k in range(6):
  if usuario[k] in jogo:
    qtd += 1
print(f'O jogo sorteado: ', jogo)
print(f'A quantidade de números certos escolhidos na rodada: {qtd}')


'''
Versão professor (sem tratar os dados para repetição)
from random import randint

sorteados = []
contador = 0

for j in range(6):
  sorteados.append(randint(1,60))

for i in range(6):
  num = int(input(f'Informe um número: ))
  if num in sorteados:
    contador += 1

print(sorteados)
print("Acertou %d dezenas: " % contador)
'''