termo = int(input('Digite o Primeiro termo: '))
razao = int(input('digite a Razão: '))
for contador in range (0,10):
    print(termo, end= ' ')
    termo += razao
    #Progressão Aritmética