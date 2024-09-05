from datetime import date

ano = int(input('Informe o ano de seu nascimento: '))

idade = date.today().year  - ano

if idade <18:
    print('Você tem {} anos, ainda não está na hora de se alistar. Ainda faltam {} ano(s)!'.format(idade, 18-idade))
elif idade == 18:
    print('Você tem 18 anos, está na hora de fazer o seu alistamento')
elif idade > 18:
    print('Você tem {} anos, o prazo de alistamento passou e está {} ano(s) atrasado'.format(idade, idade-18))