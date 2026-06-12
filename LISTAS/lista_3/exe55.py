'''
prg055 – Escreva um programa que leia 800 pesquisas. Para cada pesquisa pergunta-se a
idade, se tem internet em casa, caso tenha pergunte a velocidade da internet, se tem celular
com acesso a internet, se tem computador e se tem tablet. Seu programa ao final deve
informar a média da idade das pessoas pesquisadas, o percentual de pessoas que tem internet
em casa, a média de velocidade dessa internet, o percentual de pessoas que tem computador
e o percentual que tem tablet.
'''

'''
Vou modificar a quantidade de pesquisar para viabilizar testes ao longo da escrita. Como o que foi pedido
é um total de 800, caso seja necessário executar para essa quantidade é possível alterar a linha que contém
o for, especificamente no parâmetro dentro do range. A linha seria: 
for i in range(800):

Percentual de algo: (parte/total) * 100
'''

media_idade, contador, contador_internet, velocidadeSOMA, contador_pc, contador_tablet = 0, 0, 0, 0, 0, 0

for i in range(2):
    idade = int(input(f'Digite a sua idade: '))
    media_idade += idade
    contador += 1
    internet = str(input(f'Você tem internet em casa?\nS - para sim\nN - para não: '))
    if internet == 'S':
        contador_internet += 1
        velocidade = int(input(f'Digite a velocidade em números da sua internet: '))
        velocidadeSOMA += velocidade
    cel = str(input(f'Seu celular tem acesso à internet?\nS - para sim\nN - para não: '))
    pc = str(input(f'Você tem computador em casa?\nS - para sim\nN - para não: '))
    if pc == 'S':
        contador_pc += 1
    tablet = str(input(f'Você tem tablet?\nS - para sim\nN - para não: '))
    if tablet == 'S':
        contador_tablet += 1

media_idade = media_idade / contador
perc_internet = (contador_internet / contador) * 100
perc_pc = (contador_pc / contador) * 100
perc_tablet = (contador_tablet / contador) * 100

print(f'A média das idades é: {media_idade}')
print(f'O percentual de pessoas com internet em casa: {perc_internet}%')
print(f'O percentual de pessoas com computador em casa: {perc_pc}%')
print(f'O percentual de pessoas com tablet em casa: {perc_tablet}%')