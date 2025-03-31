cidade = str(input('Diga o Nome da Cidade Que Você Mora:'))
cidade.lower()
print(f'Sua Cidade Começa com Santo? {cidade.lower().startswith("santo")}')
#O startswith()método retorna True se a string começar com o valor especificado, caso contrário, False.
#Verificando as primeiras letras de um texto
