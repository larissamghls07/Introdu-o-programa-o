'''
4 - Modifique o programa anterior para não permitir repetições entre as 6 dezenas.
'''

from random import randint

for i in range(100):
  jogo = []
  for j in range(6):
    numero = randint(1,60)
    if numero in jogo:
      numero = randint(1,60)
    else:
      jogo.append(numero)
  print(f'Os números escolhidos na rodada {i+1}: {jogo}', end='\n')


'''
Versão do professor
from random import randint

for i in range(100):
  jogo = []
  for j in range(6):
    n = randint(1,60)
    while n in jogo: #testa se numero está em sorteado, se ele tiver, o while é executado pra sortear outro número não repetido
     n = randint(1,60)
    jogo.append(n)

  if i == 5:
    print(n)
  else:
    print(n, end='-')
'''