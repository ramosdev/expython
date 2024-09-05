velo = float(input('Digite a velocidade do carro: '))

if velo > 80:
    multa = (velo-80)*7
    print('Você foi multado pois estava acima de 80Km/h e, o valor da multa é de R${:.2f}!'.format(multa))
else:
    print('Siga a viagem')