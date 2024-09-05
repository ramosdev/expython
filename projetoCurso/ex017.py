import math

print('Calcule a hipotenusa')

cat = float(input('Insira o cateto oposto: '))
adjc = float(input('Insira o cateto adjacente: '))

print('O valor da hipotenusa do triangulo é: {:.3f}' .format(math.hypot(cat,adjc)))