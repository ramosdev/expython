m1 = int(input('Digite a primeira medida: '))
m2 = int(input('Digite a segunda medida: '))
m3 = int(input('Digite a terceira medida: '))

if m1 < m2+m3 and m2 < m1+m3 and m3 < m1+m2  :
    print('Com essas medidas podemos formar um triângulo')
else:
    print('com essas medidas não é possível formar um triângulo')