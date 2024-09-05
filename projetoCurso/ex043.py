alt = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso/(alt*alt)

if imc  < 18.5:
    print('Você está abaixo do peso')
elif imc < 25.0:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc <40:
    print('Você está obeso')
else:print('Você está com obesidade mórbida')