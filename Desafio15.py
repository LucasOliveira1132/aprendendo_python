km = float(input('Quantos Km Foi Percorridos: '))
dia = float(input('Quantos dias Ele foi Alugado?'))
valor_dia = dia*60
valor_km = km*0.15
valor_total = valor_dia + valor_km
print(f'O valor Total A Pagar é R${valor_total:.2f}')