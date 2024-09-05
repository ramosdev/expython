larg = float(input('Insira a largura da sua parede: '))
alt = float(input('Insira a altura da sua parede: '))

tamParede = larg * alt

print('O tamanho da sua parede é de {}m^2, precisa de um total de {} litros para pinta-la'.format(tamParede, tamParede/2))