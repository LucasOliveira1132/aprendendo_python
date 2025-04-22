numero = int(input('Digite um numero Inteiro:'))
total = 0
for contador in range(1,numero+1):
    if numero % contador == 0:
        print( '\033[033m', end= '')
        total += 1
    else:
        print('\033[31m', end= ' ')
    print(f'{contador}', end= ' ')
print(f'\n\033[m0 número {numero} foi divisível {total} vezes ')
if total == 2:
    print('Por isso o número é PRIMO')
else:
    print('O número NÃO É PRIMO')
#Números primos