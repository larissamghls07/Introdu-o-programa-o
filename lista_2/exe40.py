'''
prg040 - Escreva um programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
• Triângulo Equilátero ..................................: três lados iguais;
• Triângulo Isósceles.....................................: quaisquer dois lados iguais;
• Triângulo Escaleno .....................................: três lados diferentes;
'''

lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if lado1 < (lado2 + lado3) or lado2 < (lado1 + lado3) or lado3 < (lado2 + lado1):
    print('É um triângulo!')

if lado1 == lado2 == lado3:
    print(f'É um triângulo equilátero!')
else:
    if (lado1 == lado2 and lado3 != lado2) or (lado2 == lado3 and lado1 != lado2) or (lado1 == lado3 and lado2 != lado1):
        print(f'É um triângulo isósceles!')
    else:
        print(f'É um triângulo escaleno!')