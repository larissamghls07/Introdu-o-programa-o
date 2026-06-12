'''
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, 
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
'''

qtd_dia = float(input('Informe a quantidade de cigarros fumados por dia: '))
anos_fumante = float(input('Informe a quantidade de anos que passou fumando: '))

dias_perdidos = ((qtd_dia * 10 * anos_fumante * 365) / 60) / 24 


print(f'O total de dias perdidos será ${dias_perdidos}')