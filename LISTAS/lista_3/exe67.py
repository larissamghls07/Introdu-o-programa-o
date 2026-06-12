'''
prg067 – Escreva um programa que controle o saldo bancário de um cliente.
O programa lê o valor do saldo anterior e, em seguida, lê as operações
realizadas na conta. As operações podem ser as seguintes:
• Saque em dinheiro (código 10);
• Depósito (código 33);
• Pagamento de cheque (código 4, tarifa de R$ 0,50 por operação)

O programa lê o código das operações e realiza as atualizações na conta,
imprimindo uma mensagem ao usuário caso seu saldo esteja negativo.
O programa deve continuar a leitura até que o código da operação seja zero.
Códigos diferentes dos definidos devem ser ignorados. Ao final do
processamento o programa deve imprimir o saldo atual do cliente.
'''
cod, saque, saldo, deposito, chequy, qtd = 0, 0, 0, 0, 0, 0
saldo = float(input(f'Digite o seu saldo anterior: '))


while True:
    cod = int(input(f'• Saque em dinheiro (código 10);\n• Depósito (código 33);\n• Pagamento de cheque (código 4, tarifa de R$ 0,50 por operação)\nDigite 0 para sair das operações.\nO que deseja fazer? '))
    if cod == 0:
        break
    else:
        if cod == 10:
            saque = float(input(f'Valor do saque: '))
            saldo = saldo - saque
            qtd += 1
        else:
            if cod == 33:
                deposito = float(input(f'Quanto deseja depositar? '))
                saldo = saldo + deposito
                qtd += 1
            else:
                if cod == 4:
                    chequy = float(input(f'Informe quanto deseja pagar: '))
                    saldo = saldo - chequy - 0.5
                    qtd += 1
                else:
                    print(f'Digite uma operação VÁLIDA.')

if qtd == 1:   
    print(f'O saldo após a operação é de R${saldo}')
else:
    print(f'O saldo após as operações é de R${saldo}')