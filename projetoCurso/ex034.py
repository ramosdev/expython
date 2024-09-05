salario = float(input('Digite o seu salario e saiba o aumento: '))

if salario > 1250:
    salario = salario*1.1
else:
    salario = salario*1.15


print('Seu novo salário é de R$ {:.2f}'.format(salario))