'''
prg049 – Escreva um programa que execute 5 operações de soma. Para cada operação o
programa deve pedir dois números e informar a soma com o seguinte formato: Soma 1 = 10,
onde o 1 do exemplo representa o número da soma e o 10 o resultado da adição dos dois
números informados.
'''
soma = 0

for i in range(1,6):
  a = int(input(f'Digite n1: '))
  b = int(input(f'Digite o n2: '))
  soma = a + b
  print(f'A soma {i} é igual a {soma}.')


'''
%d = para números inteiros
%f = para números com ponto flutuante
%s = para strings
'''