ano = int(input('Qual a sua data de Nascimento: '))
data = 2025 - ano
calculo = 18 - data
if data <= 17:
    print(f'Quem nasceu em {ano} tem {data} anos em 2025')
    print(f'Seu Alistamento vai ser daqui a {calculo} ano')
    print('Você não precisa se Alistar')
elif data == 18:
    print(f'Quem nasceu em {ano} tem {data} anos em 2025')
    print('ALISTAR IMEDIATAMENTE')
else:
    print(f'Quem nasceu em {ano} tem {data} anos em 2025')
    print(f'Você já deveria ter se alistado há {data - 18} ano')
    
#Alistamento Militar