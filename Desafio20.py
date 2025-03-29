from random import shuffle
nome1 = str(input('Digite Um Nome:'))
nome2 = str(input('Digite Mais Um Nome:'))
nome3 = str(input('Digite Mais um Nome:'))
nome4 = str(input('Digite Mais um Nome:'))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista) 
print(f'A Ordem é {lista}')