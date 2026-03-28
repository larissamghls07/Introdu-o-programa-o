'''
prg042 - Escreva um programa que receba o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
• salários até R$ 280,00 (incluindo)...................: aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 .............: aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 ...........: aumento de 10%
• salários de R$ 1500,00 em diante...................: aumento de 5%
Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.
'''

salario = float(input('Digite o seu salário: '))

if salario <= 280:
    perc = int(20)
    aumento = 0.20 * salario
    salario_dep = 1.2 * 280
else:
    if salario <= 700:
        perc = int(15)
        aumento = 0.15 * salario
        salario_dep = 1.15 * salario
    else:
        if salario <= 1500:
            perc = int(10)
            aumento = 0.10 * salario
            salario_dep = 1.10 * salario
        else:
            perc = int(5)
            aumento = 0.05 * salario
            salario_dep = 1.05 * salario

print(f'• o salário antes do reajuste: {salario}\n• o percentual de aumento aplicado: {perc}%\n• o valor do aumento: {aumento}\n• o novo salário: {salario_dep}.')