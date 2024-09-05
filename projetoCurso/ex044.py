preco = float(input('Qual o valor do produto? '))

dig = int(input('Qual será a forma de pagamento? \n "1" à vista ou cheque'
                '\n "2" 1x no cartão'
                '\n "3" 2x no cartão'
                '\n "4" 3x ou mais no cartão \n'))

if dig == 1:
    preco = preco*0.9
elif dig == 2:
    preco = preco*0.95
elif dig == 3:
    preco = preco
elif dig == 4:
    preco = preco*1.2

print('Com a forma de pagamento escolhida, o valor do produto fica de R$ {} !'.format(preco))