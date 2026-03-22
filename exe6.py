'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
usuário. Calcule o total em segundos.
'''

dia = float(input('Digite a quantidade de dias: '))
hora = float(input('Digite a quantidade de horas: '))
minuto = float(input('Digite a quantidade de minutos: '))
segundo = float(input('Digite a quantidade de segundos: '))

segundos = (dia * 24 * 3600) + (hora * 3600 ) + (minuto * 60) + segundo

print('O total de segundos é: ', segundos)