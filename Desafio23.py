numero = int(input('Informe um número (0 a 9999): '))
unidade = numero // 1 % 10 
dezena = numero //10 % 10
centena = numero //100 % 10
milhar = numero //1000 % 10 
print(f'Analisando o número{numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

    #Meu Suposto código Certo 
# numero = str(input('Digite um Valor de 0 a 9999: '))
# print(f'Unidade: {numero[3:4]}')
# print(f'Dezena: {numero[2:3]}')
# print(f'Centena: {numero[1:2]}')
# print(f'Milhar {numero[0:1]}')
# #Separando dígitos de um número

#Separando dígitos de um número