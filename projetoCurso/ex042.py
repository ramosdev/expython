m1 = int(input('Digite a primeira medida: '))
m2 = int(input('Digite a segunda medida: '))
m3 = int(input('Digite a terceira medida: '))

if m1 < m2+m3 and m2 < m1+m3 and m3 < m1+m2  :
    print('Com essas medidas podemos formar um triângulo')
    if m1 == m2 and m2 == m3:
        print('Ele é um triângulo Equilátero')
    elif m1 == m2 or m1 == m3 or m2 == m3:
        print('Ele é um triângulo Isóceles')
    else:
        print('Ele é um triângulo Escaleno')
else:
    print('com essas medidas não é possível formar um triângulo')