'''
prg051 – Escreva um programa que leia a temperatura inicial de um motor e quantos graus ela
ganha a cada leitura de 10 segundos, por fim calcule e informe quantos graus ela terá após 16
leituras.
'''


temp_inicial = float(input(f'Digite a temperatura inicial: '))
aumento_acada10s = float(input(f'Digite a quantidade de graus que aumenta a cada 10s: '))

temp_final = temp_inicial

for i in range(16):
  temp_final += aumento_acada10s

print(f'A temperatura final do motor será de: {temp_final}°C')