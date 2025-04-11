lado1 = float(input('Digite um lado: '))
lado2 = float(input('Digite mais um lado: '))
lado3 = float(input('Digite mais um lado: '))

if lado1 == lado2 == lado3:
    print('Todos os lados são igual e pode formar um EQUILÁTERO ')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Todos os lados são diferente e pode formar um ESCALENO')
else:
    print('Dois lados são igual e pode formar um ISÓSCELES')
#Analisando Triângulos v2.0


