'''Faça um programa que leia um total em segundos
 e gere na tela esse tempo e dias, minutos e segundos'''

tot_s = int(input('Digite o total em segundos: '))
dias = tot_s // 86400 #Total em segundos dividido por 86400 (24 * 60 * 60)
horas = tot_s % 86400 // 3600 #Total de segundos em horas
minutos = tot_s % 86400 % 3600 // 60
segundos = tot_s % 86400 % 3600 % 60
print(f'O total em dias: {dias};\nhoras: {horas};\nminutos: {minutos};\nsegundos: {segundos}.')