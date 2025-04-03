velocidade = float(input('Qual a Velocidade do carro: '))
km = velocidade - 80
multa = km*7
if velocidade <= 80:
    print('Você está na velocidade normal, Continue assim')
else:
    print(f'Você Passou do Limite de Velocidade, Sua MULTA É R${multa}')
#Radar eletrônico