peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura**2)
print('Seu IMC é {:.2f}' .format(imc))
if imc < 18.5:
    print('Voçê está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Voçê está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Voçê está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Voçê está com obesidade.')
else:
    print('Voçê está com obesidade mórbida.')