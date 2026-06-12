'''
Faça um programa que simule um jogo de dados. Seu programa deve simular um jogador
e lançar dois dados 5 vezes. O total de cada lançamento deve ser adicionado ao vetor.
Ao final imprima o conteúdo do vetor. 
'''


from random import randint


sorteados = []

for i in range(5):
  sorteados.append(randint(1,6)+randint(1,6))

print(sorteados)