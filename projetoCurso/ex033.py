num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um para finalizar: '))
maior = 0
menor = 0
meio = 0

if num > num2 and num > num3:
    maior = num
elif num > num2 or num > num3:
    meio = num
else :
    menor = num

if num2 > num and num2 > num3:
    maior = num2
elif num2 > num or num2 > num3:
    meio = num2
else :
    menor = num2

if num3 > num and num3 > num2:
    maior = num3
elif num3 > num or num3 > num2:
    meio = num3
else :
    menor = num3


print(maior,meio,menor)