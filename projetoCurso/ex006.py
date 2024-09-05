num = int(input('Insira um número: '))

#print('O número que você digitou foi: {}. O dobro desse número é {}, o triplo é {} e a raiz quadrada é {:.0f}.'.format(num, num*2, num*3, num**(1/2)))
print('O número que você digitou foi: {}. O dobro desse número é {}, o triplo é {} e a raiz quadrada é {:.0f}!'.format(num, num*2, num*3, pow(num, (1/2))))