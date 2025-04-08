valor_casa = float(input('Qual o valor da casa ?'))
salario = float(input('Qual o seu sálario? '))
tempo = float(input('Quantos anos você pretende pagar a casa? '))
mes = tempo*12
imposto = salario*30 /100
valor_pago_mesalmente = valor_casa / mes
if valor_pago_mesalmente <= imposto:
    print('Você vai conseguir financiar a casa!')
    print(f'será {mes} parcelas de {valor_pago_mesalmente:.2f}')
else:
    print('Você não vai conseguir financiar a casa!')
    print(f'para pagar a casa de {valor_casa:.0f} em {tempo} anos a prestação vai ser de R${valor_pago_mesalmente:.2f}')
