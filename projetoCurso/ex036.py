print('Faça o seu empréstimo')
valor = float(input('Qual o valor da casa? '))
sal = float (input('Qual o valor do seu salário? '))
anos = int (input('Em quantos anos você irá pagar?'))

parcela = valor/(12*anos)

if parcela <= sal * 0.3:
    print('Seu emprestimo foi aprovado, em {} parcelas de R$ {:.2f}!'.format(12*anos, parcela))
elif parcela > sal * 0.3:
    print('Seu emprestimo foi negado pois compromete sua renda')
