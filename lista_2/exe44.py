'''
prg044 - Escreva um programa que calcule o que deve ser pago por um produto, considerando
o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado. 
Código Condição de pagamento
1 À vista em dinheiro ou cartão de débito, recebe 15% de desconto
2 À vista no cartão de crédito, recebe 10% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em duas vezes, preço normal de etiqueta mais juros de 10%
'''
preco = float(input('Digite o preço do produto: '))
tipo = int(input('1 À vista em dinheiro ou cartão de débito, recebe 15% de desconto\n2 À vista no cartão de crédito, recebe 10% de desconto\n3 Em duas vezes, preço normal de etiqueta sem juros\n4 Em duas vezes, preço normal de etiqueta mais juros de 10%\nQual será a forma de pagamento: '))

if tipo == 1:
    preco = 0.85 * preco
else:
    if tipo == 2:
        preco = 0.90 * preco
    else:
        if tipo == 3:
            preco = preco
        else:
            if tipo == 4:
                preco = 1.1 * preco

print(f'O preço alinhado à forma de pagamento: R${preco}')