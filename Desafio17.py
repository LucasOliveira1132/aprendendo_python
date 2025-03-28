
from math import pow, sqrt
cateto_oposto = float(input('Qual o Comprimento Do Cateto Oposto: '))
cateto_adjacente = float(input('Qual o comprimento Do Cateto Adjacente:'))
num_oposto = pow(cateto_oposto,2)
num_adjacente = pow(cateto_adjacente,2 )
soma = num_oposto + num_adjacente
raiz = sqrt(soma)
print(f'A Hipotenusa Vai Medir {raiz:.2f}')
#Jeito que fiz com Base Nas Função Que Ele Mostrou 


""""
from math import hypot
cateto_oposto = float(input('Qual o Comprimento Do Cateto Oposto: '))
cateto_adjacente = float(input('Qual o comprimento Do Cateto Adjacente:'))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A Hipotenusa Vai Medir {hipotenusa:.2f}')"
"""
#Jeito Que o Guanabara fez Usando A Função "hypot" Da Blibioteca Math, Não Sabia Dessa Função Na época (27/03/2025)