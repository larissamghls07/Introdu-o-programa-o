'''
prg019 - Escreva um programa que receba o ano de nascimento de uma pessoa e o ano atual,
calcule e mostre:
 a idade dessa pessoa em anos;
 a idade dessa pessoa em meses;
 a idade dessa pessoa em dias;
 a idade dessa pessoa em semanas.
'''

anonasci = int(input('Digite o ano de nascimento: '))
anoatual = int(input('Digite o ano atual: '))

print(f'A idade dessa pessoa em anos {anoatual - anonasci};\nA idade dessa pessoa em meses {(anoatual - anonasci) * 12};\nA idade dessa pessoa em dias {(anoatual - anonasci) * 365};\nA idade da pessoa em semanas {(anoatual - anonasci) * 12 * 4}.')