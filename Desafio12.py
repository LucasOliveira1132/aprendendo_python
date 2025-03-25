valor = float(input('Digite Um Preço De Um Produto R$: '))
desconto = valor*5/100
total = valor - desconto

print(f'O Produto que Custava R${valor}, Na Promoção Com Desconto de 5% Vai Custar {total:.2f}')
#Calculando Descontos 