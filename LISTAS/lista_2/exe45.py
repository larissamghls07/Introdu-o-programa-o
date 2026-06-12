'''
prg045 - Escreva um programa que leia o peso e a altura de um adulto, calcule o IMC por meio da fórmula a seguir e mostre sua condição de acordo com a tabela abaixo.

Fórmula: IMC = peso. altura2
• Abaixo de 18,5 ............. : Abaixo do peso
• Entre 18,5 e 25 ............. : Peso normal
• Entre 25 e 30 ................ : Acima do peso
• Acima de 30 ................. : Obeso
'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Abaixo do peso!')
else:
    if imc < 25:
        print('Peso normal!')
    else:
        if imc <= 30:
            print('Acima do peso!')
        else:
            print('Obeso!')