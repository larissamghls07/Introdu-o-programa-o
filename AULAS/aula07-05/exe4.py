'''
Faça um programa que leia os preços de 15 produtos. Ao final calcule e informe: 

a) a soma dos preços (acumulador)
b) a média dos preços
c) a qtd de produtos que custam entre R$5 e R$10
'''
#j, soma, qtd = 0, 0, 0 
'''pq se inicializa a variável: executa da direita p esquerda antes de criar a variável, se não criar antes
vai dar erro de variável não criada ou não existe''' 

j= 0
soma = 0
qtd = 0
for i in range(15):
  preco = float(input(f'Digite o preço do produto: '))
  soma += preco #letra a 
  j += 1
  if 5<preco<10: 
    qtd += 1 #letra c

media = soma / j #letra b
print(f'A soma é: ', soma)
print(f'A média é: ', media)
print(f'A quantidade de produtos que custam entre R$5 e R$10: ', qtd)