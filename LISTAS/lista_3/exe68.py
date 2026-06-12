'''
prg068 – Escreva um programa que ajude o DETRAN a saber o total de recursos que serão
arrecadados com a aplicação de multas de trânsito. O programa deve ler, para cada motorista, as seguintes informações:
• O número da carteira de motorista
• O número de multas
• O valor de cada uma das multas
Deve ser impresso o valor da dívida para cada motorista e, ao final da leitura, o total de
recursos arrecadados (somatório de todas as multas). O programa deverá imprimir também o
número da carteira do motorista que obteve o maior número de multas. O programa termina
ao ler a carteira de motorista de valor 0.
'''
divida, totowolf, maior = 0, 0, 0
bancodedados = []

while True:
    divida = 0
    carteira = int(input(f'Digite o número da sua carteira: '))
    if carteira == 0:
        break  
    multas = int(input(f'Informe o número de multas: '))
    bancodedados.append((carteira,multas))
    for j in range(len(bancodedados)):
        if bancodedados[j][1] > maior:
            maior = bancodedados[j][0]
    for i in range(1,multas+1):
        multa = float(input(f'Informe o valor da {i} multa: '))
        divida += multa
    totowolf += divida
    print(f'A sua dívida é de R${divida}')   

print(f'O motorista com a carteira {maior} tem a maior quantidade de multas.')

print(f'A arrecadação total: R${totowolf}')
