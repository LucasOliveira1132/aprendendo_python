print('Escolha um Item para comprar: ')
print('''[ 1 ] Celular - R$ 1500.00
[ 2 ] Headset - R$ 200.00
[ 3 ] Teclado - R$ 250.00
[ 4 ] Monitor - R$ 900.00     ''')
produto = int(input('Digite o número do produto:'))

print('')

print('Escolha uma Opcão de pagamento: ')
print('''[ 1 ] À Vista no Dinheiro - 10% De Desconto
[ 2 ] À Vista no Cartão - 5% De Desconto
[ 3 ] Cartão 2x - Preço Normal
[ 4 ] Cartão Mais de 3x - 20% Juros ''')
pagamento = int(input('Digite a forma de Pagamento: '))

print('')

celular = 1500.00
if produto == 1 and pagamento == 1:
    desconto = celular* 10 / 100
    print(f'O Produto Celular com o Desconto de 10% fica R$ {celular - desconto} ')

elif produto == 1 and pagamento == 2:
    desconto = celular * 5 / 100
    print(f'O Produto Celular com o Desconto de 5% fica R$ {celular - desconto} ')

elif produto == 1 and pagamento == 3:
    print(f'Seu Produto Ficou o preço normal de R$ {celular}')

elif produto == 1 and pagamento == 4: 
    celular = 1500.00
    juros = celular * 20 / 100
    print(f'Seu Produto com %20 de Juros vai ficar por R$ {celular + juros}')

elif produto == 2 and pagamento == 1:
    headset = 200.00
    desconto = headset * 10 / 100
    print(f'O Produto Headset com o Desconto de 10% fica R$ {headset - desconto}')

elif produto == 2 and pagamento == 2:
    headset = 200.00
    desconto = headset * 5 / 100
    print(f'O Produto Headset com o Desconto de 5% fica R$ {headset - desconto}')

elif produto == 2 and pagamento == 3:
    headset = 200.00
    print(f'Seu Produto Ficou o preço normal de R$ {headset}')

elif produto == 2 and pagamento == 4: 
    headset = 200.00 
    juros = headset *20 / 100
    print(f'Seu Produto com %20 de Juros vai ficar por R$ {headset + juros}')

elif produto == 3 and pagamento == 1:
    teclado = 250.00
    desconto = teclado * 10 / 100
    print(f'O Produto Teclado com o Desconto de 10% fica R$ {teclado - desconto} ')

elif produto == 3 and pagamento == 2:
    teclado = 250.00
    desconto = teclado * 5 / 100
    print(f'O Produto Teclado com o Desconto de 5% fica R$ {teclado - desconto} ')

elif produto == 3 and pagamento == 3:
    teclado = 250.00
    print(f'Seu Produto Ficou o preço normal de R$ {teclado} ')

elif produto == 3 and pagamento == 4:
     teclado = 250.00
     juros = teclado * 20 / 100
     print(f'Seu Produto com %20 de Juros vai ficar por R$ {teclado + produto} ')

elif produto == 4 and pagamento == 1:
    monitor = 900.00
    desconto = monitor * 10 / 100
    print(f'O Produto Monitor com o Desconto de 10% fica R$ {monitor - desconto} ')

elif produto == 4 and pagamento == 2:
    monitor = 900.00
    desconto = monitor * 5 / 100
    print(f'O Produto Monitor com o Desconto de 5% fica R$ {monitor - desconto} ')

elif produto == 4 and pagamento == 3:
    monitor = 900.00
    print(f'Seu Produto Ficou o preço normal de R$ {monitor} ')

elif produto == 4 and pagamento == 4:
    monitor = 900.00
    juros = monitor * 20 / 100 
    print(f'Seu Produto com %20 de Juros vai ficar por R$ {monitor + juros}')

else:
     print('Essa Opcão Não EXISTE')
     #Gerenciador de Pagamentos