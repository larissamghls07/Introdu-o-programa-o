'''
1 - Crie um programa que leia números inteiros até o mesmo 0 (zero) ser digitado. Armazene-os em um vetor e ao final exiba o conteúdo do vetor.
'''

numeros = [] #criando um vetor vazio, caso fosse necessário poderia escolher a quantidade de posições, por exemplo: um vetor de 10 posições - numeros[10]

while True:
  num = int(input(f'Digite um número:'))
  if num == 0:
    break
  numeros.append(num)

print(f'O vetor final: ', numeros)

'''
A prova será feita somente de programas.
O número dentro dos [] é o número que representa o índice do vetor.
numero[0] = 5
numero[1] = 8

O vetor na posição 0 recebeu um valor de 5, já o vetor na posição 1 recebeu o valor de 8. 
Um intervalo de 0 a 9 tem 10 posições. 
'''


'''
numeros = []

num = int(input(f'Digite um número: ))

while num != 0:
  numeros.append(num)
  num = int(input(f'Digite um número ou zero para finalizar: ))

print(numeros)
Informe a quantidade de números que foram adicionados 
print(len(numeros))
'''


