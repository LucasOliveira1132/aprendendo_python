soma = 0
for contador in range (0,6):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma entre os numeros Pares é {soma}')