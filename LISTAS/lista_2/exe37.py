'''
prg037 - Escreva um programa que leia dois números e que pergunte qual operação você
deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('----------------------------------')
op = input('+ - soma\n- - subtração\n* - multiplicação\n/ - divisão\nQual operação você deseja realizar:  ')


if op == '+':
    print(f'A soma é {n1+n2}.')
if op == '-':
    if n1 > n2:
        print(f'A subtração é {n1 - n2}.')
    else:
        print(f'A subtração é {n2 - n1}.')
if op == '*':
    print(f'A multiplicação é {n1*n2}.')
if op == '/':
    if n1 > n2:
        print(f'A divisão é {n1/n2}.')
    else:
        print(f'A divisão é {n2/n1}.')

