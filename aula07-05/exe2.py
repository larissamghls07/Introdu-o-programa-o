'''
Faça um programa que leia 5 números inteiros e ao final informe a sua soma.
'''
soma = 0
j = 0
for i in range(5):
  num = int(input(f'Digite um número: '))
  soma += num
  j += 1
print(j)
media = soma / j

print(soma, media)