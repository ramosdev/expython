from random import choice

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))

lista = [a1,a2,a3,a4]

escolhido = choice(lista)

print(escolhido)