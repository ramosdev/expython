frase = 'Eu faço programa'

print(frase)

print(frase[3]) #numero entre colchetes indica a posição da letra a ser impressa
print (frase[3:10:2])#estrutura: 3:10:2 o três indica onde irá começar, o dez indica o final e o dois que irá pular de dois em dois
print(frase.count('o')) #tudo em python é um objeto
print(frase.replace('Eu faço', 'Sou um garoto de')) #replace substitui em instância uma parte da frase ou ela toda
print('programa' in frase) # in frase retorta True ou False
print(frase.upper()) #transforma todos os caractéres em maíusculo
print(frase.lower()) #transforma todos os caractéres em minúsculo
print(frase.title()) #capitaliza a frase
print(frase.split()) #quebra a frase a cada espaço e armazena em uma lista
print(len(frase))
