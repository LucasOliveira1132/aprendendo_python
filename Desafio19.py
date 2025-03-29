import random 
nome1 = str(input('Digite um Nome:'))
nome2 = str(input('Digite Mais Um Nome:'))
nome3 = str(input('Digite Mais Um Nome:'))
nome4 = str(input('Digite Mais um Nome:'))
sortudo = random.choice([nome1, nome2, nome3, nome4])
print(f'A Pessoa Escolhida Foi {sortudo}')