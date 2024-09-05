num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num > num2:
    print('O primeiro valor "{}" é maior que o segundo "{}"!'.format(num, num2))
elif num2 > num:
    print('O segundo número "{}" é maior que o primeiro "{}"!'.format(num2, num))
else:
    print('Não existe número maior, os dois são iguais!')