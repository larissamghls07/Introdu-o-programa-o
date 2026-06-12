'''
prg052 – Escreva um programa que leia 10 números reais e por fim informe a soma dos
números lidos.
'''

soma = 0

for i in range(10):
  n = float(input(f'Digite o número: '))
  soma += n

print(f'A soma dos 10 números é: {soma}')