idade = int(input('Qual a sua idade: '))
print(f'A sua idade é {idade} anos ')
if idade <= 9: 
    print('Sua Classe é MIRIM')
elif idade <= 14:
    print('Sua Classe é INFATIL')
elif idade <= 19:
    print('Sua Classe é JUNIOR')
elif idade == 20:
    print('Sua Classe é SÊNIOR')
elif idade <=100:
    print('Sua Classe é MASTER')
elif idade > 100:
    print('Sua Classe é DEFUNTO')
    #Classificando Atletas