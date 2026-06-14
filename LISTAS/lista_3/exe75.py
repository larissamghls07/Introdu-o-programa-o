'''
prg075 – Faça um programa parecido com os anteriores, mas agora com a validação do CNPJ.
'''
soma, soma2, digito1, digito2 = 0, 0, 0, 0 

cnpj = input(f'Infome o seu CNPJ: ')

#o cnpj precisa ter 12 elementos 
if int(len(cnpj)) != 12:
    print(f'Informe um CNPJ válido!')
else:
    print('podemos continuar')

int(cnpj)

#verificação do primeiro dígito 
for i in range(4):
    soma += cnpj[i] * (5 - i)

for j in range(8):
    soma += cnpj[j+4] * (9 - j)

if (soma % 11) < 2:
    digito1 = 0
else:
    digito1 = 11 - (soma % 11) 
#fim da verificação do primeiro dígito 

#verificação do segundo dígito 
for l in range(5):
    soma2 += cnpj[l] * (6 - l)

for k in range(7):
    soma2 += cnpj[k+5] * (9 - k)

if (soma2 % 11) < 2:
    digito2 = 0
else:
    digito2 = 11 - (soma2 % 11)
#fim da verificação do segundo dígito

print(digito1, digito2)