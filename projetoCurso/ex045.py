from random import randint
from time import sleep

print('====== BEM VINDO AO JOKENPOURRA =======')

user = int (input(' Escolha 1 para Pedra \n Escolha 2 para Papel \n Escolha 3 para Tesoura \n'))
pc = randint(1,3)

escolhas = ['','pedra', 'papel', 'tesoura']

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('=================')
print('Você escolheu {} e a máquina escolheu {}!'.format(escolhas[user], escolhas[pc]))

if user == 1 and pc == 3 or user == 2 and pc == 1 or user == 3 and pc == 2:
    print('Parabéns, você venceu!!')
elif user == pc:
    print('O jogo empatou, tente novamente!')
else:
    print('Que pena, não foi dessa vez, você perdeu!')