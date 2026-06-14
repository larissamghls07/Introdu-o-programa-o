'''
prg075 – Faça um programa parecido com os anteriores, mas agora com a validação do CNPJ.
'''
soma, soma2 = 0, 0 

cnpj = input(f'Infome o seu CNPJ: ')

if int(len(cnpj)) != 12:
    print(f'Informe um CNPJ válido!')
else:
    print('podemos continuar')


for i in range(4):
    soma += int(cnpj[i]) * (5 - i)

for j in range(8):
    soma += int(cnpj[j+4]) * (9 - j)
    print(int(cnpj[j+4]) * (9 - j))

