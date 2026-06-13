'''
prg074 – Escreva um programa que leia um CPF e informe se é um CPF válido ou não. Caso não
seja um CPF válido informe este fato ao usuário e pergunte se quer finalizar ou tentar
novamente.
Obs.: Pesquise a regra para validação do CPF na Internet.
'''
qtdiguais, primeirodig, segundodig, soma1, soma2, primeiro = 0, 0, 0, 0, 0, 0

while True:
    cpf = input(f'Informe seu CPF: ')
    if (len(cpf)) != 11:
        print(f'Informe um CPF válido.')
        break
    else:
        #começa o teste de verificação de números iguais 
        primeiro = cpf[0]
        for elemento in cpf:
            if elemento == primeiro:
                qtdiguais += 1
        if qtdiguais == 11:
            print(f'Números iguais, CPF inválido.')
            break
        #finaliza o teste de números igauis 

    #começo da verificação do primeiro digito
        for i in range(9):
            soma1 += int(cpf[i]) * (10 - i)
        if (soma1 % 11) <= 1:
            primeirodig = 0
        else:
            primeirodig = 11 - (soma1 % 11)
    #finaliza a verificação do primeiro digito
     
    #começo da segunda verificação
        for j in range(10):
            soma2 += int(cpf[j]) * (11 - j)
        resto = soma2 % 11
        if (resto) <= 1:
            segundodig = 0
        else:
            segundodig = 11 - (soma2 % 11)
    #finaliza a verificação do segundo digito 

        if (primeirodig == int(cpf[9])) and (segundodig == int(cpf[10])):
            print(f'Seu CPF [{cpf}] é válido.')
            decisao = int(input(f'Você quer finalizar? 1 - Sim\n2 - Não e tentar novamente: '))
            if decisao == 1:
                break
print(f'Obrigada pela verificação.')
