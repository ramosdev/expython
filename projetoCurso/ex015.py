km = float(input('Qual a quantidade de KM rodados? '))
dias = int(input('Quantidade de dias do aluguel? '))

vTotal = (dias*60) + (0.15*km)

print('O valor que total a pagar é de R${:.2f} por ter rodado {} Km(s) e {} dia(s) de aluguel'.format(vTotal, km, dias))