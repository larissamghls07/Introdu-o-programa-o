'''
prg016 - Escreva um programa que leia o custo de fábrica de um carro e imprima o custo ao
consumidor. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a
percentagem do distribuidor seja de 28% e os impostos de 45%.
'''

custo_fabrica = float(input('Digite o custo de fábrica deste carro: '))
custo_ao_consumidor = custo_fabrica + (0.28 * custo_fabrica) + (0.45 * custo_fabrica)

print('O custo ao consumidor é %d' %custo_ao_consumidor)
