nota1 = float(input('Qual a sua nota: '))
nota2 = float(input('Qual a outra nota: '))
soma = (nota1 + nota2) / 2
if soma < 5.0:
    print('REPROVADO, MLK BURRO')
elif soma <= 6.9:
    print('RECUPERAÇÃO, Estuda mais Paizão')
elif soma >= 7.0:
    print('APROVADO, MENINO BRABO')
    #Aquele clássico da Média