from random import randint
numero_aleatorio = randint(1 , 5)
numero_usuario = (int(input('Tenta Adivinhar o numero: ')))
if numero_usuario == numero_aleatorio:
    print('Você Acertou o Numero, Parabens')
else:
    print('Você Errou o Numero, Boa Sorte')

#Jogo da Adivinhação