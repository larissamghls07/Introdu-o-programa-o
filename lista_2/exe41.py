'''
prg041 - Escreva um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
Desconto do IR:
• Salário Bruto até 900 (inclusive)................: isento
• Salário Bruto até 1500 (inclusive)..............: desconto de 5%
• Salário Bruto até 2500 (inclusive)..............: desconto de 10%
• Salário Bruto acima de 2500......................: desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da
hora é R$ 50,00 e a quantidade de horas é 200.
• Salário Bruto: (50 * 200)..: R$ 10.000,00
• (-) IR (20%) .......................: R$ 2.000,00
• (-) Sindicato (3%)..............: R$ 300,00
• FGTS (11%).......................: R$ 1.100,00
• Total de descontos...........: R$ 2.300,00
• Salário Líquido..................: R$ 7.700,00
'''
valor_hora = float(input(f'Digite o valor da sua hora de trabalho: '))
qtd_hora = int(input(f'Digite a quantidade horas trabalhadas: '))

bruto = float(valor_hora * qtd_hora)

if bruto <= 900:
    (f'Isento de pagamento.')
    ir = float(0)
    desc = int(0)
else:
    if bruto <= 1500:
        desc = int(5)
        ir = float(0.05 * bruto)
    else:
        if bruto <= 2500:
            desc = int(10)
            ir = float(0.10 * bruto)
        else:
            desc = int(20)
            ir = float(0.20 * bruto)

sind = float(0.03 * bruto)
fgts = float(0.11 * bruto)
tot_desc = float(ir + sind + fgts)

#fora da estrutura condicional 

print(f'• Salário Bruto: (...........: R$ {bruto}\n• (-) IR ({desc}%) .......................: R$ {ir}\n• (-) Sindicato (3%)..............: R$ {sind}\n• FGTS (11%).......................: R$ {fgts}\n• Total de descontos...........: R$ {tot_desc}\n• Salário Líquido..................: R$ {bruto - tot_desc}')
