reta1 = float(input('Qual a Primeira reta: '))
reta2 = float(input('Qual a Segunda reta: '))
reta3 = float(input('Qual a Terceira reta: '))
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Os Segmentos Consegue FORMAR um triângulo')
else:
    print('Os Segmentos Não Consegue FORMAR um Triângulo')

#Analisando Triângulo v1.0