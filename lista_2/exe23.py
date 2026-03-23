'''
prg023 - Escreva um programa que leia uma letra e caso a letra seja C, imprima “Casado”, caso
seja “S” imprima “Solteiro” e caso não seja nenhuma das duas, imprima “Estado Civil não
encontrado”.
'''

resposta = input('C - casade\nS - solteire\nDigite seu estado civil:')
print(resposta)

if resposta == 'C':
  print('Casade!')
if resposta == 'S':
  print('Solteire!')
if resposta !='C' and resposta !='S':
  print('Estado Civil não encontrado!')
