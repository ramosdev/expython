medida = float(input('Insira sua medida em metros: '))

print('A medida que você digitou é de {} metro(s). Que são {:.0f} centímetros e {:.0f} milímetros'.format(medida, medida*100, medida*1000))