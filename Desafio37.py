numero = int(input('Digite um Número inteiro: '))    
print(''' Escolha uma das Bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print(f'{numero} Convertido para Binário é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} Convertido para Octal é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} Convertido para Hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Não existe essa opção')




#Conversor de Bases Numéricas