import math

dgree = float(input('Insira o angulo: '))

sen = math.sin(math.radians(dgree))
cos = math.cos(math.radians(dgree))
tg = math.tan(math.radians(dgree))

print('Seno de {}º ----- {:.2f} \n Coseno de {}º ----- {:.2f} \n Tangente de {}º ----- {:.2f}'.format(dgree,sen,dgree,cos,dgree,tg))