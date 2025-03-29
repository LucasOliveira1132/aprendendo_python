'''
import random 
nome1 = str(input('Digite um Nome:'))
nome2 = str(input('Digite Mais Um Nome:'))
nome3 = str(input('Digite Mais Um Nome:'))
nome4 = str(input('Digite Mais um Nome:'))
sortudo = random.choice([nome1, nome2, nome3, nome4])
print(f'A Pessoa Escolhida Foi {sortudo}')
'''

from random import choice
#choice serve Para Sortear um item de uma lista
nome1 = str(input('Digite um Nome:'))
nome2 = str(input('Digite um Nome:'))
nome3 = str(input('Digite um Nome:'))
nome4 = str(input('Digite um Nome:'))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f'o Escolhido Foi {escolhido}')