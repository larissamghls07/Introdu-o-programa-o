'''
prg067 – Escreva um programa que controle o saldo bancário de um cliente. O programa lê o
valor do saldo anterior e, em seguida, lê as operações realizadas na conta. As operações
podem ser as seguintes:
• Saque em dinheiro (código 10);
• Depósito (código 33);
• Pagamento de cheque (código 4, tarifa de R$ 0,50 por operação)
'''
cod, saque, saldo, deposito, chequy = 0, 0, 0, 0, 0

saldo_anterior = float(input(f'Digite o seu saldo anterior: '))

cod = int(input(f'• Saque em dinheiro (código 10);\n• Depósito (código 33);\n• Pagamento de cheque (código 4, tarifa de R$ 0,50 por operação)\nO que deseja fazer? '))

if cod == 10:
    saque = float(input(f'Valor do saque: '))
    saldo = saldo_anterior - saque
else:
    if cod == 33:
        deposito = float(input(f'Quanto deseja depositar? '))
        saldo = saldo_anterior + deposito
    else:
        if cod == 4:
            chequy = float(input(f'Informe quanto deseja pagar: '))
            saldo = saldo_anterior - chequy - 0.5
        else:
            print(f'Digite uma operação VÁLIDA.')


print(f'O saldo após a operação é de R${saldo}')