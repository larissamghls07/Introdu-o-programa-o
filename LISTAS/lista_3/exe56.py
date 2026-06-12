'''
prg056 – Escreva um programa que leia números até que um número negativo seja lido. Seu
programa ao final do processamento deve exibir a soma, a quantidade e a média dos números
lidos.
'''

token = True 
soma, i = 0, 0
while token:
    num = int(input(f'Digite um número: '))
    soma += num
    i += 1
    if num < 0:
        token = False

media = soma / i

print(f'A soma dos números: {soma}.\nA quantidade de números digitados foi de {i}.\nA média dos números: {media}.')