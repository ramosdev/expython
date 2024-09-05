import random
print('-------JOGO DA ADIVINHAÇÃO-------')
numpc = random.randint(0,5)

num = int(input('Digite um número entre 0 e 5 e tente superar a máquina: '))

if numpc == num:
    print('Você adivinhou o número {}. Meus parabéns!! \n VOCÊ É UM GÊNIO!!'.format(num))
else:
    print('Não foi dessa vez, você digitou: {} e o número era {}. \n tente mais uma vez!'.format(num, numpc))
