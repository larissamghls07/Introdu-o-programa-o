'''
prg057 – Atualize o seu programa anterior para exibir o maior e o menor número lido.
'''

'''
prg056 – Escreva um programa que leia números até que um número negativo seja lido. Seu
programa ao final do processamento deve exibir a soma, a quantidade e a média dos números
lidos.
'''

token = True 
menor = float('inf') 
'''qualquer número real encontrado durante a leitura ou comparação será menor que o valor inicial usado para inicializar essa variável'''
soma, i, maior = 0, 0, 0 

while token:
    num = int(input(f'Digite um número: '))
    if num < 0: 
        token = False
    else: 
        soma += num
        i += 1
        if num < menor:
            menor = num
        if num > maior:
            maior = num

if i > 0:
    media = soma / i

    print(f'A soma dos números: {soma}.\nA quantidade de números digitados foi de {i}.\nA média dos números: {media}.')
else:
    print(f'Nenhum número válido foi digitado.')