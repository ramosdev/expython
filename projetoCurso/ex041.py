from datetime import date
nasc = int(input('Insira o ano do seu nascimento: '))

idade = date.today().year - nasc

if idade < 10:
    print('Você tem {} anos e é um nadador mirim '.format(idade))
elif idade < 15:
    print('Você tem {} anos e é um nadador infantil'.format(idade))
elif idade < 20:
    print('Você tem {} anos e é um nadador junior'.format(idade))
elif idade == 20:
    print('Você tem {} anos e é um nadador sênior'.format(idade))
else:
    print('Você tem {} anos e é um nadador master'.format(idade))