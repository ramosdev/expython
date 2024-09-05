n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print('Você foi reprovado com média {} '.format(media))

elif 5.00 <= media < 6.90: #elif media >= 5.00 and media < 6.90:
    print('Você está de recuperação com média {}'.format(media))
else:
    print('Parabéns, você foi aprovado com média {}!'.format(media))