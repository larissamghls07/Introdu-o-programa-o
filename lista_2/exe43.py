'''
prg043 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

Preço por tipo e faixa de consumo
Tipo Faixa (kWh) Preço

Residencial Até 500 R$ 0,40
Acima de 500 R$ 0,65

Comercial Até 1000 R$ 0,55
Acima de 1000 R$ 0,60

Industrial Até 5000 R$ 0,55
Acima de 5000 R$ 0,60
'''

kwh = float(input('Digite a quantidade de kWh consumida: '))
tipo = input('R - residência\nI - indústria\nC - comércio\nTipo de instalação: ')

if tipo == 'R':
    if kwh <= 500:
        preco = float(kwh * 0.40)
    else:
        preco = float(kwh * 0.65)
else:
    if tipo == 'C':
        if kwh <= 1000:
            preco = float(kwh * 0.55)
        else:
            preco = float(kwh * 0.6)
    else:
        if tipo == 'I':
            if kwh <= 5000:
                preco = float(kwh * 0.55)
            else:
                preco = float(kwh *0.6)

print(f'De acordo com a instalação pedida: {tipo}, o preço será de R${preco}')