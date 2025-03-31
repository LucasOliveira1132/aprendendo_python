frase = str(input('Digite seu Nome:'))
print(f'o seu nome em maiúsculo: {frase.strip().upper()} ')
        #strip() é usado para remover espaços extras no início e no fim de uma string.
        #upper() Deixa tudo em maiúsculo.
print(f'o seu nome em minúscula: {frase.strip().lower()}')
        #lower Deixa tudo em Minúscula.
print(f'Quantas Letras em seu nome: {len(frase.replace(" ", ""))}')
        #O método replace(" ", "") no Python é usado para substituir todos os espaços em uma string por algo que você escolher.
        #Vamos entender isso em detalhes:
primeiro_numero = frase.split()
print(f'Quantas Letras tem o seu primeiro nome: {len(primeiro_numero[0])}')


#Analisador de Textos