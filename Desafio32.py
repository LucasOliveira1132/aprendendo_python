ano = int(input('Digite um Ano para descobrir se ele é Bissexto: '))
dividido = ano % 4
if dividido == 0:
    print(f'O Ano de {ano} é Bissexto')
else:
    print(f'O Ano de {ano} não é Bissexto')

#Ano Bissexto