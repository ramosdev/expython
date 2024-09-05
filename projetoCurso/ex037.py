num = int(input('Digite um número para converter sua base: '))
dig = int (input(' Digite "1" para converter em binário \n Digite "2" para converter em octal \n Digite "3" para converter em hexadecimal\n'))

if dig == 1:
    print('O número {} em Binário é: {:b} Binário'.format(num, num))
elif dig == 2:
    print('O número {} em Octal é: {:o} Octal'.format(num, num))

elif dig == 3:
    print('O número {} em Hex é: {:x} Hex'.format(num, num))