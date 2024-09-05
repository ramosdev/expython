dist = float(input('Qual a distância em KM?'))

if dist <= 200:
    print('O valor da passagem é de R${:.2f}!'.format(dist*0.50))
else:
    print('O valor da passagem é de R$ {:.2f}!'.format(dist*0.45))