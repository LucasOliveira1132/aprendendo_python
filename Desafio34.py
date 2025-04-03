salario = float(input('Qual o seu salário? '))
if salario >= 1250.00:
    aumento = salario *10/100
    print(f'Seu salário teve um aumento de {aumento} e ficou {aumento+salario:.2f}')
else:
    aumento = salario *15/100
    print(f'Seu salário teve um aumento de {aumento} e ficou {aumento+salario:.2f}')

#Aumentos múltiplos