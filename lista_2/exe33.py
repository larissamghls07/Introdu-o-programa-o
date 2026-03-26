'''
prg033 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''

velocidade = int(input('Digite a velocidade alcançada: '))

if velocidade > 80:
    multa = float((velocidade - 80) * 5)
    print(f'Você foi multado em R${multa}!')
else:
    print('Prossiga assim, respeitando o limite de 80Km/h.')