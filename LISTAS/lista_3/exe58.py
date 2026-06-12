'''
prg058 – Escreva um programa que faça orçamentos de um determinado produto. Leia o
nome da loja e o preço do produto de diversos orçamentos. Faça seu programa perguntar se
deseja continuar ou finalizar após ler cada orçamento. Por fim deve informe o nome da loja
onde o produto seja mais barato e preço praticado
'''

token = True
menor = float('inf')

while token:
    nome_loja = str(input(f'Digite o nome da loja: '))
    preco = float(input(f'Digite o preço do produto: '))
    passe = int(input(f'Deseja continuar o orçamento, 1 -- sim e 2 -- não: '))
    if passe == 2:
        token = False
    if preco < menor:
        menor = preco
        loja_maisbarata = nome_loja

print(f'O produto mais barato custa R${menor} na loja {loja_maisbarata}.')
