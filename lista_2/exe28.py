'''
prg028 - Escreva um programa que leia o nome, gênero e estado civil de uma pessoa. Caso a
pessoa seja casada e do gênero “F”, peça também o tempo do casamento em anos.
'''

nome = input('Digite o seu nome: ')
genero = input('Digite o seu gênero, F para feminino e M para masculino: ')
estado_civil = input('Digite o seu estado civil: C para casado e S para solteiro: ')

if genero == 'F' and estado_civil == 'C':
    anos_casamento = int(input('Digite os seus anos de casamento: '))
    print(f'Os anos de casados da {nome} é: {anos_casamento}.')
else:
    print('Obrigada por participar, mas não temos interesse em sua resposta.')