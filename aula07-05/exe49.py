'''
prg049 – Escreva um programa que execute 5 operações de soma. Para cada operação o
programa deve pedir dois números e informar a soma com o seguinte formato: Soma 1 = 10,
onde o 1 do exemplo representa o número da soma e o 10 o resultado da adição dos dois
números informados.
'''

for i in range(10):
  if i % 2 == 0:
    num1 = int(input(f'Digite o 1º número: '))
    num2 = int(input(f'Digite o 2º número: '))
    soma = num1 + num2
    print(f'A soma é igual a {soma}')