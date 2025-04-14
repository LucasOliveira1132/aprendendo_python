from random import choice
print('Escolha uma das Opção: ')
print('''[ 1 ] Papel 
[ 2 ] Pedra 
[ 3 ] Tesoura''')
escolha = int(input('Digite a sua opcão: '))

lista = ['pedra', 'papel', 'tesoura',]
maquina = choice(lista)
print('='*22)
if escolha == 1 and maquina == 'papel':
    print('A maquina Jogou Papel')
    print('Você Jogou Papel')
    print('Deu EMPATE')
elif escolha == 1 and maquina == 'pedra':
    print('A maquina Jogou Pedra ')
    print('Você Jogou Papel')
    print('Você GANHOU')
elif escolha == 1 and maquina == 'tesoura':
    print('A maquina Jogou tesoura')
    print('Você Jogou Papel')
    print('Você PERDEU')

elif escolha == 2 and maquina == 'papel':
    print('A mquina Jogou Papel')
    print('Você Jogou Pedra')
    print('Você PERDEU')
elif escolha == 2 and maquina == 'pedra':
    print('A maquina Jogou Pedra')
    print('Você Jogou Pedra')
    print('Deu EMPATE')
elif escolha == 2 and maquina == 'tesoura':
    print('A maquina Jogou Tesoura')
    print('Você Jogou Pedra')
    print('Você GANHOU')

elif escolha == 3 and maquina == 'papel':
    print('A maquina escolheu Papel')
    print('Você Jogou Tesoura')
    print('Você GANHOU')
elif escolha == 3 and maquina == 'pedra':
    print('A maquina Jogou Pedra')
    print('Você Jogou Tesoura')
    print('Você PERDEU')
elif escolha == 3 and maquina == 'tesoura':
    print('A maquina Jogou tesoura')
    print('Você Jogou Tesoura')
    print('Deu EMPATE')
else:
    print('Essa Opcão NÃO Existe')
    #GAME: Pedra Papel e Tesoura