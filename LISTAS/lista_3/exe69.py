'''
prg069 – Elabore um programa para calcular o valor arrecadado por um curso de informática
com a turma de programação de computadores em um mês. Cada linha de entrada deverá
conter:
• O número de matrícula do aluno
• O número de créditos cursados
• O valor da Bolsa de Estudo: (0) 20%; (1) 50%, (2) 100%
Cada crédito custa R$ 15,00. Calcule também o montante fornecido pelo curso em Bolsas de
Estudo. A entrada de dados termina quando o número de matrícula digitado é nulo.
'''

tot_creditos, tot_bolsas, desconto = 0, 0, 0 

while True:
    credito = 0
    matricula = int(input(f'Infome o número de matrícula: '))
    if matricula == 0:
        break
    credito = int(input(f'Informe a quantidade de créditos cursados: ')) * 15
    dec = int(input(f'Você é bolsista?\n 1 - Sim e 2 - Não: '))
    if dec == 1:
        bolsa = int(input(f'(0) - 20%;\n(1) - 50%;\n(2) - 100%.\nInforme o valor da bolsa de estudos: '))
        if bolsa == 0:
            desconto = 0.2 * credito
            credito -= (0.2 * credito)
        else:
            if bolsa == 1:
                desconto = 0.5 * credito    
                credito -= (0.5 * credito)

    tot_creditos += credito
    tot_bolsas += desconto
    print(tot_creditos)
    print(tot_bolsas)
print(f'O total arrecadado é de: R${tot_creditos}')
print(f'O montante de desconto fornedido foi de R${tot_bolsas}')