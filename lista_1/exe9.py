'''
Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a
distância a percorrer e a velocidade média esperada para a viagem.

'''
distancia = float(input('Digite a sua distância total: '))
velocidade = float(input('Digite a velocidade média: '))
tempo = distancia / velocidade
print('O tempo de viagem é:', tempo, 'segundos.')