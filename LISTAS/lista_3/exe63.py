'''
Leia um número e faça o seu fatorial.
'''
mult = 1
num = int(input(f'Informe um número: '))
for i in range(num,0,-1):
  mult *= i
  if i == 1:
    print(f' {i} = ',end='')
  else:
    print(' ',i, 'x', end='')
print(mult)