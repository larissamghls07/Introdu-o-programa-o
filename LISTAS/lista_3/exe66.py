'''
prg066 – Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
ano, e um país B, com 7 milhões de habitantes e uma taxa de natalidade de 2% ao ano, calcular e imprimir o tempo necessário para que a população do país A ultrapasse a população do país B.
'''


pais_A = float(5000000) 
pais_B = float(7000000)
tempo = int(1) 

while pais_A < pais_B:
    somaA = pais_A + (pais_A * 0.03 * tempo)
    pais_A += somaA
    somaB = pais_B + (pais_B * 0.02 * tempo)
    pais_B += somaB
    tempo += 1


print(f'A população do país A levou {tempo} anos para ultrapassar a população do país B.')