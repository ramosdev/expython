num = str(input('Digite um número entre 0 e 9999: '))

uni = num[len(num)-1]
dez = num[len(num)-2]
cen = num[len(num)-3]
mil = num[len(num)-4]


print('Milhar(es): {} \n Centena(s): {} \n Dezena(s): {} \n Unidade(s): {}'.format(mil, cen, dez, uni))