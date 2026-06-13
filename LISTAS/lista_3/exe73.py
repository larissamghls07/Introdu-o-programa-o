'''
prg073 – Escreva um programa que leia um endereço de email e verifique se é um endereço
de e-mail válido. Um endereço de email válido deve conter pelo menos 10 caracteres, sendo 1 deles (somente um) um ponto e um arrouba. Este arrouba e este ponto não podem estar nem no início e nem no final da cadeia lida. Caso não seja um email válido informe este fato ao usuário e pergunte se quer finalizar ou tentar novamente.
'''
arroba = '@'
ponto = '.'
qtd, qtdarroba, qtdponto = 0, 0, 0


while True:
    email = str(input(f'Informe seu e-mail: '))
    if (len(email) >= 10):
        qtd += 1
        for i, arroba in enumerate(email):
            if (arroba == '@' and (i ==1) or (i == len(email))):
                qtdarroba = 0
                break
            else:
                if arroba =='@':
                    qtdarroba += 1
        for j, ponto in enumerate(email):
            if (ponto == '.' and (j ==1) or (j == len(email))):
                qtdponto = 0
                break
            else:
                if ponto == '.':
                    qtdponto += 1

    if (qtd == 1) and (qtdarroba == 1) and (qtdponto == 1):
        print(f'E-mail válido.')
        break
    else:
        print(f'Digite um e-mail válido.')
        dec = int(input(f'Deseja continuar?\n1 - Sim e 2 - Não: '))
        if dec == 2:
            break