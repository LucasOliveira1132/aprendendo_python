numero = int(input('Digite um numero Par ou Ímpar: '))
resto_do_numero = numero/2 % 1
if resto_do_numero == 0:
    print(f'O Numero {numero} é Par')
else:
    print(f'O numero {numero} é Ímpar')
#Par ou Ímpar?