salario = float(input('insira seu salario e descubra o valor do aumento: '))

print('Seu salário atual é de: R${} com o reajuste de 15% passará a ser de: R${:.2f}!'.format(salario, salario*1.15))