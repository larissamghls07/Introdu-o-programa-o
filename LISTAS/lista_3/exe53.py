'''
prg053 – Escreva um programa que leia a descrição, o preço e a quantidade de 4 itens de um
supermercado. Seu programa deve calcular e informar para cada item o seu subtotal ( preço x
quantidade ). Seu programa por fim deve informar o total a pagar e ler o valor que o cliente
deu para pagar. Para finalizar seu programa deve informar o troco.
'''

subtotal, tot = 0,0 
for i in range(4):
  nome_item = input(f'Digite o nome do produto: ')
  preco = float(input(f'Digite o preço do produto: '))
  qtd = float(input(f'Digite a quantidade de produto: '))
  subtotal = preco * qtd
  print(f'O subtotal é: R${subtotal}')
  tot += subtotal

print(f'O total a pagar: R${tot}') 
nota = float(input(f'Informe o valor que será dado para pagar: '))
troco = float(nota - tot)
print(f'O seu troco será de R${troco}')