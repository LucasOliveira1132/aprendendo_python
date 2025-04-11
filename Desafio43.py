altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso ?'))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f}, Você está Abaixo do peso')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f}, Você está no peso ideal')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2f}, Você está com Sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é {imc:.2f}, Você está Obeso')
else:
    print(f'Seu IMC é {imc:.2f}, Você está na Obesidade Mórbida')
