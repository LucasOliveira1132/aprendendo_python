frase = str(input('Digite uma frase: ')).lower().strip()

print(f'Quantos A apareceu na sua frase: {frase.count('a' )}')
print(f'Qual foi a primeira vez que apareceu A na sua frase: {frase.find('a')+1}')
print(f'Qual foi a última vez que apareceu A na sua frase: {frase.rfind('a')+1}')

#Primeira e última ocorrência de uma string